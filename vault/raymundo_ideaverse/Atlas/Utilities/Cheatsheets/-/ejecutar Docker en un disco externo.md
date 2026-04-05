---
created: 2025-01-07
---

Descargar los binarios en una ruta del disco externo
Crear un script sh para cambiar la variable path

```sh
#/bin/bash
PATH=$PATH:$(pwd)/docker;
$(pwd)/docker/dockerd --data-root $(pwd)/dataroot --storage-driver aufs &
```

Ejecutar el script con sudo y Docker se ejecutará. Se agregó el parámetro --storage-driver para que se guarden las imagenes en el disco externo.

Referencia: https://www.youtube.com/watch?v=-d8YsQjRdjY

