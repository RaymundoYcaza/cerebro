---
up: []
related: []
created: 2026-03-26
---

# 🧠 Tabla 1 — Cuándo usar cada modelo

|Modelo|Para qué|Cuándo usarlo|
|---|---|---|
|**gemma3:4b**|Razonamiento general, análisis, planificación, PKM, Obsidian|Cuando necesites pensar, analizar, diseñar arquitectura, escribir documentación|
|**deepseek-coder:6.7b**|Programación principal (backend, proyectos grandes)|Laravel, APIs REST, refactorización grande, debugging complejo|
|**starcoder2:3b**|Frontend y web|Astro, Ionic, TypeScript, HTML, CSS, JS|
|**qwen2.5-coder:3b**|Scripts y automatización|Scripts Python, Bash, utilidades pequeñas, herramientas internas|
|**moondream**|Imágenes|Analizar logos, diagramas, capturas, OCR básico|
|**codegemma:2b**|Programación ligera rápida|Autocompletado rápido, snippets pequeños|
|**deepseek-coder:1.3b**|Emergencia / batería / offline extremo|Cuando no tengas GPU, estés con batería o necesites máxima velocidad|

---

# 🧠 Cómo se complementan (tu "equipo de agentes")

Tu stack queda así:

```
Gemma3 → cerebro general
DeepSeek 6.7B → programador senior
StarCoder2 → frontend developer
Qwen coder → script engineer
CodeGemma → junior rápido
DeepSeek 1.3B → modo supervivencia
Moondream → visión
```

Esto es **extremadamente potente para ser local**.

---

# ⚙️ Tabla 2 — Comandos para instalar en Ollama

Ejecuta estos comandos:

| Modelo              | Comando                           |
| ------------------- | --------------------------------- |
| gemma3:4b           | `ollama pull gemma3:4b`           |
| deepseek-coder:6.7b | `ollama pull deepseek-coder:6.7b` |
| starcoder2:3b       | `ollama pull starcoder2:3b`       |
| qwen2.5-coder:3b    | `ollama pull qwen2.5-coder:3b`    |
| moondream           | `ollama pull moondream`           |
| codegemma:2b        | `ollama pull codegemma:2b`        |
| deepseek-coder:1.3b | `ollama pull deepseek-coder:1.3b` |

---

# Orden recomendado de instalación

Para no saturar disco, instala en este orden:

Primero esenciales:

```bash
ollama pull gemma3:4b
ollama pull deepseek-coder:6.7b
ollama pull moondream
```

Luego complementarios:

```bash
ollama pull starcoder2:3b
ollama pull qwen2.5-coder:3b
```

Luego opcionales:

```bash
ollama pull codegemma:2b
ollama pull deepseek-coder:1.3b
```

---

# Espacio aproximado que ocuparán

|Modelo|Tamaño aproximado|
|---|---|
|gemma3:4b|~3-4 GB|
|deepseek-coder:6.7b|~5-6 GB|
|starcoder2:3b|~2 GB|
|qwen2.5-coder:3b|~2 GB|
|moondream|~1 GB|
|codegemma:2b|~1.5 GB|
|deepseek-coder:1.3b|~800 MB|

Total aproximado:

**~15–18 GB**

Muy razonable.

---

# Bonus — Cómo ver tus modelos instalados

```bash
ollama list
```

---

# Bonus 2 — Cómo cambiar rápido de modelo

Ejemplo:

```bash
ollama run deepseek-coder:6.7b
```

Luego:

```bash
ollama run gemma3:4b
```

O en Open WebUI simplemente eliges el modelo.

---

Con esto tienes:

- Copilot local
    
- ChatGPT local
    
- Vision local
    
- RAG local
    
- Offline completo
    

Y sin pagar suscripciones.