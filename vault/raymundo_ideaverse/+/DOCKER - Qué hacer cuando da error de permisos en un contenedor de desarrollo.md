---
up:
  - "[[Docker MOC]]"
related: []
created: 2025-05-08
---


Conectarse al servidor por SSH o abrir una terminal desde VS Code y ejecutar:

```bash
sudo chmod -R u+rwX /mnt/blackpearl/containers_dev/ci3_container/ci/bisstox-agricontrol/
```

Asegurarse de que el usuario es dueño del directorio:

```bash
sudo chown -R $USER:$USER /mnt/blackpearl/containers_dev/ci3_container/ci/bisstox-agricontrol/
```