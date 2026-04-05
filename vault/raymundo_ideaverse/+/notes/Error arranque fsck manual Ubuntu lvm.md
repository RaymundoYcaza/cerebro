---
up:
  - "[[Ubuntu problemas de arranque]]"
related: 
created: 2025-05-19
---

> 🔧 Error de arranque por sistema de archivos inconsistente en `/dev/mapper/ubuntu--vg-root`, solucionado ejecutando manualmente `fsck`.

Ejecutar el comando `fsck` con el argumento `-y`:

```shell
fsck -y /dev/mapper/ubuntu--vg-ubuntu--lv
```

