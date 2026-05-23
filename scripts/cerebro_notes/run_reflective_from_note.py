from __future__ import annotations

import argparse
import re
import shutil
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import yaml

from technical.config import load_config
from core.text_utils import normalize_newlines, sha256_short, slugify, unique_path
from core.tags import normalize_tags
from reflective.llm import chat_reflective_json
from reflective.markdown import render_reflective_session
from reflective.final_markdown import render_thing_note

from run_reflective_interactive import (
    as_list,
    ask_multiline,
    build_interactive_session_markdown,
)


REFLECTIVE_SOURCE_TAGS = ["note/extract"]


def wikilink_short(path: Path) -> str:
    return f"[[{path.stem}]]"


def split_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    if not content.startswith("---\n"):
        return {}, content

    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", content, flags=re.DOTALL)
    if not match:
        return {}, content

    raw_yaml = match.group(1)
    body = match.group(2)

    try:
        data = yaml.safe_load(raw_yaml) or {}
        if not isinstance(data, dict):
            data = {}
    except Exception:
        data = {}

    return data, body


def build_frontmatter(data: dict[str, Any]) -> str:
    return "---\n" + yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip() + "\n---\n\n"


def ensure_reflective_source_frontmatter(source_path: Path) -> None:
    content = source_path.read_text(encoding="utf-8")
    data, body = split_frontmatter(content)

    data.setdefault("up", [])
    data.setdefault("related", [])
    data.setdefault("created", date.today().isoformat())
    data.setdefault("sourceType", "reflection-spark")

    tags = data.get("tags")
    if not isinstance(tags, list):
        tags = []

    for tag in REFLECTIVE_SOURCE_TAGS:
        if tag not in tags:
            tags.append(tag)

    data["tags"] = tags

    source_path.write_text(
        build_frontmatter(data) + body.lstrip("\n"),
        encoding="utf-8",
    )


def move_source_to_sources(source_path: Path, sources_dir: Path) -> Path:
    sources_dir.mkdir(parents=True, exist_ok=True)

    ensure_reflective_source_frontmatter(source_path)

    dst = unique_path(sources_dir / source_path.name)
    shutil.move(str(source_path), str(dst))

    return dst


def get_input_dir(cfg) -> Path:
    if hasattr(cfg.paths, "inbox_sources_dir"):
        return cfg.paths.inbox_sources_dir
    return cfg.paths.vault_root / "+"


def get_sources_dir(cfg) -> Path:
    if hasattr(cfg.paths, "sources_dir"):
        return cfg.paths.sources_dir
    return cfg.paths.vault_root / "Atlas" / "Dots" / "Sources"


def score_file(query: str, path: Path) -> float:
    q = query.lower().strip()
    name = path.stem.lower()
    full = str(path).lower()

    if not q:
        return 0.0

    direct = 1.0 if q in name else 0.0
    partial = 0.7 if q in full else 0.0
    ratio = SequenceMatcher(None, q, name).ratio()

    return max(direct, partial, ratio)


def find_notes(base_dir: Path, query: str, limit: int = 12) -> list[Path]:
    candidates = [p for p in base_dir.rglob("*.md") if p.is_file()]

    scored = [
        (score_file(query, p), p)
        for p in candidates
    ]

    scored.sort(key=lambda x: x[0], reverse=True)

    return [p for score, p in scored[:limit] if score > 0.15]


def choose_note(base_dir: Path, query: str | None) -> Path:
    while True:
        if not query:
            query = input("Buscar nota en '+': ").strip()

        results = find_notes(base_dir, query)

        if not results:
            print("No encontré resultados. Prueba otra búsqueda.")
            query = None
            continue

        print("\nResultados:")
        for i, path in enumerate(results, 1):
            print(f"{i}. {path.name}")
            print(f"   {path}")

        choice = input("\nSelecciona número, 'r' para refinar, o Enter para 1: ").strip()

        if not choice:
            return results[0]

        if choice.lower() == "r":
            query = None
            continue

        try:
            idx = int(choice)
            if 1 <= idx <= len(results):
                return results[idx - 1]
        except ValueError:
            pass

        print("Selección inválida.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Busca una nota fuente en '+' con fuzzy search, crea sesión reflexiva/Thing Note y mueve la fuente a Sources."
    )

    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--query", help="Texto de búsqueda fuzzy.")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--output-mode",
        choices=["session", "thing", "both"],
        default="both",
    )
    parser.add_argument(
        "--no-move-source",
        action="store_true",
        help="No mover la nota fuente aunque se use --write.",
    )
    parser.add_argument("--think", action="store_true")
    parser.add_argument("--nothink", action="store_true")

    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.think and args.nothink:
        raise SystemExit("Usa solo uno: --think o --nothink.")

    cfg = load_config(args.config)

    input_dir = get_input_dir(cfg)
    sources_dir = get_sources_dir(cfg)

    if not input_dir.exists():
        raise SystemExit(f"No existe la carpeta de entrada: {input_dir}")

    source_path = choose_note(input_dir, args.query)

    raw_content = source_path.read_text(encoding="utf-8")
    content = normalize_newlines(raw_content)
    source_hash = sha256_short(content)

    think = None
    if args.think:
        think = True
    elif args.nothink:
        think = False

    extracted, model_used = chat_reflective_json(
        base_url=cfg.ollama.base_url,
        model=cfg.ollama.chat_model,
        fallback_model=cfg.ollama.fallback_chat_model,
        content=content,
        think=cfg.ollama.think_default if think is None else think,
        temperature=cfg.ollama.temperature,
        timeout_seconds=cfg.ollama.timeout_seconds,
    )

    tag_result = normalize_tags(
        model_main_tags=as_list(extracted.get("main_tags", [])),
        model_z_tags=as_list(extracted.get("z_tags", [])),
        default_main_tags=["note/reflection", "note/atomic"],
        default_z_tags=["z/LYT"],
        allowed_roots=cfg.tag_policy.allowed_roots,
        general_root=cfg.tag_policy.general_root,
        max_main_tags=cfg.tag_policy.max_main_tags,
        max_z_tags=cfg.tag_policy.max_z_tags,
    )

    print("\nFuente seleccionada:")
    print(source_path)

    print("\n=== Señal detectada ===")
    print(extracted.get("signal") or "No detectada.")

    print("\n=== Thing Note candidata ===")
    print(extracted.get("thing_note_candidate") or "Sin título candidato.")

    print("\n=== Por qué podría importar ===")
    print(extracted.get("why_it_matters") or "No detectado.")

    validation_question = (
        extracted.get("validation_question")
        or "¿Este concepto es lo que resonó contigo o hay algo más profundo?"
    )

    print("\n=== Validación ===")
    print(validation_question)

    validation = ask_multiline(validation_question)

    own_voice = ask_multiline(
        "Ahora explícalo con tu propia voz, usando tu propio sabor, gramática y sintaxis."
    )

    connection_question = (
        extracted.get("connection_question")
        or "¿Esto a qué te recuerda?"
    )

    connections = ask_multiline(
        connection_question + " Piensa en tu Atlas, notas previas, proyectos, experiencias o ideas relacionadas."
    )

    title = extracted.get("thing_note_candidate") or "nota-reflexiva"
    slug = slugify(title)

    moved_source_path = None
    source_link = wikilink_short(source_path)

    if args.write and not args.dry_run and not args.no_move_source:
        moved_source_path = move_source_to_sources(source_path, sources_dir)
        source_link = wikilink_short(moved_source_path)

    base_session_markdown = render_reflective_session(
        extracted=extracted,
        tags=tag_result.tags,
        source_hash=source_hash,
        model_used=model_used,
        original_content=content,
        review_status="guided",
    )

    session_markdown = build_interactive_session_markdown(
        base_markdown=base_session_markdown,
        own_voice=own_voice,
        validation=validation,
        connections=connections,
    )

    if source_link:
        session_markdown = session_markdown.replace(
            "source_hash:",
            f"source: {source_link}\nsource_hash:",
            1,
        )

    session_path = None
    thing_path = None
    session_link = None

    if args.write and not args.dry_run:
        if args.output_mode in {"session", "both"}:
            session_dir = cfg.paths.output_dir / "reflective-session"
            session_dir.mkdir(parents=True, exist_ok=True)

            session_path = unique_path(session_dir / f"{slug}--{source_hash[:6]}--session.md")
            session_path.write_text(session_markdown, encoding="utf-8")
            session_link = wikilink_short(session_path)

        thing_markdown = render_thing_note(
            extracted=extracted,
            tags=tag_result.tags,
            source_hash=source_hash,
            model_used=model_used,
            own_voice=own_voice,
            connections=connections,
            session_link=session_link,
            source_link=source_link,
        )

        if args.output_mode in {"thing", "both"}:
            thing_dir = cfg.paths.output_dir / "thing-note"
            thing_dir.mkdir(parents=True, exist_ok=True)

            thing_path = unique_path(thing_dir / f"{slug}--{source_hash[:6]}.md")
            thing_path.write_text(thing_markdown, encoding="utf-8")

    else:
        thing_markdown = render_thing_note(
            extracted=extracted,
            tags=tag_result.tags,
            source_hash=source_hash,
            model_used=model_used,
            own_voice=own_voice,
            connections=connections,
            session_link=None,
            source_link=source_link,
        )

        print("\nDRY-RUN: no se escriben notas y no se mueve la fuente.")

        if args.output_mode in {"session", "both"}:
            print("\n\n=== Sesión reflexiva ===\n")
            print(session_markdown)

        if args.output_mode in {"thing", "both"}:
            print("\n\n=== Thing Note limpia ===\n")
            print(thing_markdown)

        return

    if moved_source_path:
        print(f"\nOK: fuente movida a: {moved_source_path}")
    elif args.no_move_source:
        print("\nOK: fuente conservada por --no-move-source")

    if session_path:
        print(f"OK: sesión reflexiva creada: {session_path}")

    if thing_path:
        print(f"OK: Thing Note creada: {thing_path}")

    print(f"Modelo usado: {model_used}")
    print(f"Tags: {', '.join(tag_result.tags)}")


if __name__ == "__main__":
    main()
