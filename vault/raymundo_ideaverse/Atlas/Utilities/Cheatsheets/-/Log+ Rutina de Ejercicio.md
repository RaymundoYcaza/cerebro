---
created: 2024-06-01
in:
  - "[[Calendar/Logs/Logs]]"
---
Rutina principal: Lunes, míercoles y viernes
Rutina secundaria: Martes, jueves y sábado

```dataview
TABLE hours, intensity
WHERE contains(in, this.file.link) and
!contains(file.name, "Template")
SORT file.name DESC
```

