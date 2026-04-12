<<<<<<< HEAD
SUPPORTED_PROFILES = ["spark", "source", "contact", "aurora", "utilitarios"]
EXIT_OPTIONS = ["salir", "exit", "quit"]


def get_profile_config(config: dict, profile_name: str) -> dict:
    profiles = config.get("profiles", {})
    if profile_name not in profiles:
        raise ValueError(f"Perfil no soportado: {profile_name}")
    return profiles[profile_name]
=======
SUPPORTED_PROFILES = ["spark", "source", "contact", "aurora"]
EXIT_OPTIONS = ["salir", "exit", "quit"]


def get_profile_config(config: dict, profile_name: str) -> dict:
    profiles = config.get("profiles", {})
    if profile_name not in profiles:
        raise ValueError(f"Perfil no soportado: {profile_name}")
    return profiles[profile_name]
>>>>>>> bca2500 (Actualiza notas 2026-04-07 11:18:01)
