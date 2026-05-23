\
from __future__ import annotations

import json
import re
from typing import Any

import requests


class OllamaError(RuntimeError):
    pass


TECH_NOTE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "note_kind": {
            "type": "string",
            "enum": [
                "technical-howto",
                "technical-troubleshooting",
                "technical-reference",
                "source-extract",
                "technical-concept",
            ],
        },
        "main_tags": {"type": "array", "items": {"type": "string"}},
        "z_tags": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
        "problem": {"type": "string"},
        "context": {"type": "string"},
        "solution": {"type": "string"},
        "steps": {"type": "array", "items": {"type": "string"}},
        "commands": {"type": "array", "items": {"type": "string"}},
        "errors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "error": {"type": "string"},
                    "cause": {"type": "string"},
                    "fix": {"type": "string"},
                },
                "required": ["error", "cause", "fix"],
            },
        },
        "related_terms": {"type": "array", "items": {"type": "string"}},
        "suggested_links": {"type": "array", "items": {"type": "string"}},
        "gaps": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
    },
    "required": [
        "title",
        "note_kind",
        "main_tags",
        "z_tags",
        "summary",
        "problem",
        "context",
        "solution",
        "steps",
        "commands",
        "errors",
        "related_terms",
        "suggested_links",
        "gaps",
        "confidence",
    ],
}


SYSTEM_PROMPT = """\
Eres un extractor técnico para un vault Obsidian.
Tu trabajo es convertir texto crudo en una ficha técnica estructurada.

Reglas:
- Responde SOLO JSON válido.
- No inventes comandos que no estén respaldados por el texto.
- Si falta información, escríbela en "gaps".
- No agregues prosa fuera del JSON.
- Idioma de salida: español.
- Las etiquetas generales deben ir en z_tags como z/Docker, z/Laravel, z/Ubuntu.
- Fuera de z solo puedes sugerir tags con raíz source, output, note, map o cerebro.
- Usa main_tags para tags estructurales, por ejemplo note/technical, note/technical/howto, note/technical/troubleshooting.
"""


def build_user_prompt(content: str) -> str:
    return f"""\
Analiza el siguiente contenido técnico multilinea y extrae una nota técnica.

Contenido:
<<<BEGIN_CONTENT
{content}
END_CONTENT>>>

Devuelve un JSON que cumpla este esquema conceptual:
- title: título breve, accionable y específico.
- note_kind: technical-howto | technical-troubleshooting | technical-reference | source-extract | technical-concept.
- main_tags: solo tags con raíz source/output/note/map/cerebro.
- z_tags: etiquetas generales bajo z, ejemplo z/Docker, z/Laravel, z/Ubuntu.
- summary: resumen breve.
- problem: problema o necesidad.
- context: contexto técnico, versiones o entorno si aparece.
- solution: solución consolidada.
- steps: pasos ordenados.
- commands: comandos citados o inferidos con alta confianza desde el texto.
- errors: lista de objetos con error, cause, fix.
- related_terms: términos para conectar notas.
- suggested_links: títulos de notas Obsidian sugeridas, sin corchetes.
- gaps: vacíos o cosas por confirmar.
- confidence: low | medium | high.
"""


def _extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Recuperación básica si el modelo envolvió JSON en markdown o texto.
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))

    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        return json.loads(text[start : end + 1])

    raise OllamaError("No se pudo extraer JSON válido de la respuesta del modelo.")


def chat_json(
    base_url: str,
    model: str,
    content: str,
    think: bool = False,
    temperature: float = 0,
    timeout_seconds: int = 180,
    fallback_model: str | None = None,
) -> tuple[dict[str, Any], str]:
    """
    Llama a /api/chat con schema JSON.
    Devuelve (payload_json, model_used).
    """
    url = base_url.rstrip("/") + "/api/chat"
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(content)},
        ],
        "stream": False,
        "think": bool(think),
        "format": "json",
        "options": {"temperature": temperature},
    }

    try:
        resp = requests.post(url, json=body, timeout=timeout_seconds)
        resp.raise_for_status()
        raw = resp.json()
        message = raw.get("message", {})
        content_text = message.get("content") or raw.get("response") or ""
        return _extract_json(content_text), model
    except Exception as primary_exc:
        if not fallback_model or fallback_model == model:
            raise OllamaError(f"Error usando modelo {model}: {primary_exc}") from primary_exc

        body["model"] = fallback_model
        resp = requests.post(url, json=body, timeout=timeout_seconds)
        resp.raise_for_status()
        raw = resp.json()
        message = raw.get("message", {})
        content_text = message.get("content") or raw.get("response") or ""
        return _extract_json(content_text), fallback_model


def embed(
    base_url: str,
    model: str,
    inputs: list[str],
    timeout_seconds: int = 180,
) -> list[list[float]]:
    url = base_url.rstrip("/") + "/api/embed"
    body = {"model": model, "input": inputs}
    resp = requests.post(url, json=body, timeout=timeout_seconds)
    resp.raise_for_status()
    data = resp.json()
    return data["embeddings"]
