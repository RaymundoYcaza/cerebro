---
created: 2025-03-16
in:
  - "[[Tecnología MOC]]"
---
### Error de permisos con la carpeta config
El problema está claramente relacionado con los permisos del volumen mapeado (`/mnt/blackpearl/containers_data/inorizonti_n8n/n8n_data`). Cuando ejecutas el contenedor sin volúmenes, funciona correctamente porque no hay restricciones de permisos. Sin embargo, al mapear el volumen, el contenedor no puede acceder o escribir en el archivo de configuración (`/home/node/.n8n/config`) debido a permisos insuficientes.

---

### Solución definitiva:

#### 1. **Asegúrate de que el directorio del volumen tenga los permisos correctos**

El contenedor `n8n` se ejecuta bajo el usuario `node` (UID 1000 y GID 1000). Para que el contenedor pueda acceder al volumen, el directorio en el host debe ser propiedad de este usuario.

Ejecuta los siguientes comandos en tu host:

```bash
sudo chown -R 1000:1000 /mnt/blackpearl/containers_data/inorizonti_n8n/n8n_data
sudo chmod -R 755 /mnt/blackpearl/containers_data/inorizonti_n8n/n8n_data
```

Esto asegura que el usuario `node` tenga permisos de lectura y escritura en el directorio.

---

#### 2. **Verifica el archivo de configuración**

Si el archivo `/home/node/.n8n/config` ya existe en el volumen, asegúrate de que tenga los permisos correctos:

```bash
sudo chown 1000:1000 /mnt/blackpearl/containers_data/inorizonti_n8n/n8n_data/config
sudo chmod 644 /mnt/blackpearl/containers_data/inorizonti_n8n/n8n_data/config
```

#### 3. **Ejecuta el contenedor con el volumen corregido**

Una vez que los permisos estén configurados correctamente, vuelve a ejecutar el contenedor con el volumen mapeado:

```bash
docker run -it -d --rm --name n8n \
  -p 5678:5678 \
  -v /mnt/blackpearl/containers_data/inorizonti_n8n/n8n_data:/home/node/.n8n \
  -v /mnt/blackpearl/inorizonti_shared_files:/data/shared_files \
  docker.n8n.io/n8nio/n8n
```

#### 4. **Configura la variable de entorno para permisos de archivo**

El mensaje de advertencia que ves (`Permissions 0644 for n8n settings file /home/node/.n8n/config are too wide`) indica que los permisos del archivo de configuración son demasiado permisivos. Para evitar esta advertencia, puedes configurar la variable de entorno `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS`:

```bash
docker run -it -d --rm --name n8n \
  -p 5678:5678 \
  -v /mnt/blackpearl/containers_data/inorizonti_n8n/n8n_data:/home/node/.n8n \
  -v /mnt/blackpearl/inorizonti_shared_files:/data/shared_files \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  docker.n8n.io/n8nio/n8n
```

Esto asegura que `n8n` ajuste automáticamente los permisos del archivo de configuración.

---

#### 5. **Verifica que el contenedor se esté ejecutando**

Después de ejecutar el contenedor, verifica que esté en funcionamiento:

```bash
docker ps
```

Revisa los logs para asegurarte de que no haya errores:

```bash
docker logs n8n
```
