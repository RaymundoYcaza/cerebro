---
up:
  - "[[Tecnología MOC]]"
related: 
created: 2025-05-21
---


![[Pasted image 20250521141304.png]]

Volver a compilar.
```shell
npx vite build
```

Si no se genera el archivo `manifest.json` en `public/build`, copiarlo desde `public/build/.vite/`.
```shell
cp public/build/.vite/manifest.json public/build/manifest.json
```