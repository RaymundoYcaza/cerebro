---
created: 2025-02-25 
---
Errores de dependencias a pesar de tenerlas instaladas *"Cannot find module '@angular/core' or its corresponding type declarations."*
En el archivo `tsconfig.json` cambiar el valor de "baseUrl"
```json
"baseUrl": "src",
```
Error *EACCESS* al instalar un módulo con NPM
El error es similar a este
npm ERR! code EACCES
npm ERR! syscall mkdir
npm ERR! path /home/vscode/.npm-global/lib/node_modules/npm-check-updates
npm ERR! errno -13
npm ERR!
npm ERR! Your cache folder contains root-owned files, due to a bug in
npm ERR! previous versions of npm which has since been addressed.
npm ERR!
npm ERR! To permanently fix this problem, please run:
npm ERR!   sudo chown -R 1001:1001 "/home/vscode/.npm"
npm ERR! A complete log of this run can be found in: /home/vscode/.npm/_logs/2024-04-13T04_51_20_588Z-debug-0.log
Una solución probada es ejecutar el comando sugerido, pero en lugar de hacerlo sobre .npm, hacerlo sobre *.npm-global*
```bash
sudo chown -R 1001:1001 "/home/vscode/.npm-global"
```
Error de timeout
Aumentar el tiempo de espera
```
npm config set fetch-retry-maxtimeout 1000000

```