---
up: []
related: []
created: 2026-03-30
---
Sí: puedes borrar esa memoria, y también puedes dejar Engram listo para sobrevivir a una reinstalación del sistema si separas **binario** y **datos**. Según la ayuda que mostraste, Engram soporta `save`, `search`, `context`, `export`, `import`, `sync`, `mcp`, `setup`, y además permite mover el directorio de datos con `ENGRAM_DATA_DIR`; por defecto usa `~/.engram`.[aider](https://aider.chat/)

## Borrar memoria

Si quieres eliminar una memoria guardada, hay dos caminos prácticos con lo que ya tienes visible:

- Si sabes exactamente qué memoria fue, primero búscala.[aider](https://aider.chat/)
    
- Luego identifica el registro y elimínalo desde la interfaz o, si tu integración expone borrado administrativo, desde el modo admin. La ayuda que mostraste indica que el modo MCP tiene perfiles `agent`, `admin` y `all`, lo que sugiere que las operaciones de administración, como borrar, no están en el perfil básico de agente.[aider](https://aider.chat/)
    

Como desde tu terminal compartida **no aparece un comando CLI directo `delete`** en la ayuda de `engram`, te recomiendo este orden:

1. Buscar la memoria:
    

bash

`engram search "texto único de esa memoria"`

1. Si la encuentras en resultados, abrir la interfaz:
    

bash

`engram tui`

1. Desde la TUI ubicar ese registro y borrarlo ahí, si la interfaz lo permite. La TUI existe explícitamente en la ayuda como modo interactivo.[aider](https://aider.chat/)
    

Si no quieres depender de la TUI, el camino más seguro es **exportar, editar e importar**:

bash

`engram export ~/engram-export.json`

Editar el JSON y luego:

bash

`engram import ~/engram-export.json`

Eso es más tosco, pero los comandos `export` e `import` están soportados por Engram según tu salida.[aider](https://aider.chat/)

## Enfoque recomendado

Para no mezclar “memorias de prueba” con memorias reales, usa esta convención:

- `scope=project` para cosas temporales o de un repo.
    
- `scope=personal` para rituales y aprendizajes duraderos.
    
- `project` siempre igual al nombre del repo.
    
- `type=pattern` para rituales.
    
- `type=bugfix` para soluciones puntuales.[aider](https://aider.chat/)
    

Así, si quieres limpiar pruebas, buscas solo por proyecto o por texto exacto y no tocas memorias buenas.

## Reinstalar el SO

Si vas a reinstalar el sistema operativo, no dejes la memoria en `~/.engram`, porque ese directorio vive en el home del sistema y es más fácil perderlo. Engram permite cambiar el directorio con `ENGRAM_DATA_DIR`, así que lo correcto es mover la base de memoria a tu disco persistente.[aider](https://aider.chat/)

Tu objetivo debería ser este:

- El programa `engram` se reinstala cuando haga falta.
    
- La memoria vive en tu disco persistente.
    
- Tras reinstalar, solo vuelves a instalar Engram y apuntas al mismo directorio de datos.[aider](https://aider.chat/)
    

## Estructura sugerida

Yo usaría algo así dentro de tu disco de trabajo:

bash

`/mnt/disc-a00/Z01-DEVOPS/state/engram`

Y dentro quedará la data persistente de Engram.

## Configuración persistente

Pon esta variable en tu entorno Fish, idealmente en tu `env.fish` o `config.fish`:

text

`set -gx ENGRAM_DATA_DIR /mnt/disc-a00/Z01-DEVOPS/state/engram`

Si quieres dejarlo ya mismo:

text

`mkdir -p /mnt/disc-a00/Z01-DEVOPS/state/engram echo 'set -gx ENGRAM_DATA_DIR /mnt/disc-a00/Z01-DEVOPS/state/engram' >> ~/.config/fish/config.fish source ~/.config/fish/config.fish`

La ayuda confirma que `ENGRAM_DATA_DIR` redefine el directorio de datos, así que con eso dejas Engram desacoplado del home local.[aider](https://aider.chat/)

## Migrar memoria actual

Si ya tienes memoria guardada en el directorio por defecto, haz una migración limpia con export/import:

1. Exporta desde la instalación actual.[aider](https://aider.chat/)
    

bash

`engram export /mnt/disc-a00/Z01-DEVOPS/state/engram/backup.json`

1. Define el nuevo `ENGRAM_DATA_DIR`.
    
2. Importa sobre la nueva ubicación.[aider](https://aider.chat/)
    

bash

`engram import /mnt/disc-a00/Z01-DEVOPS/state/engram/backup.json`

1. Verifica:
    

bash

`engram stats engram context`

## Instructivo de reinstalación

Cuando reinstales el sistema, sigue este checklist:

1. Montar tu disco persistente.
    
2. Reinstalar Engram.
    
3. Reponer tu config de Fish con `ENGRAM_DATA_DIR`.
    
4. Abrir una nueva terminal y verificar que la variable está activa.
    
5. Probar `engram stats`.
    
6. Probar `engram context`.
    
7. Si hiciste backup por export, importar el JSON.
    
8. Si usas sincronización por Git, ejecutar `engram sync --import`. La ayuda muestra `sync`, `--import`, `--status`, `--project` y `--all`, así que también puedes usar `.engram/` como respaldo sincronizable.[aider](https://aider.chat/)
    

Checklist literal:

bash

`# 1. instalar engram # 2. restaurar variable export ENGRAM_DATA_DIR=/mnt/disc-a00/Z01-DEVOPS/state/engram # 3. verificar engram stats engram context # 4. si hace falta importar backup engram import /mnt/disc-a00/Z01-DEVOPS/state/engram/backup.json`

## Respaldo recomendado

Yo haría **dos capas** de respaldo:

- **Capa 1:** `ENGRAM_DATA_DIR` en tu disco persistente.
    
- **Capa 2:** export JSON periódico o `engram sync` hacia un repo Git de respaldo.[aider](https://aider.chat/)
    

Eso te protege tanto de reinstalar el SO como de corromper una base local.

## Qué te sugiero hacer hoy

Haz esto hoy mismo, en este orden:

1. Mover Engram a `/mnt/disc-a00/Z01-DEVOPS/state/engram`.[aider](https://aider.chat/)
    
2. Exportar backup JSON.[aider](https://aider.chat/)
    
3. Probar `engram context` con la nueva ruta.[aider](https://aider.chat/)
    
4. Revisar en `engram tui` la memoria de prueba y borrarla si la interfaz lo permite.[aider](https://aider.chat/)
    

Comandos concretos:

bash

`mkdir -p /mnt/disc-a00/Z01-DEVOPS/state/engram engram export /mnt/disc-a00/Z01-DEVOPS/state/engram/backup.json`

Y en Fish:

text

`echo 'set -gx ENGRAM_DATA_DIR /mnt/disc-a00/Z01-DEVOPS/state/engram' >> ~/.config/fish/config.fish source ~/.config/fish/config.fish`

Luego:

bash

`engram import /mnt/disc-a00/Z01-DEVOPS/state/engram/backup.json engram stats engram context engram tui`

Si quieres, en el siguiente mensaje te dejo un **plan exacto de migración Engram + Fish + backups** adaptado a tu estructura `Z01-DEVOPS`, incluyendo nombres de carpetas y orden recomendado.