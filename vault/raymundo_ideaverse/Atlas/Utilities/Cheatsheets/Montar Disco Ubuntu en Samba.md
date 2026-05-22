---
up: []
related: []
created: 2026-04-26
---

# 📂 Montar Disco Ubuntu en Samba (Configuración Rápida y Práctica)

## 🔧 Montaje del Disco (`/mnt/disco-a00`)
```bash
sudo mkdir /mnt/disco-a00
sudo mount /dev/sde1 /mnt/disco-a00/
sudo mount /dev/sde2 /mnt/disco-a00/
sudo mount /dev/sde3 /mnt/disco-a00/
```

## 🌐 Configuración Samba

### 1. Definir la ruta en el Samba
```ini
[Configura Samba]
path = /mnt/disco-a00/
```

### 2. Crear Directorio en Samba
```bash
sudo mkdir /mnt/share
sudo chown -R 999 /mnt/share
sudo chmod 755 /mnt/share
```

### 3. Permitir Acceso en el Samba
```bash
sudo setfacl /mnt/share /mnt/
```

### 4. Ejecutar al Samba
```bash
sudo mount /mnt/share
sudo su /mnt/share
```

## ✅ Ejemplo Completo

```bash
# Montar el disco
sudo mount /dev/sde1 /mnt/
sudo mount /dev/sde2 /mnt/
sudo mount /dev/sde3 /mnt/

# Configurar Samba
sudo mkdir /mnt/share
sudo chown -R 999 /mnt/share
sudo chmod 755 /mnt/share

# Configurar permisos en el Samba
sudo setfacl /mnt/share /mnt/
sudo mount /mnt/share

# Acceder al Samba
sudo su /mnt/share
```

## 📝 Alternativa (Si no tienes `/mnt/share`)

```bash
# Montar el disco desde /mnt
sudo mount /mnt
sudo su /mnt/share
```

## 🔐 Notas Importantes

- ✅ Asegura que `sudo chown -R 999 /mnt/share`
- ⚠️ Si no tienes `sudo`, no montes desde `/mnt`.
- ✅ Configura el archivo Samba en `/mnt/share`
- ⚠️ No asumas el `/mnt` sin permisos correctos

## 📝 Resumen

- ✅ **Montar `/mnt` con disco:** `sudo mount /mnt`
- ✅ **Crear Samba:** `sudo mkdir /mnt/share`
- ✅ **Permitir:** `sudo setfacl`

¡Asegúrate de que las rutas y permisos son correctos antes de empezar! 😊
