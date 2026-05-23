from __future__ import annotations

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.obsidian import build_wikilink, safe_note_filename, strip_wikilink, unique_note_path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(build_wikilink("Nota limpia") == "[[Nota limpia]]", "build_wikilink debe envolver títulos")
    require(build_wikilink("[[Nota limpia]]") == "[[Nota limpia]]", "build_wikilink debe conservar wikilinks")
    require(build_wikilink("/tmp/Mi Nota.md") == "[[Mi Nota]]", "build_wikilink debe usar stem para paths")
    require(strip_wikilink("'[[Nota limpia]]'") == "Nota limpia", "strip_wikilink debe quitar comillas y brackets")
    require(safe_note_filename("Título con acento") == "titulo-con-acento.md", "safe_note_filename debe slugificar")
    require(safe_note_filename("Título", "txt") == "titulo.txt", "safe_note_filename debe normalizar sufijo")

    with TemporaryDirectory() as tmp:
        base = Path(tmp) / "nota.md"
        require(unique_note_path(base) == base, "unique_note_path debe devolver ruta libre")
        base.write_text("x", encoding="utf-8")
        require(unique_note_path(base).name == "nota-2.md", "unique_note_path debe evitar colisiones")

    print("OK: obsidian smoke")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: obsidian smoke: {exc}", file=sys.stderr)
        raise SystemExit(1)
