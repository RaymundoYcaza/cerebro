---
in:
  - "[[Docker MOC]]"
---


Detener todos los contenedores
```
docker stop $(docker ps -a -q)
```


## Resolución de problemas
Puedo acceder por medio de localhost y de 127.0.0.1 pero no a través de la IP de mi computadora, usando Docker en Windows Subsystem for Linux (WSL)
Para acceder a tus contenedores Docker a través de la IP de tu red local, puedes intentar lo siguiente:
**Obtén la dirección IP de la interfaz eth0 en WSL**: Puedes obtener la dirección IP de la interfaz eth0 en WSL ejecutando el comando `ip addr` en la terminal de Ubuntu en WSL. Busca la entrada para eth0 (algo como `2: eth0:`) y toma la dirección inet de allí (por ejemplo, `inet 172.18.174.48`).
**Usa la dirección IP de la interfaz eth0 para acceder a tus servicios**: Una vez que tengas la dirección IP de la interfaz eth0, puedes usarla en tus solicitudes de Windows como `http://<eth0-ip>:<port>`.
**Configura tu firewall para permitir el tráfico a esa IP**: Si tienes un firewall activo, asegúrate de que permite el tráfico a la dirección IP de la interfaz eth0.
**Verifica tu archivo docker-compose.yml**: Tu archivo docker-compose.yml parece estar bien. Estás mapeando correctamente los puertos de tus servicios a los puertos del host.
## Cómo Dockerizar cualquier aplicación de Github
El Pingüino de Mario
{{video(https://www.youtube.com/watch?v=nB9QLfOhcBg)}}
## Agregar un host adicional a un contenedor
Para agregar la opción `--add-host` en un entorno Docker Compose, necesitas agregarla en tu archivo `docker-compose.yml`. Aquí te muestro cómo hacerlo:
```yaml
version: '3'
services:
  nextcloud:
    image: nextcloud
    ...
    extra_hosts:
      - "officeserver.midominio.com:192.168.0.81"
    ...
```
En este ejemplo, `nextcloud` es el nombre del servicio que estás ejecutando. Debes reemplazarlo con el nombre de tu servicio.
Después de hacer estos cambios, puedes ejecutar `docker-compose up -d` como lo haces normalmente para iniciar tus contenedores.
Por favor, ten en cuenta que este cambio solo afectará al contenedor Docker específico que estás ejecutando con esta opción. Si tienes otros contenedores que necesitan acceder a `officeserver.midominio.com` en `192.168.0.81`, deberás agregar la opción `extra_hosts` a esos contenedores también.
```yaml
extra_hosts:
  - "backoffice.inorizonti.com:192.168.0.81"
```
## Al vincular un volumen a un archivo en lugar de una carpeta, este se monta como carpeta
Esto sucede cuando se monta un archivo que aún no existe en el host, al crearlo, docker crea el punto de montaje y por defecto lo hace como carpeta.
El truco está en hacer un `touch archivo.ext` en la ubicación a la que apunta el `docker-compose.yml` antes de ejecutarlo y se enlazará correctamente.
## Operaciones con contenedores
### Renombrar un contenedor existente
```
docker rename <current_name> <new_name>
```
## Operaciones con imágenes
Remover una imagen
```bash
docker rmi nombre_imagen
```
Desarrollar Python en Docker: cree un entorno de desarrollo de Python sin instalar Python
{{video(https://www.youtube.com/watch?v=3JU7Pjwk4s0)}}
Run Android in a Docker Container!
{{video(https://www.youtube.com/watch?v=a1M40roHuRg)}}
```
docker stop $(docker ps -a -q) # stop all containers
docker rm $(docker ps -a -q) # remove all containers
docker rmi -f $(docker images -q) # remove all images
```
Limitar la memoria de un contenedor
Ejecutar con el parámetro `--memory-2g`
Cómo detener todos los contenedores
`docker stop $(docker ps -aq)`
Listar contenedores
*Referencia columnas*
Names:
```
docker ps --format '{{.Names}}'
```
ID:
```
docker ps --format '{{.ID}}'
```
Image:
```
docker ps --format '{{.Image}}'
```
Command:
```
docker ps --format '{{.Command}}'
```
Created:
```
docker ps --format '{{.RunningFor}}'
```
Status:
```
docker ps --format '{{.Status}}'
```
Ports:
```
docker ps --format '{{.Ports}}'
```
Mostrando solamente los nombres
```apl
docker ps --format '{{.Names}}'
```
Mostrando ID y nombre
```apl
docker ps --format '{{.ID}} {{.Names}}'
```
Mostrando ID, nombre y estado
```apl
docker ps --format '{{.ID}} {{.Names}} {{.Status}}'
```
