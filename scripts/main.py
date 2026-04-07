import shutil
import subprocess
import sys
from pathlib import Path

# Asegurar que el raíz del proyecto esté en PYTHONPATH
_project_root = Path(__file__).resolve().parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

try:
    from scripts.qmd_bridge import qmd_search
except ImportError:
    qmd_search = None  # type: ignore

try:
    from scripts.qmd_bridge import qmd_status  # type: ignore
except ImportError:
    qmd_status = None  # type: ignore

console = Console()

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


def show_menu():
    console.clear()
    console.print(Panel.fit(
        "🧠 [bold blue]CEREBRO v2.0[/] - (Powered by QMD)\n"
        "[dim]Conexión local y soberana establecida[/]",
        border_style="blue"
    ))

    console.print("1. [bold green]🔍 Búsqueda Híbrida (QMD)[/]")
    console.print("2. [bold magenta]📊 Auditoría de Gaps[/]")
    console.print("3. [bold cyan]✍️  Fábrica de Contenido[/]")
    console.print("4. [bold yellow]⚙️  Status del Sistema[/]")
    console.print("5. [bold red]❌ Salir[/]")


def show_content_factory_menu():
    """Sub-menú de Fábrica de Contenido."""
    console.clear()
    console.print(Panel.fit(
        "✍️  [bold cyan]Fábrica de Contenido[/]\n"
        "[dim]Selecciona el tipo de nota a crear[/]",
        border_style="cyan"
    ))

    console.print("1. [bold green]⚡ Spark[/]")
    console.print("2. [bold blue]📚 Source[/]")
    console.print("3. [bold yellow]👤 Contact[/]")
    console.print("4. [bold magenta]🌌 Aurora[/]")
    console.print("5. [bold white]📓 Daily Journal[/]")
    console.print("6. [bold cyan]🔧 Utilitarios[/]")
    console.print("7. [bold red]⬅️  Volver al menú principal[/]")


def run_utility_capture():
    """Ejecuta la captura de nota tipo Utilitarios."""
    from scripts.capture.utilities import run_utility_capture, get_subfolders

    subfolders = get_subfolders()
    if not subfolders:
        console.print("[red]No se encontraron subcarpetas en Atlas/Utilities/[/]")
        input("\nPresiona Enter para volver...")
        return

    try:
        note_path = run_utility_capture()
        console.print(f"\n[bold green]✅ Nota guardada en:[/] {note_path}")
    except SystemExit:
        pass
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")

    input("\nPresiona Enter para volver...")


def content_factory_menu():
    """Loop del sub-menú de Fábrica de Contenido."""
    while True:
        show_content_factory_menu()
        choice = Prompt.ask(
            "\nSelecciona tipo de nota",
            choices=["1", "2", "3", "4", "5", "6", "7"],
        )

        if choice == "6":
            run_utility_capture()
        elif choice == "7":
            break
        else:
            console.print(f"[yellow]Opción '{choice}' en desarrollo.[/]")
            input("\nPresiona Enter para volver...")

def main():
    while True:
        show_menu()
        choice = Prompt.ask("\n¿Qué quieres hacer?", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            # Aquí llamaremos a una función de búsqueda similar a search_advanced.py
            pass
        elif choice == "3":
            content_factory_menu()
        elif choice == "4":
            if qmd_status:
                qmd_status()
            else:
                console.print("[yellow]qmd_status no disponible. Verifica qmd_bridge.py[/]")
            input("\nPresiona Enter para volver...")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()