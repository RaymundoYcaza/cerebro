---
up:
  - "[[Codeigniter 3 Snippets MOC]]"
related: []
created: 2025-05-09
---


```php
<?php defined('BASEPATH') or exit('No direct script access allowed');

  

/**

 * Controlador de prueba para verificar la función is_admin() de ion_auth

 */

class TestAdmin extends CI_Controller

{

    public function __construct()

    {

        parent::__construct();

        $this->load->database();

        $this->load->library(['ion_auth']);

        $this->load->helper(['url', 'language']);

    }

  

    /**

     * Prueba para verificar si el usuario actual es admin

     */

    public function index()

    {

        echo "<h1>Prueba de Función is_admin()</h1>";

  

        // Verificar si el usuario está logueado

        if ($this->ion_auth->logged_in()) {

            echo "<p>Usuario está logueado: <strong>SÍ</strong></p>";

            // Obtener información del usuario

            $user = $this->ion_auth->user()->row();

            echo "<p>ID de usuario: <strong>" . $user->id . "</strong></p>";

            echo "<p>Email: <strong>" . $user->email . "</strong></p>";

            // Verificar si es administrador

            $is_admin = $this->ion_auth->is_admin();

            echo "<p>¿Es administrador?: <strong>" . ($is_admin ? 'SÍ' : 'NO') . "</strong></p>";

            // Mostrar grupos del usuario

            $user_groups = $this->ion_auth->get_users_groups()->result();

            echo "<h2>Grupos del Usuario:</h2>";

            if (empty($user_groups)) {

                echo "<p><strong>No se encontraron grupos para este usuario</strong></p>";

            } else {

                echo "<ul>";

                foreach ($user_groups as $group) {

                    echo "<li>ID: <strong>" . $group->id . "</strong>, Nombre: <strong>" . $group->name . "</strong>, Descripción: <strong>" . $group->description . "</strong></li>";

                }

                echo "</ul>";

            }

            // Inspeccionar todos los grupos disponibles

            $all_groups = $this->ion_auth->groups()->result();

            echo "<h2>Todos los Grupos Disponibles:</h2>";

            echo "<ul>";

            foreach ($all_groups as $group) {

                echo "<li>ID: <strong>" . $group->id . "</strong>, Nombre: <strong>" . $group->name . "</strong>, Descripción: <strong>" . $group->description . "</strong></li>";

            }

            echo "</ul>";

            // Ver código fuente de la función is_admin

            echo "<h2>Explicación de cómo funciona is_admin():</h2>";

            echo "<p>La función is_admin() verifica si el usuario pertenece al grupo definido como 'admin_group' en la configuración de ion_auth.</p>";

            // Verificar cuál es el grupo de administrador definido en la configuración

            $admin_group = $this->config->item('admin_group', 'ion_auth');

            echo "<p>Grupo de administrador definido en la configuración: <strong>" . $admin_group . "</strong></p>";

            // Verificar manualmente si el usuario pertenece al grupo admin

            $is_in_admin_group = $this->ion_auth->in_group($admin_group);

            echo "<p>Verificación manual: ¿Pertenece al grupo '{$admin_group}'?: <strong>" . ($is_in_admin_group ? 'SÍ' : 'NO') . "</strong></p>";

            // Depurar internamente la función is_admin

            echo "<h2>Depuración de is_admin():</h2>";

            echo "<pre>";

            var_dump([

                'admin_group' => $admin_group,

                'is_admin' => $is_admin,

                'manual_check' => $is_in_admin_group,

                'user_id' => $user->id,

                'user_groups' => $user_groups

            ]);

            echo "</pre>";

        } else {

            echo "<p>Usuario no está logueado. Debe iniciar sesión primero.</p>";

            echo "<p><a href='" . site_url('auth/login') . "'>Ir al login</a></p>";

        }

    }

}
```