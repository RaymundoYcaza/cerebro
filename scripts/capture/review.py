import re
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from config import load_config


def gum_available() -> bool:
    return shutil.which("gum") is not None


def find_tasks(efforts_dir: Path):
    tasks = []
    if not efforts_dir.exists():
        return tasks
        
    for p in efforts_dir.rglob("*.md"):
        if ".git" in p.parts: continue
        
        status = p.parent.name
        project = p.stem
        
        try:
            with open(p, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if "- [ ]" in line:
                        priority_match = re.search(r"\^(\w+)", line)
                        priority = priority_match.group(1).lower() if priority_match else "-"
                        
                        date_match = re.search(r"@(\d{4}-\d{2}-\d{2})", line)
                        task_date = date_match.group(1) if date_match else "-"
                        
                        clean_task = line.replace("- [ ]", "").strip()
                        clean_task = re.sub(r"\^\w+", "", clean_task).strip()
                        clean_task = re.sub(r"@\d{4}-\d{2}-\d{2}", "", clean_task).strip()
                        
                        tasks.append({
                            "project": project,
                            "status": status,
                            "task": clean_task,
                            "priority": priority,
                            "date": task_date,
                            "file": str(p),
                            "full_line": line.strip()
                        })
        except Exception as e:
            print(f"Error leyendo {p}: {e}")
            
    return tasks


def show_project_content(efforts_dir: Path):
    statuses = sorted([d.name for d in efforts_dir.iterdir() if d.is_dir() and not d.name.startswith(".")])
    statuses.insert(0, "(Todos)")
    
    selected_status = "(Todos)"
    if gum_available():
        result = subprocess.run(
            ["gum", "choose", "--header", "Selecciona Estado/Carpeta", *statuses],
            stdout=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            selected_status = result.stdout.strip()
        else:
            return
    else:
        print("\nEstados disponibles:")
        for i, s in enumerate(statuses):
            print(f"{i+1}. {s}")
        idx = input("Selecciona: ").strip()
        if idx.isdigit() and 1 <= int(idx) <= len(statuses):
            selected_status = statuses[int(idx)-1]

    projects = []
    search_path = efforts_dir if selected_status == "(Todos)" else efforts_dir / selected_status
    
    for p in search_path.rglob("*.md"):
        if ".git" in p.parts: continue
        rel_path = p.relative_to(efforts_dir)
        projects.append((str(rel_path), p))
    
    if not projects:
        print(f"\nNo se encontraron proyectos en {selected_status}.")
        return

    options = [p[0] for p in projects]
    selected_rel = ""
    
    if gum_available():
        result = subprocess.run(
            ["gum", "filter", "--placeholder", f"Filtrar proyectos en {selected_status}"],
            input="\n".join(options),
            stdout=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            selected_rel = result.stdout.strip()
    else:
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")
        idx = input("Selecciona ID: ").strip()
        if idx.isdigit() and 1 <= int(idx) <= len(options):
            selected_rel = options[int(idx)-1]

    if selected_rel:
        full_path = None
        for rel, path in projects:
            if rel == selected_rel:
                full_path = path
                break
        
        if full_path and full_path.exists():
            content = full_path.read_text(encoding="utf-8")
            if gum_available():
                subprocess.run(["gum", "pager"], input=content, text=True)
            else:
                print(f"\n--- CONTENIDO DE: {selected_rel} ---\n")
                print(content)
                input("\nPresiona Enter para continuar...")


def mark_done(task: dict):
    path = Path(task["file"])
    content = path.read_text(encoding="utf-8")
    old_line = task["full_line"]
    new_line = old_line.replace("- [ ]", "- [x]")
    
    new_content = content.replace(old_line, new_line)
    path.write_text(new_content, encoding="utf-8")
    print(f"\n✅ Tarea completada: {task['task']}")


def show_tasks_table(tasks: list):
    if not tasks:
        print("\nNo se encontraron tareas pendientes.")
        return None
    
    # 1. Definimos anchos constantes para sincronía total
    W_ID, W_PRIO, W_DATE, W_PROJ = 2, 9, 10, 25
    
    formatted_options = []
    for i, t in enumerate(tasks):
        prio = t['priority']
        icon = "🔴" if prio == "alta" else "🟡" if prio == "media" else "🟢" if prio == "baja" else "⚪"
        proj = t['project'][:W_PROJ]
        
        # Formateamos la fila respetando los anchos fijos
        line = f"{i:{W_ID}} | {icon} {prio:<6} | {t['date']:{W_DATE}} | {proj:{W_PROJ}} | {t['task']}"
        formatted_options.append(line)
    
    if gum_available():
        # 2. EL TRUCO: 3 espacios iniciales para compensar el indicador "• " de gum filter
        header = f"   ID | PRIORIDAD | FECHA      | PROYECTO                  | TAREA"
        
        result = subprocess.run(
            [
                "gum", "filter", 
                "--header", header, 
                "--placeholder", "Busca por proyecto, fecha o tarea... (Esc para volver)", 
                "--indicator", "•", 
                "--height", "20"
            ],
            input="\n".join(formatted_options),
            stdout=subprocess.PIPE,
            text=True
        )
        
        if result.returncode == 0 and result.stdout.strip():
            selected_row = result.stdout.strip()
            try:
                # Limpiamos el posible indicador del stdout
                clean_row = selected_row.lstrip("• ").strip()
                task_id = int(clean_row.split("|")[0].strip())
                return tasks[task_id]
            except (ValueError, IndexError):
                return None
    else:
        print(f"\nID | PRIORIDAD | FECHA      | PROYECTO                  | TAREA")
        print("-" * 100)
        for opt in formatted_options:
            print(opt)
        
        idx = input("\nID de tarea para completar (o Enter para volver): ").strip()
        if idx.isdigit() and 0 <= int(idx) < len(tasks):
            return tasks[int(idx)]
            
    return None


def run_review():
    config = load_config()
    vault_root = Path(config["vault_root"])
    efforts_dir = vault_root / "Efforts"
    
    while True:
        all_tasks = find_tasks(efforts_dir)
        
        options = [
            "Ver contenido de un Proyecto (Lectura)",
            "Todas las tareas pendientes",
            "Tareas para HOY",
            "Por Prioridad (Alta)",
            "Por Proyecto (Tareas)",
            "Volver al menú principal"
        ]
        
        choice = ""
        if gum_available():
            result = subprocess.run(
                ["gum", "choose", "--header", "REVISIÓN DE TAREAS (EFFORTS)", *options],
                stdout=subprocess.PIPE,
                text=True
            )
            choice = result.stdout.strip()
        else:
            print("\n--- REVISIÓN DE TAREAS (EFFORTS) ---")
            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")
            idx = input("Selecciona: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(options):
                choice = options[int(idx)-1]
        
        if not choice or choice == "Volver al menú principal":
            break
            
        if choice == "Ver contenido de un Proyecto (Lectura)":
            show_project_content(efforts_dir)
            continue

        filtered = []
        today = datetime.now().strftime("%Y-%m-%d")
        
        if choice == "Todas las tareas pendientes":
            filtered = all_tasks
        elif choice == "Tareas para HOY":
            filtered = [t for t in all_tasks if t["date"] == today]
        elif choice == "Por Prioridad (Alta)":
            filtered = [t for t in all_tasks if t["priority"] == "alta"]
        elif choice == "Por Proyecto (Tareas)":
            projects = sorted(list(set(t["project"] for t in all_tasks)))
            if not projects:
                print("\nNo hay proyectos con tareas pendientes.")
                if not gum_available(): input("Presiona Enter...")
                continue
                
            if gum_available():
                proj_result = subprocess.run(
                    ["gum", "filter", "--placeholder", "Selecciona proyecto", *projects],
                    stdout=subprocess.PIPE,
                    text=True
                )
                if proj_result.returncode == 0:
                    proj_choice = proj_result.stdout.strip()
                    filtered = [t for t in all_tasks if t["project"] == proj_choice]
                else:
                    continue
            else:
                for i, p in enumerate(projects): print(f"{i+1}. {p}")
                p_idx = input("ID: ").strip()
                if p_idx.isdigit() and 1 <= int(p_idx) <= len(projects):
                    filtered = [t for t in all_tasks if t["project"] == projects[int(p_idx)-1]]
        
        if filtered:
            selected_task = show_tasks_table(filtered)
            if selected_task:
                mark_done(selected_task)
                if not gum_available():
                    input("Presiona Enter para continuar...")
        else:
            print("\nNo se encontraron tareas con ese filtro.")
            if not gum_available(): input("Presiona Enter...")


if __name__ == "__main__":
    run_review()
