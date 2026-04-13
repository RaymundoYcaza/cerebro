import os
from config import load_config

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


def openai_capture_stub(profile: str) -> dict:
    config = load_config()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY no está definido en el entorno")

    if OpenAI is None:
        raise RuntimeError("Falta instalar la librería openai: pip install openai")

    client = OpenAI(api_key=api_key)
    model = config.get("defaults", {}).get("openai_model", "gpt-4o-mini")

    raw_text = input("Pega aquí el contenido libre para que OpenAI lo estructure:\n> ").strip()
    if not raw_text:
        raise RuntimeError("No se recibió contenido")

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": f"Eres un asistente que estructura notas de Obsidian para el perfil: {profile}. Devuelve JSON válido, sin markdown, con campos apropiados para este perfil."},
            {"role": "user", "content": raw_text}
        ]
    )

    # Nota: Aquí se debería parsear el JSON de response.choices[0].message.content
    # Por ahora mantenemos la lógica de devolver un dict compatible con engine.py
    import json
    try:
        data = json.loads(response.choices[0].message.content)
        if "body" not in data:
            data["body"] = raw_text
        return data
    except Exception:
        return {
            "title": "Pendiente procesar IA",
            "body": raw_text,
            "raw_llm_output": response.choices[0].message.content
        }
