---
up:
  - "[[Obsidian Resolución de Problemas MOC]]"
related: []
subtopic: 
created: 2025-05-11
---

Muchas veces he tenido problemas con la fecha en las plantillas a la hora de aplicarla. Lo he resuelto dándole formato así: 

```
{{date:YYYY-MM-DD}}
```

Generalmente, el error se debe a que se agregan, sin razón aparente, dos puntos al final:

```
{{date:YYYY-MM-DD}}:
```

Esto genera un error al momento de renderizar la plantilla. Solo hay que quitarle esos dos puntos. Se suele generar el problema cuando se agrega una propiedad a continuación de la fecha.
