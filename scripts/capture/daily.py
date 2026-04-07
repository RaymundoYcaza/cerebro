from __future__ import annotations

import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

from config import load_config
from wikilink import attach_wikilinks


DAILY_SECTIONS = ["Freewrite", "Big Things Today", "Log"]


def _get_vault_root() -> Path:
    config = load_config()
    return Path(config["vault_root"])


def _tty():
    try:
        return open("/dev/tty", "r+b", buffering=0)
    except OSError:
        return None


def _gum(*args: str, input_text: str | None = None) -> tuple[int, str]:
    """TTY-safe gum runner. Returns (returncode, stdout)."""
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


def _gum_available() -> bool:
    return shutil.which("gum") is not None


def get_daily_path(today: date | None = None) -> Path:
    if today is None:
        today = date.today()
    date_str = today.strftime("%Y-%m-%d")
    vault_root = _get_vault_root()
    return vault_root / "Calendar" / f"{date_str}.md"


def _build_empty_note(today: date) -> str:
    date_str = today.strftime("%Y-%m-%d")
    lines = [
        "---",
        "up: []",
        "related: []",
        f"created: {date_str}",
        "---",
        "",
    ]
    for section in DAILY_SECTIONS:
        lines.append(f"## {section}")
        lines.append("")
    return "\n".join(lines)


def ensure_daily_note(path: Path, today: date | None = None) -> None:
    if path.exists():
        return
    if today is None:
        today = date.today()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_build_empty_note(today), encoding="utf-8")


def append_to_section(path: Path, section: str, bullet: str) -> None:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()

    bullet_line = f"- {bullet}" if not bullet.startswith("- ") else bullet
    section_header = f"## {section}"

    section_idx = None
    for i, line in enumerate(lines):
        if line.strip() == section_header:
            section_idx = i
            break

    if section_idx is None:
        if lines and lines[-1] != "":
            lines.append("")
        lines.append(section_header)
        lines.append(bullet_line)
        lines.append("")
    else:
        insert_at = len(lines)
        for i in range(section_idx + 1, len(lines)):
            if lines[i].startswith("## "):
                insert_at = i
                while insert_at > section_idx + 1 and lines[insert_at - 1].strip() == "":
                    insert_at -= 1
                break
        lines.insert(insert_at, bullet_line)

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _choose_section() -> str:
    options = DAILY_SECTIONS + ["salir"]
    if _gum_available():
        code, choice = _gum("choose", "--header", "Selecciona la sección del diario", *options)
        if code in (1, 130) or choice == "salir":
            raise SystemExit(0)
        if choice in DAILY_SECTIONS:
            return choice
        raise SystemExit(0)

    print("Secciones disponibles:")
    for i, s in enumerate(DAILY_SECTIONS, start=1):
        print(f"  {i}. {s}")
    print(f"  {len(DAILY_SECTIONS) + 1}. salir")
    raw = input("Elige sección: ").strip()
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(DAILY_SECTIONS):
            return DAILY_SECTIONS[idx]
        raise SystemExit(0)
    if raw in DAILY_SECTIONS:
        return raw
    raise SystemExit(0)


def _ask_bullet() -> str:
    if _gum_available():
        code, text = _gum("input", "--placeholder", "Escribe tu entrada...")
        if code in (1, 130):
            return ""
        return text
    return input("Entrada: ").strip()


def run_daily_capture() -> None:
    today = date.today()
    path = get_daily_path(today)
    vault_root = _get_vault_root()

    ensure_daily_note(path, today)

    section = _choose_section()

    bullet = _ask_bullet()
    if not bullet:
        print("Entrada vacía, operación cancelada.")
        return

    bullet = attach_wikilinks(bullet, vault_root)

    append_to_section(path, section, bullet)
    print(f"\n✅ Entrada añadida en '{section}' → {path}")
