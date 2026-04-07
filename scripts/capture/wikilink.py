"""Centralised wikilink picker.

Public API
----------
pick(vault_root) -> str
    Opens a fuzzy-search UI over all .md notes in vault_root.
    Returns '[[Note title]]' on selection, or '' if cancelled.

attach_wikilinks(text, vault_root) -> str
    Interactive loop: given a base text string, lets the user append
    zero or more wikilinks to it and returns the final composed string.
    Designed to be called right after the user types a bullet/entry.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


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
        if not p.stem.startswith(".")  # skip hidden files
    )


# ---------------------------------------------------------------------------
# Fuzzy picker backends
# ---------------------------------------------------------------------------

def _pick_with_gum(titles: list[str]) -> str:
    """Use `gum filter` for fuzzy search. Returns selected title or ''."""
    try:
        result = subprocess.run(
            ["gum", "filter", "--placeholder", "Buscar nota...", "--limit", "1"],
            input="\n".join(titles),
            capture_output=True,
            text=True,
        )
        if result.returncode in (1, 130):
            return ""
        return result.stdout.strip()
    except (OSError, KeyboardInterrupt):
        return ""


def _pick_with_fzf(titles: list[str]) -> str:
    """Use `fzf` as fallback fuzzy finder. Returns selected title or ''."""
    try:
        result = subprocess.run(
            ["fzf", "--prompt", "Buscar nota> "],
            input="\n".join(titles),
            capture_output=True,
            text=True,
        )
        if result.returncode in (1, 130):
            return ""
        return result.stdout.strip()
    except (OSError, KeyboardInterrupt):
        return ""


def _pick_manual(titles: list[str]) -> str:
    """Plain-text fallback: substring search + numbered selection."""
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
    """Fuzzy-pick a note and return its wikilink string, e.g. '[[My Note]]'.

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

    if not selected:
        return ""
    return f"[[{selected}]]"


def attach_wikilinks(text: str, vault_root: Path) -> str:
    """Interactively append one or more wikilinks to *text*.

    After each selection the user is asked whether to add another link.
    Returns the final composed string.
    """
    result = text
    while True:
        # Ask if the user wants to attach a wikilink
        if _gum_available():
            try:
                choice = subprocess.run(
                    ["gum", "choose", "--header", f"Texto: {result}",
                     "añadir enlace", "listo"],
                    capture_output=True, text=True,
                ).stdout.strip()
            except (OSError, KeyboardInterrupt):
                break
            if choice != "añadir enlace":
                break
        else:
            raw = input("¿Añadir wikilink? [s/N]: ").strip().lower()
            if raw not in ("s", "si", "sí", "y", "yes"):
                break

        link = pick(vault_root)
        if link:
            result = f"{result} {link}"
            print(f"  → {result}")
        else:
            print("  (sin selección, intenta de nuevo o elige 'listo')")

    return result
