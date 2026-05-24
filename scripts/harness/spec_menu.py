#!/usr/bin/env python3
"""Interactive helper menu for spec_tools.
Provides a simple terminal UI to list specs, view progress, complete
microtasks and move specs between states without remembering long CLI
arguments.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

VALID_STATES = ["backlog", "active", "done", "cancelled"]
SPEC_ROOT = Path("specs")
SPEC_TOOLS = Path("scripts/harness/spec_tools.py")


def abort(msg: str) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(1)


def check_spec_tools() -> None:
    if not SPEC_TOOLS.is_file():
        abort("spec_tools.py not found. Please implement it before using spec_menu.")


def run_spec_tools(args: list[str]) -> subprocess.CompletedProcess:
    """Run spec_tools.py with given argument list.
    Returns CompletedProcess with stdout, stderr, returncode.
    """
    cmd = [sys.executable, str(SPEC_TOOLS)] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def list_specs(state: str) -> list[Path]:
    dir_path = SPEC_ROOT / state
    if not dir_path.is_dir():
        return []
    return sorted([p for p in dir_path.iterdir() if p.is_file() and p.suffix == ".md"])


def prompt_choice(prompt: str, choices: list[str]) -> str:
    while True:
        resp = input(prompt).strip()
        if resp in choices:
            return resp
        print(f"Invalid choice. Expected one of: {', '.join(choices)}")


def prompt_yes_no(prompt: str) -> bool:
    while True:
        resp = input(f"{prompt} [y/n]: ").strip().lower()
        if resp in {"y", "yes"}:
            return True
        if resp in {"n", "no"}:
            return False
        print("Please answer y or n.")


def display_specs(specs: list[Path]):
    if not specs:
        print("  (no specs in this state)")
        return
    cwd = Path.cwd()
    for idx, spec in enumerate(specs, start=1):
        try:
            rel = spec.relative_to(cwd)
        except ValueError:
            rel = spec
        print(f"{idx}. {rel}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="spec_menu", description="Interactive menu for spec_tools"
    )
    parser.add_argument(
        "--state",
        choices=VALID_STATES,
        default="backlog",
        help="Initial state to browse",
    )
    args = parser.parse_args()

    check_spec_tools()
    current_state = args.state
    while True:
        print(f"\n=== Specs in state: {current_state} ===")
        specs = list_specs(current_state)
        display_specs(specs)
        print("0. Cambiar estado")
        print("q. Salir")
        choice = input("Seleccione un número o comando: ").strip()
        if choice == "q":
            print("Saliendo.")
            break
        if choice == "0":
            # change state
            print("Estados disponibles:")
            for i, st in enumerate(VALID_STATES, start=1):
                print(f"{i}. {st}")
            st_choice = input("Elija estado por número o nombre: ").strip()
            # try numeric
            if st_choice.isdigit():
                idx = int(st_choice) - 1
                if 0 <= idx < len(VALID_STATES):
                    current_state = VALID_STATES[idx]
                    continue
            if st_choice in VALID_STATES:
                current_state = st_choice
                continue
            print("Opción de estado no válida.")
            continue
        if not choice.isdigit():
            print("Entrada no válida.")
            continue
        idx = int(choice) - 1
        if idx < 0 or idx >= len(specs):
            print("Número fuera de rango.")
            continue
        spec_path = specs[idx]
        # Submenu for selected spec
        while True:
            try:
                rel = spec_path.relative_to(Path.cwd())
            except ValueError:
                rel = spec_path
            print(f"\n--- Spec seleccionado: {rel} ---")
            print("1. Ver progreso")
            print("2. Completar microtarea")
            print("3. Mover a otro estado")
            print("b. Volver a lista de specs")
            sub = input("Elija acción: ").strip()
            if sub == "b":
                break
            if sub == "1":
                # progress
                res = run_spec_tools(["progress", "--spec", str(spec_path)])
                print(res.stdout)
                if res.returncode != 0:
                    print(res.stderr, file=sys.stderr)
            elif sub == "2":
                task_id = input("ID de microtarea (ej. MT-01): ").strip()
                if not task_id.upper().startswith("MT-"):
                    print("Formato de microtarea inválido.")
                    continue
                if not prompt_yes_no(
                    f"Marcar todas las checkboxes de {task_id} como completadas?"
                ):
                    continue
                res = run_spec_tools(
                    ["complete-task", "--spec", str(spec_path), "--task", task_id]
                )
                print(res.stdout)
                if res.returncode != 0:
                    print(res.stderr, file=sys.stderr)
            elif sub == "3":
                print("Estados disponibles para mover:")
                for i, st in enumerate(VALID_STATES, start=1):
                    print(f"{i}. {st}")
                dest = input("Elija estado destino: ").strip()
                if dest.isdigit():
                    d_idx = int(dest) - 1
                    if 0 <= d_idx < len(VALID_STATES):
                        dest_state = VALID_STATES[d_idx]
                    else:
                        print("Estado fuera de rango.")
                        continue
                elif dest in VALID_STATES:
                    dest_state = dest
                else:
                    print("Estado no válido.")
                    continue
                if not prompt_yes_no(f"Mover spec a '{dest_state}'?"):
                    continue
                res = run_spec_tools(
                    ["move", "--spec", str(spec_path), "--to", dest_state]
                )
                print(res.stdout)
                if res.returncode != 0:
                    print(res.stderr, file=sys.stderr)
                else:
                    # after move, refresh list and break to main loop
                    specs = list_specs(current_state)
                    break
            else:
                print("Opción no reconocida.")
        # end sub menu
    # end main loop


if __name__ == "__main__":
    main()
