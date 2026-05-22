\
from __future__ import annotations

import hashlib
import re
import unicodedata
from datetime import date


def normalize_newlines(text: str) -> str:
    """Conserva líneas en blanco, solo normaliza CRLF/CR a LF."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def compact_for_prompt(text: str, max_chars: int = 12000) -> str:
    """
    Reduce texto para prompt sin destruir su estructura multilinea.
    Para modelos pequeños, evita prompts enormes.
    """
    text = normalize_newlines(text).strip()
    if len(text) <= max_chars:
        return text
    head = text[: int(max_chars * 0.65)]
    tail = text[-int(max_chars * 0.25) :]
    return f"{head}\n\n[... contenido intermedio omitido por longitud ...]\n\n{tail}"


def sha256_short(text: str, length: int = 16) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:length]


def slugify(value: str, max_len: int = 90) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return (value or f"nota-tecnica-{date.today().isoformat()}")[:max_len].strip("-")


def unique_path(path):
    path = path.__class__(path)
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    i = 2
    while True:
        candidate = parent / f"{stem}-{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def chunk_text(text: str, chunk_chars: int = 1400, overlap: int = 180) -> list[str]:
    """
    Chunking simple por caracteres, intentando cortar en saltos de párrafo.
    Suficiente para base local; luego puedes cambiarlo por chunking semántico.
    """
    text = normalize_newlines(text).strip()
    if not text:
        return []

    chunks = []
    start = 0
    n = len(text)

    while start < n:
        end = min(start + chunk_chars, n)

        if end < n:
            window = text[start:end]
            cut = max(window.rfind("\n\n"), window.rfind("\n- "), window.rfind("\n## "))
            if cut > int(chunk_chars * 0.45):
                end = start + cut

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end >= n:
            break
        start = max(0, end - overlap)

    return chunks
