---
in:
  - "[[Redes Informáticas]]"
---



Qué significa la nomenclatura 192.168.0.0/24
En realidad, `192.168.0.0/24` no se refiere a un rango de números del 0 al 24, sino que es una notación para representar una subred en la red.
La notación `192.168.0.0/24` se llama notación CIDR (Classless Inter-Domain Routing). Aquí, `192.168.0.0` es la dirección de red y `24` es la longitud del prefijo de red. La longitud del prefijo de red indica la cantidad de bits en la dirección IP que se utilizan para la red. En este caso, `24` significa que los primeros 24 bits de la dirección IP se utilizan para la red, dejando los últimos 8 bits para los hosts (dispositivos) en la red.
Por lo tanto, `192.168.0.0/24` representa todas las direcciones IP desde `192.168.0.0` hasta `192.168.0.255`. Entonces, la dirección IP `192.168.0.92` está incluida en la subred `192.168.0.0/24`.
