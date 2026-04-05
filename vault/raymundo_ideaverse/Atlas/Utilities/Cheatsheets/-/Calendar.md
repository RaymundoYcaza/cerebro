---
up:
  - "[[Home]]"
down:
  - "[[Calendar/Logs/Logs]]"
---

[[Revisiones Mensuales]]

📅 [[Calendarios imprimibles]]

Esta es la vista que muestra todos los journal creados (aquellos archivos que tienen la fecha como parte de su nombre).
## 2025
```dataview
list from ""
WHERE startswith(file.name, "2025-")
SORT file.name DESC
```
## 2024
```dataview
list from "Calendar/Notes"
WHERE startswith(file.name, "2024-")
SORT file.name DESC
```
## 2023
```dataview
list from "Calendar/Notes"
WHERE startswith(file.name, "2023-")
SORT c.day ASC
```

## Otros
```dataview
list from "Calendar/Notes"
WHERE !startswith(file.name, "202")
SORT c.day ASC
```
