---
in:
  - "[[WordPress]]"
---




# Modelo de datos de WordPress
![image.png](../assets/image_1707448156892_0.png)
# Páginas sobre WordPress
https://decodecms.com/
# Crear tablas en WordPress
Referencias:
https://wpmudev.com/blog/creating-database-tables-for-plugins/
https://www.aeeiee.com/blog/2021/03/24/how-to-programmatically-insert-a-new-table-into-a-database-in-wordpress/
https://codex.wordpress.org/Creating_Tables_with_Plugins
# ¿Cómo obtener un listado de los usuarios de WP usando WPCli?
Para obtener un listado de usuarios en WordPress utilizando WP-CLI, puedes utilizar el comando `wp user list`. Este comando devolverá una tabla que muestra la lista de usuarios registrados en tu sitio web.
Para ejecutar este comando, abre una 
terminal y navega hasta el directorio raíz de tu sitio web WordPress. A 
continuación, escribe el siguiente comando:
```
wp user list
```
Esto mostrará una lista de usuarios con su nombre de usuario, correo electrónico y nombre de visualización.
# ¿Cómo cambiar la contraseña de un usuario usando WP-CLI?
Para cambiar la contraseña de un usuario en WordPress utilizando WP-CLI, puedes utilizar el comando `wp user update`. Este comando te permite actualizar la información del usuario, incluyendo la contraseña.
Para ejecutar este comando, abre una terminal y navega hasta el directorio raíz de tu sitio web WordPress. A continuación, escribe el siguiente comando:
```bash
wp user update NOMBRE_USUARIO --user_pass=NUEVA_CONTRASEÑA
```
Reemplaza `NOMBRE_USUARIO` por el nombre de usuario del usuario cuya contraseña deseas cambiar y `NUEVA_CONTRASEÑA` por la nueva contraseña que deseas establecer.
Por ejemplo, si deseas cambiar la contraseña del usuario "juan@ejemplo.com" a "NuevaContraseña123", el comando sería:
`wp user update juan@ejemplo.com --user_pass=NuevaContraseña123`
Este comando actualizará la contraseña del usuario "Juan" a "NuevaContraseña123". Asegúrate de que la contraseña sea segura y cumpla con los requisitos de tu sitio web para las contraseñas de usuario.
Si deseas obtener más información sobre cómo utilizar WP-CLI para administrar usuarios en WordPress, puedes consultar su documentación en línea.
# Rest API WordPress
## Aspectos básicos REST API WP
Para que WP me incluya los datos relacionados, debo incluir el parámetro _embed=true en la solicitud.
Para acceder a los datos relacionados por medio del URL, acceder al objetio embedded y luego a los datos relacionados, por ejemplo:
```
_embedded[wp:featuredmedia][0].media_details.sizes.thumbnail.source_url

_embedded[wp:featuredmedia][0].media_details.sizes.full.source_url
```
Para seleccionar solamente los campos deseados, se especifica en el parametro _fields
Ejemplo: _fields=id,title,description
## Crear un nuevo campo en la REST API para accederlo directamente en lugar de usar _embed
Usar _embed es muy útil, pero puede resultar lento y considerando que el objetivo de JSON es ser tan rápido como sea posible, es mejor buscar una alternativa.
El siguiente código puede ser utilizado en un plugin (o functions.php) para agregar un campo rest que busque el URL de la imagen por medio de su ID (el id es el que aparece en la respuesta REST original.
```php
add_action( 'rest_api_init', 'add_thumbnail_to_JSON' );
function add_thumbnail_to_JSON() {
//Add featured image
register_rest_field( 
    'post', // Where to add the field (Here, blog posts. Could be an array)
    'featured_image_src', // Name of new field (You can call this anything)
    array(
        'get_callback'    => 'get_image_src',
        'update_callback' => null,
        'schema'          => null,
         )
    );
}

function get_image_src( $object, $field_name, $request ) {
  $feat_img_array = wp_get_attachment_image_src(
    $object['featured_media'], // Image attachment ID
    'thumbnail',  // Size.  Ex. "thumbnail", "large", "full", etc..
    true // Whether the image should be treated as an icon.
  );
  return $feat_img_array[0];
}
```
Ahora, en la respuesta JSON, puedo ver un nuevo campo llamado "featured_image_src" conteniendo el URL
Para el aula virtual, utilicé un campo adicional:
```php
//Add course category
register_rest_field( 
    'sfwd-courses', // Where to add the field (Here, blog posts. Could be an array)
    'course_category', // Name of new field (You can call this anything)
    array(
        'get_callback'    => 'get_course_category_name',
        'update_callback' => null,
        'schema'          => null,
         )
    );
```
El que se apoya en la siguiente función, invocada en el get-callback:
```php
function get_course_category_name( $object, $field_name, $request ) {
	$category = get_term_by(
		'id', 
		$object['ld_course_category'][0], 
		'ld_course_category'
	);
	return $category;
}
```
