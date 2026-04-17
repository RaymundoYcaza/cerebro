from efforts.capture import run_capture_task
from efforts.manage import run_manage_project
from efforts.review import run_review
from menus import choose_one


def run_efforts_menu() -> None:
    while True:
        choice = choose_one(
            "EFFORTS",
            ["Capturar tarea", "Consultar tareas", "Administrar proyecto", "Volver"],
            "Capturar tarea",
        )
        if choice == "Capturar tarea":
            run_capture_task()
        elif choice == "Consultar tareas":
            run_review()
        elif choice == "Administrar proyecto":
            run_manage_project()
        else:
            return
