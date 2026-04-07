import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Asegurar que el raíz del proyecto esté en PYTHONPATH
_project_root = Path(__file__).resolve().parent.parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from scripts.capture.utils import slugify, now_date, write_note

VAULT_ROOT = Path("/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/vault/raymundo_ideaverse")
UTILITIES_DIR = VAULT_ROOT / "Atlas" / "Utilities"


def _tty():
    try:
        return open("/dev/tty", "r+b", buffering=0)
    except OSError:
        return None


def _gum(*args: str, input_text: str | None = None) -> tuple[int, str]:
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


def gum_available() -> bool:
    return shutil.which("gum") is not None


def get_subfolders() -> list[str]:
    """Devuelve lista de subcarpetas existentes en Atlas/Utilities/."""
    if not UTILITIES_DIR.exists():
        return []
    return sorted(
        p.name for p in UTILITIES_DIR.iterdir() if p.is_dir()
    )


def ask_title() -> str:
    if gum_available():
        code, title = _gum("input", "--header", "Título de la nota", "--placeholder", "Ej: Comando útil de git")
        if code == 0 and title:
            return title
    # Fallback manual
    try:
        return input("Título: ").strip()
    except (EOFError, KeyboardInterrupt):
        raise SystemExit(0)


def ask_body() -> str:
    if gum_available():
        code, body = _gum("write", "--header", "Cuerpo de la nota", "--placeholder", "Describe la nota...", "--width", "80", "--height", "15")
        if code == 0 and body:
            return body

    # Fallback manual con sentinel
    print("\nCuerpo de la nota (Ctrl+D o línea con 'EOF' para terminar):")
    lines = []
    try:
        while True:
            line = input()
            if line.strip() == "EOF":
                break
            lines.append(line)
    except EOFError:
        pass
    return "\n".join(lines).strip()


def run_utility_capture() -> str:
    """Flujo completo de captura de nota tipo Utilitarios."""
    subfolders = get_subfolders()
    if not subfolders:
        raise RuntimeError(f"No se encontraron subcarpetas en {UTILITIES_DIR}")

    # Seleccionar subcarpeta
    if gum_available():
        code, choice = _gum("choose", "--header", "¿Dónde guardar la nota?", *subfolders)
        if code in (1, 130) or not choice:
            raise SystemExit(0)
        subfolder = choice
    else:
        print("Subcarpetas disponibles:")
        for i, sf in enumerate(subfolders, start=1):
            print(f"  {i}. {sf}")
        while True:
            try:
                raw = input("Selecciona subcarpeta [1]: ").strip()
                if not raw:
                    idx = 0
                elif raw.isdigit():
                    idx = int(raw) - 1
                else:
                    continue
                if 0 <= idx < len(subfolders):
                    subfolder = subfolders[idx]
                    break
            except (EOFError, KeyboardInterrupt):
                raise SystemExit(0)

    # Pedir título y cuerpo
    title = ask_title()
    if not title:
        title = "untitled"
    body = ask_body()

    # Generar frontmatter y contenido
    created = now_date()
    frontmatter = f"---\nup: []\nrelated: []\ncreated: {created}\n---\n\n"
    content = f"{frontmatter}# {title}\n\n{body}\n"

    # Guardar nota
    filename = f"{slugify(title)}.md"
    target_dir = UTILITIES_DIR / subfolder
    note_path = target_dir / filename
    write_note(note_path, content)

    return str(note_path)
