# QMD Portable — Inicialización Rápida

Este documento permite restaurar el entorno QMD portable en un nuevo equipo rápidamente.

---

# Ubicación Base

Carpeta portable:

C:\Users\raymundo\Downloads\CerebroPortable\qmd

Estructura esperada:

CerebroPortable
└── qmd
    ├── bin
    ├── .cache
    │   └── qmd
    │       ├── index.sqlite
    │       ├── embeddings
    │       └── collections
    ├── repo
    └── docs

---

# Paso 1 — Abrir Git Bash en carpeta QMD

cd ~/Downloads/CerebroPortable/qmd

---

# Paso 2 — Configurar cache portable

export XDG_CACHE_HOME="/c/Users/raymundo/Downloads/CerebroPortable/qmd/.cache"

Verificar:

echo $XDG_CACHE_HOME

Debe mostrar:

/c/Users/raymundo/Downloads/CerebroPortable/qmd/.cache

---

# Paso 3 — Verificar QMD

./bin/qmd status

Debe mostrar:

Index:
C:/Users/raymundo/Downloads/CerebroPortable/qmd/.cache/qmd/index.sqlite

---

# Paso 4 — Continuar embeddings si es necesario

./bin/qmd embed

Esto continuará donde se quedó.

---

# Paso 5 — Verificar colecciones

./bin/qmd ls

---

# Búsqueda de prueba

./bin/qmd search "docker error"

---

# Comandos útiles

Buscar semántico

./bin/qmd search "configurar rclone"

Buscar en colección específica

./bin/qmd search "error typescript" -c raymundo_ideaverse

Listar documentos

./bin/qmd ls raymundo_ideaverse

---

# Modelos locales usados

Embedding:
embeddinggemma-300M

Reranking:
Qwen3-Reranker-0.6B

Generation:
qmd-query-expansion-1.7B

Todos ejecutados localmente.

---

# GPU detectada

Intel HD Graphics 520
Vulkan enabled

---

# Ventajas del setup

- Portable
- Sin Ollama
- Sin servidor
- Semántico híbrido
- Compatible con agentes
- Compatible con Obsidian

---

# Si falla algo

Verificar:

./bin/qmd status

Verificar variable:

echo $XDG_CACHE_HOME
