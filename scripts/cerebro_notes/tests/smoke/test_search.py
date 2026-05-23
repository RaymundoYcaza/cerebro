from __future__ import annotations

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.search import find_markdown_notes, score_file


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        target = root / "Usar Dataclass para estructuras limpias.md"
        other = root / "Stack MERN.md"
        nested = root / "inbox" / "Estadistica descriptiva.md"
        ignored = root / "nota.txt"

        nested.parent.mkdir()
        target.write_text("# Dataclass", encoding="utf-8")
        other.write_text("# MERN", encoding="utf-8")
        nested.write_text("# Estadistica", encoding="utf-8")
        ignored.write_text("no markdown", encoding="utf-8")

        require(score_file("dataclass", target) == 1.0, "score_file debe puntuar match directo por nombre")
        require(score_file("", target) == 0.0, "score_file debe devolver 0 con query vacía")
        require(score_file("estadistica", nested) > score_file("mern", nested), "score_file debe favorecer nombres cercanos")

        results = find_markdown_notes(root, "dataclass")
        require(results and results[0] == target, "find_markdown_notes debe encontrar el markdown esperado")
        require(ignored not in results, "find_markdown_notes no debe incluir archivos no markdown")

        limited = find_markdown_notes(root, "stack", limit=1)
        require(len(limited) == 1 and limited[0] == other, "find_markdown_notes debe respetar limit")

    print("OK: search smoke")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: search smoke: {exc}", file=sys.stderr)
        raise SystemExit(1)
