---
created: 2024-05-25 
---



[[Instalar WP-Cli en WordPress Docker]]
Comandos básicos Docker-Compose
Levantar un servicio
` docker-compose up`
Levantar un servicio específico
` docker-compose up local`
Detener un servicio
`docker-compose down`
Obtener información de un contenedor
`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id`
Tomado de: https://stackoverflow.com/questions/17157721/how-to-get-a-docker-containers-ip-address-from-the-host
> Tomado de https://es.linkedin.com/pulse/docker-compose-conceptos-comandos-y-ejemplos-juan-ignacio-paz
Juan Ignacio Paz
# Cómo respaldar un contenedor Docker
Para respaldar el volumen de un contenedor Docker, puedes seguir los siguientes pasos:
Crea un contenedor temporal para hacer una copia del volumen montado. Esto se puede hacer utilizando el comando `docker run` y especificando el volumen montado en el contenedor que deseas respaldar.
```bash
docker run --rm -v <nombre_del_volumen>:/data -v <ruta_local_para_guardar_copia>:/backup alpine tar -czvf /backup/<nombre_del_volumen>.tar.gz /data
```
Este comando ejecuta un contenedor de Alpine Linux y monta el volumen `<nombre_del_volumen>` en la ruta `/data`. También monta un directorio local `<ruta_local_para_guardar_copia>` en la ruta `/backup` del contenedor. El comando `tar` se utiliza para crear un archivo `.tar.gz` de la carpeta `/data`, que se guarda en el directorio local `/backup` con el nombre `<nombre_del_volumen>.tar.gz`.
Verifica que el archivo de copia de seguridad se haya creado 
correctamente en la ruta local especificada. Puedes hacer esto 
utilizando el comando `ls` en la ruta local.

bash
ls <ruta_local_para_guardar_copia>
Este comando muestra el contenido del directorio local `<ruta_local_para_guardar_copia>`, lo que debería mostrar el archivo `<nombre_del_volumen>.tar.gz`.
Elimina el contenedor temporal que se creó en el primer paso.
bash
`docker rm <nombre_del_contenedor_temporal>
`

Este comando elimina el contenedor temporal que se creó en el primer paso.

Ahora tienes una copia de seguridad del volumen montado en el contenedor de Docker en un archivo `.tar.gz`. Para restaurar el volumen, puedes hacer lo contrario: crear un contenedor temporal y luego copiar el archivo `.tar.gz` al contenedor y extraerlo en el volumen montado.
# Crear un contenedor PHP, MariaDB con Adminer
A continuación se muestra cómo sería el archivo `docker-compose.yml` para crear el entorno de Apache 2, PHP 8, MariaDB 10 y Adminer:
```yaml
version: '3.9'

services:
  web:
    image: php:8-apache
    container_name: myapp-web
    ports:
      - "80:80"
    volumes:
      - ./app:/var/www/html/
      - ./logs/apache:/var/log/apache2
    depends_on:
      - db

  db:
    image: mariadb:10
    container_name: myapp-db
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: dev_user
      MYSQL_USER: dev_user
      MYSQL_PASSWORD: password
    volumes:
      - ./db:/var/lib/mysql
      - ./logs/mysql:/var/log/mysql

  adminer:
    image: adminer
    container_name: myapp-adminer
    ports:
      - "8080:8080"
    environment:
      ADMINER_DEFAULT_SERVER: db
      ADMINER_DEFAULT_USERNAME: dev_user
      ADMINER_DEFAULT_PASSWORD: password
```
En este archivo, creamos tres servicios:
El servicio `web` utiliza la imagen `php:8-apache` para crear un contenedor de Apache 2 con PHP 8 y el código de la aplicación. Además, se montan los volúmenes `./app` y `./logs/apache` para que los archivos de la aplicación y los archivos de registro se almacenen en el host.
El servicio `db` utiliza la imagen `mariadb:10` para crear un contenedor de MariaDB 10 para la base de datos. Se especifican las variables de entorno `MYSQL_ROOT_PASSWORD`, `MYSQL_DATABASE`, `MYSQL_USER` y `MYSQL_PASSWORD` para configurar la base de datos. También se montan los volúmenes `./db` y `./logs/mysql` para que los datos de la base de datos y los archivos de registro se almacenen en el host.
El servicio `adminer` utiliza la imagen `adminer`
para crear un contenedor de Adminer, una herramienta web para 
administrar bases de datos. Se especifican las variables de entorno `ADMINER_DEFAULT_SERVER`, `ADMINER_DEFAULT_USERNAME` y `ADMINER_DEFAULT_PASSWORD` para configurar la conexión a la base de datos.

Los valores de las variables de 
entorno que se han especificado son de ejemplo. Si los nombres de 
usuario, contraseñas o nombres de base de datos son diferentes, deben 
ser cambiados para que coincidan con las necesidades del proyecto.
