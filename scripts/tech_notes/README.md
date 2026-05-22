# Cerebro Tech Notes Base

Sistema base para convertir contenido técnico multilinea en notas Markdown para Obsidian y, opcionalmente, indexarlas en Qdrant.

Diseño:

- **Python manda**: lee, limpia, valida, crea archivos, normaliza tags e indexa.
- **Modelo local ayuda**: resume, clasifica, extrae pasos, detecta errores, sugiere enlaces y vacíos.
- **Obsidian conserva conocimiento legible**.
- **Qdrant conserva memoria semántica consultable**.

## Instalación sugerida

Desde tu raíz:

```bash
cd /mnt/c/cerebro
mkdir -p scripts/cerebro
# Descomprime la carpeta tech_notes dentro de scripts/cerebro/
cd scripts/cerebro/tech_notes

# Puedes usar el venv existente del proyecto:
source /mnt/c/cerebro/.venv/bin/activate

pip install -r requirements.txt
cp config.example.yaml config.yaml
```

Verifica Ollama:

```bash
curl http://localhost:11434/api/tags
```

Modelos sugeridos:

```bash
ollama pull qwen3.5:0.8b
ollama pull qwen3.5:2b
```

## Uso básico

Procesar un archivo:

```bash
python -m cerebro_tech.cli --input /mnt/c/cerebro/notas/docker-compose.txt --config config.yaml --write
```

Procesar texto desde stdin:

```bash
cat /mnt/c/cerebro/session.md | python -m cerebro_tech.cli --stdin --config config.yaml --write
```

Forzar thinking para casos más ambiguos:

```bash
python -m cerebro_tech.cli --input nota.txt --config config.yaml --write --think
```

Ver resultado sin escribir archivo:

```bash
python -m cerebro_tech.cli --input nota.txt --config config.yaml --dry-run
```

Indexar también en Qdrant:

1. Activa en `config.yaml`:

```yaml
vector:
  enabled: true
```

2. Ejecuta:

```bash
python -m cerebro_tech.cli --input nota.txt --config config.yaml --write --index
```

## Regla de tags

Solo estas raíces pueden existir fuera de `z`:

```text
source
output
note
map
cerebro
```

Cualquier etiqueta general como Docker, Laravel, Ubuntu, PHP, Ollama o Qdrant será normalizada a:

```text
z/Docker
z/Laravel
z/Ubuntu
z/PHP
z/Ollama
z/Qdrant
```

## Ejemplo de frontmatter generado

```yaml
---
up: []
related: []
created: 2026-05-22
sourceType: technical-note
tags:
  - note/technical
  - note/technical/howto
  - z/Docker
  - z/Ubuntu
ai:
  generated: true
  model: qwen3.5:0.8b
  reviewed: false
  review_status: pending
  confidence: medium
vector:
  indexed: false
  collection:
source:
  hash: abc123...
---
```

## Estructura generada

```text
scripts/cerebro/tech_notes/
├── README.md
├── config.example.yaml
├── requirements.txt
└── cerebro_tech/
    ├── __init__.py
    ├── cli.py
    ├── config.py
    ├── llm.py
    ├── markdown.py
    ├── pipeline.py
    ├── qdrant_store.py
    ├── tags.py
    └── text_utils.py
```

## Notas de diseño

- El modelo debe devolver JSON, pero el script incluye recuperación básica si el modelo responde con texto extra.
- Las etiquetas se validan después del modelo.
- El contenido original puede conservarse parcialmente como auditoría.
- Los vacíos detectados quedan como checklist.
- La nota se crea como `reviewed: false` para no mezclar conocimiento consolidado con notas generadas.
