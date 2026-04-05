---
in:
  - "[[Docker MOC]]"
---



Repositorio Origen
https://github.com/robingenz/docker-ionic-capacitor-dev
Compilar
```bash
docker build --platform linux/amd64 -t bisstox/ionic-capacitor-dev .
```
Ejecutar imagen
```
docker run -it -v $(pwd):/home/vscode/put_apk --name bisstox_mobile-env bisstox/ionic-capacitor-dev bash
```
Instalar dependencias
```
npm install
```
Instalar angular/cli
```
npm install -g @angular/cli
```
Instalar angular/devkit-core
`npm i @angular-devkit/core`
