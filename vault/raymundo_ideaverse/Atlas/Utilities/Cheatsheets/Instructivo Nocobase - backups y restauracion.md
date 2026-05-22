# Instructivo de Backups y Restauración — NocoBase + PostgreSQL + Dokploy

[Docker Compose NocoBase](https://chatgpt.com/c/69fb8de9-c2f4-83e9-9ec8-a80cfca1f990)

## Arquitectura actual

```text
NocoBase
├── PostgreSQL → volumen Docker interno
├── Storage/uploads → disco externo USB
└── Compose/.env/scripts → disco externo USB
```

Ruta base:

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase
```

---

# 1. Estructura recomendada

## Crear carpetas

```bash
mkdir -p /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/{backups/postgres,backups/storage,scripts}
```

---

# 2. Backup de PostgreSQL

## Crear script

Archivo:

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-postgres.sh
```

Contenido:

```bash
#!/usr/bin/env bash

set -euo pipefail

BASE_DIR="/mnt/disc-a00/Z01-DEVOPS/containers/nocobase"
BACKUP_DIR="$BASE_DIR/backups/postgres"

DATE=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"

echo "==> Generando backup PostgreSQL..."

docker exec \
  infraestructura-nocobase-qolsue-postgres-1 \
  pg_dump \
  -U nocobase \
  -d nocobase \
  -F c \
  -b \
  --quote-all-identifiers \
  -f /tmp/nocobase.dump

docker cp \
  infraestructura-nocobase-qolsue-postgres-1:/tmp/nocobase.dump \
  "$BACKUP_DIR/nocobase_${DATE}.dump"

docker exec \
  infraestructura-nocobase-qolsue-postgres-1 \
  rm -f /tmp/nocobase.dump

echo "==> Backup completado:"
echo "$BACKUP_DIR/nocobase_${DATE}.dump"
```

---

## Dar permisos

```bash
chmod +x /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-postgres.sh
```

---

## Ejecutar backup manual

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-postgres.sh
```

---

# 3. Backup de Storage (uploads/plugins)

## Crear script

Archivo:

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-storage.sh
```

Contenido:

```bash
#!/usr/bin/env bash

set -euo pipefail

BASE_DIR="/mnt/disc-a00/Z01-DEVOPS/containers/nocobase"
SOURCE_DIR="$BASE_DIR/data/storage"
BACKUP_DIR="$BASE_DIR/backups/storage"

DATE=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"

echo "==> Comprimiendo storage..."

tar -czf \
  "$BACKUP_DIR/storage_${DATE}.tar.gz" \
  -C "$BASE_DIR/data" \
  storage

echo "==> Backup completado:"
echo "$BACKUP_DIR/storage_${DATE}.tar.gz"
```

---

## Dar permisos

```bash
chmod +x /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-storage.sh
```

---

## Ejecutar backup manual

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-storage.sh
```

---

# 4. Backup completo (recomendado)

## Crear script

Archivo:

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-all.sh
```

Contenido:

```bash
#!/usr/bin/env bash

set -euo pipefail

BASE_DIR="/mnt/disc-a00/Z01-DEVOPS/containers/nocobase"

echo "==> Iniciando backup completo..."

"$BASE_DIR/scripts/backup-postgres.sh"
"$BASE_DIR/scripts/backup-storage.sh"

echo "==> Backup completo finalizado."
```

---

## Permisos

```bash
chmod +x /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-all.sh
```

---

## Ejecutar backup completo

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-all.sh
```

---

# 5. Restauración de PostgreSQL

## IMPORTANTE

La restauración:

- elimina el contenido actual de la base,
    
- sobrescribe datos,
    
- requiere detener NocoBase temporalmente.
    

---

## Obtener nombre del contenedor

Verificar:

```bash
docker ps
```

Debe existir algo parecido a:

```text
infraestructura-nocobase-qolsue-postgres-1
infraestructura-nocobase-qolsue-nocobase-1
```

---

## Detener NocoBase

```bash
docker stop infraestructura-nocobase-qolsue-nocobase-1
```

---

## Copiar backup al contenedor

Ejemplo:

```bash
docker cp \
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/backups/postgres/nocobase_2026-05-06_18-00-00.dump \
infraestructura-nocobase-qolsue-postgres-1:/tmp/restore.dump
```

---

## Restaurar base

```bash
docker exec -it infraestructura-nocobase-qolsue-postgres-1 bash
```

Dentro del contenedor:

```bash
dropdb -U nocobase nocobase

createdb -U nocobase nocobase

pg_restore \
  -U nocobase \
  -d nocobase \
  --clean \
  --if-exists \
  /tmp/restore.dump
```

Salir:

```bash
exit
```

---

## Reiniciar NocoBase

```bash
docker start infraestructura-nocobase-qolsue-nocobase-1
```

---

# 6. Restauración de Storage

## Respaldar storage actual

```bash
mv \
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/data/storage \
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/data/storage.bak.$(date +%Y-%m-%d_%H-%M-%S)
```

---

## Restaurar backup

Ejemplo:

```bash
tar -xzf \
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/backups/storage/storage_2026-05-06_18-00-00.tar.gz \
-C /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/data
```

---

# 7. Restauración completa

Orden correcto:

```text
1. Detener NocoBase
2. Restaurar PostgreSQL
3. Restaurar Storage
4. Iniciar NocoBase
```

---

# 8. Automatizar backups diarios

## Editar cron

```bash
crontab -e
```

---

## Backup diario 2 AM

```cron
0 2 * * * /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/scripts/backup-all.sh >> /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/backups/backup.log 2>&1
```

---

# 9. Política recomendada de retención

Mantener:

```text
7 backups diarios
4 backups semanales
3 backups mensuales
```

---

# 10. Verificación de backups

## Ver archivos generados

```bash
ls -lah /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/backups/postgres
```

```bash
ls -lah /mnt/disc-a00/Z01-DEVOPS/containers/nocobase/backups/storage
```

---

# 11. Backup externo recomendado

Idealmente sincronizar además hacia:

- otro disco,
    
- NAS,
    
- Google Drive,
    
- OneDrive,
    
- Backblaze,
    
- rclone remoto.
    

Ejemplo con rclone:

```bash
rclone sync \
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase/backups \
gdrive:nocobase-backups
```

---

# 12. Restauración completa después de formateo/migración

## Instalar

- Docker
    
- Docker Compose
    
- Dokploy
    

---

## Restaurar carpeta

Copiar nuevamente:

```bash
/mnt/disc-a00/Z01-DEVOPS/containers/nocobase
```

---

## Redeploy en Dokploy

Usar el mismo `docker-compose.yml`.

---

## Restaurar PostgreSQL

Usar el dump más reciente.

---

## Restaurar storage

Extraer backup storage más reciente.

---

# 13. Recomendación crítica

Antes de:

- actualizar NocoBase,
    
- instalar plugins,
    
- permitir acceso IA/MCP,
    
- modificar workflows masivos,
    

ejecutar SIEMPRE:

```bash
backup-all.sh
```

Porque NocoBase guarda:

- schema,
    
- ACL,
    
- workflows,
    
- formularios,
    
- plugins,
    
- layouts,
    
- metadatos,
    

dentro de PostgreSQL.