---
up:
  - "[[Tecnología MOC]]"
related: 
created: 2025-05-20
---

# Recursos
## Estructura de archivos
```
laravel-dev/
├── docker/
│   └── nginx/
│       └── laravel.conf
├── src/
├── Dockerfile
├── docker-compose.yml
└── .env
```


## Archivo Dockerfile

```bash
FROM php:8.2-fpm

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    libpq-dev

# Instalar Node.js 20.x (LTS actual)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && corepack enable

# Instalar extensiones de PHP
RUN docker-php-ext-install pdo_pgsql mbstring exif pcntl bcmath gd

# Instalar Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html
RUN chown -R www-data:www-data /var/www/html
```


## Archivo docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - ./src:/var/www/html
    environment:
      - DB_CONNECTION=pgsql
      - DB_HOST=postgresql
      - DB_PORT=5432
      - DB_DATABASE=laravel
      - DB_USERNAME=laravel
      - DB_PASSWORD=secret
    networks:
      - laravel-network
    depends_on:
      - postgresql

  webserver:
    image: nginx:alpine
    ports:
      - "6005:80"
    volumes:
      - ./src:/var/www/html
      - ./docker/nginx/laravel.conf:/etc/nginx/conf.d/default.conf
    networks:
      - laravel-network
    depends_on:
      - app

  postgresql:
    image: postgres:15
    ports:
      - "6006:5432"
    environment:
      - POSTGRES_DB=laravel
      - POSTGRES_USER=laravel
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - laravel-network

volumes:
  postgres-data:

networks:
  laravel-network:
    driver: bridge
```

## Archivo laravel.conf

```
server {
    listen 80;
    server_name localhost;
    root /var/www/html/public;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";

    index index.php;

    charset utf-8;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass app:9000;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }
}
```

### Si la instalación se hace en un subdirectorio
```
server {
    listen 80;
    server_name localhost;
    root /var/www/html/bisstox-agricontrol/public;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";

    index index.php;

    charset utf-8;

    location /bisstox-agricontrol/ {
        try_files $uri $uri/ /bisstox-agricontrol/index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass app:9000;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }
}
```
## Archivo .env

```.env
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost:6005

DB_CONNECTION=pgsql
DB_HOST=postgresql
DB_PORT=5432
DB_DATABASE=laravel
DB_USERNAME=laravel
DB_PASSWORD=secret
```

### Si la instalación se realiza en un subdirectorio

```env
APP_URL=http://192.168.100.81:6010/bisstox-agricontrol
```
## Resumen
Esta configuración incluye:

- PHP 8.2 con extensiones necesarias para Laravel
- PostgreSQL 15 con persistencia de datos
- Nginx configurado para Laravel
- Variables de entorno preconfiguradas
- Red aislada entre los servicios
- Volúmenes para persistencia de código y base de datos
# Pasos para configurar

## Crear estructura de directorios
1. Crea la estructura de directorios en tu servidor Ubuntu:
```bash
mkdir -p laravel-dev/{docker/nginx,src}
```

2. Coloca los archivos en sus respectivas ubicaciones según la estructura mostrada
3. Desde el directorio raíz `laravel-dev`, ejecuta:
```bash
docker-compose up -d --build
```

# Crear un nuevo proyecto
1. Para crear un nuevo proyecto Laravel:
```bash
docker-compose exec app composer create-project laravel/laravel=12.0.7 .
```

2. Genera la clave de la aplicación:
```bash
docker-compose exec app php artisan key:generate
```

3. Establece los permisos correctos
```bash
docker-compose exec app chmod -R 775 storage
docker-compose exec app chmod -R 775 bootstrap/cache
```

**Para acceder desde tu laptop con Windows 10:**

1. Servidor web: `http://<ip-del-servidor>:6005`
    
2. PostgreSQL: `<ip-del-servidor>:6006`
    
    - Usuario: laravel
    - Contraseña: secret
    - Base de datos: laravel
        

**Configuración recomendada en VS Code:**

1. Instala la extensión "Remote - SSH"
2. Conéctate a tu servidor Ubuntu
3. Abre el directorio del proyecto
4. Instala las extensiones recomendadas para PHP y Laravel

# Resolución de problemas
## Error 500 por problemas de permisos
1. **Permisos insuficientes en el sistema de archivos** para el directorio `storage/framework/views`.
2. **El usuario que ejecuta el servidor web (por ejemplo, `www-data`, `apache`, `nginx`) no tiene permisos de escritura** en el directorio mencionado.
3. **El archivo Blade compilado no puede ser creado o sobrescrito** debido a restricciones de permisos.
4. **Configuración incorrecta de permisos o propiedad del directorio `storage` o `bootstrap/cache`**.
5. **Fallo en la compilación de vistas Blade** por no poder escribir archivos temporales.
6. **Errores en el manejo de excepciones de Laravel** al intentar renderizar una vista con errores.
7. **Posible corrupción o bloqueo del sistema de archivos** en el entorno de producción o desarrollo.

Este error ocurre por problemas de permisos en los directorios de almacenamiento de Laravel. 

Ejecuta estos comandos para corregir los permisos:
```bash
docker-compose exec app chown -R www-data:www-data /var/www/html/storage
docker-compose exec app chown -R www-data:www-data /var/www/html/bootstrap/cache
docker-compose exec app chmod -R 775 /var/www/html/storage
docker-compose exec app chmod -R 775 /var/www/html/bootstrap/cache
```

Si el problema persiste, limpia la caché de vistas:
```bash
docker-compose exec app php artisan view:clear
docker-compose exec app php artisan cache:clear
```

Verifica que los directorios existen y tienen la estructura correcta:
```bash
docker-compose exec app ls -la /var/www/html/bisstox-agricontrol/storage/framework/
```

Deberías ver estos subdirectorios:

- cache
- sessions
- testing
- views

Si faltan algunos directorios, créalos manualmente:
```bash
docker-compose exec app mkdir -p /var/www/html/bisstox-agricontrol/storage/framework/{cache,sessions,views}
docker-compose exec app mkdir -p /var/www/html/bisstox-agricontrol/storage/logs
```

Reinicia los servicios para asegurar que los cambios surtan efecto:
```bash
docker-compose down
docker-compose up -d
```

**Nota adicional:**  
Si estás usando bind mounts (volúmenes mapeados a tu sistema host), los permisos deben coincidir entre el host y el contenedor. En tu servidor Ubuntu, ejecuta:

```bash
sudo chown -R $USER:$USER ./bisstox-agricontrol/storage
sudo chmod -R 775 ./bisstox-agricontrol/storage
```
# Comandos útiles
Ejecutar migraciones
```bash
docker-compose exec app php artisan migrate
```

Limpiar la caché de vistas:
```bash
docker-compose exec app php artisan view:clear
docker-compose exec app php artisan cache:clear
```

Instalar dependencias:
```bash
docker-compose exec app composer install
```

Acceder a la consola PostgreSQL:
```bash
docker-compose exec postgresql psql -U laravel -d laravel
```

Listar el contenido de un directorio:
```bash
docker-compose exec app ls -la /var/www/html/bisstox-agricontrol
```

Revisar los logs de Nginx:
```bash
docker-compose logs webserver
```

Si necesitas mantener la URL sin el `/public`, asegúrate de que:

- El root en Nginx apunte al directorio `public`
- Los archivos de Laravel estén correctamente ubicados en `bisstox-agricontrol`

Instalar node en el contenedor:
```bash
docker-compose exec app bash -lc "\
  apt-get update && \
  apt-get install -y curl && \
  curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
  apt-get install -y nodejs npm && \
  cd /var/www/html/bisstox-agricontrol && \
  npm install && \
  npm run build \
"
```

# Agregar hojas de estilo personalizadas

Crear la nueva hoja en `resources/css/custom.css`
Importar en `resources/js/app.js`
```js
import '../css/custom.css';
```
Agregar a la plantilla `app.blade.php`
```php
@vite(['resources/js/app.js'])
```
Compilar en Vite
```bash
npx vite build
```
Copiar el archivo`manifest.json` desde `public/build/.vite` a `public/build`
Limpiar la caché de vistas
```php
php artisan view:clear
```
# Datos de prueba

## 150 usuarios de prueba

```SQL
-- 1. Verificar si el grupo "Usuarios" ya existe, si no, crearlo
DO $$
DECLARE
    grupo_id bigint;
    max_user_id bigint;
BEGIN
    -- Intentar obtener el ID del grupo existente
    SELECT id INTO grupo_id FROM sys_user_groups WHERE name = 'Usuarios';
    
    -- Si no existe, crearlo
    IF NOT FOUND THEN
        INSERT INTO sys_user_groups (name, description, created_at, updated_at)
        VALUES ('Usuarios', 'Grupo para usuarios estándar del sistema', NOW(), NOW())
        RETURNING id INTO grupo_id;
    END IF;
    
    -- 2. Obtener el máximo ID de usuario actual y resetear la secuencia
    SELECT COALESCE(MAX(id), 0) INTO max_user_id FROM sys_users;
    PERFORM setval('sys_users_id_seq', max_user_id + 1);
    
    -- 3. Insertar 150 usuarios y asignarlos al grupo
    FOR i IN 1..150 LOOP
        DECLARE
            user_id bigint;
            user_num bigint := max_user_id + i;
            user_email text := 'usuario' || user_num || '@ejemplo.com';
            user_name text := 'Usuario ' || user_num;
        BEGIN
            -- Insertar el usuario
            INSERT INTO sys_users (name, email, password, created_at, updated_at)
            VALUES (user_name, user_email, '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', NOW(), NOW())
            RETURNING id INTO user_id;
            
            -- Asignar el usuario al grupo
            INSERT INTO sys_user_group_user (sys_user_group_id, sys_user_id, created_at, updated_at)
            VALUES (grupo_id, user_id, NOW(), NOW());
        END;
    END LOOP;
END $$;

-- Verificación
SELECT COUNT(*) as total_usuarios FROM sys_users;
SELECT COUNT(*) as usuarios_en_grupo FROM sys_user_group_user WHERE sys_user_group_id = 
    (SELECT id FROM sys_user_groups WHERE name = 'Usuarios');
```

