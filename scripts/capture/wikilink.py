"""Centralised wikilink picker.

Public API
----------
pick(vault_root) -> str
    Opens a fuzzy-search UI over all .md notes in vault_root.
    Returns '[[Note title]]' on selection, or '' if cancelled.

attach_wikilinks(text, vault_root) -> str
    Interactive composition loop. Starting from an initial text the user
    can keep appending free text or wikilinks until they choose 'listo'.
    Returns the final composed string.
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
    try:
        return open("/dev/tty", "r+b", buffering=0)
    except OSError:
        return None


def _gum(*args: str, input_text: str | None = None) -> tuple[int, str]:
    """Run a gum command with TTY-safe I/O. Returns (returncode, stdout)."""
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
    return "" if code in (1, 130) else selected


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
        return "" if result.returncode in (1, 130) else result.stdout.strip()
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


def attach_wikilinks(initial_text: str, vault_root: Path) -> str:
    """Composition loop: append free text or wikilinks to *initial_text*.

    Options presented each iteration:
      - añadir texto   → open gum input (or plain input) to append more text
      - añadir enlace  → open fuzzy picker and append wikilink
      - listo           → finish and return the composed string

    Nothing is printed as intermediate state; the header always shows the
    current accumulated text so the user knows what they have so far.
    """
    result = initial_text

    while True:
        preview = result if len(result) <= 60 else result[:57] + "…"

        if _gum_available():
            code, choice = _gum(
                "choose",
                "--header", f"Entrada actual: {preview}",
                "añadir texto",
                "añadir enlace",
                "listo",
            )
            if code in (1, 130):
                break
        else:
            print(f"  Entrada actual: {result}")
            print("  1. añadir texto")
            print("  2. añadir enlace")
            print("  3. listo")
            raw = input("  Opción [3]: ").strip()
            choice = {"1": "añadir texto", "2": "añadir enlace", "3": "listo", "": "listo"}.get(raw, "listo")

        if choice == "añadir texto":
            if _gum_available():
                code, extra = _gum("input", "--placeholder", "Texto adicional...")
                extra = extra if code == 0 else ""
            else:
                extra = input("Texto adicional: ").strip()
            if extra:
                result = f"{result} {extra}"

        elif choice == "añadir enlace":
            link = pick(vault_root)
            if link:
                result = f"{result} {link}"

        else:  # listo
            break

    return result
