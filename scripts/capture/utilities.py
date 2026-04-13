import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Asegurar que el directorio actual esté en el path
sys.path.append(str(Path(__file__).resolve().parent))

from config import load_config
from utils import slugify, now_date, write_note


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


def get_utilities_dir():
    config = load_config()
    vault_root = Path(config["vault_root"])
    return vault_root / "Atlas" / "Utilities"


def get_subfolders() -> list[str]:
    """Devuelve lista de subcarpetas existentes en Atlas/Utilities/."""
    utilities_dir = get_utilities_dir()
    if not utilities_dir.exists():
        utilities_dir.mkdir(parents=True, exist_ok=True)
        return []
    return sorted(
        p.name for p in utilities_dir.iterdir() if p.is_dir()
    )


def ask_title() -> str:
    if gum_available():
        code, title = _gum("input", "--header", "Título de la nota", "--placeholder", "Ej: Comando útil de git")
        if code == 0 and title:
            return title
    try:
        return input("Título: ").strip()
    except (EOFError, KeyboardInterrupt):
        raise SystemExit(0)


def ask_body() -> str:
    if gum_available():
        code, body = _gum("write", "--header", "Cuerpo de la nota", "--placeholder", "Describe la nota...", "--width", "80", "--height", "15")
        if code == 0 and body:
            return body

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
    utilities_dir = get_utilities_dir()

    if not subfolders:
        print(f"Aviso: No se encontraron subcarpetas en {utilities_dir}. Se guardará en la raíz de Utilities.")
        subfolder = ""
    else:
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
    target_dir = utilities_dir / subfolder
    note_path = target_dir / filename
    write_note(note_path, content)

    return str(note_path)
