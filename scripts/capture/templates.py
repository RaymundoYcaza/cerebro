import re
from pathlib import Path


def load_template(config: dict, template_path: str) -> str:
    vault_root = Path(config["vault_root"])
    full_path = vault_root / template_path

    if not full_path.exists():
        raise FileNotFoundError(f"No existe la plantilla: {full_path}")

    return full_path.read_text(encoding="utf-8")


def render_template(template_text: str, data: dict) -> str:
    rendered = template_text

    for key, value in data.items():
        if isinstance(value, list):
            value = "[" + ", ".join(value) + "]"
        elif value is None:
            value = ""
        else:
            value = str(value)

        pattern = r"\{\{\s*" + re.escape(key) + r"\s*\}\}"
        rendered = re.sub(pattern, value, rendered)

    return rendered
