---
up:
  - "[[Maximax Server Logs]]"
related: []
created: 2025-05-19
---

 Al realizar la conexión `SSH` la consola indica que el servidor no puede ser encontrado. Luego de varias pruebas [[Script Python para descubrir IPs en uso dentro de la red local]] se determinó que el servidor no estaba recibiendo la IP esperada `192.168.0.81`. Esto se debe al evento [[2025-05-18 Instalación de Fibra Óptica Claro - Cambio de modem viejo]]

Con el cambio de modem, ya no es posible entrar a la configuración y asignar una IP fija como estaba antes, por lo que se tiene que adoptar un enfoque diferente.

Se solucionó el problema, asignando una IP fija con **Netplan** [[Asignar IP fija en Ubuntu Linux con Netplan]]
