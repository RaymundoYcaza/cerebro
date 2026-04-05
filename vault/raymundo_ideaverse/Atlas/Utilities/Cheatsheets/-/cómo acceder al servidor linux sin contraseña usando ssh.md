---
created: 2025-01-07
---

---

### Copiar manualmente la clave SSH al servidor desde PowerShell

1. Genera la clave SSH en tu laptop (si no lo has hecho aún):

```sh
ssh-keygen -t rsa -b 4096
```

- Esto generará dos archivos en `~/.ssh/`:
    
    - `id_rsa` (clave privada)
    - `id_rsa.pub` (clave pública).
- Abre el archivo `id_rsa.pub` con un editor (como Notepad o VS Code):

Linux
```sh
code ~/.ssh/id_rsa.pub
```

Windows 
```sh
code C:\Users\raymundo\.ssh\id_rsa.pub
```

- Copia el contenido del archivo.
    
- Conéctate al servidor usando tu contraseña:

```sh
ssh usuario@tu-servidor
```

En el servidor, crea la carpeta `~/.ssh/` (si no existe) y establece los permisos adecuados:

```sh
mkdir -p ~/.ssh
chmod 700 ~/.ssh

```

Abre o crea el archivo `authorized_keys`:

```sh
nano ~/.ssh/authorized_keys

```

- Pega el contenido de tu clave pública (`id_rsa.pub`) en este archivo y guarda los cambios.
    
- Establece los permisos correctos para el archivo:

```sh
chmod 600 ~/.ssh/authorized_keys

```

Prueba la conexión sin contraseña:

```sh
ssh usuario@tu-servidor
```

