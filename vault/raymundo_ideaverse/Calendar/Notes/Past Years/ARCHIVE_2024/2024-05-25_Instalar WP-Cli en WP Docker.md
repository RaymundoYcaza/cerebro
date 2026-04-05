---
created: 2024-05-25 
---



### Usando docker-compose
Si se ha instalado WP con 
docker-compose, y se asume que el servicio wp se llama 'wordpress',se 
puede ingresar al contenedor directamente desde el directorio en el que 
se encuentra el archivo docker-compose.yaml con el siguiente comando:\
`docker-compose wordpress /bin/bash`
Dirigirse a un directorio adecuado y descargar el archivo
`curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar`
O descargarlo del repositorio local
`curl -O http://192.168.0.16/apps/filemanager/Sistemas/WordPress/wp-cli.phar`
A continuación, comprueba el archivo Phar para verificar que está funcionando:
`php wp-cli.phar --info`
Para usar WP-CLI desde la línea de comandos tecleando `wp`, haz que el archivo sea ejecutable y muévelo a algún lugar de tu `PATH`. Por ejemplo:
Si WP-CLI se instaló correctamente, deberías ver algo como esto cuando ejecutas `wp --info`:
```bash
$ wp --info
OS:     Linux 4.19.128-microsoft-standard #1 SMP Tue Jun 23 12:58:10 UTC 2020 x86_64
Shell:  /usr/bin/zsh
PHP binary:     /usr/bin/php
PHP version:    8.0.5
php.ini used:   /etc/php/8.0/cli/php.ini
MySQL binary:   /usr/bin/mysql
MySQL version:  mysql  Ver 8.0.23-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
SQL modes:
WP-CLI root dir:        /home/wp-cli/
WP-CLI vendor dir:      /home/wp-cli/vendor
WP_CLI phar path:
WP-CLI packages dir:    /home/wp-cli/.wp-cli/packages/
WP-CLI global config:
WP-CLI project config:  /home/wp-cli/wp-cli.yml
WP-CLI version: 2.5.0
```
### Actualización
Puedes actualizar WP-CLI con `wp cli update` ([doc](https://developer.wordpress.org/cli/commands/cli/update/)), o repitiendo los pasos de instalación.

Si WP-CLI es propiedad de root u otro usuario del sistema, necesitarás ejecutar `sudo wp cli update`.

¿Quieres vivir la vida al límite? Ejecuta `wp cli update --nightly`
para usar la última compilación nocturna (nightly build) de WP-CLI. Una
compilación nocturna es más o menos lo suficientemente estable como 
para que puedas utilizarla en tu entorno de desarrollo, y siempre 
incluye las últimas y mejores características de WP-CLI.
### Autocompletar con el tabulador
WP-CLI también viene con un scripts para autocompletar con el tabulador para Bash y ZSH. Tan sólo descarga [wp-completion.bash](https://raw.githubusercontent.com/wp-cli/wp-cli/v2.3.0/utils/wp-completion.bash) y usa el comando `source` desde `~/.bash_profile`:
`source /FULL/PATH/TO/wp-completion.bash`
No te olvides de ejecutar `source ~/.bash_profile` después.
Si usa la shell zsh, es posible que debas cargar e iniciar `bashcompinit` antes de usar el comando `source`. Pon lo siguiente en tu `.zshrc`:
```bash
autoload bashcompinit
bashcompinit
source /RUTA/COMPLETA/HASTA/wp-completion.bash
```
No te olvides de ejecutar `source ~/.bash_profile` después.
Si usa la shell zsh, es posible que debas cargar e iniciar `bashcompinit` antes de usar el comando `source`. Pon lo siguiente en tu `.zshrc`:
```bash
autoload bashcompinit
bashcompinit
source /RUTA/COMPLETA/HASTA/wp-completion.bash
```
