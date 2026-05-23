---
up: []
related: []
created: '2026-05-22'
sourceType: null
tags:
- note/extract
- source/clips
---

El límite de RAM de WSL2 se configura normalmente en el archivo:

```txt
C:\Users\TU_USUARIO\.wslconfig
```

Por ejemplo:

```txt
C:\Users\Raymundo\.wslconfig
```

El contenido suele verse así:

```ini
[wsl2]
memory=4GB
processors=4
swap=2GB
localhostForwarding=true
```

Después de modificarlo debes reiniciar WSL con:

```bash
wsl --shutdown
```

y luego volver a abrir tu distro.

Si quieres verificar el archivo rápidamente desde PowerShell:

```powershell
notepad $env:USERPROFILE\.wslconfig
```

o:

```powershell
cat $env:USERPROFILE\.wslconfig
```