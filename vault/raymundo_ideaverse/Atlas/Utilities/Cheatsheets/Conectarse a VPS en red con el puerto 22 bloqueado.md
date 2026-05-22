Vas bien, pero aquí hay un detalle clave que te está bloqueando:

👉 **Tu configuración es correcta, pero el servicio no está escuchando en 443 realmente.**

Ese comentario en tu archivo no es decorativo:

```
# When systemd socket activation is used (the default)...
# systemctl restart ssh.socket
```

Eso cambia completamente el comportamiento.

---

# 🔥 El problema real

En muchas imágenes (incluyendo las de DigitalOcean), SSH **no usa directamente sshd**, sino:

👉 **systemd socket activation (`ssh.socket`)**

Eso significa:

- El puerto se define en el _socket_, no en `sshd_config`
    
- Reiniciar `ssh` **no aplica cambios de puertos**
    

Por eso obtienes:

```
Connection refused
```

---

# ✅ Solución correcta (la que te va a funcionar)

## 1. Edita el socket de SSH:

```bash
sudo nano /lib/systemd/system/ssh.socket
```

Busca esta línea:

```
ListenStream=22
```

Y cámbiala a:

```
ListenStream=22
ListenStream=443
```

---

## 2. Recargar systemd

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
```

---

## 3. Reiniciar el socket (NO el servicio ssh)

```bash
sudo systemctl restart ssh.socket
```

---

## 4. Verifica que esté escuchando

```bash
sudo ss -tlnp | grep ssh
```

Deberías ver algo como:

```
:22
:443
```

---

## 5. Prueba conexión

```bash
ssh -p 443 root@165.22.14.10
```

---

# ⚠️ Alternativa (más simple y recomendable)

Desactiva socket activation y usa SSH normal:

```bash
sudo systemctl disable --now ssh.socket
sudo systemctl enable --now ssh
```

Luego:

```bash
sudo systemctl restart ssh
```

👉 En este modo, **sí funciona `sshd_config` como esperas** (más predecible).

---

# 🧠 Diagnóstico rápido de tu caso

Tu situación fue:

- ✔ Editaste `sshd_config` correctamente
    
- ✔ Reiniciaste `ssh`
    
- ❌ Pero el sistema está usando `ssh.socket`
    
- ❌ Por eso nunca abrió el puerto 443
    

---

# 🎯 Recomendación práctica

Para lo que estás haciendo (acceso rápido + control):

👉 Usa **modo clásico (sin socket activation)**

Es más simple, más controlable, y evita este tipo de problemas.

---

Si quieres, en el siguiente paso te dejo un **checklist de hardening mínimo** para dejar SSH en 443 sin exponerte innecesariamente (fail2ban, claves, etc.).

Aquí lo tienes **listo para copiar y pegar**, limpio y correcto para habilitar también el 443:

```ini
[Unit]
Description=OpenBSD Secure Shell server socket
Before=sockets.target ssh.service
ConditionPathExists=!/etc/ssh/sshd_not_to_be_run

[Socket]
ListenStream=0.0.0.0:22
ListenStream=0.0.0.0:443
ListenStream=[::]:22
ListenStream=[::]:443
BindIPv6Only=ipv6-only
Accept=no
FreeBind=yes

[Install]
WantedBy=sockets.target
RequiredBy=ssh.service
```

---

# 🚀 Luego ejecuta EXACTAMENTE esto:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl restart ssh.socket
```

---

# 🔍 Verifica que funcione:

```bash
sudo ss -tlnp | grep ssh
```

Debes ver **puerto 22 y 443** escuchando.

---

# 🧪 Prueba conexión:

```bash
ssh -p 443 root@165.22.14.10
```

---

# ⚠️ Si aún falla (muy común en DigitalOcean)

Ejecuta esto (firewall):

```bash
sudo ufw allow 443/tcp
sudo ufw reload
```

---

# 🧠 Nota breve (importante)

Si quieres evitar estos problemas en el futuro:

👉 Desactiva socket activation completamente:

```bash
sudo systemctl disable --now ssh.socket
sudo systemctl enable --now ssh
```

Y te quedas solo con `sshd_config` (más simple).

---

Si después de esto no conecta, el problema ya no sería SSH sino red/firewall, y lo diagnosticamos en 1 comando.