"""Centralised wikilink picker.

Public API
----------
pick(vault_root) -> str
    Opens a fuzzy-search UI over all .md notes in vault_root.
    Returns '[[Note title]]' on selection, or '' if cancelled.

attach_wikilinks(text, vault_root) -> str
    Interactive loop: lets the user append zero or more wikilinks to a
    base text string and returns the final composed string.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# TTY-safe gum helper
# ---------------------------------------------------------------------------

def _tty():
    """Return an open file object for /dev/tty (the real terminal).

    This ensures gum can render its TUI even when stdout/stdin are
    redirected (e.g. inside subprocess.check_output chains).
    Falls back to sys.stdin/sys.stderr on Windows or missing /dev/tty.
    """
    try:
        return open("/dev/tty", "r+b", buffering=0)
    except OSError:
        return None


def _gum(*args: str, input_text: str | None = None) -> tuple[int, str]:
    """Run a gum command with TTY-safe I/O.

    Returns (returncode, stdout_text).
    stdin  -> /dev/tty  (so gum can read keyboard)
    stdout -> pipe      (so we can capture the selection)
    stderr -> /dev/tty  (so gum can render its UI)
    """
    tty = _tty()
    try:
        result = subprocess.run(
            ["gum", *args],
            input=input_text.encode() if input_text is not None else None,
            stdin=None if input_text is not None else (tty or sys.stdin),
            stdout=subprocess.PIPE,
            stderr=tty or sys.stderr,
            text=False,
        )
        stdout = result.stdout.decode("utf-8", errors="replace").strip()
        return result.returncode, stdout
    except (OSError, KeyboardInterrupt):
        return 130, ""
    finally:
        if tty:
            tty.close()


# ---------------------------------------------------------------------------
# Tool detection
# ---------------------------------------------------------------------------

def _gum_available() -> bool:
    return shutil.which("gum") is not None


def _fzf_available() -> bool:
    return shutil.which("fzf") is not None


# ---------------------------------------------------------------------------
# Note index
# ---------------------------------------------------------------------------

def _collect_note_titles(vault_root: Path) -> list[str]:
    """Return sorted list of note stems (filenames without .md extension)."""
    return sorted(
        p.stem
        for p in vault_root.rglob("*.md")
        if not p.stem.startswith(".")
    )


# ---------------------------------------------------------------------------
# Fuzzy picker backends
# ---------------------------------------------------------------------------

def _pick_with_gum(titles: list[str]) -> str:
    code, selected = _gum(
        "filter", "--placeholder", "Buscar nota...", "--limit", "1",
        input_text="\n".join(titles),
    )
    if code in (1, 130):
        return ""
    return selected


def _pick_with_fzf(titles: list[str]) -> str:
    try:
        tty = _tty()
        result = subprocess.run(
            ["fzf", "--prompt", "Buscar nota> "],
            input="\n".join(titles),
            stdin=None,
            stdout=subprocess.PIPE,
            stderr=tty or sys.stderr,
            text=True,
        )
        if tty:
            tty.close()
        if result.returncode in (1, 130):
            return ""
        return result.stdout.strip()
    except (OSError, KeyboardInterrupt):
        return ""


def _pick_manual(titles: list[str]) -> str:
    query = input("Buscar nota (fragmento): ").strip().lower()
    if not query:
        return ""
    matches = [t for t in titles if query in t.lower()]
    if not matches:
        print("No se encontraron notas.")
        return ""
    if len(matches) == 1:
        return matches[0]
    for i, m in enumerate(matches, start=1):
        print(f"  {i}. {m}")
    raw = input("Elige número (Enter para cancelar): ").strip()
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(matches):
            return matches[idx]
    return ""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def pick(vault_root: Path) -> str:
    """Fuzzy-pick a note and return its wikilink, e.g. '[[My Note]]'.

    Returns '' if the user cancels or no notes are found.
    """
    titles = _collect_note_titles(vault_root)
    if not titles:
        print("No se encontraron notas en la bóveda.")
        return ""

    if _gum_available():
        selected = _pick_with_gum(titles)
    elif _fzf_available():
        selected = _pick_with_fzf(titles)
    else:
        selected = _pick_manual(titles)

    return f"[[{selected}]]" if selected else ""


def attach_wikilinks(text: str, vault_root: Path) -> str:
    """Interactively append one or more wikilinks to *text*.

    Returns the final composed string.
    """
    result = text
    while True:
        if _gum_available():
            code, choice = _gum(
                "choose",
                "--header", f"Vista previa: {result}",
                "añadir enlace", "listo",
            )
            if code in (1, 130) or choice != "añadir enlace":
                break
        else:
            raw = input("¿Añadir wikilink? [s/N]: ").strip().lower()
            if raw not in ("s", "si", "sí", "y", "yes"):
                break

        link = pick(vault_root)
        if link:
            result = f"{result} {link}"
            print(f"  → {result}")

    return result
