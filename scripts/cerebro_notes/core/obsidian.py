from __future__ import annotations

import re
from pathlib import Path

from core.text_utils import slugify, unique_path


def strip_wikilink(value: str) -> str:
    text = str(value).strip().strip("'").strip('"').strip()

    if text.startswith("[[") and text.endswith("]]"):
        text = text[2:-2].strip()

    return re.sub(r"[\[\]]", "", text).strip()


def build_wikilink(title_or_path: str) -> str:
    text = strip_wikilink(title_or_path)

    if not text:
        return ""

    if "/" in text or "\\" in text or Path(text).suffix:
        text = Path(text).stem

    return f"[[{text}]]"


def wikilink_from_path(path: Path) -> str:
    return build_wikilink(Path(path).stem)


def safe_note_filename(title: str, suffix: str = ".md") -> str:
    clean_suffix = suffix if suffix.startswith(".") else f".{suffix}"
    return f"{slugify(title)}{clean_suffix}"


def unique_note_path(path: Path) -> Path:
    return unique_path(path)
