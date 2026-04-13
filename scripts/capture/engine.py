from pathlib import Path
import re

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
    if profile == "effort":
        return save_effort(profile_data)
        
    destination, rendered = build_note(profile, profile_data)
    write_note(destination, rendered)
    return destination


def save_effort(data: dict) -> Path:
    config = load_config()
    vault_root = Path(config["vault_root"])
    
    # Formatear la tarea: - [ ] Tarea ^prioridad @fecha
    task_line = f"- [ ] {data['task']}"
    if data.get("priority"):
        task_line += f" ^{data['priority']}"
    if data.get("task_date"):
        task_line += f" @{data['task_date']}"
    
    if data.get("is_new"):
        # Crear nuevo archivo
        profile_config = get_profile_config(config, "effort")
        # El status define la subcarpeta en Efforts
        status = data.get("status", "On")
        output_dir = vault_root / "Efforts" / status
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = build_filename(
            profile_config["filename_strategy"],
            data["title"],
            config["defaults"]["filename_max_length"],
        )
        destination = output_dir / filename
        
        template_text = load_template(config, profile_config["template_path"])
        # Renderizar propiedades
        rendered = render_template(template_text, data)
        
        # Agregar la tarea al final o bajo el subproyecto
        subproject = data.get("subproject")
        if subproject and subproject != "(Raíz)":
            rendered += f"\n\n## {subproject}\n{task_line}\n"
        else:
            rendered += f"\n\n{task_line}\n"
            
        write_note(destination, rendered)
        return destination
    else:
        # Actualizar archivo existente
        destination = Path(data["effort_path"])
        content = destination.read_text(encoding="utf-8")
        
        subproject = data.get("subproject")
        if not subproject or subproject == "(Raíz)":
            # Insertar antes del primer H2 si existe, o al final
            if "\n## " in content:
                parts = content.split("\n## ", 1)
                new_content = parts[0].rstrip() + f"\n{task_line}\n\n## " + parts[1]
            else:
                new_content = content.rstrip() + f"\n\n{task_line}\n"
        else:
            header = f"## {subproject}"
            if header in content:
                # Insertar después del header H2
                parts = content.split(header, 1)
                # Buscar el siguiente header para no salirnos del subproyecto
                if "\n## " in parts[1]:
                    sub_parts = parts[1].split("\n## ", 1)
                    new_content = parts[0] + header + sub_parts[0].rstrip() + f"\n{task_line}\n\n## " + sub_parts[1]
                else:
                    new_content = parts[0] + header + parts[1].rstrip() + f"\n{task_line}\n"
            else:
                # Crear el H2 al final
                new_content = content.rstrip() + f"\n\n## {subproject}\n{task_line}\n"
        
        destination.write_text(new_content, encoding="utf-8")
        return destination
