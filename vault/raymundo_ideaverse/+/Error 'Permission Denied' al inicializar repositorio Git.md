---
up:
  - "[[Tecnología MOC]]"
related: 
created: 2025-05-21
---
 
El error **"Permission denied"** al intentar inicializar un repositorio Git en VS Code generalmente ocurre porque el usuario actual no tiene permisos suficientes para crear o escribir en el directorio **`.git`** dentro de tu proyecto.

### Posibles causas y soluciones:

#### 1. **Permisos incorrectos en la carpeta del proyecto**

- Si estás trabajando en un entorno Linux/WSL o Docker, es posible que la carpeta tenga permisos restringidos para tu usuario actual.
    
- **Solución:**  
    Ejecuta en la terminal (dentro de la carpeta del proyecto):

```shell
sudo chown -R $USER:$USER .
sudo chmod -R 755 .
```

Esto cambiará el propietario de los archivos a tu usuario y dará permisos de lectura/escritura.

#### 2. **VS Code no tiene permisos suficientes**

- Si estás usando VS Code en un entorno remoto (WSL, Docker, SSH), puede que no tenga acceso a los archivos locales.
    
- **Solución:**
    
    - Asegúrate de que VS Code tenga permisos en el sistema de archivos.
    - Si usas WSL, abre VS Code desde la terminal de WSL con:

