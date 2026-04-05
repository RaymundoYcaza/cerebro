---
created: 2025-03-31
in:
  - "[[Tecnología MOC]]"
---

  
# Cambiar ubicación de modelos de Ollama en Ubuntu (solución definitiva)

## 1. Detener el servicio Ollama

```bash

sudo systemctl stop ollama

```


## 2\. Crear directorio nuevo para modelos

```bash

sudo mkdir -p /mnt/blackpearl/ollama_models

sudo chown -R ollama:ollama /mnt/blackpearl/ollama_models

sudo chmod -R 770 /mnt/blackpearl/ollama_models

```

  

## 3\. Mover modelos existentes (si los hay)

```bash

sudo mv /usr/share/ollama/.ollama/models/* /mnt/blackpearl/ollama_models/

```

## 4\. Configurar el servicio Ollama

```bash

sudo mkdir -p /etc/systemd/system/ollama.service.d

sudo nano /etc/systemd/system/ollama.service.d/override.conf

```

Pegar este contenido:

```ini

[Service]

Environment="OLLAMA_MODELS=/mnt/blackpearl/ollama_models"

```

## 5\. Alternativa: Solución nuclear (si lo anterior falla)

```bash

sudo systemctl stop ollama

sudo mv /usr/share/ollama /mnt/blackpearl/

sudo ln -s /mnt/blackpearl/ollama /usr/share/ollama

sudo chown -R ollama:ollama /mnt/blackpearl/ollama

```


## 6\. Reiniciar y verificar

```bash

sudo systemctl daemon-reload

sudo systemctl restart ollama

  

# Verificar

sudo systemctl show ollama.service | grep Environment

ls -lh /mnt/blackpearl/ollama_models

```

  

## 7\. Probar con un modelo nuevo

```bash

ollama run llama2

```

## Solución para errores persistentes

Si aparece "no space left on device":

```bash

# Limpiar caché temporal

sudo rm -rf /usr/share/ollama/.ollama/models/*-partial

  

# Verificar espacio

df -h /mnt/blackpearl

  

# Forzar permisos

sudo chown -R ollama:ollama /mnt/blackpearl/ollama*

sudo chmod -R 770 /mnt/blackpearl/ollama*

```

## Notas importantes:

- Asegúrate que `/mnt/blackpearl` esté montado permanentemente (en `/etc/fstab`)

- Si usaste instalación Snap/Docker, la configuración es diferente

- El usuario del servicio es `ollama`, no tu usuario normal
