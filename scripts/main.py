from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from scripts.qmd_bridge import qmd_status

console = Console()

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

def main():
    while True:
        show_menu()
        choice = Prompt.ask("\n¿Qué quieres hacer?", choices=["1", "2", "3", "4", "5"])
        
        if choice == "1":
            # Aquí llamaremos a una función de búsqueda similar a search_advanced.py
            pass
        elif choice == "4":
            qmd_status()
            input("\nPresiona Enter para volver...")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()