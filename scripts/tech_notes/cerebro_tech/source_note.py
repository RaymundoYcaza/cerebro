from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import shutil

import yaml

from .text_utils import unique_path


REQUIRED_SOURCE_TAGS = ["note/extract", "source/clips"]


def split_frontmatter(content: str) -> tuple[dict, str]:
    """
    Devuelve (frontmatter, body).
    Si no hay frontmatter YAML, devuelve ({}, contenido completo).
    """
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


def build_frontmatter(data: dict) -> str:
    return "---\n" + yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip() + "\n---\n\n"


def ensure_source_frontmatter(source_path: Path) -> None:
    """
    Asegura que la nota fuente tenga frontmatter de source clip,
    preservando contenido original y propiedades existentes útiles.
    """
    content = source_path.read_text(encoding="utf-8")
    data, body = split_frontmatter(content)

    data.setdefault("up", [])
    data.setdefault("related", [])
    data.setdefault("created", date.today().isoformat())
    data.setdefault("sourceType", None)

    tags = data.get("tags")
    if not isinstance(tags, list):
        tags = []

    for tag in REQUIRED_SOURCE_TAGS:
        if tag not in tags:
            tags.append(tag)

    data["tags"] = tags

    source_path.write_text(build_frontmatter(data) + body.lstrip("\n"), encoding="utf-8")


def move_source_note_to_sources(source_path: str | None, sources_dir: Path) -> Path | None:
    """
    Solo se debe llamar en modo write.
    Asegura frontmatter y mueve la fuente a Atlas/Dots/Sources.
    """
    if not source_path:
        return None

    src = Path(source_path)

    if not src.exists():
        raise FileNotFoundError(f"No existe la nota fuente: {src}")

    sources_dir.mkdir(parents=True, exist_ok=True)

    ensure_source_frontmatter(src)

    dst = unique_path(sources_dir / src.name)
    shutil.move(str(src), str(dst))

    return dst
