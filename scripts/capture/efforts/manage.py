from pathlib import Path

from config import load_config
from efforts import STATUS_OPTIONS
from efforts.mutate import create_subproject, move_project
from efforts.repository import list_projects
from efforts.review import open_project
from menus import ask_text, choose_one, filter_one


def _efforts_dir() -> Path:
    config = load_config()
    return Path(config["vault_root"]) / "Efforts"


def _choose_project_path() -> Path | None:
    projects = list_projects(_efforts_dir())
    if not projects:
        print("\nNo hay proyectos para administrar.")
        return None
    options = [f"{project.status} / {project.title}" for project in projects]
    selected = filter_one(options, "Selecciona proyecto")
    if not selected:
        return None
    return projects[options.index(selected)].path


def run_manage_project() -> None:
    project_path = _choose_project_path()
    if project_path is None:
        return

    while True:
        action = choose_one(
            f"ADMINISTRAR PROYECTO: {project_path.stem}",
            ["Mover de estado", "Crear subproyecto", "Abrir contenido", "Volver"],
            "Volver",
        )
        if action == "Mover de estado":
            new_status = choose_one("Nuevo estado", STATUS_OPTIONS, project_path.parent.name)
            if new_status and new_status != project_path.parent.name:
                project_path = move_project(project_path, new_status)
                print(f"\n✅ Proyecto movido a: {new_status}")
        elif action == "Crear subproyecto":
            name = ask_text("Nombre del nuevo subproyecto")
            if name:
                create_subproject(project_path, name)
                print(f"\n✅ Subproyecto creado en: {project_path.stem}")
        elif action == "Abrir contenido":
            open_project(project_path)
        else:
            return
