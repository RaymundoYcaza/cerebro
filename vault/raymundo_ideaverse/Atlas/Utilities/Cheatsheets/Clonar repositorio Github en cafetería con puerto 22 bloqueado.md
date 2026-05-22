Si estás en una red pública (cafetería, coworking, etc.) con puertos restringidos, el problema casi seguro es que el puerto **22 (SSH)** está bloqueado. Pero hay varias formas prácticas de rodearlo sin hacer nada “oscuro”.

---

## 🔧 Opción 1: Usar SSH sobre puerto 443 (la más limpia)

GitHub permite SSH por el puerto **443**, que casi siempre está abierto (porque es HTTPS).

### Paso 1: probar conexión

```bash
ssh -T -p 443 git@ssh.github.com
```

Si funciona, verás un mensaje tipo:

```
Hi username! You've successfully authenticated...
```

### Paso 2: configurar tu SSH

Edita tu archivo:

```bash
nano ~/.ssh/config
```

Y agrega:

```
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
```

### Paso 3: clonar normalmente

```bash
git clone git@github.com:Inorizonti/inorizonti_sgc.git
```

---

## 🔄 Opción 2: Usar HTTPS en lugar de SSH

Si no necesitas claves SSH específicamente:

```bash
git clone https://github.com/Inorizonti/inorizonti_sgc.git
```

✔ Ventajas:

- Funciona casi siempre (usa puerto 443)
    
- No depende de configuración SSH
    

❗ Desventaja:

- Si haces push, te pedirá credenciales (puedes usar un **Personal Access Token**)
    

---

## 🔌 Opción 3: Túnel SSH externo (más avanzado)

Si tienes acceso a un servidor externo (VPS o máquina en casa), puedes hacer un túnel:

```bash
ssh -D 1080 usuario@tu-servidor.com
```

Y luego usarlo como proxy SOCKS.

Pero esto ya es más complejo y solo vale la pena si:

- Estás en un entorno muy restringido
    
- Necesitas trabajar frecuentemente desde ahí
    

---

## 🧠 Recomendación práctica

En tu caso:

👉 Usa **SSH por puerto 443** (opción 1)  
Es la solución más profesional y mantiene tu flujo de trabajo intacto.

---

Si quieres, puedo ayudarte a validar tu config actual (`~/.ssh/config`, llaves, etc.) o detectar exactamente qué está bloqueando la red.