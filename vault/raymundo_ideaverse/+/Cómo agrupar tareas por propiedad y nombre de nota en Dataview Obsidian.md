---
up:
  - "[[Obsidian Dataview MOC]]"
related: 
created: 2025-05-22
---

 Sí, es posible agrupar primero por los enlaces en la propiedad `up` y luego por el nombre del archivo en tu consulta de Dataview. Puedes hacerlo usando una expresión de agrupación anidada. Aquí te muestro cómo modificarla:

```clojure
TASK
FROM "Efforts/On"
WHERE !completed
GROUP BY up + " > " + file.name
```

O si prefieres una agrupación más jerárquica/clara:

```clojure
TASK
FROM "Efforts/On"
WHERE !completed
GROUP BY up
GROUP BY file.name
```

Si la propiedad `up` contiene enlaces (como `[[Enlace]]`), Dataview los tratará como valores para agrupar. La primera versión concatenará ambos valores, mientras que la segunda creará grupos anidados (primero por `up`, luego por `file.name` dentro de cada grupo `up`).

Si necesitas un formato más específico, podrías usar:

```clojure
TASK
FROM "Efforts/On"
WHERE !completed
GROUP BY choice(up, up + " > " + file.name, "Sin up > " + file.name)
```

Esto último manejaría el caso donde algunos archivos no tienen propiedad `up`.

