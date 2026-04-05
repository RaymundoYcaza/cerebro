---
up:
  - "[[Raymundo Ycaza Morales]]"
in:
  - "[[Apuntes]]"
related:
  - "[[Terminal]]"
subtopic: 
tags:
  - "#tags"
  - "#tags
created: 2025-03-31
acr: true
---



## Ubuntu Linux
### Cómo descargar un archivo desde SSH

```bash
scp jabes@192.168.0.81:/mnt/blackpearl/containers_data/inorizonti_shared_files/archivo.ext .
```

  > [!info] El punto define que se descargará en la carpeta actual.
  
## Ver memoria RAM disponible

```shell
free
```

  
```shell 
 htop
```
> [!info] htop muestra una infertaz similar al administrador de tareas


## Ver consumo de disco

```shell
df -h
```


## Montar persistentemente un volumen

Verifica que /mnt/blackpearl esté montado persistentemente (en /etc/fstab)