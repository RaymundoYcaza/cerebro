from __future__ import annotations

import re
from typing import Any

import yaml


class ObsidianDumper(yaml.SafeDumper):
    """YAML dumper compatible con Obsidian/Dataview."""


def is_wikilink(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    value = value.strip()
    return value.startswith("[[") and value.endswith("]]")


def _str_presenter(dumper: yaml.SafeDumper, data: str):
    """
    Representa wikilinks como strings YAML con comilla simple:

    source: '[[Mi nota]]'

    Evita que YAML los interprete como listas anidadas.
    """
    if is_wikilink(data):
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="'")

    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


ObsidianDumper.add_representer(str, _str_presenter)


def as_list(value: Any) -> list[str]:
    """
    Normaliza valores del modelo a lista.

    Casos cubiertos:
    - None -> []
    - string simple -> [string]
    - string con saltos reales o escapados -> lista por línea
    - lista -> lista limpia de strings
    - otro tipo -> [str(value)]
    """
    if value is None:
        return []

    if isinstance(value, str):
        value = value.replace("\\n", "\n").strip()
        if not value:
            return []
        return [x.strip(" -\t") for x in value.splitlines() if x.strip()]

    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(as_list(item))
        return [x for x in out if x.strip()]

    text = str(value).strip()
    return [text] if text else []


def normalize_wikilink(value: str | None) -> str | None:
    """
    Devuelve un wikilink limpio sin comillas manuales.

    Entrada:
    - "Nota" -> "[[Nota]]"
    - "[[Nota]]" -> "[[Nota]]"
    - "'[[Nota]]'" -> "[[Nota]]"
    """
    if value is None:
        return None

    text = str(value).strip()

    if not text:
        return None

    # Quitar comillas manuales externas si existen.
    text = text.strip("'").strip('"').strip()

    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2].strip()
    else:
        inner = text

    inner = re.sub(r"[\[\]]", "", inner).strip()
    if not inner:
        return None

    return f"[[{inner}]]"


def normalize_wikilinks(values: Any) -> list[str]:
    links: list[str] = []

    for item in as_list(values):
        link = normalize_wikilink(item)
        if link and link not in links:
            links.append(link)

    return links


def clean_none_values(data: dict[str, Any]) -> dict[str, Any]:
    """
    Mantiene claves útiles, pero elimina None en listas y normaliza estructuras simples.
    No elimina None top-level porque algunas propiedades vacías son intencionales
    para Obsidian/Dataview.
    """
    cleaned: dict[str, Any] = {}

    for key, value in data.items():
        if isinstance(value, list):
            cleaned[key] = [x for x in value if x is not None and str(x).strip()]
        else:
            cleaned[key] = value

    return cleaned


def safe_yaml_dump(data: dict[str, Any]) -> str:
    return yaml.dump(
        clean_none_values(data),
        Dumper=ObsidianDumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip()


def build_frontmatter(data: dict[str, Any]) -> str:
    return "---\n" + safe_yaml_dump(data) + "\n---\n"
