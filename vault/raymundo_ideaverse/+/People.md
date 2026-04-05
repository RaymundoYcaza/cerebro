---
up: []
related: []
created: 2026-03-12
---
Perfecto. Para trackear interacciones y follow-ups en Obsidian con un subconjunto de contactos, la mejor aproximación es un mini-**PRM (Personal Relationship Management)** dentro de tu vault. Aquí el diseño:

## Estructura de la nota de persona

```markdown
---
name: "Juan Pérez"
connection: 1
tags:
  - contact
  - contact/1st
track: true          # solo en contactos que quieres seguir
next_followup: 2026-03-20
last_contact: 2026-03-12
channel: "LinkedIn"  # email, WhatsApp, reunión, etc.
---

```

La propiedad `track: true` es la clave — te permite filtrar solo los contactos que te importan seguir, sin tocar los demás.

## Sección de interacciones en la nota

Dentro del cuerpo de la nota, mantén un log cronológico simple:

```markdown
## Interacciones

- **2026-03-12** — Reunión por Zoom. Habló de proyecto X. Interesado en colaborar.
- **2026-02-28** — Mensaje en LinkedIn. Respondió rápido.

## Follow-up pendiente

- [ ] Enviarle propuesta antes del 2026-03-20
- [ ] Preguntar sobre contacto con empresa Y

```

## Queries Dataview útiles

**Contactos con follow-up próximo:**

```
TABLE name, next_followup, channel
FROM #contact
WHERE track = true
SORT next_followup ASC
```

**Contactos sin contacto reciente (más de 30 días):**

```
TABLE name, last_contact
FROM #contact
WHERE track = true AND date(last_contact) < date(today) - dur(30 days)
SORT last_contact ASC

```

