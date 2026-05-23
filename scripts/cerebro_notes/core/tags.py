\
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass


@dataclass
class TagNormalizationResult:
    tags: list[str]
    moved_to_z: list[str]
    rejected: list[str]


def _clean_segment(segment: str) -> str:
    segment = segment.strip().replace("#", "")
    segment = re.sub(r"\s+", "-", segment)
    segment = re.sub(r"[^A-Za-z0-9_\-/áéíóúÁÉÍÓÚñÑüÜ]+", "", segment)
    return segment.strip("-/")


def _to_pascalish(value: str) -> str:
    value = value.replace("#", "").replace("_", " ").replace("-", " ").replace("/", " ")
    value = unicodedata.normalize("NFKC", value).strip()
    parts = [p for p in re.split(r"\s+", value) if p]
    if not parts:
        return "General"
    fixed = []
    known_upper = {"api", "php", "sql", "http", "https", "ssh", "dns", "wsl", "llm", "ia", "ui", "ux", "json", "yaml"}
    for p in parts:
        if p.lower() in known_upper:
            fixed.append(p.upper())
        else:
            fixed.append(p[:1].upper() + p[1:])
    return "".join(fixed)


def normalize_tags(
    model_main_tags: list[str] | None,
    model_z_tags: list[str] | None,
    default_main_tags: list[str],
    default_z_tags: list[str],
    allowed_roots: list[str],
    general_root: str = "z",
    max_main_tags: int = 8,
    max_z_tags: int = 12,
) -> TagNormalizationResult:
    """
    Política:
    - Fuera de z solo se aceptan source, output, note, map, cerebro como raíz.
    - Todo lo demás se transforma en z/Algo.
    """
    allowed = set(allowed_roots)
    final: list[str] = []
    moved: list[str] = []
    rejected: list[str] = []

    def add(tag: str):
        tag = _clean_segment(tag)
        if tag and tag not in final:
            final.append(tag)

    for tag in default_main_tags or []:
        add(tag)

    for tag in model_main_tags or []:
        raw = (tag or "").strip().replace("#", "")
        if not raw:
            continue
        root = raw.split("/", 1)[0]
        if root in allowed:
            add(raw)
        elif root == general_root:
            add(raw)
        else:
            ztag = f"{general_root}/{_to_pascalish(raw)}"
            add(ztag)
            moved.append(raw)

    for tag in default_z_tags or []:
        if tag.startswith(f"{general_root}/"):
            add(tag)
        else:
            add(f"{general_root}/{_to_pascalish(tag)}")

    for tag in model_z_tags or []:
        raw = (tag or "").strip().replace("#", "")
        if not raw:
            continue
        if raw.startswith(f"{general_root}/"):
            add(raw)
        else:
            add(f"{general_root}/{_to_pascalish(raw)}")

    main = []
    ztags = []
    for tag in final:
        if tag.startswith(f"{general_root}/"):
            ztags.append(tag)
        else:
            root = tag.split("/", 1)[0]
            if root in allowed:
                main.append(tag)
            else:
                moved.append(tag)
                ztags.append(f"{general_root}/{_to_pascalish(tag)}")

    main = main[:max_main_tags]
    ztags = ztags[:max_z_tags]

    return TagNormalizationResult(tags=main + ztags, moved_to_z=moved, rejected=rejected)
