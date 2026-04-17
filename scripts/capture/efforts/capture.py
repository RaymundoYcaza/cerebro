from pathlib import Path

from config import load_config
from efforts import STATUS_OPTIONS
from efforts.mutate import append_task, create_project, create_subproject
from efforts.repository import get_project, list_projects
from efforts.review import open_project, run_review
from menus import ask_date, ask_text, choose_one, confirm, filter_one

ROOT_OPTION = "(Raíz)"
NEW_PROJECT_OPTION = "Proyecto nuevo"
EXISTING_PROJECT_OPTION = "Proyecto existente"
NEW_SUBPROJECT_OPTION = "Nuevo subproyecto"
NO_PRIORITY_OPTION = "(sin prioridad)"


def _efforts_dir() -> Path:
    config = load_config()
    return Path(config["vault_root"]) / "Efforts"


def _choose_project_path() -> Path | None:
    projects = list_projects(_efforts_dir())
    if not projects:
        print("\nNo hay proyectos existentes. Se creará uno nuevo.")
        return None

    options = [f"{project.status} / {project.title}" for project in projects]
    selected = filter_one(options, "Selecciona proyecto")
    if not selected:
        return None

    return projects[options.index(selected)].path


def _choose_subproject(project_path: Path) -> str | None:
    project = get_project(project_path)
    options = [ROOT_OPTION, *project.subprojects, NEW_SUBPROJECT_OPTION]
    selected = choose_one("Selecciona ubicación de la tarea", options, ROOT_OPTION)
    if not selected:
        return None
    if selected == ROOT_OPTION:
        return ROOT_OPTION
    if selected == NEW_SUBPROJECT_OPTION:
        name = ask_text("Nombre del nuevo subproyecto")
        if not name:
            return None
        create_subproject(project_path, name)
        return name
    return selected


def _choose_priority() -> str | None:
    options = ["alta", "media", "baja", NO_PRIORITY_OPTION]
    selected = choose_one("Prioridad", options, NO_PRIORITY_OPTION)
    if selected in ("", NO_PRIORITY_OPTION):
        return None
    return selected


def run_capture_task() -> None:
    efforts_dir = _efforts_dir()
    context = choose_one(
        "CAPTURAR TAREA",
        [EXISTING_PROJECT_OPTION, NEW_PROJECT_OPTION, "volver"],
        EXISTING_PROJECT_OPTION,
    )
    if not context or context == "volver":
        return

    created = ""
    project_path = None
    if context == EXISTING_PROJECT_OPTION:
        project_path = _choose_project_path()
        if project_path is None:
            if confirm("No se seleccionó proyecto. ¿Crear uno nuevo?", default=True):
                context = NEW_PROJECT_OPTION
            else:
                return

    if context == NEW_PROJECT_OPTION:
        title = ask_text("Título del proyecto")
        if not title:
            print("\nNo se creó el proyecto porque falta el título.")
            return
        status = choose_one("Estado inicial", STATUS_OPTIONS[:-1], "On")
        if not status:
            return
        created = ask_date("Fecha de creación del effort (YYYY-MM-DD, vacío = hoy)", "", "created")
        project_path = create_project(title, status, created or None)

    if project_path is None:
        return

    subproject = _choose_subproject(project_path)
    if subproject is None:
        return
    task_text = ask_text("Tarea")
    if not task_text:
        print("\nNo se guardó ninguna tarea.")
        return
    priority = _choose_priority()
    scheduled_date = ask_date("Fecha programada (YYYY-MM-DD, vacío = ninguna)", "", "task_date")

    normalized_subproject = None if subproject == ROOT_OPTION else subproject
    location = subproject
    preview = [
        f"Proyecto: {project_path.stem}",
        f"Estado: {project_path.parent.name}",
        f"Ubicación: {location}",
        f"Tarea: {task_text}",
        f"Prioridad: {priority or '-'}",
        f"Fecha: {scheduled_date or '-'}",
    ]
    print("\n" + "\n".join(preview))
    if not confirm("¿Guardar tarea?", default=True):
        print("Operación cancelada.")
        return

    append_task(project_path, task_text, subproject=normalized_subproject, priority=priority, scheduled_date=scheduled_date or None)
    print(f"\n✅ Tarea guardada en: {project_path}")

    while True:
        follow_up = choose_one(
            "¿Qué deseas hacer ahora?",
            [
                "Agregar otra tarea al mismo proyecto",
                "Abrir proyecto",
                "Consultar pendientes de este proyecto",
                "Volver",
            ],
            "Volver",
        )
        if follow_up == "Agregar otra tarea al mismo proyecto":
            next_subproject = _choose_subproject(project_path)
            if next_subproject is None:
                continue
            next_task = ask_text("Tarea")
            if not next_task:
                continue
            next_priority = _choose_priority()
            next_date = ask_date("Fecha programada (YYYY-MM-DD, vacío = ninguna)", "", "task_date")
            append_task(
                project_path,
                next_task,
                subproject=None if next_subproject == ROOT_OPTION else next_subproject,
                priority=next_priority,
                scheduled_date=next_date or None,
            )
            print(f"\n✅ Tarea guardada en: {project_path}")
        elif follow_up == "Abrir proyecto":
            open_project(project_path)
        elif follow_up == "Consultar pendientes de este proyecto":
            run_review(initial_project=project_path.stem)
        else:
            return
