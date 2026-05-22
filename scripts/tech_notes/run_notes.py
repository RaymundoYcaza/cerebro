#!/usr/bin/env python3

from pathlib import Path
from difflib import SequenceMatcher
import subprocess
import sys

BASE_DIR = Path("/mnt/c/cerebro/scripts/tech_notes")
CONFIG_PATH = BASE_DIR / "config.yaml"
SEARCH_ROOT = Path("/mnt/c/cerebro/vault/raymundo_ideaverse/+")


def score(query: str, text: str) -> float:
    q = query.lower().strip()
    t = text.lower().strip()

    if not q:
        return 0

    filename_score = SequenceMatcher(None, q, t).ratio()

    bonus = 0
    for part in q.split():
        if part in t:
            bonus += 0.15

    if q in t:
        bonus += 0.5

    return filename_score + bonus


def find_notes(query: str, limit: int = 10):
    files = list(SEARCH_ROOT.rglob("*.md"))

    scored = []
    for file in files:
        rel = file.relative_to(SEARCH_ROOT)
        searchable = f"{file.stem} {rel.as_posix()}"
        scored.append((score(query, searchable), file))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [(s, f) for s, f in scored[:limit] if s > 0]


def ask_mode() -> tuple[str, str]:
    print("\nModo de escritura:")
    print("1) dry-run [default]")
    print("2) write")
    write_choice = input("> ").strip()

    mode = "--write" if write_choice == "2" else "--dry-run"

    print("\nModo de razonamiento:")
    print("1) nothink [default]")
    print("2) think")
    think_choice = input("> ").strip()

    think = "--think" if think_choice == "2" else "--nothink"

    return mode, think


def run_cli(note_path: Path, mode: str, think: str):
    cmd = [
        sys.executable,
        "-m",
        "cerebro_tech.cli",
        "--input",
        str(note_path),
        "--config",
        str(CONFIG_PATH),
        mode,
        think,
    ]

    print("\nEjecutando:\n")
    print(" ".join(f"'{x}'" if " " in x else x for x in cmd))
    print()

    subprocess.run(cmd, cwd=BASE_DIR)


def main():
    if not SEARCH_ROOT.exists():
        print(f"No existe SEARCH_ROOT: {SEARCH_ROOT}")
        sys.exit(1)

    if not CONFIG_PATH.exists():
        print(f"No existe config.yaml: {CONFIG_PATH}")
        sys.exit(1)

    while True:
        query = input("\nBuscar nota en '+': ").strip()

        if query.lower() in {"q", "quit", "exit", "salir"}:
            return

        results = find_notes(query)

        if not results:
            print("Sin resultados. Refina la búsqueda.")
            continue

        print("\nResultados:")
        for i, (s, file) in enumerate(results, start=1):
            rel = file.relative_to(SEARCH_ROOT)
            print(f"{i}) [{s:.2f}] {rel}")

        print("\nElige número, 'r' para refinar o 'q' para salir.")
        choice = input("> ").strip().lower()

        if choice in {"q", "quit", "exit", "salir"}:
            return

        if choice in {"r", ""}:
            continue

        if not choice.isdigit():
            print("Opción inválida.")
            continue

        index = int(choice) - 1

        if index < 0 or index >= len(results):
            print("Número fuera de rango.")
            continue

        selected = results[index][1]
        print(f"\nSeleccionado: {selected}")

        mode, think = ask_mode()
        run_cli(selected, mode, think)
        return


if __name__ == "__main__":
    main()
