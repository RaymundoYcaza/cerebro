---
up:
  - "[[Excel MOC]]"
related: 
created_at: 2025-04-20
---

En Excel, puedes contar cuántas veces aparece el punto (.) en una celda usando esta fórmula:

```
=LEN(A1)-LEN(SUSTITUIR(A1,".",""))
```

### ¿Cómo funciona?

- `LEN(A1)` cuenta todos los caracteres de la celda.
- `SUSTITUIR(A1,".","")` elimina todos los puntos.
- Al restar el largo de la cadena sin puntos al largo original, obtienes cuántos puntos había.
    

### Ejemplo:

Si en la celda `A1` tienes el valor `"1.01.01.01"`, esta fórmula te devolverá