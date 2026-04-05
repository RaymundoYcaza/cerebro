---
created: 2025-02-23
---

### Ejecución y compilación
Ejecutar en el navegador
```
ionic serve
```
Ejecutar la aplicación en el emulador o dispositivo con livereload
Si estás desarrollando directamente en tu computadora
```
ionic cap run android --external -livereload
```
Si estás usando un contenedor Docker, corriendo en WSL
Conectar el emulador (o el dispositivo físico)
En la máquina host (Windows):
Listar los dispositivos para ver la IP asignada
```bash
adb devices
```
Conectarse al dispositivo seleccionado (cambiar la IP por la correspondiente)
```bash
adb connect 192.168.56.101:5555
```
Verificar que sigue conectado el dispositivo
```bash
adb devices
```
En el WSL (Ubuntu)
Conectarse al equipo de manera similar al paso anterior (es necesario usar la extensión .exe)
```bash
adb.exe connect 192.168.56.101:5555
```
En el contenedor Docker que corre en el WSL (ionic-dev, por ejemplo)
Conectarse al equipo de manera similar a los pasos anteriores
```bash
adb connect 192.168.56.101:5555
```
Usar el comando para ejecutar la aplicación en dispositivo externo con livereload
```bash
ionic cap run android --external -livereload
```
