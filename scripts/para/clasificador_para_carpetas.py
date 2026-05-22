"""
Clasificador PARA + Obsidian
FASE 2

Procesa archivos/carpetas de primer nivel en P:/PARA/00-INBOX, permite clasificarlos,
los mueve a una carpeta PARA y crea una nota Markdown en Obsidian/zResources.

Caracteristicas:
- Configurable por config.yaml
- Si P:/PARA/00-INBOX no existe, permite indicar ruta alternativa
- Menu: modo rapido / logica completa / buscar / deshacer ultimo movimiento
- Búsqueda difusa si rapidfuzz esta instalado; fallback simple si no
- Confirmacion obligatoria antes de mover
- Manejo de duplicados: reemplazar / renombrar / cancelar
- Portada: elegir imagen cercana, elegir ruta manual, portada generica o sin portada
- Carpetas completas: cursos, series de videos y colecciones como un solo recurso
- Logs: CSV, Markdown y JSON para deshacer
- Deshacer ultimo movimiento: mueve archivo/carpeta a origen y elimina nota creada

Requisitos recomendados:
    pip install pyyaml rapidfuzz python-slugify rich

Ejecutar:
    python clasificador_para.py
"""

from __future__ import annotations

import csv
import json
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

try:
    from rapidfuzz import process, fuzz  # type: ignore
except Exception:  # pragma: no cover
    process = None
    fuzz = None

try:
    from slugify import slugify as external_slugify  # type: ignore
except Exception:  # pragma: no cover
    external_slugify = None

try:
    from rich.console import Console  # type: ignore
    from rich.table import Table  # type: ignore
    from rich.prompt import Prompt, Confirm  # type: ignore
except Exception:  # pragma: no cover
    Console = None
    Table = None
    Prompt = None
    Confirm = None


APP_NAME = "Clasificador PARA + Obsidian"
CONFIG_FILE = "config.yaml"


DEFAULT_CONFIG = {
    "vault_path": "C:/cerebro/vault/raymundo_ideaverse",
    "default_para_root": "P:/PARA",
    "default_inbox_path": "P:/PARA/00-INBOX",
    "obsidian_resources_path": "zResources",
    "obsidian_templates_path": "x/Templates/PARA",
    "obsidian_covers_path": "x/Images/Covers",
    "logs_path": "zResources/_logs",
    "movement_csv": "movimientos-para.csv",
    "movement_md": "movimientos-para.md",
    "last_movement_json": "ultimo-movimiento.json",
    "use_slug_names": True,
    "create_note_for_archived": True,
    "generic_cover_fallback": True,
    "confirm_before_move": True,
    "process_first_level_only": True,
    "tags_root": "z",
}

RESOURCE_DESTINATIONS = {
    "Biblioteca": {
        "windows": "03-RECURSOS/Biblioteca",
        "obsidian": "zResources/Biblioteca",
        "tags": ["z/recurso", "z/biblioteca"],
    },
    "Aprendizaje": {
        "windows": "03-RECURSOS/Aprendizaje",
        "obsidian": "zResources/Aprendizaje",
        "tags": ["z/recurso", "z/curso"],
    },
    "Software": {
        "windows": "03-RECURSOS/Software-y-Herramientas",
        "obsidian": "zResources/Software",
        "tags": ["z/recurso", "z/software"],
    },
    "Multimedia": {
        "windows": "03-RECURSOS/Multimedia-Referencia",
        "obsidian": "zResources/Multimedia",
        "tags": ["z/recurso", "z/multimedia"],
    },
    "Imagenes": {
        "windows": "03-RECURSOS/Creatividad-y-Diseno/Imagenes-Referencia",
        "obsidian": "zResources/Imagenes",
        "tags": ["z/recurso", "z/imagen"],
    },
    "Audio": {
        "windows": "03-RECURSOS/Multimedia-Referencia/Audio",
        "obsidian": "zResources/Audio",
        "tags": ["z/recurso", "z/audio"],
    },
    "Documentos": {
        "windows": "02-AREAS/Identidad-y-Documentos",
        "obsidian": "zResources/Documentos",
        "tags": ["z/recurso", "z/documento"],
    },
    "Legal": {
        "windows": "02-AREAS/Legal-y-Tramites",
        "obsidian": "zResources/Legal",
        "tags": ["z/recurso", "z/legal"],
    },
    "Finanzas": {
        "windows": "02-AREAS/Finanzas",
        "obsidian": "zResources/Finanzas",
        "tags": ["z/recurso", "z/finanzas"],
    },
    "Contactos": {
        "windows": "02-AREAS/Contactos",
        "obsidian": "zResources/Contactos",
        "tags": ["z/recurso", "z/contacto"],
    },
    "PKM": {
        "windows": "03-RECURSOS/PKM-y-Obsidian",
        "obsidian": "zResources/PKM",
        "tags": ["z/recurso", "z/pkm"],
    },
    "Plantillas": {
        "windows": "03-RECURSOS/Creatividad-y-Diseno/Plantillas",
        "obsidian": "zResources/Plantillas",
        "tags": ["z/recurso", "z/plantilla"],
    },
    "Revisar": {
        "windows": "04-ARCHIVO/Material-Historico/Revisar",
        "obsidian": "zResources/Revisar",
        "tags": ["z/recurso", "z/revisar"],
    },
    "Archivo": {
        "windows": "04-ARCHIVO/Material-Historico",
        "obsidian": "zResources/Revisar",
        "tags": ["z/recurso", "z/archivo"],
    },
}

EXTENSION_TYPE_MAP = {
    ".pdf": "documento",
    ".epub": "ebook",
    ".mobi": "ebook",
    ".azw3": "ebook",
    ".cbz": "ebook",
    ".cbr": "ebook",
    ".mp4": "video",
    ".mov": "video",
    ".mkv": "video",
    ".avi": "video",
    ".webm": "video",
    ".jpg": "imagen",
    ".jpeg": "imagen",
    ".png": "imagen",
    ".webp": "imagen",
    ".gif": "imagen",
    ".svg": "imagen",
    ".mp3": "audio",
    ".wav": "audio",
    ".m4a": "audio",
    ".flac": "audio",
    ".ogg": "audio",
    ".exe": "software",
    ".msi": "software",
    ".bat": "software",
    ".ps1": "software",
    ".py": "software",
    ".zip": "archivo_comprimido",
    ".rar": "archivo_comprimido",
    ".7z": "archivo_comprimido",
    ".doc": "documento",
    ".docx": "documento",
    ".xls": "documento",
    ".xlsx": "documento",
    ".ppt": "documento",
    ".pptx": "documento",
    ".txt": "documento",
    ".md": "documento",
}

TYPE_DEFAULT_CATEGORY = {
    "ebook": "Biblioteca",
    "video": "Multimedia",
    "imagen": "Imagenes",
    "audio": "Audio",
    "software": "Software",
    "archivo_comprimido": "Software",
    "documento": "Documentos",
    "carpeta": "Revisar",
    "curso": "Aprendizaje",
    "serie_video": "Multimedia",
    "coleccion_ebooks": "Biblioteca",
    "coleccion_imagenes": "Imagenes",
    "coleccion_audio": "Audio",
}

STATUS_VALUES = {
    "ebook": ["pendiente", "leyendo", "leido", "referencia", "descartado"],
    "video": ["pendiente", "viendo", "visto", "referencia", "descartado"],
    "curso": ["pendiente", "en_progreso", "completado", "referencia", "descartado"],
    "serie_video": ["pendiente", "viendo", "visto", "referencia", "descartado"],
    "coleccion_ebooks": ["pendiente", "en_revision", "referencia", "descartado"],
    "coleccion_imagenes": ["pendiente", "en_revision", "referencia", "descartado"],
    "coleccion_audio": ["pendiente", "escuchando", "escuchado", "referencia", "descartado"],
    "software": ["pendiente", "instalado", "probado", "en_uso", "descartado"],
    "documento": ["pendiente", "revisar", "vigente", "cerrado", "historico"],
    "general": ["pendiente", "en_uso", "consultado", "terminado", "referencia", "descartado"],
}

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".jfif", ".gif"}


@dataclass
class Classification:
    source: Path
    title: str
    resource_type: str
    para: str
    category: str
    subcategory: str
    status: str
    archived: bool
    summary: str
    target_path: Path
    note_path: Path
    cover: str
    tags: List[str]


class UI:
    def __init__(self) -> None:
        self.rich = Console is not None
        self.console = Console() if Console else None

    def print(self, msg: str = "", style: Optional[str] = None) -> None:
        if self.console:
            self.console.print(msg, style=style)
        else:
            print(msg)

    def input(self, msg: str, default: Optional[str] = None) -> str:
        if Prompt:
            return Prompt.ask(msg, default=default)
        suffix = f" [{default}]" if default is not None else ""
        value = input(f"{msg}{suffix}: ").strip()
        return value if value else (default or "")

    def confirm(self, msg: str, default: bool = True) -> bool:
        if Confirm:
            return bool(Confirm.ask(msg, default=default))
        suffix = "S/n" if default else "s/N"
        value = input(f"{msg} ({suffix}): ").strip().lower()
        if not value:
            return default
        return value in {"s", "si", "sí", "y", "yes"}


ui = UI()


def load_config(script_dir: Path) -> Dict:
    config_path = script_dir / CONFIG_FILE
    config = dict(DEFAULT_CONFIG)
    if config_path.exists() and yaml is not None:
        with config_path.open("r", encoding="utf-8") as f:
            loaded = yaml.safe_load(f) or {}
        config.update(loaded)
    elif config_path.exists() and yaml is None:
        ui.print("ADVERTENCIA: config.yaml existe, pero pyyaml no esta instalado. Usando config por defecto.", "yellow")
    return config


def slug(text: str) -> str:
    if external_slugify:
        value = external_slugify(text, lowercase=True, separator="-")
        return value or "sin-titulo"
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return normalized or "sin-titulo"


def file_uri(path: Path) -> str:
    p = path.resolve()
    # Windows-friendly file URI with encoded spaces/special chars.
    s = str(p).replace("\\", "/")
    if re.match(r"^[A-Za-z]:/", s):
        return "file:///" + quote(s, safe=":/")
    return "file://" + quote(s, safe="/")


def as_posix_rel(path: Path, base: Path) -> str:
    try:
        return path.relative_to(base).as_posix()
    except Exception:
        return path.as_posix()


def choose_path_if_missing(path: Path, label: str, must_exist: bool = True) -> Path:
    if path.exists() or not must_exist:
        return path
    ui.print(f"No se encontro {label}: {path}", "yellow")
    while True:
        raw = ui.input(f"Indica ruta alternativa para {label}")
        candidate = Path(raw.strip().strip('"'))
        if candidate.exists() or not must_exist:
            return candidate
        ui.print("La ruta indicada no existe. Intenta otra vez.", "red")


def list_first_level(inbox: Path) -> List[Path]:
    return sorted([p for p in inbox.iterdir() if p.name not in {"desktop.ini", "Thumbs.db"}], key=lambda p: (p.is_file(), p.name.lower()))


def print_items(items: List[Path], limit: int = 50) -> None:
    if Table and ui.console:
        table = Table(title="Items en INBOX")
        table.add_column("#", justify="right")
        table.add_column("Tipo")
        table.add_column("Nombre")
        for idx, item in enumerate(items[:limit], 1):
            table.add_row(str(idx), "carpeta" if item.is_dir() else "archivo", item.name)
        ui.console.print(table)
    else:
        for idx, item in enumerate(items[:limit], 1):
            kind = "[D]" if item.is_dir() else "[F]"
            print(f"{idx:3}. {kind} {item.name}")
    if len(items) > limit:
        ui.print(f"Mostrando {limit} de {len(items)} items.", "yellow")


def fuzzy_search(items: List[Path], query: str, limit: int = 15) -> List[Path]:
    if not query.strip():
        return items[:limit]
    names = [p.name for p in items]
    if process is not None and fuzz is not None:
        matches = process.extract(query, names, scorer=fuzz.WRatio, limit=limit)
        selected_names = [m[0] for m in matches if m[1] >= 40]
        return [p for p in items if p.name in selected_names]
    q = query.lower()
    return [p for p in items if q in p.name.lower()][:limit]


def detect_resource_type(path: Path) -> str:
    if path.is_dir():
        return "carpeta"
    return EXTENSION_TYPE_MAP.get(path.suffix.lower(), "documento")


def folder_profile_options() -> List[str]:
    return [
        "carpeta",
        "curso",
        "serie_video",
        "coleccion_ebooks",
        "coleccion_imagenes",
        "coleccion_audio",
    ]


def suggest_folder_profile(source: Path) -> Tuple[str, str]:
    """Sugiere tipo/subcategoria para una carpeta completa segun extensiones dominantes."""
    if not source.is_dir():
        return detect_resource_type(source), ""
    counts: Dict[str, int] = {}
    try:
        for child in source.rglob("*"):
            if child.is_file():
                detected = detect_resource_type(child)
                counts[detected] = counts.get(detected, 0) + 1
    except Exception:
        return "carpeta", ""
    if not counts:
        return "carpeta", ""
    dominant = max(counts, key=counts.get)
    total = sum(counts.values()) or 1
    ratio = counts[dominant] / total
    if dominant == "video" and ratio >= 0.45:
        return "serie_video", "Videos"
    if dominant == "ebook" and ratio >= 0.45:
        return "coleccion_ebooks", "Ebooks"
    if dominant == "imagen" and ratio >= 0.45:
        return "coleccion_imagenes", "Imagenes"
    if dominant == "audio" and ratio >= 0.45:
        return "coleccion_audio", "Audio"
    return "carpeta", ""


def choose_from_list(title: str, options: List[str], default_index: int = 0) -> str:
    ui.print(f"\n{title}", "bold")
    for i, opt in enumerate(options, 1):
        marker = "*" if i - 1 == default_index else " "
        ui.print(f"{i}. {opt} {marker}")
    while True:
        raw = ui.input("Opcion", default=str(default_index + 1))
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        ui.print("Opcion invalida.", "red")


def quick_classification(source: Path, para_root: Path, vault_path: Path, config: Dict) -> Classification:
    resource_type = detect_resource_type(source)
    suggested_subcategory = ""

    if source.is_dir():
        suggested_type, suggested_subcategory = suggest_folder_profile(source)
        folder_types = folder_profile_options()
        default_type_index = folder_types.index(suggested_type) if suggested_type in folder_types else 0
        ui.print("\nEl item seleccionado es una carpeta completa.", "bold")
        ui.print("Se movera la carpeta entera como un solo recurso y se creara una nota indice en Obsidian.")
        resource_type = choose_from_list("Tipo de carpeta", folder_types, default_index=default_type_index)

    default_category = TYPE_DEFAULT_CATEGORY.get(resource_type, "Revisar")
    categories = list(RESOURCE_DESTINATIONS.keys())
    default_index = categories.index(default_category) if default_category in categories else categories.index("Revisar")

    title_default = source.stem if source.is_file() else source.name
    title = ui.input("Titulo de la nota", default=title_default)

    if not source.is_dir():
        type_options = sorted(set(list(EXTENSION_TYPE_MAP.values()) + ["carpeta", "documento", "curso", "serie_video", "coleccion_ebooks", "coleccion_imagenes", "coleccion_audio"]))
        type_default_index = type_options.index(resource_type) if resource_type in type_options else 0
        resource_type = choose_from_list("Tipo de recurso", type_options, default_index=type_default_index)

    category = choose_from_list("Categoria curada en zResources", categories, default_index=default_index)
    subcategory = ui.input("Subcategoria", default=suggested_subcategory)

    status_options = STATUS_VALUES.get(resource_type, STATUS_VALUES["general"])
    status = choose_from_list("Estado de uso/lectura", status_options, default_index=0)
    archived = ui.confirm("¿Marcar como archivado?", default=(category == "Archivo"))
    summary = ui.input("Resumen breve", default="")

    return build_classification(source, title, resource_type, "recurso" if category != "Archivo" else "archivo", category, subcategory, status, archived, summary, para_root, vault_path, config)


def full_logic_classification(source: Path, para_root: Path, vault_path: Path, config: Dict) -> Classification:
    ui.print("\nLogica completa PARA", "bold")
    ui.print("Proyecto = resultado activo y concreto.")
    ui.print("Area = responsabilidad permanente.")
    ui.print("Recurso = material de consulta, aprendizaje o referencia.")
    ui.print("Archivo = cerrado, viejo, historico, duplicado o sin uso inmediato.\n")

    title_default = source.stem if source.is_file() else source.name
    title = ui.input("Titulo de la nota", default=title_default)
    resource_type = detect_resource_type(source)
    suggested_subcategory = ""

    if source.is_dir():
        suggested_type, suggested_subcategory = suggest_folder_profile(source)
        folder_types = folder_profile_options()
        default_type_index = folder_types.index(suggested_type) if suggested_type in folder_types else 0
        ui.print("\nEl item seleccionado es una carpeta completa.", "bold")
        ui.print("Se movera la carpeta entera como un solo recurso y se creara una nota indice en Obsidian.")
        resource_type = choose_from_list("Tipo de carpeta", folder_types, default_index=default_type_index)

    if ui.confirm("¿Tiene un resultado activo y concreto?", default=False):
        para = "proyecto"
        category = "Revisar"
    elif ui.confirm("¿Pertenece a una responsabilidad permanente?", default=False):
        para = "area"
        area_categories = ["Legal", "Finanzas", "Contactos", "Documentos", "Revisar"]
        category = choose_from_list("Area principal", area_categories, default_index=len(area_categories) - 1)
    elif ui.confirm("¿Es material de consulta, aprendizaje, inspiracion o referencia?", default=True):
        para = "recurso"
        categories = [c for c in RESOURCE_DESTINATIONS.keys() if c != "Archivo"]
        default_category = TYPE_DEFAULT_CATEGORY.get(resource_type, "Revisar")
        default_index = categories.index(default_category) if default_category in categories else categories.index("Revisar")
        category = choose_from_list("Categoria de recurso", categories, default_index=default_index)
    else:
        para = "archivo"
        category = "Archivo"

    subcategory = ui.input("Subcategoria", default=suggested_subcategory)
    status_options = STATUS_VALUES.get(resource_type, STATUS_VALUES["general"])
    status = choose_from_list("Estado de uso/lectura", status_options, default_index=0)
    archived = ui.confirm("¿Marcar como archivado?", default=(para == "archivo" or category == "Archivo"))
    summary = ui.input("Resumen breve", default="")

    return build_classification(source, title, resource_type, para, category, subcategory, status, archived, summary, para_root, vault_path, config)


def build_classification(source: Path, title: str, resource_type: str, para: str, category: str, subcategory: str, status: str, archived: bool, summary: str, para_root: Path, vault_path: Path, config: Dict) -> Classification:
    dest = RESOURCE_DESTINATIONS.get(category, RESOURCE_DESTINATIONS["Revisar"])
    target_dir = para_root / Path(dest["windows"])
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / source.name

    note_dir = vault_path / Path(dest["obsidian"])
    note_dir.mkdir(parents=True, exist_ok=True)
    note_slug = slug(title)
    note_path = unique_path(note_dir / f"{note_slug}.md")

    tags = list(dest["tags"])
    type_tag = f"z/{resource_type.replace('_', '-')}"
    if type_tag not in tags:
        tags.append(type_tag)
    if para == "archivo" and "z/archivo" not in tags:
        tags.append("z/archivo")

    cover = choose_cover(source, resource_type, title, vault_path, config)

    return Classification(
        source=source,
        title=title,
        resource_type=resource_type,
        para=para,
        category=category,
        subcategory=subcategory,
        status=status,
        archived=archived,
        summary=summary,
        target_path=target_path,
        note_path=note_path,
        cover=cover,
        tags=tags,
    )


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    base = path.with_suffix("")
    suffix = path.suffix
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = Path(f"{base}__{stamp}{suffix}")
    i = 2
    while candidate.exists():
        candidate = Path(f"{base}__{stamp}-{i}{suffix}")
        i += 1
    return candidate


def choose_cover(source: Path, resource_type: str, title: str, vault_path: Path, config: Dict) -> str:
    """
    Flujo interactivo para elegir portada.

    Opciones:
    1. Buscar imagen junto al archivo y permitir seleccionar una.
    2. Elegir imagen manualmente por ruta.
    3. Usar portada generica.
    4. Sin portada.
    """
    ui.print("\nPortada", "bold")
    options = [
        "Buscar imagen junto al archivo",
        "Elegir imagen manualmente",
        "Usar portada generica",
        "Sin portada",
    ]
    choice = choose_from_list("Selecciona opcion de portada", options, default_index=2)

    covers_relative_dir = config.get("obsidian_covers_path", "x/Images/Covers")

    if choice == "Buscar imagen junto al archivo":
        cover = elegir_imagen_cercana(
            archivo_origen=source,
            vault_path=vault_path,
            covers_relative_dir=covers_relative_dir,
            resource_type=resource_type,
            titulo=title,
        )
        if cover:
            return cover
        ui.print("No se selecciono imagen cercana. Se usara portada generica.", "yellow")
        return generic_cover(resource_type)

    if choice == "Elegir imagen manualmente":
        selected = elegir_imagen_manual(
            vault_path=vault_path,
            covers_relative_dir=covers_relative_dir,
            resource_type=resource_type,
            titulo=title,
        )
        if selected:
            return selected
        ui.print("No se selecciono una imagen valida. Se usara portada generica.", "yellow")
        return generic_cover(resource_type)

    if choice == "Usar portada generica":
        return generic_cover(resource_type)

    return ""

def cover_folder_for_type(resource_type: str) -> str:
    return {
        "ebook": "ebooks",
        "video": "videos",
        "imagen": "imagenes",
        "audio": "audio",
        "software": "software",
        "documento": "documentos",
        "carpeta": "carpetas",
        "curso": "cursos",
        "serie_video": "videos",
        "coleccion_ebooks": "ebooks",
        "coleccion_imagenes": "imagenes",
        "coleccion_audio": "audio",
        "archivo_comprimido": "software",
    }.get(resource_type, "documentos")


def generic_cover(resource_type: str) -> str:
    mapping = {
        "ebook": "[[x/Images/Covers/_generic/ebook-cover_generic.png]]",
        "video": "[[x/Images/Covers/_generic/video-cover_generic.png]]",
        "imagen": "[[x/Images/Covers/_generic/imagen-cover_generic.png]]",
        "audio": "[[x/Images/Covers/_generic/audio-cover_generic.png]]",
        "software": "[[x/Images/Covers/_generic/software-cover_generic.png]]",
        "documento": "[[x/Images/Covers/_generic/documento-cover_generic.png]]",
        "carpeta": "[[x/Images/Covers/_generic/carpeta-cover_generic.png]]",
        "curso": "[[x/Images/Covers/_generic/curso-cover_generic.png]]",
        "serie_video": "[[x/Images/Covers/_generic/video-cover_generic.png]]",
        "coleccion_ebooks": "[[x/Images/Covers/_generic/ebook-cover_generic.png]]",
        "coleccion_imagenes": "[[x/Images/Covers/_generic/imagen-cover_generic.png]]",
        "coleccion_audio": "[[x/Images/Covers/_generic/audio-cover_generic.png]]",
        "archivo_comprimido": "[[x/Images/Covers/_generic/software-cover_generic.png]]",
    }
    return mapping.get(resource_type, "[[x/Images/Covers/_generic/documento-cover_generic.png]]")


def find_nearby_image(source: Path) -> Optional[Path]:
    parent = source if source.is_dir() else source.parent
    candidates = [p for p in parent.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS]
    if not candidates:
        return None
    # Prefer cover-like filenames, otherwise nearest first alphabetically.
    preferred_words = ["cover", "portada", "poster", "thumbnail", "thumb"]
    for word in preferred_words:
        for p in candidates:
            if word in p.stem.lower():
                return p
    return sorted(candidates, key=lambda p: p.name.lower())[0]


def resolve_duplicate_target(target: Path) -> Optional[Path]:
    if not target.exists():
        return target
    ui.print(f"\nYa existe un item en destino: {target}", "yellow")
    choice = choose_from_list("Que deseas hacer?", ["Reemplazar", "Renombrar automaticamente", "Cancelar"], default_index=1)
    if choice == "Cancelar":
        return None
    if choice == "Renombrar automaticamente":
        return unique_path(target)
    if choice == "Reemplazar":
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()
        return target
    return None


def render_note(c: Classification, vault_path: Path) -> str:
    now = datetime.now().strftime("%Y-%m-%d")
    tags_yaml = "\n".join([f"  - {t}" for t in c.tags])
    note_rel = as_posix_rel(c.note_path, vault_path)
    folder_uri = file_uri(c.target_path if c.target_path.is_dir() else c.target_path.parent)
    target_uri = file_uri(c.target_path)
    source_uri = file_uri(c.source)

    return f"""---
type: recurso
resource_type: {c.resource_type}
title: "{escape_yaml(c.title)}"
summary: "{escape_yaml(c.summary)}"

para: {c.para}
category: {c.category}
subcategory: "{escape_yaml(c.subcategory)}"

status: {c.status}
archived: {str(c.archived).lower()}

source_path: "{source_uri}"
target_path: "{target_uri}"
folder_path: "{folder_uri}"
obsidian_note: "{note_rel}"

cover: "{escape_yaml(c.cover)}"

created: {now}
updated: {now}
reviewed:

tags:
{tags_yaml}
---

# {c.title}

## Resumen

{c.summary or 'Pendiente de describir.'}

## Ubicacion fisica

- Archivo o carpeta: [Abrir recurso]({target_uri})
- Carpeta contenedora: [Abrir carpeta]({folder_uri})

## Clasificacion

| Campo | Valor |
|---|---|
| PARA | {c.para} |
| Categoria | {c.category} |
| Subcategoria | {c.subcategory} |
| Tipo | {c.resource_type} |
| Estado | {c.status} |
| Archivado | {str(c.archived).lower()} |

## Notas

- 

## Relaciones

- 
"""


def escape_yaml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def confirm_and_execute(c: Classification, vault_path: Path, config: Dict) -> bool:
    ui.print("\nResumen de clasificacion", "bold")
    ui.print(f"Origen:  {c.source}")
    ui.print(f"Destino: {c.target_path}")
    ui.print(f"Nota:    {c.note_path}")
    ui.print(f"Tipo:    {c.resource_type}")
    ui.print(f"Categoria: {c.category}")
    ui.print(f"Estado:  {c.status}")
    ui.print(f"Archivado: {c.archived}")
    ui.print(f"Cover:   {c.cover}")
    ui.print(f"Tags:    {', '.join(c.tags)}")

    choice = choose_from_list("Confirmar", ["Confirmar y mover", "Cancelar"], default_index=0)
    if choice != "Confirmar y mover":
        ui.print("Operacion cancelada.", "yellow")
        return False

    final_target = resolve_duplicate_target(c.target_path)
    if final_target is None:
        ui.print("Operacion cancelada por duplicado.", "yellow")
        return False

    c.target_path = final_target
    c.target_path.parent.mkdir(parents=True, exist_ok=True)
    c.note_path.parent.mkdir(parents=True, exist_ok=True)

    shutil.move(str(c.source), str(c.target_path))
    note_content = render_note(c, vault_path)
    c.note_path.write_text(note_content, encoding="utf-8")
    write_logs(c, vault_path, config)
    ui.print("Clasificacion completada.", "green")
    return True


def write_logs(c: Classification, vault_path: Path, config: Dict) -> None:
    logs_dir = vault_path / Path(config.get("logs_path", "zResources/_logs"))
    logs_dir.mkdir(parents=True, exist_ok=True)
    csv_path = logs_dir / config.get("movement_csv", "movimientos-para.csv")
    md_path = logs_dir / config.get("movement_md", "movimientos-para.md")
    last_path = logs_dir / config.get("last_movement_json", "ultimo-movimiento.json")
    now = datetime.now().isoformat(timespec="seconds")

    if not csv_path.exists():
        csv_path.write_text("fecha,accion,archivo_origen,archivo_destino,nota_obsidian,tipo,categoria,subcategory,status,archived\n", encoding="utf-8")
    with csv_path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([now, "move_create_note", str(c.source), str(c.target_path), str(c.note_path), c.resource_type, c.category, c.subcategory, c.status, c.archived])

    with md_path.open("a", encoding="utf-8") as f:
        f.write(f"\n## {now}\n")
        f.write(f"- Accion: move_create_note\n")
        f.write(f"- Origen: `{c.source}`\n")
        f.write(f"- Destino: `{c.target_path}`\n")
        f.write(f"- Nota: `{c.note_path}`\n")
        f.write(f"- Tipo: `{c.resource_type}`\n")
        f.write(f"- Categoria: `{c.category}`\n")
        f.write(f"- Status: `{c.status}`\n")
        f.write(f"- Archived: `{c.archived}`\n")

    last_payload = {
        "fecha": now,
        "accion": "move_create_note",
        "source_original": str(c.source),
        "target_path": str(c.target_path),
        "note_path": str(c.note_path),
        "resource_type": c.resource_type,
        "category": c.category,
        "status": c.status,
        "archived": c.archived,
    }
    last_path.write_text(json.dumps(last_payload, ensure_ascii=False, indent=2), encoding="utf-8")


def undo_last(vault_path: Path, config: Dict) -> None:
    logs_dir = vault_path / Path(config.get("logs_path", "zResources/_logs"))
    last_path = logs_dir / config.get("last_movement_json", "ultimo-movimiento.json")
    if not last_path.exists():
        ui.print("No existe registro de ultimo movimiento.", "yellow")
        return
    data = json.loads(last_path.read_text(encoding="utf-8") or "{}")
    if not data or data.get("accion") != "move_create_note":
        ui.print("No hay movimiento valido para deshacer.", "yellow")
        return

    source_original = Path(data["source_original"])
    target_path = Path(data["target_path"])
    note_path = Path(data["note_path"])

    ui.print("\nUltimo movimiento", "bold")
    ui.print(f"Mover de vuelta: {target_path} -> {source_original}")
    ui.print(f"Eliminar nota: {note_path}")

    if not ui.confirm("¿Deshacer este movimiento?", default=False):
        ui.print("Deshacer cancelado.", "yellow")
        return

    if target_path.exists():
        source_original.parent.mkdir(parents=True, exist_ok=True)
        final_source = resolve_duplicate_target(source_original)
        if final_source is None:
            ui.print("No se pudo deshacer por conflicto en origen.", "red")
            return
        shutil.move(str(target_path), str(final_source))
    else:
        ui.print("El archivo/carpeta destino ya no existe. No se puede mover de vuelta.", "yellow")

    if note_path.exists():
        note_path.unlink()
        ui.print("Nota eliminada.", "green")
    else:
        ui.print("La nota ya no existe.", "yellow")

    data["undone_at"] = datetime.now().isoformat(timespec="seconds")
    data["accion"] = "undone"
    last_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    ui.print("Ultimo movimiento deshecho.", "green")


def select_item_interactively(inbox: Path) -> Optional[Path]:
    items = list_first_level(inbox)
    if not items:
        ui.print("INBOX esta vacio.", "yellow")
        return None
    print_items(items)
    while True:
        raw = ui.input("Selecciona numero, escribe busqueda, o ENTER para cancelar", default="")
        if raw == "":
            return None
        if raw.isdigit() and 1 <= int(raw) <= len(items):
            return items[int(raw) - 1]
        matches = fuzzy_search(items, raw)
        if not matches:
            ui.print("Sin resultados.", "yellow")
            continue
        print_items(matches, limit=15)
        raw2 = ui.input("Selecciona numero de resultado, ENTER para volver", default="")
        if raw2.isdigit() and 1 <= int(raw2) <= len(matches):
            return matches[int(raw2) - 1]

def elegir_imagen_cercana(
    archivo_origen: Path,
    vault_path: Path,
    covers_relative_dir: str,
    resource_type: str,
    titulo: str,
) -> str:
    """
    Busca imagenes cercanas al archivo/carpeta procesado.
    Para archivos: revisa la carpeta contenedora.
    Para carpetas: permite buscar solo en primer nivel o tambien dentro de subcarpetas.
    Copia la imagen elegida dentro del vault y devuelve el wikilink para cover.
    """
    carpeta = archivo_origen if archivo_origen.is_dir() else archivo_origen.parent

    if archivo_origen.is_dir():
        modo = choose_from_list(
            "Busqueda de portada para carpeta completa",
            ["Solo primer nivel", "Incluir subcarpetas"],
            default_index=0,
        )
        iterator = carpeta.rglob("*") if modo == "Incluir subcarpetas" else carpeta.iterdir()
    else:
        iterator = carpeta.iterdir()

    imagenes = sorted(
        [p for p in iterator if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS],
        key=lambda p: (
            0 if any(w in p.stem.lower() for w in ["cover", "portada", "poster", "thumbnail", "thumb"]) else 1,
            p.name.lower(),
        ),
    )

    if not imagenes:
        ui.print("\nNo se encontraron imagenes cercanas.", "yellow")
        return ""

    max_show = 50
    ui.print("\nImagenes cercanas encontradas:", "bold")
    for i, img in enumerate(imagenes[:max_show], start=1):
        try:
            shown = img.relative_to(carpeta).as_posix()
        except Exception:
            shown = img.name
        ui.print(f"{i}. {shown}")
    if len(imagenes) > max_show:
        ui.print(f"Mostrando {max_show} de {len(imagenes)} imagenes encontradas.", "yellow")
    ui.print("0. No usar imagen cercana")

    while True:
        opcion = ui.input("Selecciona imagen de portada", default="0").strip()

        if opcion == "0":
            return ""

        if opcion.isdigit() and 1 <= int(opcion) <= min(len(imagenes), max_show):
            seleccionada = imagenes[int(opcion) - 1]
            return copiar_portada_a_vault(
                imagen_origen=seleccionada,
                vault_path=vault_path,
                covers_relative_dir=covers_relative_dir,
                resource_type=resource_type,
                titulo=titulo,
            )

        ui.print("Opcion invalida.", "red")


def elegir_imagen_manual(
    vault_path: Path,
    covers_relative_dir: str,
    resource_type: str,
    titulo: str,
) -> str:
    """
    Permite escribir/pegar una ruta de imagen local, la copia dentro del vault
    y devuelve el wikilink para YAML.
    """
    raw = ui.input("Ruta de imagen", default="").strip().strip('"')
    if not raw:
        return ""

    imagen = Path(raw)
    if not imagen.exists() or not imagen.is_file() or imagen.suffix.lower() not in IMAGE_EXTENSIONS:
        ui.print("La ruta no existe o no es una imagen soportada.", "red")
        return ""

    return copiar_portada_a_vault(
        imagen_origen=imagen,
        vault_path=vault_path,
        covers_relative_dir=covers_relative_dir,
        resource_type=resource_type,
        titulo=titulo,
    )


def copiar_portada_a_vault(
    imagen_origen: Path,
    vault_path: Path,
    covers_relative_dir: str,
    resource_type: str,
    titulo: str,
) -> str:
    """
    Copia una imagen al directorio de portadas dentro del vault.
    Usa nombres slugificados y evita sobrescribir archivos existentes.
    """
    tipo_carpeta = cover_folder_for_type(resource_type)
    destino_rel = Path(covers_relative_dir) / tipo_carpeta / f"{slug(titulo)}-cover{imagen_origen.suffix.lower()}"
    destino_abs = vault_path / destino_rel
    destino_abs.parent.mkdir(parents=True, exist_ok=True)

    destino_final = unique_path(destino_abs)
    shutil.copy2(imagen_origen, destino_final)

    rel_obsidian = as_posix_rel(destino_final, vault_path)
    return f"[[{rel_obsidian}]]"

def main() -> None:
    script_dir = Path(__file__).resolve().parent
    config = load_config(script_dir)
    vault_path = choose_path_if_missing(Path(config["vault_path"]), "vault_path")
    para_root = choose_path_if_missing(Path(config["default_para_root"]), "default_para_root")
    inbox = Path(config.get("default_inbox_path", str(para_root / "00-INBOX")))
    if not inbox.exists():
        ui.print(f"No se encontro INBOX configurado: {inbox}", "yellow")
        inbox = choose_path_if_missing(para_root / "00-INBOX", "INBOX")

    while True:
        ui.print(f"\n========================================\n{APP_NAME}\n========================================", "bold")
        ui.print(f"Vault: {vault_path}")
        ui.print(f"PARA:  {para_root}")
        ui.print(f"INBOX: {inbox}")
        option = choose_from_list("Menu inicial", ["Modo rapido", "Modo logica completa", "Ver archivos disponibles", "Buscar archivo", "Deshacer ultimo movimiento", "Salir"], default_index=0)

        if option == "Salir":
            break
        if option == "Ver archivos disponibles":
            print_items(list_first_level(inbox), limit=100)
            continue
        if option == "Deshacer ultimo movimiento":
            undo_last(vault_path, config)
            continue

        item = select_item_interactively(inbox)
        if item is None:
            continue

        if option in {"Modo rapido", "Buscar archivo"}:
            classification = quick_classification(item, para_root, vault_path, config)
        else:
            classification = full_logic_classification(item, para_root, vault_path, config)
        confirm_and_execute(classification, vault_path, config)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelado por el usuario.")
        sys.exit(1)
