def ask(prompt_text: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt_text}{suffix}: ").strip()
    return value if value else default


def ask_profile_data(profile: str) -> dict:
    if profile == "spark":
        title = ask("Título breve", "")
        body = ask("Contenido")
        return {
            "title": title or "Spark",
            "body": body,
        }

    if profile == "source":
        subtype = ask("Subtipo (book, blog, youtube, course, conversation, reflection)", "blog")
        title = ask("Título")
        author = ask("Autor")
        url = ask("URL")
        source_date = ask("Fecha de la fuente", "")
        notes = ask("Notas rápidas", "")
        return {
            "subtype": subtype,
            "title": title,
            "author": author,
            "url": url,
            "source_date": source_date,
            "notes": notes,
        }

    if profile == "contact":
        name = ask("Nombre")
        birthday = ask("Fecha de nacimiento (YYYY-MM-DD)", "")
        address = ask("Dirección", "")
        phone = ask("Teléfono", "")
        email = ask("Email", "")
        organization = ask("Organización", "")
        role = ask("Cargo / relación", "")
        notes = ask("Notas", "")
        return {
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

def ask(prompt_text: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt_text}{suffix}: ").strip()
    return value if value else default


def ask_created_date() -> str:
    """
    Pregunta por la fecha de la nota.
    Si el usuario deja vacío, el engine usará la fecha actual.
    """
    return ask("Fecha de la nota (YYYY-MM-DD, vacío = hoy)", "")


def ask_profile_data(profile: str) -> dict:
    # campo común para todos los perfiles
    created = ask_created_date()

    if profile == "spark":
        title = ask("Título breve", "")
        body = ask("Contenido")
        return {
            "created": created,  # puede ser "" → engine decidirá
            "title": title or "Spark",
            "body": body,
        }

    if profile == "source":
        subtype = ask("Subtipo (book, blog, youtube, course, conversation, reflection)", "blog")
        title = ask("Título")
        author = ask("Autor")
        url = ask("URL")
        source_date = ask("Fecha de la fuente", "")
        notes = ask("Notas rápidas", "")
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
        birthday = ask("Fecha de nacimiento (YYYY-MM-DD)", "")
        address = ask("Dirección", "")
        phone = ask("Teléfono", "")
        email = ask("Email", "")
        organization = ask("Organización", "")
        role = ask("Cargo / relación", "")
        notes = ask("Notas", "")
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
