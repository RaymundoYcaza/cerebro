from __future__ import annotations

from datetime import date
from typing import Any

import yaml


class ObsidianDumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper, data):
    if isinstance(data, str) and data.startswith("[[") and data.endswith("]]"):
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="'")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


ObsidianDumper.add_representer(str, _str_presenter)


def _yaml_block(data: dict[str, Any]) -> str:
    return "---\n" + yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip() + "\n---\n"


def _as_list(value) -> list[str]:
    """
    Normaliza valores del modelo a lista.
    Evita que un string se itere carácter por carácter.
    Maneja strings con saltos \\n reales o escapados.
    """
    if value is None:
        return []

    if isinstance(value, str):
        value = value.replace("\\n", "\n").strip()
        if not value:
            return []
        lines = [x.strip(" -\t") for x in value.splitlines() if x.strip()]
        return lines if lines else [value]

    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]

    return [str(value).strip()] if str(value).strip() else []


def _list_lines(items, empty: str = "_No detectado._") -> str:
    cleaned = _as_list(items)
    if not cleaned:
        return empty
    return "\n".join(f"- {x}" for x in cleaned)


def _checkbox_lines(items, empty: str = "_Sin pendientes detectados._") -> str:
    cleaned = _as_list(items)
    if not cleaned:
        return empty
    return "\n".join(f"- [ ] {x}" for x in cleaned)


def wikilink_title(title: str) -> str:
    title = str(title).replace("[", "").replace("]", "").strip()
    return f"[[{title}]]" if title else ""


def quote_wikilink(value: str | None) -> str | None:
    """
    Normaliza wikilinks sin agregar comillas manuales.
    El YAML dumper decide cómo serializarlos.
    """
    if not value:
        return value
    return str(value).strip()


def render_reflective_session(
    *,
    extracted: dict[str, Any],
    tags: list[str],
    source_hash: str,
    model_used: str,
    original_content: str,
    review_status: str = "guided",
) -> str:
    title = extracted.get("thing_note_candidate") or "Nota reflexiva sin título"
    today = date.today().isoformat()

    possible_links = [
        wikilink_title(x)
        for x in _as_list(extracted.get("possible_links", []))
        if str(x).strip()
    ]

    frontmatter = {
        "up": [],
        "related": possible_links,
        "created": today,
        "sourceType": "reflection-spark",
        "source_hash": source_hash,
        "tags": tags,
        "ai_assisted": True,
        "ai_model": model_used,
        "ai_reviewed": False,
        "ai_review_status": review_status,
        "ai_confidence": extracted.get("confidence", "medium"),
    }

    parts = [
        _yaml_block(frontmatter),
        f"# {title}",
        "",
        "## Spark original",
        "",
        "```text",
        original_content.strip(),
        "```",
        "",
        "## Señal detectada",
        "",
        extracted.get("signal") or "_No detectado._",
        "",
        "## Por qué podría importar",
        "",
        extracted.get("why_it_matters") or "_No detectado._",
        "",
        "## Desafío de voz propia",
        "",
        extracted.get("own_voice_challenge")
        or "Explícalo con tu propio sabor, gramática y sintaxis. No copies la fuente.",
        "",
        "> Escribe aquí tu reformulación.",
        "",
        "## Validación",
        "",
        extracted.get("validation_question")
        or "¿Este concepto es lo que resonó contigo o hay algo más profundo?",
        "",
        "- [ ] Validado por mí",
        "",
        "## Conexión",
        "",
        extracted.get("connection_question") or "¿Esto a qué te recuerda?",
        "",
        "> Escribe aquí conexiones personales, notas relacionadas o ideas previas.",
        "",
        "## Posibles enlaces sugeridos",
        "",
        _list_lines(possible_links),
        "",
        "## Vacíos / cosas por aclarar",
        "",
        _checkbox_lines(extracted.get("gaps", [])),
    ]

    return "\n".join(parts).rstrip() + "\n"
