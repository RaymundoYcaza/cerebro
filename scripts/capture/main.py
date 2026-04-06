import sys

from manual_prompt import ask, ask_profile_data
from engine import save_note
from profiles import SUPPORTED_PROFILES


def choose_profile() -> str:
    print("Perfiles disponibles:")
    for i, p in enumerate(SUPPORTED_PROFILES, start=1):
        print(f"{i}. {p}")

    raw = input("Elige perfil: ").strip()

    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(SUPPORTED_PROFILES):
            return SUPPORTED_PROFILES[idx]

    if raw in SUPPORTED_PROFILES:
        return raw

    raise ValueError("Perfil no válido")


def choose_assistant() -> str:
    mode = ask("Modo de captura (manual/openai)", "manual").lower()
    if mode not in ("manual", "openai"):
        mode = "manual"
    return mode


def main():
    try:
        profile = choose_profile()
        assistant = choose_assistant()

        if assistant == "openai":
            from ai_prompt import openai_capture_stub
            data = openai_capture_stub(profile)
        else:
            data = ask_profile_data(profile)

        path = save_note(profile, data)
        print(f"\n✅ Nota guardada en: {path}")

    except KeyboardInterrupt:
        print("\nCancelado.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
