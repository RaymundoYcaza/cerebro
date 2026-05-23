from __future__ import annotations

import json
import re
from typing import Any

import requests

from .prompts import SYSTEM_PROMPT, build_user_prompt


class ReflectiveLLMError(RuntimeError):
    pass


def _extract_json(text: str) -> dict[str, Any]:
    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))

    start = text.find("{")
    end = text.rfind("}")

    if start >= 0 and end > start:
        return json.loads(text[start : end + 1])

    raise ReflectiveLLMError("No se pudo extraer JSON válido de la respuesta del modelo.")


def chat_reflective_json(
    *,
    base_url: str,
    model: str,
    content: str,
    think: bool = False,
    temperature: float = 0,
    timeout_seconds: int = 180,
    fallback_model: str | None = None,
) -> tuple[dict[str, Any], str]:
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
            raise ReflectiveLLMError(f"Error usando modelo {model}: {primary_exc}") from primary_exc

        body["model"] = fallback_model

        resp = requests.post(url, json=body, timeout=timeout_seconds)
        resp.raise_for_status()

        raw = resp.json()
        message = raw.get("message", {})
        content_text = message.get("content") or raw.get("response") or ""

        return _extract_json(content_text), fallback_model
