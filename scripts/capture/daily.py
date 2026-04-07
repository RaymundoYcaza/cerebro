from __future__ import annotations

import subprocess
from datetime import date
from pathlib import Path

from config import load_config
from utils import now_date


DAILY_SECTIONS = ["Freewrite", "Big Things Today", "Log"]


def _get_vault_root() -> Path:
    config = load_config()
    return Path(config["vault_root"])


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
    """Create the daily note file if it does not exist yet."""
    if path.exists():
        return
    if today is None:
        today = date.today()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_build_empty_note(today), encoding="utf-8")


def append_to_section(path: Path, section: str, bullet: str) -> None:
    """Append a bullet to the given section, creating the section if absent."""
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()

    bullet_line = f"- {bullet}" if not bullet.startswith("- ") else bullet
    section_header = f"## {section}"

    # Find the section
    section_idx = None
    for i, line in enumerate(lines):
        if line.strip() == section_header:
            section_idx = i
            break

    if section_idx is None:
        # Section does not exist — append it at the end
        if lines and lines[-1] != "":
            lines.append("")
        lines.append(section_header)
        lines.append(bullet_line)
        lines.append("")
    else:
        # Find the end of this section (next ## or EOF)
        insert_at = len(lines)
        for i in range(section_idx + 1, len(lines)):
            if lines[i].startswith("## "):
                # Insert before this next section header
                # Walk back to skip trailing blank lines
                insert_at = i
                while insert_at > section_idx + 1 and lines[insert_at - 1].strip() == "":
                    insert_at -= 1
                break
        lines.insert(insert_at, bullet_line)

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _gum_available() -> bool:
    import shutil
    return shutil.which("gum") is not None


def _gum_choose(options: list[str], header: str = "") -> str:
    try:
        cmd = ["gum", "choose"]
        if header:
            cmd.extend(["--header", header])
        cmd.extend(options)
        output = subprocess.check_output(cmd, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        if e.returncode in (1, 130):
            return "salir"
        return ""
    except (KeyboardInterrupt, Exception):
        return "salir"


def _gum_input(placeholder: str = "") -> str:
    try:
        cmd = ["gum", "input", "--placeholder", placeholder]
        output = subprocess.check_output(cmd, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        if e.returncode in (1, 130):
            return ""
        return ""
    except (KeyboardInterrupt, Exception):
        return ""


def _choose_section() -> str:
    options = DAILY_SECTIONS + ["salir"]
    if _gum_available():
        choice = _gum_choose(options, "Selecciona la sección del diario")
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
        text = _gum_input("Escribe tu entrada...")
        return text
    return input("Entrada: ").strip()


def run_daily_capture() -> None:
    """Full daily-journal capture flow."""
    today = date.today()
    path = get_daily_path(today)

    ensure_daily_note(path, today)

    section = _choose_section()

    bullet = _ask_bullet()
    if not bullet:
        print("Entrada vacía, operación cancelada.")
        return

    append_to_section(path, section, bullet)
    print(f"\n✅ Entrada añadida en '{section}' → {path}")
