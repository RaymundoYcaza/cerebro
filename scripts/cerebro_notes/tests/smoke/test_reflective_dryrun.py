from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from reflective.final_markdown import render_thing_note
from reflective.markdown import render_reflective_session
from technical.markdown import render_note


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_markdown(markdown: str, label: str) -> None:
    require(markdown.startswith("---\n"), f"{label} debe iniciar con frontmatter")
    require("\n---\n" in markdown, f"{label} debe cerrar frontmatter")
    require("\n# " in markdown, f"{label} debe contener título markdown")
    require("'''" not in markdown, f"{label} no debe contener triples comillas")


def validate_renderers() -> None:
    extracted_reflective = {
        "thing_note_candidate": "Idea de prueba",
        "possible_links": ["[[Mapa Cerebro]]"],
        "signal": "Una señal mínima.",
        "why_it_matters": "Importa para validar render.",
        "gaps": ["Aclarar alcance"],
    }

    session = render_reflective_session(
        extracted=extracted_reflective,
        tags=["note/reflection", "z/LYT"],
        source_hash="abc123",
        model_used="smoke-model",
        original_content="Contenido original",
    )
    validate_markdown(session, "sesión reflexiva")

    thing = render_thing_note(
        extracted=extracted_reflective,
        tags=["note/reflection", "z/LYT"],
        source_hash="abc123",
        model_used="smoke-model",
        own_voice="Redacción propia.",
        connections="[[Mapa Cerebro]]",
        session_link="[[Idea de prueba--session]]",
        source_link="[[Fuente]]",
    )
    validate_markdown(thing, "Thing Note")

    technical = render_note(
        extracted={
            "title": "Nota técnica",
            "summary": "Resumen",
            "suggested_links": ["Docker"],
            "steps": ["Paso uno"],
            "commands": ["echo ok"],
            "errors": [],
            "gaps": [],
        },
        tags=["note/technical"],
        source_hash="def456",
        model_used="smoke-model",
        source_type="technical-note",
        review_status="pending",
        original_content="echo ok",
        include_original_excerpt=False,
    )
    validate_markdown(technical, "nota técnica")


def validate_reflective_dryrun() -> None:
    result = subprocess.run(
        [
            "python3",
            "run_reflective.py",
            "--text",
            "Una idea de prueba para smoke test.",
            "--config",
            "config.yaml",
            "--dry-run",
            "--nothink",
        ],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
        timeout=240,
    )

    if result.returncode != 0:
        raise AssertionError(
            "run_reflective.py --dry-run falló\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )

    validate_markdown(result.stdout, "reflective dry-run")
    require("source_hash:" in result.stdout, "reflective dry-run debe incluir source_hash")


def main() -> None:
    validate_renderers()
    validate_reflective_dryrun()
    print("OK: reflective dry-run smoke")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: reflective dry-run smoke: {exc}", file=sys.stderr)
        raise SystemExit(1)
