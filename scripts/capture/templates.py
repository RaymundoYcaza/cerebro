from pathlib import Path


def load_template(config: dict, template_name: str) -> str:
    templates_root = Path(config["templates_root"])
    template_path = templates_root / template_name

    if not template_path.exists():
        raise FileNotFoundError(f"No existe la plantilla: {template_path}")

    return template_path.read_text(encoding="utf-8")


def render_template(template_text: str, data: dict) -> str:
    rendered = template_text
    for key, value in data.items():
        placeholder = "{{" + key + "}}"
        if isinstance(value, list):
            value = "[" + ", ".join(value) + "]"
        elif value is None:
            value = ""
        else:
            value = str(value)
        rendered = rendered.replace(placeholder, value)
    return rendered
