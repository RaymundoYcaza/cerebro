from __future__ import annotations

import argparse
from pathlib import Path

from technical.config import load_config
from core.text_utils import normalize_newlines, sha256_short, slugify, unique_path
from reflective.llm import chat_reflective_json
from reflective.markdown import render_reflective_session
from reflective.final_markdown import render_thing_note
from core.tags import normalize_tags


def as_list(value) -> list[str]:
    if value is None:
        return []

    if isinstance(value, str):
        value = value.replace("\\n", "\n").strip()
        if not value:
            return []
        return [x.strip(" -\t") for x in value.splitlines() if x.strip()]

    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]

    return [str(value).strip()] if str(value).strip() else []


def read_text_source(path: str | None, text: str | None) -> str:
    if text:
        return text

    if path:
        return Path(path).read_text(encoding="utf-8")

    print("Pega el Spark. Termina con Ctrl+D:")
    chunks = []
    try:
        while True:
            chunks.append(input())
    except EOFError:
        pass

    return "\n".join(chunks)


def ask_multiline(prompt: str) -> str:
    print()
    print(prompt)
    print("(Escribe tu respuesta. Termina con una línea vacía.)")

    lines = []

    while True:
        line = input("> ")
        if not line.strip():
            break
        lines.append(line)

    return "\n".join(lines).strip()


def build_interactive_session_markdown(
    *,
    base_markdown: str,
    own_voice: str,
    validation: str,
    connections: str,
) -> str:
    text = base_markdown

    text = text.replace(
        "> Escribe aquí tu reformulación.",
        f"> {own_voice}" if own_voice else "> Pendiente.",
    )

    text = text.replace(
        "- [ ] Validado por mí",
        f"- [x] Validado por mí\n\n> {validation}" if validation else "- [ ] Validado por mí",
    )

    text = text.replace(
        "> Escribe aquí conexiones personales, notas relacionadas o ideas previas.",
        f"> {connections}" if connections else "> Pendiente.",
    )

    return text


def source_to_wikilink(path: Path, vault_root: Path | None = None) -> str:
    """
    Usa wikilink corto por nombre de archivo.

    Obsidian resuelve mejor [[archivo]] cuando la nota está dentro de la bóveda,
    aunque no esté en Atlas. Además evita rutas largas innecesarias.
    """
    return f"[[{path.stem}]]"

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Sesión interactiva para convertir un Spark en una sesión reflexiva y/o Thing Note limpia."
    )

    parser.add_argument("--config", default="config.yaml", help="Ruta a config.yaml.")
    parser.add_argument("--input", help="Archivo Markdown/texto a procesar.")
    parser.add_argument("--text", help="Texto directo a procesar.")

    parser.add_argument("--write", action="store_true", help="Escribir archivos.")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar resultado sin escribir.")

    parser.add_argument(
        "--output-mode",
        choices=["session", "thing", "both"],
        default="both",
        help="Qué generar: session, thing o both.",
    )

    parser.add_argument("--think", action="store_true", help="Activar thinking.")
    parser.add_argument("--nothink", action="store_true", help="Desactivar thinking.")

    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.think and args.nothink:
        raise SystemExit("Usa solo uno: --think o --nothink.")

    cfg = load_config(args.config)
    raw_content = read_text_source(args.input, args.text)
    content = normalize_newlines(raw_content)

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

    source_hash = sha256_short(content)

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

    title = extracted.get("thing_note_candidate") or "nota-reflexiva"
    slug = slugify(title)

    session_path = None
    thing_path = None
    session_link = None

    if args.write and not args.dry_run:
        if args.output_mode in {"session", "both"}:
            session_dir = cfg.paths.output_dir / "reflective-session"
            session_dir.mkdir(parents=True, exist_ok=True)

            session_path = unique_path(session_dir / f"{slug}--{source_hash[:6]}--session.md")
            session_path.write_text(session_markdown, encoding="utf-8")
            session_link = source_to_wikilink(session_path, cfg.paths.vault_root)

        thing_markdown = render_thing_note(
            extracted=extracted,
            tags=tag_result.tags,
            source_hash=source_hash,
            model_used=model_used,
            own_voice=own_voice,
            connections=connections,
            session_link=session_link,
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
        )

        if args.output_mode in {"session", "both"}:
            print("\n\n=== Sesión reflexiva ===\n")
            print(session_markdown)

        if args.output_mode in {"thing", "both"}:
            print("\n\n=== Thing Note limpia ===\n")
            print(thing_markdown)

        return

    if session_path:
        print(f"\nOK: sesión reflexiva creada: {session_path}")

    if thing_path:
        print(f"OK: Thing Note creada: {thing_path}")

    print(f"Modelo usado: {model_used}")
    print(f"Tags: {', '.join(tag_result.tags)}")


if __name__ == "__main__":
    main()
