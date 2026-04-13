---
up:
  - "[[Home]]"
related: []
created: 2026-04-12
type: meta
tags:
  - system/reglamento
---

# Reglamento del Vault

> [!info]- Estado
> Versión 1.0 — 2026-04-12
> Este documento es vivo. Púlelo cuando tu sistema evolucione.

---

## Propósito

Separar dos tipos de conocimiento:

| Tipo | Nombre | Descripción | Ejemplos |
|------|--------|-------------|----------|
| **Cerebro** | `atom` | Conocimiento que requiere conexiones, reflexión y evoluciona con el tiempo | Ideas, conceptos, reflexiones, síntesis personales |
| **Referencia** | `ref` | Conocimiento de consulta rápida — instrucciones, comandos, fixes | Comandos Docker, errores Laravel, cheatsheets |

---

## Las Dos Leyes Fundamentales

### Ley 1 — El Cerebro va a Atlas
Todo conocimiento que **requiera conexiones, reflexión o evolución** pertenece a `Atlas/Dots/`.

### Ley 2 — La Referencia va a Sources o Utilities
Todo conocimiento que **existe para ser consultado sin reflexión** pertenece a:
- `Sources/` — para referencias externas (artículos, libros, enlaces)
- `Atlas/Utilities/Cheatsheets/` — para comandos y procedimientos técnicos

---

## Clasificación por Carpeta

### `Atlas/Dots/` — Cerebro (conocimiento vivo)

**Subcarpetas:**

| Subcarpeta | Qué va ahí | Ejemplo |
|------------|------------|----------|
| `Things/` | Átomos: ideas, conceptos, principios | `Antifragility.md`, `Apofenia.md` |
| `Sources/` | Notas de fuentes externas: libros, artículos, videos, biblical | `Atomic Habits (book).md`, `Fuente I Ezequiel 16.md` |
| `Quotes/` | Citas coleccionadas | — |
| `Statements/` | Afirmaciones/tesis personales | `ACE honors the 3 head spaces of PKM.md` |
| `People/` | Notas sobre personas reales | `raymundo-ycaza-morales.md` |
| `X/` | Misceláneo que no calza en arriba | — |

**Frontmatter requerido:**
```yaml
---
up:          # MOC al que pertenece (e.g., "[[Concepts]]")
related:     # Enlaces a notas relacionadas (evita auto-links vacíos)
created:     # YYYY-MM-DD
in:          # Colección (e.g., "[[Concepts]]")
tags:        # type: atom | ref | effort | daily | moc
---
```

### `Sources/` — Referencia pura

**Qué va aquí:**
- Notas capturadas de artículos externos sin procesar
- Referencias rápidas a servicios (Stripe, AWS, etc.)
- Notas que no tienen frontmatter rico ni buscan conexión

**Frontmatter mínimo:**
```yaml
---
created: YYYY-MM-DD
tags: [ref]
---
```

### `Atlas/Utilities/Cheatsheets/` — Cheatsheets técnicos

**Qué va aquí:**
- Comandos Docker, Git, SSH, Ubuntu
- Fixes recurrentes (errores Laravel, configs)
- Listas de referencia horizontal (no narrativa)

**Frontmatter:**
```yaml
---
in:          # MOC al que pertenece (e.g., "[[Docker MOC]]")
created: YYYY-MM-DD
tags: [ref, cheatsheet]
---
```

### `+` (Inbox) — Zona de caos temporal

**Regla:** Nada permanece aquí más de 48 horas.

**Proceso obligatorio:**
1. Captura en `+/` con timestamp
2. En 48h: clasificar y mover a su ubicación definitiva
3. Si no se procesó en 48h → mover a `x/Inbox/` como desecho

**Subcarpetas:**
- `+/sparks/` — Chispas efímeras (captura rápida, procesar o tirar)
- `+/20260406-...` — Notas capturadas con fecha (ya con nombre, moverlas)

### `Calendar/` — Tiempo (no es cerebro)

Notas diarias, logs, reuniones.

**Frontmatter:**
```yaml
---
up: []
related: []
created: YYYY-MM-DD
tags: [daily]
---
```

### `Efforts/` — Acción/proyectos

**Frontmatter:**
```yaml
---
up:
  - "[[Logs]]"
related: []
created: YYYY-MM-DD
searchText:  # para Dataview
tags: [effort]
---
```

---

## Sistema de Tags

```
#type/atom      — Conocimiento vivo (Atlas/Dots)
#type/ref       — Referencia pura (Sources, Cheatsheets)
#type/effort    — Esfuerzo/proyecto
#type/daily     — Nota diaria
#type/moc       — Mapa de contenido
#type/contact   — Contacto
#type/meta      — Documentación del sistema

#status/raw     — Sin procesar (en inbox)
#status/refined — Clasificado y en su ubicación definitiva
#status/archived — Archivado (x/)
```

---

## Proceso de Atomización (Inbox → Cerebro)

```
+/nota-cruda.md
    │
    ├─► ¿Requiere reflexión, conexiones o evolución?
    │       NO → Sources/ o Utilities/Cheatsheets/
    │       SÍ → Atlas/Dots/Things/ o Sources/
    │
    └─► 1. Crear frontmatter completo
        2. Agregar a MOC relevante vía campo `in`
        3. Linkear desde MOC
        4. Borrar de +/
```

---

## Frontmatter Estándar por Tipo

### Átomo (Atlas/Dots/Things)
```yaml
---
up:
  - "[[Concepts]]"        # MOC principal
related:
  - "[[Antifragility]]"   # Notas relacionadas
created: 2026-04-12
in:
  - "[[Concepts]]"        # Colección
tags:
  - type/atom
---
```

### Referencia / Cheatsheet
```yaml
---
in:
  - "[[Docker MOC]]"
created: 2026-04-12
tags:
  - type/ref
  - ref/cheatsheet
---
```

### Nota diaria
```yaml
---
up: []
related: []
created: 2026-04-12
tags:
  - type/daily
---
```

### Esfuerzo
```yaml
---
up:
  - "[[Logs]]"
related: []
created: 2026-04-12
tags:
  - type/effort
status: active
---
```

---

## MOCs Obligatorios (mantener actualizados)

Cada MOC en `Atlas/Maps/` debe tener enlaces actualizados a sus átomos. Si un átomo vive en un MOC, debe estar linkeado desde ese MOC.

**MOCs principales:**
- `Concepts` — conceptos y ideas
- `Thinking Map` — reflexiones y marcos mentales
- `Life Map` — vida personal
- `Habits Map` — hábitos
- `Aurora MOC` — espiritual/bíblico
- MOCs adicionales según necesidad

---

## Reglas de Evolución

### Un átomo evoluciona cuando:
- Se conecta con nuevas notas (agregar a `related`)
- Se refina su definición
- Aparece una "colisión conceptual" con otra nota

### Una referencia NO evoluciona:
- Se consulta, se usa, se deja como está
- Si se vuelve demasiado compleja → considerar atomizarla

### Regla de oro:
> Si la nota te hace decir "esto se conecta con...", es un **átomo**.
> Si la nota te hace decir "esto lo voy a consultar...", es una **referencia**.

---

## Anti-patrones (qué NO hacer)

- [ ] Poner notas conceptuales en `+/` permanentemente
- [ ] Mezclar comandos técnicos con reflexiones en el mismo archivo
- [ ] Usar `related:` con enlaces vacíos `[[]]`
- [ ] Crear MOCs que solo linkean a sí mismos
- [ ] Dejar notas en `+/sparks/` sin procesarlas en 48h
- [ ] Usar `type/atom` en notas que son puramente referencia

---

## Metadata del documento

- **Creado:** 2026-04-12
- **Versión:** 1.0
- **Ubicación:** `x/Meta/Reglamento del Vault.md`
- **Revisar:** cuando el sistema de clasificación cambie
