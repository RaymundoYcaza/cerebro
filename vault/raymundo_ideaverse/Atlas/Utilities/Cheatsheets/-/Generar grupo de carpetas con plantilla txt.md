---
created: 2024-05-26
in:
  - "[[Batch]]"
tags: []
---
Este código genera directorios y subdirectorios en la misma ruta, tomando como referencia la estructura definida en el archivo de texto.

Código del archivo .bat

```vb
@echo off

set /P id="Trabajo: "

for /f %%I in ('wmic os get localdatetime ^|find "20"') do set dt=%%I
echo %dt%

set fullpath="%dt%%id%"

mkdir "%fullpath%"

for /f "tokens=*" %%a in (plantilla.txt) do (

mkdir "%fullpath%\%%a"

)
```


Plantilla en archivo txt

```
00-Presupuesto
01-Recibido
02-Desarrollo
03-Entregable
04-Revisiones
```
