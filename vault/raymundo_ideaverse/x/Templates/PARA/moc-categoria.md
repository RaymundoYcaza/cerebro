---
type: moc
title: "{{title}}"
category: "{{category}}"
tags:
  - z/moc
  - z/recurso
---

# {{title}}

## Descripcion

Mapa de contenido para la categoria {{category}}.

## Carpetas fisicas relacionadas

- 

## Recursos relacionados

```dataview
TABLE resource_type, status, archived, updated
FROM "zResources"
WHERE category = "{{category}}"
SORT updated DESC
```
