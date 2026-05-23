# Spec: Fase 6 — Búsqueda semántica opcional

## Estado

backlog

## Objetivo

Agregar búsqueda semántica opcional con Qdrant/Ollama para sugerir conexiones.

## Tareas

- [ ] Crear `core/vector_search.py`.
- [ ] Crear `reflective/connections.py`.
- [ ] Leer configuración de vector y Ollama.
- [ ] Implementar fallback fuzzy.
- [ ] No fallar si Qdrant no está disponible.
- [ ] Crear smoke tests opcionales.
- [ ] Documentar funcionalidad.

## Criterios de aceptación

- [ ] Qdrant no es obligatorio.
- [ ] Fallback fuzzy funciona.
- [ ] No modifica notas.
- [ ] Solo sugiere conexiones.
- [ ] `harness check` pasa.
