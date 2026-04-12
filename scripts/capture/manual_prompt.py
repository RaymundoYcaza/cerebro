import shutil
import subprocess
from datetime import date


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
