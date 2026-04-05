---
up: []
related: []
created: 2025-05-29
---


¿Es factible tener un gran entorno virtual con todas las librerias Python?

## 1. Ventajas y desventajas de un único “mega-entorno”

| Ventajas                                                   | Desventajas                                                                                   |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| - Ahorro de espacio al no duplicar paquetes comunes.       | - **Conflictos de versiones:** A+B exigen v1.x mientras C+D exigen v2.x de la misma librería. |
| - Sólo un único directorio que respaldar o copiar offline. | - Entorno m uy “pesado”: cuesta más tiempo crear, copiar o mover.                             |
| - Sencillo de usar: siempre activas el mismo `venv`.       | - Menos aislamiento: no hay garantías de reproducibilidad limpia por proyecto.                |

> **Conclusión:** Viable si controlas bien las versiones y tu conjunto de proyectos es relativamente estable.  

---

## 2. Alternativas más robustas para entornos offline

### a) Crear un “Wheelhouse” local
1. En tu máquina con Internet, ejecuta:
   ```bash
   mkdir wheelhouse
   pip download -d wheelhouse -r requirements.txt
   ```
2. Copia la carpeta `wheelhouse/` al entorno sin Internet.
3. Instala desde ahí:
   ```bash
   pip install --no-index --find-links=wheelhouse -r requirements.txt
   ```
- **Pro:** Puedes mantener múltiples `requirements.txt` para cada proyecto.  
- **Contra:** Necesitas regenerar el wheelhouse cuando cambian dependencias.  

### b) Mirror o proxy PyPI local
- **Herramientas:** [devpi](https://devpi.net/), [Artifactory OSS], [bandersnatch].  
- Montas un mini-servidor PyPI en tu red local o disco, que “cachea” cualquier paquete que instales.  
- **Pro:** Automático: la primera vez que pides un paquete lo baja y luego queda disponible offline.  
- **Contra:** Requiere algo de configuración inicial y espacio (equivalente a lo que cachees).

### c) Gestores de entornos más avanzados
- **Conda / Mamba:** manejan librerías Python y no-Python, con buenos mecanismos de cache y canales offline.  
- Puedes exportar un `.tar.bz2` de un ambiente completo y luego importarlo en una máquina sin red.

### d) Pipenv / Poetry
- Construyen un cache local de ruedas (`~/.cache/pip` o similar).  
- Usando `poetry config cache-dir` y luego `poetry lock && poetry export`, permites instalaciones offline a partir del lockfile.

---

## 3. Recomendación general

1. **Para proyectos múltiples**  
   - Mantén carpetas de wheelhouse separadas por gran bloque funcional (e.g., ML, web, data), o bien un único wheelhouse pero bien versionado.  
2. **Para un “espejo” local**  
   - Instala `devpi` en un servidor (aunque sea una VM o un NAS), y apúntalo desde tus clientes:
     ```bash
     pip install devpi-client
     devpi use http://mi-nas.local:3141/root/pypi/
     ```
3. **Respaldos rutinarios**  
   - Haz snapshots (o copias rsync) de tu wheelhouse o caché de PyPI tras cada actualización significativa.  

De este modo te aseguras de tener **todos** los paquetes que necesites, sin depender de Internet, con un consumo de espacio controlado y evitando conflictos de versiones irreconciliables.

## 🐧 Instructivo detallado (Linux/macOS) - Wheelhouse Offline

### 📁 Estructura general

```bash
offline-cache/
├── wheelhouse/                # Aquí vivirán todos los paquetes descargados
├── projects/
│   ├── excel-automation/
│   │   ├── requirements.txt
│   │   └── src/
│   ├── data-analysis/
│   │   ├── requirements.txt
│   │   └── src/
│   ├── text-processing/
│   │   ├── requirements.txt
│   │   └── src/
│   └── web-scraper/           # proyecto inventado
│       ├── requirements.txt
│       └── src/
└── sync-wheelhouse.sh         # script para regenerar wheelhouse
```

---

### 1. Preparar tu máquina online

```bash
mkdir -p offline-cache/{wheelhouse,projects}
cd offline-cache
```

#### Agrega tus archivos `requirements.txt`

- `excel-automation/requirements.txt`  
  ```
  openpyxl>=3.0
  pandas>=1.5
  xlwings>=0.28
  ```

- `data-analysis/requirements.txt`  
  ```
  numpy>=1.24
  pandas>=1.5
  matplotlib>=3.7
  seaborn>=0.12
  scipy>=1.10
  ```

- `text-processing/requirements.txt`  
  ```
  nltk>=3.8
  regex>=2023.6
  chardet>=5.1
  ```

- `web-scraper/requirements.txt`  
  ```
  requests>=2.31
  beautifulsoup4>=4.12
  lxml>=4.9
  ```

---

### 2. Script `sync-wheelhouse.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail
WHEELHOUSE="$(pwd)/wheelhouse"
rm -rf "$WHEELHOUSE" && mkdir -p "$WHEELHOUSE"

for req in projects/*/requirements.txt; do
  echo "Descargando paquetes de $req..."
  pip download --dest "$WHEELHOUSE" -r "$req"
done

echo "✅ Wheelhouse actualizado con todas las dependencias."
```

```bash
chmod +x sync-wheelhouse.sh
./sync-wheelhouse.sh
```

---

### 3. Uso en máquina offline

```bash
cd offline-cache/projects/excel-automation
python3 -m venv .venv
source .venv/bin/activate

pip install --no-index \
  --find-links ../../wheelhouse \
  -r requirements.txt
```

Repite para cada proyecto.

---

### 4. Buenas prácticas

```bash
cp -r wheelhouse wheelhouse-$(date +%Y%m%d)
ls wheelhouse | sort | uniq -c
```

```bash
# Verifica contenido
ls wheelhouse/
```

```bash
# Limpieza manual de versiones viejas si es necesario
```


## Instructivo detallado (Windows CMD / PowerShell) - Wheelhouse Offline

### 📁 Estructura general

```
offline-cache\
├── wheelhouse\               # Aquí vivirán todos los paquetes descargados
├── projects\
│   ├── excel-automation\
│   │   ├── requirements.txt
│   │   └── src\
│   ├── data-analysis\
│   │   ├── requirements.txt
│   │   └── src\
│   ├── text-processing\
│   │   ├── requirements.txt
│   │   └── src\
│   └── web-scraper\          # proyecto inventado
│       ├── requirements.txt
│       └── src\
└── sync-wheelhouse.ps1       # script para regenerar wheelhouse
```

---

### 1. Preparar tu máquina online

Abre PowerShell:

```powershell
New-Item -ItemType Directory -Path .\offline-cache\wheelhouse
New-Item -ItemType Directory -Path .\offline-cache\projects
```

Crea los archivos `requirements.txt` en cada subcarpeta de proyecto como se describe en la versión Linux.

---

### 2. Script PowerShell `sync-wheelhouse.ps1`

```powershell
$wheelhouse = "$PSScriptRoot\wheelhouse"
Remove-Item -Recurse -Force $wheelhouse
New-Item -ItemType Directory -Path $wheelhouse

$projectPaths = Get-ChildItem -Path "$PSScriptRoot\projects" -Directory

foreach ($proj in $projectPaths) {
    $reqFile = Join-Path $proj.FullName "requirements.txt"
    if (Test-Path $reqFile) {
        Write-Host "Descargando paquetes desde $reqFile"
        pip download --dest $wheelhouse -r $reqFile
    }
}

Write-Host "✅ Wheelhouse actualizado con todas las dependencias."
```

Ejecútalo desde PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\sync-wheelhouse.ps1
```

---

### 3. Uso en máquina offline

En CMD o PowerShell:

```powershell
cd offline-cache\projects\excel-automation
python -m venv .venv
.\.venv\Scripts\activate

pip install --no-index `
  --find-links ..\..\wheelhouse `
  -r requirements.txt
```

Repite el mismo proceso para los demás proyectos.

---

### 4. Buenas prácticas

- Hacer copias de seguridad de la carpeta `wheelhouse\` regularmente.
- Comprimirla si deseas transportarla por USB.
- Para verificar el contenido:
  ```powershell
  Get-ChildItem ..\..\wheelhouse
  ```
