SUPPORTED_PROFILES = ["spark", "source", "contact", "aurora"]
EXIT_OPTIONS = ["salir", "exit", "quit"]


def get_profile_config(config: dict, profile_name: str) -> dict:
    profiles = config.get("profiles", {})
    if profile_name not in profiles:
        raise ValueError(f"Perfil no soportado: {profile_name}")
    return profiles[profile_name]
