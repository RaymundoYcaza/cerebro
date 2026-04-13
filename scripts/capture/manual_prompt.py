import shutil
import subprocess
import re
from datetime import date
from pathlib import Path
from config import load_config


def gum_available() -> bool:
    return shutil.which("gum") is not None


def ask(prompt_text: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt_text}{suffix}: ").strip()
    return value if value else default


def ask_multiline(prompt_text: str = "Contenido") -> str:
    """
    Usa gum write si está disponible; si no, cae a input tradicional.
    En gum write:
    - Ctrl+D o Esc terminan la entrada
    - Ctrl+C cancela
    """
    if gum_available():
        try:
            result = subprocess.check_output(
                ["gum", "write", "--placeholder", prompt_text],
                text=True
            )
            return result.rstrip()
        except subprocess.CalledProcessError:
            return ""
        except KeyboardInterrupt:
            return ""

    print(f"{prompt_text} (finaliza con una línea que solo contenga ::end)")
    lines = []
    while True:
        line = input()
        if line.strip() == "::end":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def validate_iso_date(value: str, field_name: str) -> str:
    if not value:
        return ""
    try:
        date.fromisoformat(value)
        return value
    except ValueError:
        raise ValueError(f"{field_name} debe tener formato YYYY-MM-DD")


def ask_created_date() -> str:
    value = ask("Fecha de la nota (YYYY-MM-DD, vacío = hoy)", "")
    return validate_iso_date(value, "created")


def ask_profile_data(profile: str) -> dict:
    created = ask_created_date()

    if profile == "effort":
        config = load_config()
        vault_root = Path(config["vault_root"])
        efforts_dir = vault_root / "Efforts"
        
        # 1. Seleccionar Proyecto
        options = ["Nuevo Proyecto"]
        effort_files = []
        if efforts_dir.exists():
            for p in efforts_dir.rglob("*.md"):
                if ".git" in p.parts: continue
                rel_path = p.relative_to(efforts_dir)
                effort_files.append((str(rel_path), p))
                options.append(str(rel_path))

        selected_effort = "Nuevo Proyecto"
        if gum_available() and len(options) > 1:
            result = subprocess.run(
                ["gum", "filter", "--placeholder", "Selecciona un proyecto o crea uno nuevo"],
                input="\n".join(options),
                stdout=subprocess.PIPE,
                text=True,
            )
            if result.returncode == 0:
                selected_effort = result.stdout.strip()
        else:
            if len(options) > 1:
                print("\nProyectos existentes:")
                for i, opt in enumerate(options):
                    print(f"{i}. {opt}")
                idx = ask("Elige proyecto (número o nombre)", "0")
                if idx.isdigit() and int(idx) < len(options):
                    selected_effort = options[int(idx)]
                elif idx in options:
                    selected_effort = idx

        is_new = selected_effort == "Nuevo Proyecto"
        effort_path = None
        if not is_new:
            for rel, full in effort_files:
                if rel == selected_effort:
                    effort_path = full
                    break
            
            # Opción de mover proyecto
            if gum_available():
                confirm = subprocess.run(
                    ["gum", "confirm", "¿Deseas mover este proyecto a otro estado (On/Ongoing...)?"]
                )
                if confirm.returncode == 0:
                    status_options = ["On", "Ongoing", "Simmering", "Sleeping", "Borradores", "Archived"]
                    result = subprocess.run(
                        ["gum", "choose", "--header", "Nuevo Estado", *status_options],
                        stdout=subprocess.PIPE,
                        text=True
                    )
                    new_status = result.stdout.strip()
                    if new_status:
                        # Mover archivo
                        new_dir = vault_root / "Efforts" / new_status
                        new_dir.mkdir(parents=True, exist_ok=True)
                        new_path = new_dir / effort_path.name
                        shutil.move(str(effort_path), str(new_path))
                        effort_path = new_path
                        print(f"✅ Proyecto movido a {new_status}")
            else:
                if ask("¿Mover proyecto? (s/n)", "n").lower() == "s":
                    new_status = ask("Nuevo estado (On/Ongoing/Simmering/Sleeping/Borradores/Archived)", "On")
                    new_dir = vault_root / "Efforts" / new_status
                    new_dir.mkdir(parents=True, exist_ok=True)
                    new_path = new_dir / effort_path.name
                    shutil.move(str(effort_path), str(new_path))
                    effort_path = new_path
                    print(f"✅ Proyecto movido a {new_status}")

        # 2. Datos del Proyecto/Subproyecto
        title = ""
        status = "On"
        if is_new:
            title = ask("Título del nuevo proyecto")
            status_options = ["On", "Ongoing", "Simmering", "Sleeping", "Borradores"]
            if gum_available():
                result = subprocess.run(
                    ["gum", "choose", "--header", "Estado inicial", *status_options],
                    stdout=subprocess.PIPE,
                    text=True
                )
                status = result.stdout.strip() or "On"
            else:
                status = ask(f"Estado ({'/'.join(status_options)})", "On")
        else:
            title = effort_path.stem

        # 3. Subproyecto (H2)
        h2_headers = ["(Raíz)"]
        if effort_path and effort_path.exists():
            with open(effort_path, "r", encoding="utf-8") as f:
                content = f.read()
                h2_headers.extend(re.findall(r"^##\s+(.+)$", content, re.MULTILINE))
        
        h2_headers.append("Nuevo Subproyecto")
        selected_h2 = "(Raíz)"
        if gum_available() and (len(h2_headers) > 1 or not is_new):
            result = subprocess.run(
                ["gum", "filter", "--placeholder", "Selecciona subproyecto (H2)"],
                input="\n".join(h2_headers),
                stdout=subprocess.PIPE,
                text=True,
            )
            if result.returncode == 0:
                selected_h2 = result.stdout.strip()
        else:
            if len(h2_headers) > 1:
                print("\nSubproyectos (H2):")
                for i, h in enumerate(h2_headers):
                    print(f"{i}. {h}")
                idx = ask("Elige subproyecto", "0")
                if idx.isdigit() and int(idx) < len(h2_headers):
                    selected_h2 = h2_headers[int(idx)]

        if selected_h2 == "Nuevo Subproyecto":
            selected_h2 = ask("Nombre del nuevo subproyecto")

        # 4. Tarea y Metadatos
        task_text = ask("Tarea")
        priority = ""
        priority_options = ["baja", "media", "alta", "(ninguna)"]
        if gum_available():
            result = subprocess.run(
                ["gum", "choose", "--header", "Prioridad", *priority_options],
                stdout=subprocess.PIPE,
                text=True
            )
            priority = result.stdout.strip()
        else:
            priority = ask("Prioridad (baja/media/alta)", "")
        
        if priority == "(ninguna)": priority = ""
        
        task_date = ask("Fecha programada (YYYY-MM-DD, vacío = ninguna)", "")
        
        return {
            "created": created,
            "is_new": is_new,
            "title": title,
            "status": status,
            "effort_path": str(effort_path) if effort_path else None,
            "subproject": selected_h2,
            "task": task_text,
            "priority": priority,
            "task_date": task_date,
            "mode": "effort"
        }

    if profile in ("spark", "aurora"):
        title = ask("Título breve", "")
        body = ask_multiline("Pega o escribe el contenido de la nota")
        return {
            "created": created,
            "title": title or ("Aurora" if profile == "aurora" else "Spark"),
            "body": body,
        }

    if profile == "source":
        subtype = ask("Subtipo (book, blog, youtube, course, conversation, reflection)", "blog")
        title = ask("Título")
        author = ask("Autor")
        url = ask("URL")
        source_date = validate_iso_date(
            ask("Fecha de la fuente (YYYY-MM-DD, opcional)", ""),
            "source_date"
        )
        notes = ask_multiline("Notas rápidas")
        return {
            "created": created,
            "subtype": subtype,
            "title": title,
            "author": author,
            "url": url,
            "source_date": source_date,
            "notes": notes,
        }

    if profile == "contact":
        name = ask("Nombre")
        birthday = validate_iso_date(
            ask("Fecha de nacimiento (YYYY-MM-DD, opcional)", ""),
            "birthday"
        )
        address = ask("Dirección", "")
        phone = ask("Teléfono", "")
        email = ask("Email", "")
        organization = ask("Organización", "")
        role = ask("Cargo / relación", "")
        notes = ask_multiline("Notas")
        return {
            "created": created,
            "name": name,
            "birthday": birthday,
            "address": address,
            "phone": phone,
            "email": email,
            "organization": organization,
            "role": role,
            "notes": notes,
        }

    raise ValueError(f"Perfil no soportado: {profile}")
