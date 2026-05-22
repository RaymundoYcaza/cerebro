---
up:
  - "[[Comandos Consola Ubuntu Linux]]"
related: 
created: 2025-05-19
---

✅ 1. Usar `less` para paginar la salida:

```shell
ip link | less 
```

Esto te permitirá:

- Navegar con las flechas arriba/abajo.
- Subir con `k`, bajar con `j`
- Avanzar página con `Espacio`.
- Retroceder página con `b`.
- Salir con `q`.

✅ 2. Alternativa con `more` (más simple que `less`):

```shell
ip link | more
```

Esto muestra una pantalla a la vez. Presiona `Espacio` para avanzar.