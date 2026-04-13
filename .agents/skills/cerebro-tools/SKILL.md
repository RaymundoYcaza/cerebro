---
name: cerebro-tools
description: Colección de herramientas operativas para gestionar el vault Cerebro. Incluye atomización de notas, resúmenes diarios, investigación profunda y gestión del Inbox (Vault Manager). Úsala para procesar el Inbox (+/), crear notas evergreen en Atlas/Dots/ y generar reportes de actividad.
---

# Cerebro Tools

Esta skill proporciona flujos de trabajo especializados para mantener la integridad y utilidad del vault personal de Raymundo siguiendo el sistema Ideaverse.

## Flujos de Trabajo (Workflows)

### 1. Atomize (Atomizar nota)
Convierte una nota del Inbox (`+/`) o una idea cruda en una nota "evergreen" para `Atlas/Dots/`.

- **Regla de Oro**: Una sola idea por nota.
- **Proceso**:
    1. Extraer la idea central.
    2. Generar Frontmatter (título, tags, fecha, tipo: atom).
    3. Redactar el cuerpo de forma concisa.
    4. Sugerir 2-5 enlaces a notas relacionadas o MOCs en `Atlas/Maps/`.
- **Destino sugerido**: `vault/raymundo_ideaverse/Atlas/Dots/Nombre de la nota.md`

### 2. Daily Summary (Resumen Diario)
Genera un reporte de actividad basado en las notas creadas hoy en `Calendar/` y los logs de sesión.

- **Estructura**:
    - **Qué pasó hoy**: Resumen narrativo breve.
    - **Completado**: Lista de tareas o hitos terminados.
    - **Pendiente**: Tareas abiertas para mañana.
    - **Bloqueos**: Problemas detectados.
    - **Próximas acciones**: Pasos inmediatos sugeridos.

### 3. Deep Research (Investigación Profunda)
Síntesis estructurada sobre un tema técnico o estratégico usando el vault como base.

- **Proceso**:
    1. Buscar en el vault con `qmd` (mínimo 3 queries distintas).
    2. Usar fuentes externas solo si el vault es insuficiente.
    3. Comparar opciones y presentar tradeoffs.
    4. Proponer una recomendación accionable.

### 4. Vault Manager (Gestor del Inbox)
Mantenimiento operativo del Inbox (`+/`) y normalización del vault.

- **Tareas**:
    - Escanear `+/` para detectar notas sin frontmatter.
    - Sugerir tipos (atom, moc, daily, effort, inbox).
    - Proponer tags y títulos descriptivos.
- **Acción Manual**: Ejecuta `scripts/vault_manager/repair-ui.sh` o `scripts/vault_manager/repair.py --apply` solo tras confirmación del usuario.

## Comandos Útiles

- **Reparar Vault**: `python3 scripts/vault_manager/repair.py` (simulación)
- **Reindexar**: `./qmd.sh embed`
- **Buscar**: `qmd query "término"`

## Ejemplo de Frontmatter Estándar

```yaml
---
title: Título descriptivo
tags: [tag1, tag2]
created: YYYY-MM-DD
type: atom
---
```
