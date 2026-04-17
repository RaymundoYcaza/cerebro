from pathlib import Path

from config import load_config
from profiles import get_profile_config
from templates import load_template, render_template
from utils import now_date, build_filename, write_note


def build_common_fields(config: dict) -> dict:
    return {
        "up": [],
        "related": [],
    }


def build_note(profile: str, profile_data: dict) -> tuple[Path, str]:
    config = load_config()
    profile_config = get_profile_config(config, profile)

    vault_root = Path(config["vault_root"])
    output_dir = vault_root / profile_config["output_dir"]

    common = build_common_fields(config)

    created = profile_data.get("created")
    if not created:
        created = now_date(config["defaults"]["date_format"])

    data = {**common, **profile_data, "created": created}

    if profile == "spark":
        title = data.get("title") or "Spark"
    elif profile == "aurora":
        title = data.get("title") or "Aurora"
    elif profile == "source":
        title = data.get("title") or "Fuente"
    elif profile == "contact":
        title = data.get("name") or "Contacto"
        data["title"] = title
    elif profile == "effort":
        title = data.get("title") or "Effort"
    else:
        title = "Nota"

    filename = build_filename(
        profile_config["filename_strategy"],
        title,
        config["defaults"]["filename_max_length"],
    )

    template_text = load_template(config, profile_config["template_path"])
    rendered = render_template(template_text, data)

    destination = output_dir / filename
    return destination, rendered


def save_note(profile: str, profile_data: dict) -> Path:
    destination, rendered = build_note(profile, profile_data)
    write_note(destination, rendered)
    return destination
