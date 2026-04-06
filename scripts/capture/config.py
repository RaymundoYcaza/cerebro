from pathlib import Path
import yaml


CONFIG_PATH = Path(__file__).resolve().parent / "config.yaml"


def load_config():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"No existe config.yaml en {CONFIG_PATH}")
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
