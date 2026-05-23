from __future__ import annotations

from difflib import SequenceMatcher
from pathlib import Path


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


def find_markdown_notes(base_dir: Path, query: str, limit: int = 12) -> list[Path]:
    candidates = [p for p in base_dir.rglob("*.md") if p.is_file()]

    scored = [
        (score_file(query, p), p)
        for p in candidates
    ]

    scored.sort(key=lambda x: x[0], reverse=True)

    return [p for score, p in scored[:limit] if score > 0.15]


def choose_note_interactive(base_dir: Path, query: str | None = None) -> Path:
    while True:
        if not query:
            query = input("Buscar nota en '+': ").strip()

        results = find_markdown_notes(base_dir, query)

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
