from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.frontmatter import build_frontmatter


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    frontmatter = build_frontmatter(
        {
            "title": "Café y señal",
            "source": "[[Nota]]",
            "related": ["[[A]]", "[[B]]"],
            "summary": "línea uno\\nlínea dos",
            "tags": ["note/reflection", "z/Prueba"],
        }
    )

    require(frontmatter.startswith("---\n"), "frontmatter debe abrir con ---")
    require(frontmatter.endswith("\n---\n"), "frontmatter debe cerrar con ---")
    require("source: '[[Nota]]'" in frontmatter, "source wikilink debe serializarse como string con comilla simple")
    require("- '[[A]]'" in frontmatter and "- '[[B]]'" in frontmatter, "related debe serializar wikilinks como lista")
    require("'''" not in frontmatter, "frontmatter no debe contener triples comillas simples")
    require("Café y señal" in frontmatter, "unicode debe preservarse")

    yaml_body = frontmatter.removeprefix("---\n").removesuffix("\n---\n")
    parsed = yaml.safe_load(yaml_body)

    require(parsed["source"] == "[[Nota]]", "source debe parsear como string")
    require(parsed["related"] == ["[[A]]", "[[B]]"], "related debe parsear como lista real")
    require(parsed["summary"] == "línea uno\\nlínea dos", "strings con saltos escapados deben preservarse")
    require(parsed["tags"] == ["note/reflection", "z/Prueba"], "tags debe seguir siendo lista")

    print("OK: frontmatter smoke")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: frontmatter smoke: {exc}", file=sys.stderr)
        raise SystemExit(1)
