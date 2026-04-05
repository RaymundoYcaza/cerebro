---
up: []
related: []
created: 2025-05-29
---
 

# Instructivo para conectar OneDrive Personal como Unidad de Red (WebDAV)

Este método permite conectar tu cuenta de **OneDrive Personal** como una **unidad de red WebDAV** que solo consume espacio cuando estás en línea.

---

## 1. Obtener tu CID (Customer ID)

1. Abre tu navegador y entra a: https://onedrive.live.com
2. Inicia sesión con tu cuenta de Microsoft.
3. Una vez dentro, observa la URL en la barra de direcciones. Verás algo como:

   ```
   https://onedrive.live.com/?cid=0123456789ABCDEF
   ```

4. Copia el valor que aparece después de `cid=`. Este es tu **CID**.

---

## 2. Construir la URL WebDAV

Usa la siguiente estructura para tu URL de WebDAV:

```
https://d.docs.live.net/<tu_CID>/
```

Ejemplo:

```
https://d.docs.live.net/0123456789ABCDEF/
```

Puedes agregar una carpeta específica al final si lo deseas:

```
https://d.docs.live.net/0123456789ABCDEF/MisDocumentos/
```

---

## 3. Conectar como unidad de red en Windows

1. Abre **Explorador de archivos**.
2. Haz clic derecho sobre **Este equipo** y elige **Conectar a unidad de red**.
3. Selecciona una letra de unidad (por ejemplo, `Z:`).
4. En el campo **Carpeta**, pega la URL WebDAV:

   ```
   https://d.docs.live.net/0123456789ABCDEF/
   ```

5. Marca **“Conectarse nuevamente al iniciar sesión”**.
6. Haz clic en **Finalizar**.
7. Introduce tus credenciales de Microsoft (correo y contraseña de OneDrive).

---

## 4. (Opcional) Conectar vía línea de comandos (BAT)

Puedes crear un archivo `.bat` con este contenido para montar la unidad automáticamente:

```bat
net use Z: "https://d.docs.live.net/0123456789ABCDEF/" /user:tuemail@outlook.com TuContraseña /persistent:yes
```

Reemplaza:

- `Z:` por la letra de unidad que desees.
- `0123456789ABCDEF` por tu CID.
- `tuemail@outlook.com` y `TuContraseña` por tus credenciales.

---

> ✅ Este método solo accede a los archivos cuando estás conectado a internet y **no ocupa espacio local** como la sincronización clásica de OneDrive.
