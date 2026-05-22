---
up:
  - "[[Codeigniter 3 Gestión de Datos MOC]]"
related:
  - "[[Codeigniter 3 MOC]]"
created: 2025-05-07
acr: true
---


## Configurar las migraciones
Para empezar con las migraciones en un proyecto Code Igniter 3, primer hay que habilitarlas en el archivo de configuraciones:

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$config['migration_enabled'] = TRUE;
$config['migration_type'] = 'timestamp'; // Recomendado para proyectos existentes
$config['migration_table'] = 'migrations'; // Tabla que registrará las migraciones ejecutadas
$config['migration_auto_latest'] = FALSE;
$config['migration_version'] = 0; // Se actualizará automáticamente
$config['migration_path'] = APPPATH . 'migrations/';
```

Luego, hay que crear el directorio `migrations` en la raíz del proyecto:

```bash
application/
  migrations/           // Crear este directorio
```

A continuación se crea un controlador para gestionar las migraciones:

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

/**
 * Migrations Controller
 * 
 * Controlador para gestionar las migraciones de la base de datos
 *
 * @package     Lifprodecsa
 * @category    Controllers
 */
class Migrations extends CI_Controller {

    /**
     * Constructor del controlador
     */
    public function __construct() {
        parent::__construct();
        // Verificar si el usuario es administrador
        if (!$this->ion_auth->is_admin()) {
            show_error('Solo los administradores pueden ejecutar migraciones.');
        }
        $this->load->library('migration');
    }

    /**
     * Ejecuta la última migración disponible
     */
    public function index() {
        if ($this->migration->current() === FALSE) {
            show_error($this->migration->error_string());
        } else {
            echo 'Migración completada exitosamente.';
        }
    }
    
    /**
     * Ejecuta una versión específica de migración
     *
     * @param int $version Número de versión a migrar
     */
    public function version($version) {
        if ($this->migration->version($version) === FALSE) {
            show_error($this->migration->error_string());
        } else {
            echo 'Migración a versión ' . $version . ' completada exitosamente.';
        }
    }
    
    /**
     * Revierte todas las migraciones
     */
    public function reset() {
        if ($this->migration->current(0) === FALSE) {
            show_error($this->migration->error_string());
        } else {
            echo 'Todas las migraciones han sido revertidas.';
        }
    }
}
```

Crear la tabla de migraciones en la base de datos

```sql
CREATE TABLE `migrations` (
  `version` BIGINT(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

```

> [!warning] En migraciones tipo `timestamp`, **CodeIgniter no inserta una nueva fila en la tabla `migrations`, sino que actualiza una fila existente.**

Crear el primer registro manual mente:

```sql
INSERT INTO migrations (version) VALUES (0);
```

## Crear archivos de migraciones
Para nuevas tablas o modificaciones, se creará migraciones con timestamp (un número de 14 dígitos en formato YYYYMMDDHHMMSS),  por ejemplo,  `20250507120000_create_subtasks_log.php`. 
Es importante recordar que el nombre de clase de una migración debe comenzar con la palabra `Migration`, por ejemplo `Migration_Create_subtasks_log`.
El nombre del archivo, debe ser un timestamp, seguido de un subguión y el nombre de la clase, sin la palabra `Migration`, por ejemplo: `20250507140928_Create_subtasks_log.php`.
## Migración inicial

Migración inicial con una línea base existente, para representar el estado actual.

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Migration_Initial_schema extends CI_Migration {

    public function up() {
        // Como las tablas ya existen, el método up() no necesita crear nada
        // pero debes registrar esta migración para futuras modificaciones
        echo "Las tablas ya existen en la base de datos.";
    }

    public function down() {
        // No es recomendable eliminar todas las tablas en el método down()
        // para una migración inicial en un sistema existente
        echo "Método down() no implementado para la migración inicial.";
    }
}
```

## Crear una migración para una nueva tabla o modificación

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Migration_Crear_tabla_ejemplo extends CI_Migration {

    public function up() {
        $this->dbforge->add_field([
            'id' => [
                'type' => 'INT',
                'constraint' => 11,
                'unsigned' => TRUE,
                'auto_increment' => TRUE
            ],
            'nombre' => [
                'type' => 'VARCHAR',
                'constraint' => 100
            ],
            'descripcion' => [
                'type' => 'TEXT',
                'null' => TRUE
            ],
            'created_at' => [
                'type' => 'DATETIME',
                'null' => FALSE
            ],
            'updated_at' => [
                'type' => 'DATETIME',
                'null' => TRUE
            ]
        ]);
        $this->dbforge->add_key('id', TRUE);
        $this->dbforge->create_table('ejemplo', TRUE);
    }

    public function down() {
        $this->dbforge->drop_table('ejemplo', TRUE);
    }
}
```

## Migración para modificar una tabla existente

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Migration_Modificar_tabla_existente extends CI_Migration {

    public function up() {
        // Agregar un nuevo campo a una tabla existente
        $fields = [
            'nuevo_campo' => [
                'type' => 'VARCHAR',
                'constraint' => 50,
                'null' => TRUE,
                'after' => 'campo_existente'
            ]
        ];
        $this->dbforge->add_column('tabla_existente', $fields);
        
        // Modificar un campo existente
        $fields = [
            'campo_existente' => [
                'name' => 'campo_modificado',
                'type' => 'VARCHAR',
                'constraint' => 100
            ]
        ];
        $this->dbforge->modify_column('tabla_existente', $fields);
    }

    public function down() {
        // Revertir los cambios
        $this->dbforge->drop_column('tabla_existente', 'nuevo_campo');
        
        $fields = [
            'campo_modificado' => [
                'name' => 'campo_existente',
                'type' => 'VARCHAR',
                'constraint' => 50
            ]
        ];
        $this->dbforge->modify_column('tabla_existente', $fields);
    }
}
```

## Ejecutar las migraciones

Para ejecutar las migraciones, se puede acceder a:

- Para ejecutar hasta la última migración: `http://aplicacion.com/migrations`
- Para ejecutar hasta una versión específica: `http://aplicacion.com/migrations/version/20240501000100`
- Para revertir todas las migraciones: `http://aplicación.com/migrations/reset`

## Consideraciones adicionales

1. **Seguridad**: Limitar el acceso al controlador de migraciones solo para administradores.
2. **Respaldo**: Siempre realizar una copia de seguridad de la base de datos antes de ejecutar migraciones.
3. **Entorno de desarrollo**: Probar las migraciones en un entorno de desarrollo antes de aplicarlas en producción.
