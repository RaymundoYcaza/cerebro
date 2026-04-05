

## Método universal (si conoces el puerto)

Linux/macOS:

lsof -ti:4321 | xargs kill -9

Windows (PowerShell):
Get-NetTCPConnection -LocalPort 4321 | Select-Object -ExpandProperty OwningProcess | ForEach-Object { Stop-Process -Id $_ -Force }

Windows (CMD más simple):
netstat -ano | findstr :4321
taskkill /PID <PID> /F


-----------------------------

Linux/macOS
# Buscar el proceso de Astro
ps aux | grep astro

# O más específico para node
ps aux | grep node

# Matar por PID (reemplaza <PID> con el número que veas)
kill <PID>

# Si no responde, forzar
kill -9 <PID>



Método más rápido - matar todos los procesos de node:


pkill -f astro
# o
pkill node



Windows (PowerShell/CMD)

# Ver procesos de node
tasklist | findstr node

# Matar por PID
taskkill /PID <PID> /F

# Matar todos los node.exe
taskkill /IM node.exe /F



-------------------------------------------


## Limpiar el caché de Astro

rm -rf .astro node_modules/.astro


