---
up:
  - "[[Snippets]]"
  - "[[Obsidian MOC]]"
related: 
created: 2025-06-01
---


A continuación tienes dos versiones de la consulta usando solo `filename = Inorizonti - P1 - Hacer.md`. Una versión filtra las tareas **recurrentes** y la otra filtra las tareas **no recurrentes**.

**1. Solo tareas recurrentes en “Inorizonti - P1 - Hacer.md”**

```js
not done
due before tomorrow
filename = Inorizonti - P1 - Hacer.md
is recurring
group by filename
group by heading
```

- `filename = Inorizonti - P1 - Hacer.md` limita las tareas únicamente a ese archivo (incluye la extensión `.md`). [Obsidian](https://publish.obsidian.md/tasks/Queries/Filters?utm_source=chatgpt.com)
- `is recurring` selecciona exclusivamente las tareas que tienen una regla de recurrencia válida. [Obsidian](https://publish.obsidian.md/tasks/Queries/Filters?utm_source=chatgpt.com)
- `group by filename` crea el primer nivel de agrupación usando el nombre del archivo (sin la extensión) como encabezado. [Obsidian](https://publish.obsidian.md/tasks/Queries/Grouping?utm_source=chatgpt.com)
- `group by heading` anida cada tarea bajo el encabezado correspondiente dentro de la nota (o `(No heading)` si no hay encabezado). [Obsidian](https://publish.obsidian.md/tasks/Queries/Grouping?utm_source=chatgpt.com)

**2. Solo tareas no recurrentes en “Inorizonti - P1 - Hacer.md”**

```js
not done
due before tomorrow
filename = Inorizonti - P1 - Hacer.md
is not recurring
group by filename
group by heading
```

- `filename = Inorizonti - P1 - Hacer.md` asegura que solo se incluyan las tareas de ese archivo. [Obsidian](https://publish.obsidian.md/tasks/Queries/Filters?utm_source=chatgpt.com)
- `is not recurring` filtra las tareas que **no** tienen regla de recurrencia. [Obsidian](https://publish.obsidian.md/tasks/Queries/Filters?utm_source=chatgpt.com)
- El anidado `group by filename` y `group by heading` funciona igual que en la versión anterior, organizando primero por nombre de nota y luego por encabezado. [Obsidian](https://publish.obsidian.md/tasks/Queries/Grouping?utm_source=chatgpt.com)
