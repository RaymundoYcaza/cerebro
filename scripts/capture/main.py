import shutil
import subprocess
import sys

from manual_prompt import ask, ask_profile_data
from engine import save_note
from profiles import SUPPORTED_PROFILES, EXIT_OPTIONS


def gum_available() -> bool:
    return shutil.which("gum") is not None


def gum_choose(options: list[str], header: str = "") -> str:
    try:
        cmd = ["gum", "choose"]
        if header:
            cmd.extend(["--header", header])
        cmd.extend(options)

        output = subprocess.check_output(cmd, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        if e.returncode in (1, 130):
            return "salir"
        return ""
    except KeyboardInterrupt:
        return "salir"
    except Exception:
        return ""


def choose_profile() -> str:
    options = SUPPORTED_PROFILES + ["salir"]

    if gum_available():
        choice = gum_choose(options, "Selecciona el tipo de nota")
        if choice == "salir":
            raise SystemExit(0)
        if choice in SUPPORTED_PROFILES:
            return choice

    print("Perfiles disponibles:")
    for i, p in enumerate(SUPPORTED_PROFILES, start=1):
        print(f"{i}. {p}")
    print(f"{len(SUPPORTED_PROFILES) + 1}. salir")

    raw = input("Elige perfil: ").strip().lower()

    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(SUPPORTED_PROFILES):
            return SUPPORTED_PROFILES[idx]
        if idx == len(SUPPORTED_PROFILES):
            raise SystemExit(0)

    if raw in SUPPORTED_PROFILES:
        return raw

    if raw in EXIT_OPTIONS:
        raise SystemExit(0)

    raise ValueError("Perfil no válido")


def choose_assistant() -> str:
    options = ["manual", "openai", "salir"]

    if gum_available():
        choice = gum_choose(options, "Selecciona modo de captura")
        if choice == "salir":
            raise SystemExit(0)
        if choice in ("manual", "openai"):
            return choice

    mode = ask("Modo de captura (manual/openai/salir)", "manual").lower()
    if mode in EXIT_OPTIONS:
        raise SystemExit(0)
    if mode not in ("manual", "openai"):
        mode = "manual"
    return mode


def ask_continue() -> bool:
    if gum_available():
        choice = gum_choose(["nueva nota", "salir"], "¿Qué deseas hacer ahora?")
        return choice == "nueva nota"

    raw = ask("¿Crear otra nota? (s/n)", "s").lower()
    return raw in ("s", "si", "sí", "y", "yes")


def run_once():
    profile = choose_profile()
    assistant = choose_assistant()

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
            run_once()
            if not ask_continue():
                print("Salida sin cambios adicionales.")
                sys.exit(0)

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
