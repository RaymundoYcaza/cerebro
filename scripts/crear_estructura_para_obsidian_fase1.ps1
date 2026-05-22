# ============================================
# Crear estructura PARA + Obsidian + Scripts
# FASE 1
# ============================================

$VaultPath = "C:\cerebro\vault\raymundo_ideaverse"
$ScriptsPath = "C:\cerebro\scripts\para"
$ParaRoot = "P:\PARA"

# ----------------------------
# Carpetas en Obsidian
# ----------------------------

$ObsidianFolders = @(
    "$VaultPath\x\Templates\PARA",

    "$VaultPath\x\Images\Covers\_generic",
    "$VaultPath\x\Images\Covers\ebooks",
    "$VaultPath\x\Images\Covers\videos",
    "$VaultPath\x\Images\Covers\imagenes",
    "$VaultPath\x\Images\Covers\audio",
    "$VaultPath\x\Images\Covers\software",
    "$VaultPath\x\Images\Covers\documentos",
    "$VaultPath\x\Images\Covers\carpetas",

    "$VaultPath\zResources\Biblioteca",
    "$VaultPath\zResources\Aprendizaje",
    "$VaultPath\zResources\Software",
    "$VaultPath\zResources\Multimedia",
    "$VaultPath\zResources\Legal",
    "$VaultPath\zResources\Finanzas",
    "$VaultPath\zResources\Contactos",
    "$VaultPath\zResources\PKM",
    "$VaultPath\zResources\Plantillas",
    "$VaultPath\zResources\Imagenes",
    "$VaultPath\zResources\Audio",
    "$VaultPath\zResources\Documentos",
    "$VaultPath\zResources\Revisar",
    "$VaultPath\zResources\_logs"
)

foreach ($Folder in $ObsidianFolders) {
    New-Item -ItemType Directory -Force -Path $Folder | Out-Null
}

# ----------------------------
# Carpetas PARA en disco externo
# Solo si la unidad existe
# ----------------------------

if (Test-Path $ParaRoot) {
    $ParaFolders = @(
        "$ParaRoot\00-INBOX",
        "$ParaRoot\01-PROYECTOS",
        "$ParaRoot\02-AREAS",
        "$ParaRoot\03-RECURSOS\Biblioteca",
        "$ParaRoot\03-RECURSOS\Aprendizaje",
        "$ParaRoot\03-RECURSOS\Creatividad-y-Diseno",
        "$ParaRoot\03-RECURSOS\Software-y-Herramientas",
        "$ParaRoot\03-RECURSOS\Multimedia-Referencia",
        "$ParaRoot\03-RECURSOS\PKM-y-Obsidian",
        "$ParaRoot\04-ARCHIVO\Proyectos-Cerrados",
        "$ParaRoot\04-ARCHIVO\Descargas-Antiguas",
        "$ParaRoot\04-ARCHIVO\Duplicados-Pendientes-Revisar",
        "$ParaRoot\04-ARCHIVO\Material-Historico"
    )

    foreach ($Folder in $ParaFolders) {
        New-Item -ItemType Directory -Force -Path $Folder | Out-Null
    }
}
else {
    Write-Host "ADVERTENCIA: No se encontro $ParaRoot. Se omite creacion de carpetas en disco externo." -ForegroundColor Yellow
}

# ----------------------------
# Carpeta de scripts
# ----------------------------

New-Item -ItemType Directory -Force -Path $ScriptsPath | Out-Null

# ----------------------------
# Crear archivos de log
# ----------------------------

$CsvLog = "$VaultPath\zResources\_logs\movimientos-para.csv"
$MdLog = "$VaultPath\zResources\_logs\movimientos-para.md"
$LastMovement = "$VaultPath\zResources\_logs\ultimo-movimiento.json"

if (!(Test-Path $CsvLog)) {
    "fecha,accion,archivo_origen,archivo_destino,nota_obsidian,tipo,categoria,subcategory,status,archived" | Out-File -Encoding UTF8 $CsvLog
}

if (!(Test-Path $MdLog)) {
    "# Log de movimientos PARA`n" | Out-File -Encoding UTF8 $MdLog
}

if (!(Test-Path $LastMovement)) {
    "{}" | Out-File -Encoding UTF8 $LastMovement
}

# ----------------------------
# Crear marcadores de portadas genericas
# ----------------------------

$GenericCoverMarkers = @(
    "ebook",
    "video",
    "imagen",
    "audio",
    "software",
    "documento",
    "carpeta"
)

foreach ($Name in $GenericCoverMarkers) {
    $Path = "$VaultPath\x\Images\Covers\_generic\$Name.md"
    if (!(Test-Path $Path)) {
        "# Portada generica: $Name`n" | Out-File -Encoding UTF8 $Path
    }
}

# ----------------------------
# Crear config.yaml
# ----------------------------

$ConfigPath = "$ScriptsPath\config.yaml"

if (!(Test-Path $ConfigPath)) {
@'
vault_path: "C:/cerebro/vault/raymundo_ideaverse"

default_para_root: "P:/PARA"
default_inbox_path: "P:/PARA/00-INBOX"

obsidian_resources_path: "zResources"
obsidian_templates_path: "x/Templates/PARA"
obsidian_covers_path: "x/Images/Covers"

logs_path: "zResources/_logs"
movement_csv: "movimientos-para.csv"
movement_md: "movimientos-para.md"
last_movement_json: "ultimo-movimiento.json"

use_slug_names: true
create_note_for_archived: true
generic_cover_fallback: true
confirm_before_move: true
process_first_level_only: true

tags_root: "z"

allowed_tags:
  - z/recurso
  - z/proyecto
  - z/area
  - z/archivo
  - z/biblioteca
  - z/ebook
  - z/video
  - z/audio
  - z/imagen
  - z/software
  - z/documento
  - z/legal
  - z/finanzas
  - z/contacto
  - z/pkm
  - z/plantilla
  - z/curso
  - z/tutorial
  - z/revisar
  - z/duplicado
  - z/descarga
  - z/multimedia

status_values:
  ebook:
    - pendiente
    - leyendo
    - leido
    - referencia
    - descartado
  video:
    - pendiente
    - viendo
    - visto
    - referencia
    - descartado
  software:
    - pendiente
    - instalado
    - probado
    - en_uso
    - descartado
  documento:
    - pendiente
    - revisar
    - vigente
    - cerrado
    - historico
  general:
    - pendiente
    - en_uso
    - consultado
    - terminado
    - referencia
    - descartado
'@ | Out-File -Encoding UTF8 $ConfigPath
}

# ----------------------------
# Crear requirements.txt
# ----------------------------

$RequirementsPath = "$ScriptsPath\requirements.txt"

if (!(Test-Path $RequirementsPath)) {
@'
pyyaml
rapidfuzz
python-slugify
rich
'@ | Out-File -Encoding UTF8 $RequirementsPath
}

# ----------------------------
# Crear README.md
# ----------------------------

$ReadmePath = "$ScriptsPath\README.md"

if (!(Test-Path $ReadmePath)) {
@'
# Clasificador PARA + Obsidian

Este script clasifica archivos desde `P:\PARA\00-INBOX`, los mueve a la estructura PARA correspondiente y crea una nota de metadatos en Obsidian dentro de `zResources`.

## Rutas principales

- Vault: `C:\cerebro\vault\raymundo_ideaverse`
- Scripts: `C:\cerebro\scripts\para`
- INBOX: `P:\PARA\00-INBOX`
- Notas de recursos: `zResources`
- Plantillas: `x\Templates\PARA`
- Portadas: `x\Images\Covers`
- Logs: `zResources\_logs`

## Reglas

- El script procesa solo archivos/carpetas del primer nivel de `00-INBOX`.
- Siempre debe pedir confirmacion antes de mover.
- Si el disco P no existe, debe permitir seleccionar otra ruta.
- Siempre crea nota si el recurso tiene valor de registro, incluso si va a archivo.
- El ultimo movimiento debe poder deshacerse.
'@ | Out-File -Encoding UTF8 $ReadmePath
}

# ----------------------------
# Crear esqueleto clasificador_para.py
# ----------------------------

$PythonScriptPath = "$ScriptsPath\clasificador_para.py"

if (!(Test-Path $PythonScriptPath)) {
@'
"""
Clasificador PARA + Obsidian

FASE 2:
- Leer config.yaml
- Detectar P:/PARA/00-INBOX
- Permitir seleccionar ruta alternativa si no existe
- Listar archivos de primer nivel
- Busqueda difusa
- Modo rapido / modo logica completa
- Confirmar antes de mover
- Crear nota Markdown en zResources
- Guardar log CSV/MD/JSON
- Permitir deshacer ultimo movimiento
"""

from pathlib import Path


def main():
    print("Clasificador PARA + Obsidian")
    print("FASE 1 completada. La logica se implementara en FASE 2.")


if __name__ == "__main__":
    main()
'@ | Out-File -Encoding UTF8 $PythonScriptPath
}

# ----------------------------
# Crear plantillas Markdown
# ----------------------------

$TemplatesPath = "$VaultPath\x\Templates\PARA"

$Templates = @{}

$Templates["recurso-base.md"] = @'
---
type: recurso
resource_type: 
title: "{{title}}"
summary: ""

para: recurso
category: 
subcategory: 

status: pendiente
archived: false

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
---

# {{title}}

## Resumen

Pendiente de describir.

## Ubicacion fisica

- Archivo: [Abrir archivo]({{target_file_uri}})
- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Clasificacion

| Campo | Valor |
|---|---|
| PARA | recurso |
| Categoria |  |
| Subcategoria |  |
| Tipo |  |
| Estado | pendiente |
| Archivado | false |

## Notas

- 

## Relaciones

- 
'@

$Templates["recurso-ebook.md"] = @'
---
type: recurso
resource_type: ebook
title: "{{title}}"
author: 
summary: ""

para: recurso
category: Biblioteca
subcategory: Ebooks

status: pendiente
archived: false

format: "{{extension}}"
language: 
pages: 
isbn: 

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
  - z/biblioteca
  - z/ebook
---

# {{title}}

## Resumen

Pendiente de describir.

## Datos del libro

| Campo | Valor |
|---|---|
| Autor |  |
| Formato | {{extension}} |
| Idioma |  |
| Estado | pendiente |

## Ubicacion fisica

- Archivo: [Abrir ebook]({{target_file_uri}})
- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Ideas o notas de lectura

- 

## Temas relacionados

- 
'@

$Templates["recurso-video.md"] = @'
---
type: recurso
resource_type: video
title: "{{title}}"
summary: ""

para: recurso
category: Multimedia
subcategory: Videos

status: pendiente
archived: false

duration: 
source: 
topic: 

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
  - z/video
  - z/multimedia
---

# {{title}}

## Resumen

Pendiente de describir.

## Datos del video

| Campo | Valor |
|---|---|
| Tema |  |
| Duracion |  |
| Fuente |  |
| Estado | pendiente |

## Ubicacion fisica

- Archivo: [Abrir video]({{target_file_uri}})
- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Notas

- 

## Posibles usos

- 
'@

$Templates["recurso-imagen.md"] = @'
---
type: recurso
resource_type: imagen
title: "{{title}}"
summary: ""

para: recurso
category: Imagenes
subcategory: 

status: referencia
archived: false

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
  - z/imagen
---

# {{title}}

## Resumen

Pendiente de describir.

## Ubicacion fisica

- Archivo: [Abrir imagen]({{target_file_uri}})
- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Uso posible

- 
'@

$Templates["recurso-audio.md"] = @'
---
type: recurso
resource_type: audio
title: "{{title}}"
summary: ""

para: recurso
category: Audio
subcategory: 

status: pendiente
archived: false

duration: 
source: 

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
  - z/audio
---

# {{title}}

## Resumen

Pendiente de describir.

## Ubicacion fisica

- Archivo: [Abrir audio]({{target_file_uri}})
- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Notas

- 
'@

$Templates["recurso-software.md"] = @'
---
type: recurso
resource_type: software
title: "{{title}}"
summary: ""

para: recurso
category: Software
subcategory: 

status: pendiente
archived: false

version: 
platform: windows
license: 
website: 

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
  - z/software
---

# {{title}}

## Resumen

Pendiente de describir.

## Datos del software

| Campo | Valor |
|---|---|
| Plataforma | Windows |
| Version |  |
| Licencia |  |
| Estado | pendiente |

## Ubicacion fisica

- Archivo: [Abrir archivo]({{target_file_uri}})
- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Instalacion / uso

- 

## Observaciones

- 
'@

$Templates["recurso-documento.md"] = @'
---
type: recurso
resource_type: documento
title: "{{title}}"
summary: ""

para: recurso
category: Documentos
subcategory: 

status: revisar
archived: false

document_type: 
owner: 
date_document: 

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
  - z/documento
---

# {{title}}

## Resumen

Pendiente de describir.

## Datos del documento

| Campo | Valor |
|---|---|
| Tipo documento |  |
| Propietario |  |
| Fecha documento |  |
| Estado | revisar |

## Ubicacion fisica

- Archivo: [Abrir documento]({{target_file_uri}})
- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Notas

- 
'@

$Templates["recurso-carpeta.md"] = @'
---
type: recurso
resource_type: carpeta
title: "{{title}}"
summary: ""

para: recurso
category: 
subcategory: 

status: pendiente
archived: false

source_path: "{{source_path}}"
target_path: "{{target_path}}"
folder_path: "{{folder_path}}"
obsidian_note: "{{obsidian_note}}"

cover: "{{cover}}"

created: "{{date}}"
updated: "{{date}}"
reviewed: 

tags:
  - z/recurso
---

# {{title}}

## Resumen

Pendiente de describir.

## Carpeta fisica

- Carpeta: [Abrir carpeta]({{folder_file_uri}})

## Contenido esperado

- 

## Notas

- 
'@

$Templates["moc-categoria.md"] = @'
---
type: moc
title: "{{title}}"
category: "{{category}}"
tags:
  - z/moc
  - z/recurso
---

# {{title}}

## Descripcion

Mapa de contenido para la categoria {{category}}.

## Carpetas fisicas relacionadas

- 

## Recursos relacionados

```dataview
TABLE resource_type, status, archived, updated
FROM "zResources"
WHERE category = "{{category}}"
SORT updated DESC
```
'@

$Templates["moc-carpeta-windows.md"] = @'
---
type: moc
title: "{{title}}"
windows_path: "{{windows_path}}"
tags:
  - z/moc
  - z/carpeta
---

# {{title}}

## Carpeta Windows

[Abrir carpeta]({{folder_file_uri}})

## Proposito

Pendiente de describir.

## Recursos relacionados

- 

## Observaciones

- 
'@

foreach ($TemplateName in $Templates.Keys) {
    $TemplateFile = Join-Path $TemplatesPath $TemplateName
    if (!(Test-Path $TemplateFile)) {
        $Templates[$TemplateName] | Out-File -Encoding UTF8 $TemplateFile
    }
}

Write-Host "FASE 1 completada correctamente." -ForegroundColor Green
Write-Host "Vault: $VaultPath"
Write-Host "Scripts: $ScriptsPath"
Write-Host "PARA: $ParaRoot"
