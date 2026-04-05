---
type: engram
domain: devops
status: refined
topic_key: ubuntu-systemd-static-server
updated: 2026-04-03
---

## What: (Qué se hizo)

Se creó una plantilla reutilizable para desplegar **servidores estáticos persistentes** en Ubuntu usando **systemd + python http.server**.

Características del servidor:

- Persistente (no depende de terminal)
- Reinicio automático si falla
- Inicio automático al reiniciar servidor
- Bajo consumo y rápida configuración

Convención:

Ruta base:

/mnt/disc-a00/Z00_SERVER-FILES/{proyecto}

Proceso:

1. Crear carpeta del proyecto
2. Copiar archivos estáticos
3. Crear servicio systemd
4. Activar servicio
5. Acceder por puerto asignado

Plantilla service:

- WorkingDirectory → carpeta del proyecto
- ExecStart → python http.server
- Restart → always

Se soportan múltiples proyectos usando **puertos distintos**.

También se creó **script de automatización**:

create-static-site.sh

Uso:

bash create-static-site.sh [nombre] [puerto]


---

## Why: (Racional técnico)

Se necesitaba:

- Publicar exportaciones estáticas (Obsidian, docs, dashboards)
- Evitar procesos manuales o nohup
- Mantener servicios persistentes
- Permitir múltiples sitios simultáneos
- Solución ligera sin nginx ni apache

systemd ofrece:

- Supervisión del proceso
- Restart automático
- Arranque al boot
- Logs centralizados

python http.server ofrece:

- Configuración mínima
- Sin dependencias adicionales
- Ideal para contenido estático interno


---

## Where: (Nombre y ruta del archivo/proyecto)

Servicios:

/etc/systemd/system/[proyecto].service

Archivos estáticos:

/mnt/disc-a00/Z00_SERVER-FILES/[proyecto]

Script automatización:

create-static-site.sh

Ejemplo:

Servicio:
sgc-inorizonti.service

Ruta:
mnt/disc-a00/Z00_SERVER-FILES/sgc-inorizonti

Acceso:
http://IP:8888


---

## Learned: (Lección aprendida/Error evitado)

- systemd es mejor que nohup o screen para servicios persistentes
- python http.server es suficiente para contenido estático interno
- Mantener convención de carpetas evita desorden
- Un puerto por proyecto evita conflictos
- Reiniciar servicio tras cambios asegura consistencia
- Script de automatización reduce errores manuales
- Mantener servicios en /etc/systemd/system facilita administración

Patrón reutilizable:

static-server + systemd + carpeta dedicada + puerto único
