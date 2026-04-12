import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


def openai_capture_stub(profile: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY no está definido")

    if OpenAI is None:
        raise RuntimeError("Falta instalar la librería openai: pip install openai")

    client = OpenAI(api_key=api_key)

    raw_text = input("Pega aquí el contenido libre para que OpenAI lo estructure:\n> ").strip()
    if not raw_text:
        raise RuntimeError("No se recibió contenido")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
Eres un asistente que estructura notas de Obsidian.
Perfil: {profile}
Devuelve JSON válido, sin markdown, con campos apropiados para este perfil.
Texto:
{raw_text}
""".strip(),
    )

    return {
        "raw_llm_output": response.output_text,
        "title": "Pendiente procesar IA",
        "body": raw_text,
    }
