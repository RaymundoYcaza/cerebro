---
in:
  - "[[Git]]"
---



# Error al realizar push: se desconecta el servidor
Al realizar push muestra un error indicando que el servidor se ha desconectado repentinamente
`The remote end hung up unexpectedly`
Probablemente guarde relación con el tamaño del buffer. Una posible solución sería el aumentar el tamaño de buffer sobre http
`git config http.postBuffer 524288000`
