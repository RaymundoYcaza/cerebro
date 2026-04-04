import sys
import os
import subprocess
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from pathlib import Path

# Configurar acceso a módulos hermanos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.core_config import QMD_JS_PATH, MODEL_REASONING, LLM_PROVIDER
from scripts.qmd_bridge import qmd_search
import ollama

console = Console()

def get_obsidian_link(file_path):
    # Ajustamos el link para tu bóveda específica
    vault_name = "raymundo_ideaverse"
    # QMD suele devolver rutas relativas o absolutas, limpiamos para Obsidian
    rel_path = os.path.basename(file_path) 
    return f"obsidian://open?vault={vault_name}&file={rel_path}"

def search_loop():
    while True:
        console.clear()
        console.print(Panel("[bold green]🔍 BUSCADOR HÍBRIDO CEREBRO v2.0[/]\n[dim]QMD Engine + Ollama Remote Reasoning[/]", border_style="green"))
        
        query = console.input("\n[bold yellow]¿Qué buscas? (o 'exit' para volver): [/bold yellow]")
        if query.lower() in ['exit', 'quit', 'q']: break

        console.print("[dim]Consultando índices locales...[/]")
        
        # Ejecutamos la búsqueda vía QMD
        # Usamos --intent para que QMD use su expansión interna
        results = qmd_search(query, limit=7)

        if not results or "error" in results:
            console.print("[red]No se encontraron resultados o hubo un error en QMD.[/red]")
            console.input("\nPresiona Enter para intentar de nuevo...")
            continue

        # Mostrar Tabla de Resultados (Estilo similar a tu cerebro.py anterior)
        table = Table(title=f"Resultados para: {query}", show_lines=True, expand=True)
        table.add_column("Score", justify="center", style="cyan", no_wrap=True)
        table.add_column("Documento", style="white")
        table.add_column("Snippet / Contexto", style="dim")

        context_for_llm = ""
        
        for res in results:
                    # En QMD 2.0, los campos son 'score', 'path' y 'snippet'
                    score_val = res.get('score', 0)
                    score_str = f"{score_val:.3f}"
                    full_path = res.get('path', 'Sin ruta')
                    filename = os.path.basename(full_path)
                    snippet = res.get('snippet', 'Sin vista previa disponible').replace("\n", " ")
                    
                    obs_link = get_obsidian_link(full_path)
                    
                    # Formateamos la fila igual que en tu antiguo Cerebro
                    table.add_row(
                        score_str, 
                        f"[bold white]{filename}[/]\n[dim blue]{obs_link}[/]", 
                        f"[grey50]{snippet[:200]}...[/]"
                    )
                    
                    context_for_llm += f"DOCUMENTO: {filename}\nCONTENIDO: {snippet}\n---\n"

        console.print(table)

        # 2. Análisis con el Servidor Remoto (Ubuntu 192.168.100.81)
        if context_for_llm:
            confirm = console.input("\n[bold magenta]¿Deseas que el servidor analice estos hallazgos? (s/n): [/bold magenta]")
            
            if confirm.lower() == 's':
                prompt = f"""
                Actúa como el Sistema Cerebro. Basándote en los siguientes fragmentos de mi bóveda, 
                responde a la pregunta: "{query}"
                
                Contexto recuperado:
                {context_for_llm}
                
                Instrucciones: Sé directo, técnico y cita el nombre del archivo si es relevante.
                """
                
                console.print(f"\n[bold blue]🧠 Cerebro ({MODEL_REASONING}) pensando en el servidor...[/bold blue]")
                
                # Aquí usamos la IP del servidor que definimos en tu arquitectura
                client = ollama.Client(host='http://192.168.100.81:11434')
                
                try:
                    stream = client.chat(
                        model=MODEL_REASONING,
                        messages=[{'role': 'user', 'content': prompt}],
                        stream=True,
                    )
                    
                    console.print(Panel.fit("[bold white]Respuesta Integrada:[/bold white]", border_style="magenta"))
                    for chunk in stream:
                        console.print(chunk['message']['content'], end="")
                    print("\n")
                    console.input("[dim]Presiona Enter para continuar...[/]")
                except Exception as e:
                    console.print(f"[red]Error conectando con el servidor Ubuntu: {e}[/red]")
                    console.input("\nPresiona Enter...")

if __name__ == "__main__":
    search_loop()