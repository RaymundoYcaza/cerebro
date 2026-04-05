---
in:
  - "[[Expresiones Regulares]]"
---



Validar una dirección de email válida
`^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
Esta expresión regular verifica que la cadena de texto:
Comienza con una secuencia de uno o más caracteres alfanuméricos, puntos, porcentajes, signos más o guiones.
Seguido de un arroba (@).
Seguido de una secuencia de uno o más caracteres alfanuméricos, puntos o guiones.
Termina con un punto y una secuencia de dos o más caracteres alfabéticos.
Validar una dirección de email perteneciente a dominio1.com o dominio2.com
`^[a-zA-Z0-9._%+-]+@(dominio1\.com|dominio2\.com)$`
Esta expresión regular verifica que la cadena de texto:
Comienza con una secuencia de uno o más caracteres alfanuméricos, puntos, porcentajes, signos más o guiones.
Seguido de un arroba (@).
Termina con `dominio1.com` o `dominio2.com`.
Validar una dirección web
`^(http|https)://[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}(/[\w-]*)*/?$`
Esta expresión regular verifica que la cadena de texto:
Comienza con `http://` o `https://`.
Seguido de una secuencia de uno o más caracteres alfanuméricos, guiones o puntos.
Seguido de un punto y una secuencia de dos o más caracteres alfabéticos.
Seguido opcionalmente de una o más secuencias de caracteres alfanuméricos o guiones, cada uno precedido por una barra (/).
Termina opcionalmente con una barra (/).
Validar una dirección web en formato IP con puerto 8888
`^(http|https)://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:8888(/[\w-]*)*/?$`
Esta expresión regular verifica que la cadena de texto:
Comienza con `http://` o `https://`.
Seguido de una dirección IP (cuatro números entre 0 y 255 separados por puntos).
Seguido de `:8888` que representa el puerto.
Seguido opcionalmente de una o más secuencias de caracteres alfanuméricos o guiones, cada uno precedido por una barra (/).
Termina opcionalmente con una barra (/).
