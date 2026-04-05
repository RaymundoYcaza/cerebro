---
up:
  - "[[Maximax Server Logs]]"
related: 
created: 2025-05-19
---
 Aparentemente el servidor tuvo un problema debido a una **desconexión abrupta** que sucedió al mover el mueble del servidor durante [[2025-05-18 Instalación de Fibra Óptica Claro - Cambio de modem viejo|la instalación de la conexión de fibra óptica]]
 
El mensaje en consola era
```shell
/dev/mapper/ubuntu-vg-root: UNEXPECTED INCONSISTENCY; Run fsck MANUALLY.
```

Donde `ubuntu-vg-root` es referencial, ya que el verdadero valor no se registró.

Se aplicó una solución [[Error arranque fsck manual Ubuntu lvm]]

El servidor quedó funcionando correctamente.