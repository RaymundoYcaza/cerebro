---
up: []
related: []
created: 2026-04-12
---

# Cómo crear config SSH para Github

Para crear y usar **SSH con GitHub en Ubuntu** debes hacer 4 pasos:

---

# 1. Verificar si ya tienes una clave SSH

Primero revisa si ya existe una:

```bash
ls -al ~/.ssh
```

Si ves archivos como:

- `id_ed25519`
- `id_ed25519.pub`

Ya tienes una clave.
Si no, créala.

---

# 2. Crear nueva clave SSH (recomendado: ed25519)

Ejecuta:

```bash
ssh-keygen -t ed25519 -C "tu_email_github@example.com"
```

Ejemplo:

```bash
ssh-keygen -t ed25519 -C "juan@gmail.com"
```

Presiona **Enter** en todo:

```
Enter file in which to save the key → Enter
Enter passphrase → Enter (opcional)
```

Esto creará:

```
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

---

# 3. Iniciar el agente SSH y agregar la clave

Ejecuta:

```bash
eval "$(ssh-agent -s)"
```

Luego:

```bash
ssh-add ~/.ssh/id_ed25519
```

---

# 4. Copiar la clave pública

Ejecuta:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copiarás algo así:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... tu_email@gmail.com
```

---

# 5. Agregar la clave en GitHub

Ve a:

GitHub → Settings → SSH and GPG keys

O directamente:

[https://github.com/settings/keys](https://github.com/settings/keys)

Luego:

1. Click **New SSH key**
2. Title: `Ubuntu Laptop` (o el nombre que quieras)
3. Pega la clave
4. Save

---

# 6. Probar conexión

Ejecuta:

```bash
ssh -T git@github.com
```

Debe salir algo como:

```
Hi usuario! You've successfully authenticated...
```

---

# 7. Usar repositorios con SSH

En vez de usar:

```
https://github.com/user/repo.git
```

Usa:

```
git@github.com:user/repo.git
```

Ejemplo:

```bash
git clone git@github.com:usuario/proyecto.git
```

---

# Opcional (Recomendado si usas múltiples claves)

Crear config SSH:

```bash
nano ~/.ssh/config
```

Agregar:

```
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
```

Guardar:

```
Ctrl + O
Enter
Ctrl + X
```

---

# Uso con fish

Estás usando **Fish shell**, y ese comando es de **bash/zsh**, por eso falla.
En **fish** debes usar la versión compatible.

---

# Solución correcta para Fish

Ejecuta:

```fish
ssh-agent -c
```

O mejor aún (recomendado):

```fish
eval (ssh-agent -c)
```

Luego agrega la clave:

```fish
ssh-add ~/.ssh/id_ed25519
```

---

# Alternativa más limpia (Recomendada para Fish)

Fish suele usar esto:

```fish
ssh-agent | source
```

Luego:

```fish
ssh-add ~/.ssh/id_ed25519
```

---

# Verifica que funcionó

```fish
ssh-add -l
```

Debe mostrar algo como:

```
256 SHA256:xxxxx id_ed25519 (ED25519)
```

---

# Bonus (Para que no tengas que hacerlo siempre)

Agrega esto a tu config de fish:

```fish
nano ~/.config/fish/config.fish
```

Añade:

```fish
if not set -q SSH_AUTH_SOCK
    ssh-agent -c | source
end
```

Así el SSH agent se inicia automáticamente al abrir terminal.

---

Una pregunta rápida para afinar la configuración:

¿Estás usando Ubuntu en:

- WSL
- VPS
- Desktop local
- Server remoto por SSH

Te doy la configuración más correcta según tu caso.
