from datetime import datetime
from pathlib import Path

from config import load_config
from efforts.models import EffortTask, TaskQuery
from efforts.mutate import change_task_priority, mark_task_done, reschedule_task
from efforts.repository import find_tasks, list_projects, list_statuses
from menus import ask_date, ask_text, choose_one, filter_one, pager

NO_PRIORITY_OPTION = "(sin prioridad)"


def _efforts_dir() -> Path:
    config = load_config()
    return Path(config["vault_root"]) / "Efforts"


def open_project(project_path: Path) -> None:
    content = project_path.read_text(encoding="utf-8")
    pager(content, header=f"Proyecto: {project_path.parent.name} / {project_path.stem}")


def _format_task(task: EffortTask) -> str:
    subproject = task.subproject or "-"
    priority = task.priority or "-"
    scheduled_date = task.scheduled_date or "-"
    return f"{task.status:<10} | {task.project:<24} | {subproject:<20} | {scheduled_date:<10} | {priority:<5} | {task.text}"


def _select_task(tasks: list[EffortTask]) -> EffortTask | None:
    if not tasks:
        print("\nNo se encontraron tareas pendientes.")
        return None
    header = "ESTADO     | PROYECTO                 | SUBPROYECTO          | FECHA      | PRIO  | TAREA"
    options = [_format_task(task) for task in tasks]
    selected = filter_one(options, "Busca por proyecto, estado o tarea", header=header)
    if not selected:
        return None
    return tasks[options.index(selected)]


def _select_project() -> str | None:
    projects = list_projects(_efforts_dir())
    if not projects:
        print("\nNo hay proyectos con tasks registradas.")
        return None
    options = [f"{project.status} / {project.title}" for project in projects]
    selected = filter_one(options, "Selecciona proyecto")
    if not selected:
        return None
    return projects[options.index(selected)].title


def _build_query(choice: str, initial_project: str | None = None) -> TaskQuery:
    today = datetime.now().strftime("%Y-%m-%d")
    if initial_project:
        return TaskQuery(project=initial_project)
    if choice == "Hoy":
        return TaskQuery(scheduled_date=today)
    if choice == "Alta prioridad":
        return TaskQuery(priority="alta")
    if choice == "Por proyecto":
        project = _select_project()
        return TaskQuery(project=project) if project else TaskQuery(text="__no_results__")
    if choice == "Por estado":
        statuses = list_statuses(_efforts_dir())
        status = choose_one("Selecciona estado", statuses + ["volver"], "volver")
        return TaskQuery(status=status) if status and status != "volver" else TaskQuery(text="__no_results__")
    if choice == "Buscar texto":
        text = ask_text("Texto a buscar")
        return TaskQuery(text=text) if text else TaskQuery(text="__no_results__")
    return TaskQuery()


def _act_on_task(task: EffortTask) -> None:
    while True:
        action = choose_one(
            "Acción sobre la tarea",
            ["Marcar done", "Reprogramar", "Cambiar prioridad", "Abrir proyecto", "Volver"],
            "Volver",
        )
        if action == "Marcar done":
            mark_task_done(task)
            print(f"\n✅ Tarea completada: {task.text}")
            return
        if action == "Reprogramar":
            new_date = ask_date("Nueva fecha (YYYY-MM-DD, vacío = quitar)", "", "task_date")
            reschedule_task(task, new_date or None)
            print("\n✅ Fecha actualizada.")
            return
        if action == "Cambiar prioridad":
            priority = choose_one("Nueva prioridad", ["alta", "media", "baja", NO_PRIORITY_OPTION], NO_PRIORITY_OPTION)
            change_task_priority(task, None if priority in ("", NO_PRIORITY_OPTION) else priority)
            print("\n✅ Prioridad actualizada.")
            return
        if action == "Abrir proyecto":
            open_project(task.file)
            continue
        return


def run_review(initial_project: str | None = None) -> None:
    while True:
        if initial_project:
            tasks = find_tasks(_efforts_dir(), TaskQuery(project=initial_project))
            selected = _select_task(tasks)
            if selected:
                _act_on_task(selected)
            return

        choice = choose_one(
            "CONSULTAR TAREAS",
            ["Hoy", "Alta prioridad", "Por proyecto", "Por estado", "Todas", "Buscar texto", "Volver"],
            "Hoy",
        )
        if not choice or choice == "Volver":
            return

        query = _build_query(choice)
        tasks = find_tasks(_efforts_dir(), query)
        selected = _select_task(tasks)
        if selected:
            _act_on_task(selected)
