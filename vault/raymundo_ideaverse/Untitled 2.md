---
up: []
related:
- '[[Instalaci├│n de Docker Engine en Ubuntu]]'
- '[[Gesti├│n de contenedores con Docker Compose]]'
created: '2026-05-22'
sourceType: technical-note
tags:
- note/technical
- note/technical/howto
- note/technical/troubleshooting
- z/Technical
- z/Docker
- z/Ubuntu
ai:
- generated: true
- model: gemma4:31b-cloud
- reviewed: false
- review_status: pending
- confidence: medium
vector:
  indexed: false
  collection: null
source:
  hash: 86aacee0c1392d70
---

# Instalaci├│n de Docker Compose en Ubuntu 24.04

## Resumen

Gu├¡a para instalar Docker Compose en Ubuntu 24.04 y resolver el error de comando desconocido.

## Problema

El usuario intenta ejecutar Docker Compose pero recibe el error 'docker: unknown command: docker compose'.

## Contexto

Ubuntu 24.04

## Soluci├│n

Instalar el plugin de Docker Compose para habilitar la funcionalidad del comando 'docker compose'.

## Paso a paso

1. Actualizar los repositorios del sistema
2. Instalar el paquete docker-compose-plugin

## Comandos

_No detectado._

## Errores comunes / s├¡ntomas

- **Error:** docker: unknown command: docker compose
  - **Causa:** El plugin de Docker Compose no est├í instalado o no est├í configurado correctamente en el sistema.
  - **Correcci├│n:** Instalar el paquete docker-compose-plugin mediante el gestor de paquetes de Ubuntu.

## T├⌐rminos relacionados

- Docker Engine
- Containerization
- CLI Plugin

## Enlaces sugeridos

- [[Instalaci├│n de Docker Engine en Ubuntu]]
- [[Gesti├│n de contenedores con Docker Compose]]

## Vac├¡os detectados

- [ ] El texto no proporciona los comandos exactos de instalaci├│n (ej. apt-get install)
- [ ] No se especifica si se requiere la configuraci├│n de repositorios oficiales de Docker antes de la instalaci├│n

## Extracto original

```text
C├│mo instalar Docker Compose en Ubuntu 24.04. Error: docker: unknown command: docker compose.
```
