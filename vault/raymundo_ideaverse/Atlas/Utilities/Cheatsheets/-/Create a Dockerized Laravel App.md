---
in:
  - "[[Cheat Sheet Laravel]]"
created: 2024-08-23
---



### Crear la aplicación
```
docker run --rm -v /mnt/c/Users/raymundo/Documents/_desarrollo/_Bisstox/_containers/fintra/:/app composer create-project --prefer-dist laravel/laravel /app
```

### Organizar los proyectos dentro de una carpeta llamada 'src'

![[0_USZRHfSbnosh8zwD.webp]]

### Crear un archivo docker compose `docker-compose.yml` con el siguiente contenido

```yaml
version: '3.8'  
  
  
services:  
  # Application Service  
  app:  
    container_name: blog  
    build:  
      context: ./php  
      dockerfile: Dockerfile  
    volumes:  
      - ./src:/var/www  
    ports:  
      - "9000:9000"  
    working_dir: /var/www  
    depends_on:  
      - db  
  
  
  # Database Service  
  db:  
    image: postgres  
    container_name: postgres  
    volumes:  
      - ./postgresql/data:/var/lib/postgresql/data  
    ports:  
      - "5432:5432"  
    environment:  
      POSTGRES_DB: blog  
      POSTGRES_USER: root  
      POSTGRES_PASSWORD: password  
  
  
  # Web Server Service  
  nginx:  
    image: nginx:alpine  
    container_name: nginx  
    ports:  
      - "8081:80"  
    volumes:  
      - ./src:/var/www  
      - ./nginx/conf.d/:/etc/nginx/conf.d/  
    depends_on:  
      - app  
      - db  
  
  
  # pgAdmin Service  
  pgadmin:  
    image: dpage/pgadmin4  
    container_name: pgAdmin  
    ports:  
      - "5050:80"  
    depends_on:  
      - db  
    environment:  
      PGADMIN_DEFAULT_EMAIL: prasunamudawari@gmail.com  
      PGADMIN_DEFAULT_PASSWORD: password
```

### Crear el archivo de configuración Nginx: Crear una carpeta llamada nginx en la ruta del proyecto y dentro, crear un archivo llamado `default.conf` con la configuración de Nginx

![[0_jyIO848YDTFenEn5.webp]]

```
server {  
  listen 80;  
  index index.php index.htm index.html;  
  error_log /var/log/nginx/error.log;  
  access_log /var/log/nginx/access.log;  
  server_name localhost;  
  root /var/www/public;  
  
  
  location / {  
      try_files $uri $uri/ /index.php?$query_string;  
  }  
  
  
  location /index.php {  
      try_files $uri = 404;  
      fastcgi_split_path_info ^(.+\.php)(/.+)$;  
      fastcgi_pass app:9000;  
      fastcgi_index index.php;  
      include fastcgi_params;  
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;  
      fastcgi_param PATH_INFO $fastcgi_path_info;  
  
  
  }  
}
```

### Crear un archivo Dockerfile para PHP: dentro de una carpeta llamada `php` crear un archivo llamado `Dockerfile` con el siguiente contenido

![[0_HOmiRGh-GwNB-WF--1.webp]]

```Dockerfile
FROM php:8.2.11-fpm  
  
  
# Install Composer  
RUN echo "Install COMPOSER"  
RUN cd /tmp \  
    && curl -sS https://getcomposer.org/installer -o composer-setup.php \  
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
    && rm composer-setup.php  
  
  
# Install required PHP extensions  
RUN docker-php-ext-install pdo pdo_mysql  
  
  
# Update package manager and install useful tools  
RUN apt-get update && apt-get -y install apt-utils nano wget dialog vim  
  
  
# Install important libraries  
RUN echo "Install important libraries"  
RUN apt-get -y install --fix-missing \  
    apt-utils \  
    build-essential \  
    git \  
    curl \  
    libcurl4 \  
    libcurl4-openssl-dev \  
    zlib1g-dev \  
    libzip-dev \  
    zip \  
    libbz2-dev \  
    locales \  
    libmcrypt-dev \  
    libicu-dev \  
    libonig-dev \  
    libxml2-dev  
  
  
# Install Postgres PDO (adjust for Windows if needed)  
RUN apt-get install -y libpq-dev \  
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
    && docker-php-ext-install pdo pdo_pgsql pgsql  
  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
  
# Add any additional configurations or adjustments as needed  
  
  
# Set the working directory  
WORKDIR /var/www  
  
  
# Expose the port  
EXPOSE 9000  
  
  
# Define the entry point  
CMD ["php-fpm"]
```

### Compilar y ejecutar los contenedores docker, ejecutnado los siguientes comandos

```
docker-compose build  
docker-compose up -d
```

### Revisar los contenedores para verificar que se encuentran en ejecución

```
docker ps
```

### Revisar el log `/var/www/storage/logs/laravel.log` dentro del contenedor de PHP

![[0_LamBygSIalBTHCCE.webp]]

