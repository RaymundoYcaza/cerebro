---
in:
  - "[[Nextcloud]]"
---



## Checklist reconstrucción de contenedor
Instalar el módulo *smbclient* para conectarse con el NAS
#### PHP Module smbclient
`apt install smbclient libsmbclient-dev` `pecl install smbclient` `docker-php-ext-enable smbclient`
## Configurar el cron en NextCloud
Verifica que el paquete `cron` está instalado en tu contenedor Docker.
Para instalarlo, puedes ejecutar el siguiente comando dentro de tu contenedor:
```
apt-get update && apt-get install cron -y
```
Una vez que hayas instalado `cron`, deberías poder usar el comando `crontab -e` para editar el archivo crontab.
Sin embargo, ten en cuenta que los cambios realizados dentro del contenedor se perderán cuando el contenedor se reinicie, a menos que hayas creado un Dockerfile personalizado que instale `cron` durante la construcción del contenedor.
Para configurar el cron en tu contenedor Docker de Nextcloud para que ejecute el `cron.php` de Nextcloud cada 5 minutos, puedes seguir estos pasos:
Primero, necesitas acceder al contenedor de Docker. Puedes hacerlo con el siguiente comando:
```
docker exec -it <container_id> bash
```
En este comando, `<container_id>` debe ser reemplazado por el ID de tu contenedor de Nextcloud.
Una vez dentro del contenedor, abre el archivo crontab con el siguiente comando:
```
crontab -u www-data -e
```
Agrega la siguiente línea al final del archivo:
```
*/5 * * * * php -f /var/www/html/cron.php
```
Verifica que el trabajo ha sido programado
```
crontab -u www-data -l
```
Debería retornar:
```
*/5  *  *  *  * php -f /var/www/nextcloud/cron.php
```
Esta línea configura el cron para ejecutar el archivo `cron.php` cada 5 minutos. `/var/www/html/cron.php` es la ruta típica al archivo `cron.php` en una instalación de Nextcloud, pero puede variar dependiendo de tu configuración.
Guarda el archivo y cierra el editor de texto.
Finalmente, sal del contenedor de Docker con el comando `exit`.
## Un módulo no está activo en la instalación con docker
#### PHP Module bz2
`docker-php-ext-install bz2`
#### PHP Module imap
`apt install libc-client-dev libkrb5-dev` `docker-php-ext-configure imap --with-kerberos --with-imap-ssl` `docker-php-ext-install imap`
#### PHP Module gmp
`apt install libgmp3-dev` `docker-php-ext-install gmp`
#### PHP Module smbclient
`apt install smbclient libsmbclient-dev` `pecl install smbclient` `docker-php-ext-enable smbclient`
#### ffmpeg
`apt install ffmpeg`
#### imagemagick SVG support
`apt install libmagickcore-6.q16-6-extra`
#### LibreOffice
`apt install libreoffice`
#### CRON via supervisor
`apt install supervisor` `mkdir /var/log/supervisord /var/run/supervisord`
The following Dockerfile commands are also necessary for a sucessfull cron installation:
`COPY supervisord.conf /etc/supervisor/supervisord.conf` `CMD ["/usr/bin/supervisord"]`
## Usando una carpeta en el host para 'External Storage', opción 'Local'
**Caso de uso**: Se requiere crear un directorio en `/mnt/nextcloud_files/inorizonti` y almacenar allí los archivos de NextCloud, que *se encuentra en un contenedor Docker*,  para usarlo como fuente de almacenamiento 'Externo', de manera que permita al mismo tiempo mapearlo como un disco de red.
Si tu Nextcloud está ejecutándose en un contenedor y tu disco duro está conectado al host, necesitarás configurar el montaje de volúmenes para que el contenedor pueda acceder al directorio en el host.
Primero, asegúrate de que el directorio `/mnt/nexcloud_files/inorizonti` exista en el host. Si no existe, puedes crearlo con el comando `mkdir -p /mnt/nexcloud_files/inorizonti`.
Cuando ejecutes tu contenedor de Nextcloud, necesitarás definir el montaje del volumen directamente en el archivo de configuración.
```yml
version: '3'
services:
  nextcloud:
    image: nextcloud
    volumes:
      - /mnt/nexcloud_files/inorizonti:/var/www/html/data/inorizonti
```
En este archivo de configuración, `/mnt/nexcloud_files/inorizonti` es la ruta del directorio en el host y `/var/www/html/data/inorizonti` es la ruta donde se montará el directorio en el contenedor.
Después de guardar estos cambios en tu archivo `docker-compose.yml`, puedes ejecutar `docker-compose up -d` para iniciar tu contenedor de Nextcloud con el nuevo volumen montado.
Asignar los permisos necesarios
Para asignar los permisos adecuados al directorio `/mnt/nexcloud_files/inorizonti`, puedes usar el comando `chown` para cambiar el propietario del directorio y el comando `chmod` para cambiar los permisos del directorio.
Primero, necesitas saber qué usuario está ejecutando el servidor web dentro del contenedor de Nextcloud. Por lo general, este usuario es `www-data`, pero puede variar dependiendo de tu configuración.
Luego, puedes cambiar el propietario del directorio al usuario del servidor web con el siguiente comando:
```
sudo chown -R www-data:www-data /mnt/nexcloud_files/inorizonti
```
Después, puedes cambiar los permisos del directorio para que el usuario del servidor web tenga acceso de lectura, escritura y ejecución al directorio con el siguiente comando:
```
sudo chmod -R 755 /mnt/nexcloud_files/inorizonti
```
Ten encuenta que estos comandos deben ejecutarse en el host, no dentro del contenedor.
Además, debes agregar al usuario seleccionado, en este ejemplo, `Inorizonti` al grupo www-data para que pueda conectarse a la carpeta.
Agrega al usuario `inorizonti` al grupo `www-data` con el siguiente comando:
```
sudo usermod -a -G www-data inorizonti
```
Cambia el grupo del directorio `/mnt/nextcloud_files` a `www-data` con el siguiente comando:
```
sudo chgrp -R www-data /mnt/nextcloud_files
```
Cambia los permisos del directorio para que el grupo tenga acceso de lectura, escritura y ejecución al directorio con el siguiente comando:
```
sudo chmod -R 775 /mnt/nextcloud_files
```
Esto debería permitir que tanto Nextcloud (ejecutándose como `www-data`) como el usuario `inorizonti` tengan acceso al directorio `/mnt/nextcloud_files`.
Configurar `External Storage`
Ve a **Settings** > **Administration** > **External Storages**.
Haz clic en el botón **Add storage** y selecciona **Local** en el menú desplegable.
En el campo **Folder name**, introduce `Inorizonti`.
En el campo **Configuration**, introduce la ruta del directorio dentro del contenedor, en este caso, `/var/www/html/data/inorizonti`.
En **Available for**, puedes especificar los usuarios de Nextcloud que tendrán acceso a este almacenamiento. Si dejas este campo en blanco, el almacenamiento estará disponible para todos los usuarios.
Finalmente, haz clic en el icono de verificación para guardar la configuración.
Mapear el disco en red
Antes de empezar, asegúrate de que está creado el usuario que tendrá acceso al disco en red, si no lo está, créalo.
Para crear un usuario llamado `inorizonti` que solo pueda conectarse a la carpeta `/mnt/nextcloud_files`, puedes seguir estos pasos:
Primero, crea el usuario `inorizonti` con el siguiente comando:
```
sudo adduser inorizonti
```
Este comando te pedirá que ingreses una contraseña para el nuevo usuario y algunos detalles adicionales.
Luego, cambia el propietario del directorio `/mnt/nextcloud_files` al usuario `inorizonti` con el siguiente comando:
```
sudo chown -R inorizonti:inorizonti /mnt/nextcloud_files
```
Para mapear `/mnt/nextcloud_files/` como una unidad de red en Windows, puedes usar el protocolo SMB (Server Message Block). Aquí te dejo los pasos:
Primero, necesitas instalar el servidor SMB en tu máquina Ubuntu. Puedes hacerlo con el siguiente comando:
```
sudo apt-get update
sudo apt-get install samba
```
Luego, debes agregar una nueva entrada para tu directorio en el archivo de configuración de Samba. Puedes hacerlo con un editor de texto como `nano` o `vi`. Aquí está el comando para abrir el archivo con `nano`:
```
sudo nano /etc/samba/smb.conf
```
Agrega la siguiente entrada al final del archivo:
```
[nextcloud_files]
   path = /mnt/nextcloud_files
   available = yes
   valid users = inorizonti
   read only = no
   browsable = yes
   public = yes
   writable = yes
```
Guarda el archivo y cierra el editor de texto.
Reinicia el servicio Samba para que los cambios surtan efecto:
```
sudo service smbd restart
```
Establece una contraseña de Samba para el usuario `inorizonti` con el siguiente comando:
```
sudo smbpasswd -a inorizonti
```
Ahora, deberías poder mapear la unidad de red en Windows usando la dirección IP de tu máquina Ubuntu y el nombre de la carpeta compartida (`nextcloud_files`).
**Observación**: Cuando guardas un archivo en una carpeta externa configurada en Nextcloud, Nextcloud también registra la información del archivo en su base de datos. Esto incluye metadatos como el nombre del archivo, la ubicación, el tamaño, la fecha de la última modificación y la propiedad. Sin embargo, Nextcloud no realiza un seguimiento automático de los cambios realizados en el almacenamiento externo fuera de Nextcloud. Por lo tanto, si agregas, modificas o eliminas archivos directamente en el directorio `/mnt/nextcloud_files` en el sistema de archivos, Nextcloud no se dará cuenta de estos cambios de inmediato.
Para actualizar la vista de Nextcloud de la carpeta externa, puedes usar el comando `occ files:scan` en la línea de comandos para escanear el almacenamiento externo en busca de cambios. Aquí está el comando completo:
```
sudo -u www-data php /path/to/nextcloud/occ files:scan --all
```
En este comando, `/path/to/nextcloud/` debe ser reemplazado por la ruta a tu instalación de Nextcloud.
## Hacer que Nextcloud detecte cambios en una carpeta externa
Cuando se agregan o modifican archivos, sobre todo si son muchos, en una carpeta externa, NextCloud necesita ejecutar un escaneo.
**Observación**: Cuando guardas un archivo en una carpeta externa configurada en Nextcloud, Nextcloud también registra la información del archivo en su base de datos. Esto incluye metadatos como el nombre del archivo, la ubicación, el tamaño, la fecha de la última modificación y la propiedad. Sin embargo, Nextcloud no realiza un seguimiento automático de los cambios realizados en el almacenamiento externo fuera de Nextcloud. Por lo tanto, si agregas, modificas o eliminas archivos directamente en el directorio `/mnt/nextcloud_files` en el sistema de archivos, Nextcloud no se dará cuenta de estos cambios de inmediato.
Para actualizar la vista de Nextcloud de la carpeta externa, puedes usar el comando `occ files:scan` en la línea de comandos para escanear el almacenamiento externo en busca de cambios. Aquí está el comando completo:
```
sudo -u www-data php /path/to/nextcloud/occ files:scan --all
```
En este comando, `/path/to/nextcloud/` debe ser reemplazado por la ruta a tu instalación de Nextcloud.
## Configurar el cron en NextCloud
Verifica que el paquete `cron` está instalado en tu contenedor Docker.
Para instalarlo, puedes ejecutar el siguiente comando dentro de tu contenedor:
```
apt-get update && apt-get install cron -y
```
Una vez que hayas instalado `cron`, deberías poder usar el comando `crontab -e` para editar el archivo crontab.
Sin embargo, ten en cuenta que los cambios realizados dentro del contenedor se perderán cuando el contenedor se reinicie, a menos que hayas creado un Dockerfile personalizado que instale `cron` durante la construcción del contenedor.
Para configurar el cron en tu contenedor Docker de Nextcloud para que ejecute el `cron.php` de Nextcloud cada 5 minutos, puedes seguir estos pasos:
Primero, necesitas acceder al contenedor de Docker. Puedes hacerlo con el siguiente comando:
```
docker exec -it <container_id> bash
```
En este comando, `<container_id>` debe ser reemplazado por el ID de tu contenedor de Nextcloud.
Una vez dentro del contenedor, abre el archivo crontab con el siguiente comando:
```
crontab -u www-data -e
```
Agrega la siguiente línea al final del archivo:
```
*/5 * * * * php -f /var/www/html/cron.php
```
Verifica que el trabajo ha sido programado
```
crontab -u www-data -l
```
Debería retornar:
```
*/5  *  *  *  * php -f /var/www/nextcloud/cron.php
```
Esta línea configura el cron para ejecutar el archivo `cron.php` cada 5 minutos. `/var/www/html/cron.php` es la ruta típica al archivo `cron.php` en una instalación de Nextcloud, pero puede variar dependiendo de tu configuración.
Guarda el archivo y cierra el editor de texto.
Finalmente, sal del contenedor de Docker con el comando `exit`.
## Resolver el problema con `/.well-known/caldav` y `/.well-known/carddav`
Para resolver el problema con las rutas `/.well-known/caldav` y `/.well-known/carddav` en Nginx Proxy Manager, puedes agregar las reglas de reescritura directamente en la interfaz de Nginx Proxy Manager.
Aquí te dejo los pasos:
Abre Nginx Proxy Manager y ve a la configuración de tu proxy host.
Ve a la pestaña “Advanced”.
En el cuadro “Custom Nginx Configuration”, agrega las siguientes líneas:
```
**location** = /.well-known/carddav {
  return 301 $scheme://$host/remote.php/dav;
}
**location** = /.well-known/caldav {
  return 301 $scheme://$host/remote.php/dav;
}
```
Haz clic en “Save” para guardar tus cambios.
Estas reglas redirigen las solicitudes a `/.well-known/carddav` y `/.well-known/caldav` a `/remote.php/dav`, que es el punto de entrada para CalDAV y CardDAV en Nextcloud.
