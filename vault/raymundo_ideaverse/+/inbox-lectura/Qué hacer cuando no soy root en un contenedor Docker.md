---
up:
  - "[[Docker MOC]]"
related: 
created_at: 2025-04-25
---


Si entrando a un contenedor Docker, por ejemplo:

```bash
docker exec -ti n8n sh
```

Y tratando de hacer algo como editar el archivo hosts da error de permisos, entonces hay que acceder como root de la siguiente forma:

```bash
docker exec -u 0 -ti n8n sh
```