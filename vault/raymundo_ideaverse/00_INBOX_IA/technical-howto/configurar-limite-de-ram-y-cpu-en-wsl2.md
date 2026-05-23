---
up: []
related:
- '[[Optimización de recursos en Windows]]'
- '[[Instalación de WSL2]]'
- '[[Gestión de memoria en Linux]]'
created: '2026-05-22'
sourceType: technical-note
source: '[[Cómo controlar el limite de memoria RAM en WSL 2]]'
source_hash: b4db414bf417ce65
tags:
- note/technical
- note/technical/howto
- z/Technical
- z/WSL2
- z/Windows
- z/Linux
ai_generated: true
ai_model: gemma4:31b-cloud
ai_reviewed: false
ai_review_status: pending
ai_confidence: high
vector_indexed: false
vector_collection: null
---

# Configurar límite de RAM y CPU en WSL2

## Resumen

Guía rápida para limitar el consumo de recursos (RAM, procesadores y swap) de WSL2 mediante el archivo de configuración global .wslconfig.

## Problema

Consumo excesivo de memoria RAM por parte de WSL2 en el sistema anfitrión Windows.

## Contexto

Entorno Windows con WSL2 instalado.

## Solución

Crear o editar el archivo `.wslconfig` en el directorio del perfil de usuario para definir los límites de hardware.

## Paso a paso

1. Localizar o crear el archivo `.wslconfig` en `C:\Users\<USUARIO>\.wslconfig`.
2. Definir los parámetros de memoria, procesadores y swap bajo la sección `[wsl2]`.
3. Guardar los cambios.
4. Reiniciar la instancia de WSL para aplicar la configuración.

## Comandos

```bash
{'command': 'wsl --shutdown', 'description': 'Apaga todas las distribuciones de WSL para aplicar cambios de configuración.'}
```

```bash
{'command': 'notepad $env:USERPROFILE\\.wslconfig', 'description': 'Abre el archivo de configuración en el Bloc de notas desde PowerShell.'}
```

```bash
{'command': 'cat $env:USERPROFILE\\.wslconfig', 'description': 'Muestra el contenido del archivo de configuración en la consola de PowerShell.'}
```

## Errores comunes / síntomas

_No detectado._

## Términos relacionados

- .wslconfig
- WSL2 Memory Limit
- Swap space
- localhostForwarding

## Enlaces sugeridos

- [[Optimización de recursos en Windows]]
- [[Instalación de WSL2]]
- [[Gestión de memoria en Linux]]

## Vacíos detectados

- [ ] No se especifica el formato de unidad para la memoria (ej. si acepta MB o solo GB)
- [ ] No se menciona el comportamiento por defecto si el archivo no existe
