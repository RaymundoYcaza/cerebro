#!/usr/bin/env python3
"""
Analiza el Inbox y propone categorización y frontmatter.
No edita el vault, solo muestra recomendaciones.
"""

import os
import sys
from pathlib import Path
import re
from datetime import datetime
from typing import List, Dict, Tuple

VAULT_DIR = Path("/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/vault/raymundo_ideaverse")
INBOX_DIR = VAULT_DIR / "+"
DOTS_DIR = VAULT_DIR / "Atlas" / "Dots"
MAPS_DIR = VAULT_DIR / "Atlas" / "Maps"

def detect_frontmatter(path: Path) -> Dict[str, str]:
    try:
        content = path.read_text("utf-8")
        # Busca el bloque ***
        parts = re.split(r"^\*\*\*$", content, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm = parts[1].strip()
            result = {}
            for line in fm.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    result[k.strip()] = v.strip()
            return result
    except Exception:
        pass
    return {}

def suggest_type(path: Path, fm: Dict[str, str]) -> str:
    title = fm.get("title", "").lower()
    if ".md" not in path.name:
        return "misc_file"
    if "daily" in title or "diario" in title:
        return "daily"
    if "effort" in title or "proyecto" in title or "area" in title:
        return "effort"
    if "map" in title or "moc" in title:
        return "moc"
    return "atom"

def report_on_inbox():
    print("=== VAULT MANAGER: INBOX ANALYSIS ===\n")
    for path in sorted(INBOX_DIR.glob("*.md")):
        fm = detect_frontmatter(path)
        note_type = suggest_type(path, fm)

        print(f"File: {path}")
        if fm:
            print(f"  Frontmatter: {fm}")
        else:
            print("  Frontmatter: None")

        print(f"  Suggested type: {note_type}")

        if note_type == "atom":
            print(f"  Suggested destination: {DOTS_DIR}")

        if note_type in ("moc", "map"):
            print(f"  Suggested destination: {MAPS_DIR}")

        print()

        print("  Example frontmatter proposal:")
        print("  ---")
        print(f"  title: {path.stem}")
        print("  tags: [energy, tech]")
        print(f"  created: {datetime.now().strftime('%Y-%m-%d')}")
        print(f"  type: {note_type}")
        print("  ---")

        print("-" * 80)

report_on_inbox()
