import sys
from manual_prompt import ask, ask_profile_data
from engine import save_note
from profiles import SUPPORTED_PROFILES, EXIT_OPTIONS
from daily import run_daily_capture
from efforts.menu import run_efforts_menu
from menus import choose_one

DIARY_OPTION = "diario"


def choose_note_profile() -> str:
    choice = choose_one(
        "Selecciona el tipo de nota",
        [DIARY_OPTION] + SUPPORTED_PROFILES + ["volver"],
        DIARY_OPTION,
    )
    if not choice or choice == "volver" or choice in EXIT_OPTIONS:
        return ""
    return choice


def choose_assistant() -> str:
    options = ["manual", "openai", "volver"]
    choice = choose_one("Selecciona modo de captura", options, "manual")
    if not choice or choice == "volver":
        return ""
    if choice in ("manual", "openai"):
        return choice
    mode = ask("Modo de captura (manual/openai/salir)", "manual").lower()
    if mode in EXIT_OPTIONS:
        raise SystemExit(0)
    if mode not in ("manual", "openai"):
        mode = "manual"
    return mode


def ask_continue() -> bool:
    choice = choose_one(
        "¿Qué deseas hacer ahora?",
        ["Capturar otra nota", "Volver al menú principal", "Salir"],
        "Volver al menú principal",
    )
    if choice == "Capturar otra nota":
        return True
    if choice == "Salir":
        print("Salida sin cambios adicionales.")
        raise SystemExit(0)
    return False


def run_note_capture():
    profile = choose_note_profile()
    if not profile:
        return

    if profile == DIARY_OPTION:
        run_daily_capture()
        return

    if profile == "utilitarios":
        from utilities import run_utility_capture
        path = run_utility_capture()
        print(f"\n✅ Nota guardada en: {path}")
        return

    assistant = choose_assistant()
    if not assistant:
        return

    if assistant == "openai":
        from ai_prompt import openai_capture_stub
        data = openai_capture_stub(profile)
    else:
        data = ask_profile_data(profile)

    path = save_note(profile, data)
    print(f"\n✅ Nota guardada en: {path}")


def main():
    try:
        while True:
            choice = choose_one(
                "CEREBRO - Gestión de Conocimiento",
                ["Capturar nota", "Efforts", "Salir"],
                "Capturar nota",
            )
            if not choice or choice == "Salir":
                print("Salida.")
                sys.exit(0)

            if choice == "Efforts":
                run_efforts_menu()
                continue

            run_note_capture()
            if not ask_continue():
                continue

    except SystemExit as e:
        if e.code == 0:
            print("Salida sin cambios.")
            sys.exit(0)
        raise
    except KeyboardInterrupt:
        print("\nCancelado.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
