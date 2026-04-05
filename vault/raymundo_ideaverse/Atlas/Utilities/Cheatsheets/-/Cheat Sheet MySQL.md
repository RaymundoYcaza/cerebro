---
in:
  - "[[MySQL]]"
---


#### Basics Cheat Sheet
![[GHHB0f4WoAADjrc_1713073449685_0.jpg]]
## Crear una base de datos
Base de datos colación spanish
```sql
CREATE DATABASE fastapi
CHARACTER SET utf8mb4
COLLATE utf8mb4_spanish_ci;
```
Cómo ver todas las restricciones de una tabla (constraint foreign keys)
Ejecutar con la DB de interés seleccionada
```sql
SELECT 
  TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME, REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME
FROM
  INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
  REFERENCED_TABLE_SCHEMA = (SELECT DATABASE()) AND
  REFERENCED_TABLE_NAME = 'ventas_clientes'
```
Cómo eliminar una restricción (constraint foreign key) de una tabla
```sql
ALTER TABLE finanzas_inv DROP FOREIGN KEY fk_ventas_cli_finanzas_i_qokg7p1ll_;

```
## Crear un usuario de base de datos
Usuario developer con acceso completo a la base de datos **fastapi** sin acceso remoto
```sql
CREATE USER 'developer'@'localhost' IDENTIFIED BY 'developer';

GRANT ALL PRIVILEGES ON fastapi.* TO 'developer'@'localhost';

FLUSH PRIVILEGES;
```
Usuario developer con acceso completo a la bse de datos **fastapi** con acceso remoto
```sql
CREATE USER 'developer'@'%' IDENTIFIED BY 'developer';

GRANT ALL PRIVILEGES ON fastapi.* TO 'developer'@'%';

FLUSH PRIVILEGES;

```
Usuairo developer con acceso completo a todas las bases de datos con acceso remoto
```sql
CREATE USER 'developer'@'%' IDENTIFIED BY 'developer';

GRANT ALL PRIVILEGES ON *.* TO 'developer'@'%';

FLUSH PRIVILEGES;

```
## Alterar un usuario de base de datos
Alterar al usuario developer que tiene acceso local, para que tenga acceso remoto
```sql
ALTER USER 'developer'@'localhost' IDENTIFIED WITH mysql_native_password BY 'developer';
RENAME USER 'developer'@'localhost' TO 'developer'@'%';
GRANT ALL PRIVILEGES ON fastapi.* TO 'developer'@'%';
FLUSH PRIVILEGES;
```
## Editando usuarios
### Cómo crear usuarios
```
CREATE USER 'wordpressuser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
```
### Cómo otorgar todos los privilegios en una base de datos en MySQL
```
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'%';	
```
Como paso final, se debe ejecutar:
```
FLUSH PRIVILEGES;
```
Tomado de: [https://chartio.com/resources/tutorials/how-to-grant-all-privileges-on-a-database-in-mysql/](https://chartio.com/resources/tutorials/how-to-grant-all-privileges-on-a-database-in-mysql/)
### Cómo mostrar las bases de datos
```
sudo mysql -u root -p -e "show databases;"
```
### Cómo ver las tablas de una base de datos
```
sudo mysql -u root -p -e "show tables in [nombre de la base de datos];"
```
### Cómo crear una base de datos
```
sudo mysql -u root -p -e "create database [nombre de la base de datos];"
```
### Cómo mostrar los usuarios
```
sudo mysql -u root -p -e "select User from mysql.user;"
```
### Cómo ver los detalles de un usuario
```
mysql -u root -p -e "show grants for [nombre del usuario]@localhost;"
```
### Cómo dar acceso a un usuario a todas las tablas que comiencen por «pruebas_»
```
sudo mysql -u root -p
```



```
CREATE USER 'usuario_pruebas'@'localhost' IDENTIFIED BY 'contraseña_pruebas';
```
```
GRANT ALL PRIVILEGES ON `pruebas_%`.* TO 'usuario_pruebas'@'localhost';
```
Verificar

```
SHOW GRANTS FOR 'usuario_pruebas'@'localhost';
```
# Cómo obtener la versión de MySQL / Maria DB con una consulta de base de datos
```sql
SHOW VARIABLES LIKE 'version';
```
