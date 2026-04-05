---
up: []
related: []
created: 2026-03-28
---

# 🚀 Plantilla Rápida — Servidor Estático Persistente (Ubuntu + systemd)

Este instructivo permite publicar **sitios estáticos** (como exportaciones de Obsidian, documentación, dashboards, etc.) en un **servidor persistente** que:

- No se detiene al cerrar terminal
    
- Se reinicia automáticamente si falla
    
- Arranca automáticamente al reiniciar el servidor
    
- Es rápido y ligero
    

---

# 📁 Convención de Carpetas

Todos los proyectos deben ubicarse en:

```
/mnt/disc-a00/Z00_SERVER-FILES/xxx
```

Donde:

- `xxx` = nombre del proyecto
    

Ejemplos:

```
/mnt/disc-a00/Z00_SERVER-FILES/obsidian-vault
/mnt/disc-a00/Z00_SERVER-FILES/docs-internos
/mnt/disc-a00/Z00_SERVER-FILES/sgc-inorizonti
```

---

# 🧩 Paso 1 — Crear carpeta del proyecto

```
mkdir -p /mnt/disc-a00/Z00_SERVER-FILES/xxx
```

Copiar los archivos estáticos allí.

---

# ⚙️ Paso 2 — Crear servicio systemd

```
sudo nano /etc/systemd/system/xxx.service
```

Plantilla:

```
[Unit]
Description=Servidor Estático xxx
After=network.target

[Service]
Type=simple
User=jabes
WorkingDirectory=/mnt/disc-a00/Z00_SERVER-FILES/xxx
ExecStart=/usr/bin/python3 -m http.server 8888
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

---

# 🔄 Paso 3 — Activar servicio

```
sudo systemctl daemon-reload
sudo systemctl enable xxx
sudo systemctl start xxx
```

---

# 🔍 Paso 4 — Verificar estado

```
sudo systemctl status xxx
```

Debe aparecer:

```
Active: active (running)
```

---

# 🌐 Acceso

Desde navegador:

```
http://IP-SERVIDOR:8888
```

Ejemplo:

```
http://192.168.1.10:8888
```

---

# 🔢 Múltiples Proyectos (Puertos distintos)

Proyecto 1

```
obsidian-vault → puerto 8888
```

Proyecto 2

```
docs → puerto 8889
```

Proyecto 3

```
dashboard → puerto 8890
```

Modificar:

```
ExecStart=/usr/bin/python3 -m http.server 8889
```

---

# 🛠️ Comandos útiles

Reiniciar servicio

```
sudo systemctl restart xxx
```

Detener

```
sudo systemctl stop xxx
```

Ver logs

```
journalctl -u xxx -n 50
```

Eliminar servicio

```
sudo systemctl disable xxx
sudo rm /etc/systemd/system/xxx.service
sudo systemctl daemon-reload
```

---

# 📋 Ejemplo Real

Servicio:

```
sgc-inorizonti.service
```

Ruta:

```
/mnt/disc-a00/Z00_SERVER-FILES/sgc-inorizonti
```

Puerto:

```
8888
```

Acceso:

```
http://IP:8888
```

---

# 💡 Buenas prácticas

- Un puerto por proyecto
    
- Nombres cortos y claros
    
- Mantener todo en `/Z00_SERVER-FILES`
    
- Reiniciar servicio tras actualizar archivos
    

---

# ⚡ Crear proyecto en 30 segundos

1. Copiar archivos
    
2. Crear servicio
    
3. Activar
    
4. Listo
    

---

# 🚀 Opcional — Script rápido (Automatizar)

```
sudo nano create-static-site.sh
```

```
#!/bin/bash

NAME=$1
PORT=$2

sudo tee /etc/systemd/system/$NAME.service > /dev/null <<EOF
[Unit]
Description=Servidor Estático $NAME
After=network.target

[Service]
Type=simple
User=jabes
WorkingDirectory=/mnt/disc-a00/Z00_SERVER-FILES/$NAME
ExecStart=/usr/bin/python3 -m http.server $PORT
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable $NAME
sudo systemctl start $NAME

echo "Sitio $NAME creado en puerto $PORT"
```

Uso:

```
bash create-static-site.sh obsidian 8888
```

---

# 🎯 Resultado

Servidor estático rápido, persistente y escalable.
