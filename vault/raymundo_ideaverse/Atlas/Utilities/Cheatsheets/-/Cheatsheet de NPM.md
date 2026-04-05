---
in:
  - "[[NPM]]"
---



Instalar Angular CLI
```
npm install -g @angular/cli
```
Cómo averiguar la versión de un paquete instalado con npm
```bash
npm list
```
Luego de ejecutar el comando, buscar el paquete en cuestión y ver la versión.
Cómo hacer un upgrade o un downgrade a un paquete en npm
Ejecutar
```bash
npm install <package>@<version>
```
Esto removerá la versión actual y la reemplazará por la nueva
## Resolución de problemas
Al ejecutar `npm install` se genera un error relacionado con la red `npm ERR! code ETIMEDOUT`
```
npm config delete proxy
```
