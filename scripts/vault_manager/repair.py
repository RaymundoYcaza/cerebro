#!/usr/bin/env python3
"""
Vault Manager repair: Reparador de Frontmatter (Estilo LYT / ACE)

- Escanea notas en el Inbox (+).
- Asegura que el frontmatter contenga: up, related, created.
- Respeta metadatos existentes.
- NO mueve notas de carpeta (el sensemaking requiere fricción manual).
"""

from __future__ import annotations
import argparse
import json
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List

VAULT_ROOT = Path("/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/vault/raymundo_ideaverse")
INBOX_DIR = VAULT_ROOT / "+"

@dataclass
class Proposal:
    relative_path: str
    action_summary: List[str]
    current_frontmatter: Dict[str, object]
    suggested_frontmatter: Dict[str, object]
    source_path: str

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def detect_frontmatter(content: str) -> Dict[str, object]:
    lines = content.splitlines()
    if len(lines) >= 3 and lines[0].strip() in ("---", "***"):
        delimiter = lines[0].strip()
        for i in range(1, len(lines)):
            if lines[i].strip() == delimiter:
                fm_lines = lines[1:i]
                result = {}
                for line in fm_lines:
                    if ":" in line:
                        k, v = line.split(":", 1)
                        k = k.strip()
                        v = v.strip()
                        # Detectar listas simples como [] o [algo]
                        if v.startswith("[") and v.endswith("]"):
                            inner = v[1:-1].strip()
                            result[k] = [x.strip() for x in inner.split(",")] if inner else []
                        else:
                            result[k] = v
                return result
    return {}

def strip_frontmatter(content: str) -> str:
    lines = content.splitlines()
    if len(lines) >= 3 and lines[0].strip() in ("---", "***"):
        delimiter = lines[0].strip()
        for i in range(1, len(lines)):
            if lines[i].strip() == delimiter:
                return "\n".join(lines[i + 1:]).lstrip()
    return content

def make_proposal(path: Path) -> Proposal:
    content = read_text(path)
    fm = detect_frontmatter(content)
    
    proposed_fm = fm.copy()
    actions = []
    
    # Reglas LYT
    if "up" not in proposed_fm:
        proposed_fm["up"] = []
        actions.append("add:up")
    if "related" not in proposed_fm:
        proposed_fm["related"] = []
        actions.append("add:related")
    if "created" not in proposed_fm:
        proposed_fm["created"] = datetime.now().strftime("%Y-%m-%d")
        actions.append("add:created")
        
    rel_path = str(path.relative_to(VAULT_ROOT))
    
    return Proposal(
        relative_path=rel_path,
        action_summary=actions,
        current_frontmatter=fm,
        suggested_frontmatter=proposed_fm,
        source_path=str(path)
    )

def render_frontmatter(fm: Dict[str, object]) -> str:
    lines = ["---"]
    # Forzamos el orden LYT sugerido al principio
    order = ["up", "related", "created"]
    keys = order + [k for k in fm.keys() if k not in order]
    
    for key in keys:
        if key not in fm: continue
        val = fm[key]
        if isinstance(val, list):
            if val:
                lines.append(f"{key}: [{', '.join(map(str, val))}]")
            else:
                lines.append(f"{key}: []")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)

def apply_proposal(proposal: Proposal, auto_yes: bool) -> bool:
    if not proposal.action_summary:
        return False
        
    src = Path(proposal.source_path)
    body = strip_frontmatter(read_text(src))
    new_content = render_frontmatter(proposal.suggested_frontmatter) + "\n\n" + body
    
    print(f"Modificando: {proposal.relative_path} ({', '.join(proposal.action_summary)})")
    
    if not auto_yes:
        ans = input("¿Aplicar cambios? [y/N]: ").strip().lower()
        if ans not in ("y", "yes"):
            return False
            
    src.write_text(new_content, encoding="utf-8")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("items", nargs="*", default=["*.md"])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--yes", action="store_true")
    parser.add_argument("--format", choices=["human", "json"], default="human")
    args = parser.parse_args()

    files = sorted(INBOX_DIR.glob("*.md"))
    proposals = [make_proposal(f) for f in files]
    
    # Filtrar notas que ya están perfectas
    proposals = [p for p in proposals if p.action_summary]

    if args.format == "json":
        print(json.dumps([asdict(p) for p in proposals], ensure_ascii=False, indent=2))
        return

    print(f"=== Notas a reparar: {len(proposals)} ===")
    for p in proposals:
        print(f"- {p.relative_path} -> Faltan: {', '.join(p.action_summary)}")

    if args.apply:
        for p in proposals:
            apply_proposal(p, args.yes)

if __name__ == "__main__":
    main()
