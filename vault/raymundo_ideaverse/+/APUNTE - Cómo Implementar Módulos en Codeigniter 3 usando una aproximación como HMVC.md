---
up:
  - "[[Codeigniter 3 MOC]]"
related: []
created: 2025-05-11
---

En CodeIgniter 3, los módulos no son una característica nativa del framework, pero se pueden implementar usando aproximaciones como HMVC (Hierarchical Model-View-Controller) o estructuras modulares personalizadas. Aquí te explico cómo implementar tu módulo de Haciendas:

### Estructura Recomendada para el Módulo

```text
application/
├── modules/
│   └── Haciendas/
│       ├── config/          # Configuraciones específicas
│       ├── controllers/     # Controladores
│       ├── models/          # Modelos
│       ├── views/           # Vistas
│       ├── language/        # Traducciones
│       ├── libraries/       # Librerías propias
│       └── migrations/      # Migraciones de BD
```

### 1. Estructura de Archivos Detallada

Para tu módulo de Haciendas-Lotes-Módulos:

```text
modules/Haciendas/
├── controllers/
│   ├── Haciendas.php        # Controlador principal
│   ├── Lotes.php            # Controlador de lotes
│   └── Modulos.php          # Controlador de módulos
├── models/
│   ├── Hacienda_model.php
│   ├── Lote_model.php
│   └── Modulo_model.php
├── views/
│   ├── haciendas/
│   │   ├── listar.php
│   │   ├── crear.php
│   │   └── editar.php
│   ├── lotes/
│   │   ├── listar.php
│   │   └── gestion.php
│   └── modulos/
│       ├── listar.php
│       └── dashboard.php
├── config/
│   └── routes.php           # Rutas específicas del módulo
└── migrations/
    ├── 001_create_haciendas.php
    ├── 002_create_lotes.php
    └── 003_create_modulos.php
```

### 2. Configuración Inicial

**application/config/routes.php**

```php
$route['haciendas'] = 'haciendas/haciendas';
$route['haciendas/(:num)/lotes'] = 'haciendas/lotes/index/$1';
$route['haciendas/lotes/(:num)/modulos'] = 'haciendas/modulos/index/$1';
```

### 3. Ejemplo de Controlador

**modules/Haciendas/controllers/Haciendas.php**

```php
class Haciendas extends MY_Controller { // Hereda de tu controlador base
    public function __construct() {
        parent::__construct();
        $this->load->model('haciendas/Hacienda_model');
    }

    public function index() {
        $data['haciendas'] = $this->Hacienda_model->get_all();
        $this->template->render('haciendas/listar', $data); // Usando tu sistema de templates
    }

    public function crear() {
        if ($this->input->post()) {
            // Validación y guardado
        }
        $this->template->render('haciendas/crear');
    }
}
```

### 4. Modelo Relacional

**modules/Haciendas/models/Hacienda_model.php**

```php
class Hacienda_model extends CI_Model {
    public function get_all() {
        return $this->db->get('haciendas')->result();
    }

    public function get_with_lotes($id) {
        $this->db->select('*');
        $this->db->from('haciendas');
        $this->db->join('lotes', 'lotes.hacienda_id = haciendas.id');
        $this->db->where('haciendas.id', $id);
        return $this->db->get()->row();
    }
}
```

### 5. Migraciones (usando CI Migrations)

**modules/Haciendas/migrations/001_create_haciendas.php**

```php
class Migration_Create_haciendas extends CI_Migration {
    public function up() {
        $this->dbforge->add_field([
            'id' => ['type' => 'INT', 'constraint' => 11, 'auto_increment' => TRUE],
            'nombre' => ['type' => 'VARCHAR', 'constraint' => 100],
            'hectareas' => ['type' => 'DECIMAL', 'constraint' => '10,2'],
            'created_at' => ['type' => 'DATETIME']
        ]);
        $this->dbforge->add_key('id', TRUE);
        $this->dbforge->create_table('haciendas');
    }
}
```

### 6. Vista Jerárquica

**modules/Haciendas/views/haciendas/listar.php**

```php
<?php $this->template->header('Gestión de Haciendas'); ?>

<table class="table">
    <?php foreach ($haciendas as $h): ?>
    <tr>
        <td><?= $h->nombre ?></td>
        <td>
            <a href="<?= site_url("haciendas/{$h->id}/lotes") ?>" class="btn btn-info">
                Ver Lotes
            </a>
        </td>
    </tr>
    <?php endforeach; ?>
</table>

<?php $this->template->footer(); ?>
```

### 7. Sistema de Rutas Anidadas

Para manejar la relación jerárquica:

```bash
haciendas/1/lotes/5/modulos
```

En el controlador de Lotes:

```php
class Lotes extends MY_Controller {
    public function index($hacienda_id) {
        $this->load->model('haciendas/Lote_model');
        $data['lotes'] = $this->Lote_model->get_by_hacienda($hacienda_id);
        $this->template->render('lotes/listar', $data);
    }
}
```

### 8. Integración con Tu Sistema Existente

1. **Menú Dinámico**:
    
    - Registrar las rutas del módulo en tu tabla de menús
        
    - Ejemplo: "Haciendas" -> "/haciendas"
        
2. **Permisos**:
    
    - Crear permisos específicos:
        
        - `haciendas/view`
            
        - `haciendas/create`
            
        - `lotes/manage`
            
3. **API**:
    
    - Crear endpoints para móvil:
        
        - `/api/haciendas`
            
        - `/api/haciendas/{id}/lotes`
            

### 9. Consideraciones Adicionales

1. **Relaciones en BD**:

```sql
haciendas (id, nombre)
lotes (id, hacienda_id, nombre)
modulos (id, lote_id, nombre)
```

2. **Validación de Propiedad**:
    
    - Asegurar que cada usuario solo acceda a sus propias entidades
        
    - En cada método del controlador:

```php
$this->Hacienda_model->belongs_to_user($hacienda_id, $this->session->userdata('user_id'));
```

3. **Widgets/Dashboard**:
    
    - Crear componentes reutilizables para mostrar resúmenes

```php
<?php $this->load->view('haciendas/widgets/resumen_haciendas'); ?>
```

### 10. Ejemplo de Uso Completo

Para acceder a los módulos de un lote:

```php
// Controlador Modulos.php
public function index($lote_id) {
    $this->load->model('haciendas/Modulo_model');
    $data['modulos'] = $this->Modulo_model->get_by_lote($lote_id);
    $this->template->render('modulos/listar', $data);
}
```

Esta estructura te permite:

- Mantener un código organizado y escalable
    
- Reutilizar el módulo en diferentes proyectos
    
- Gestionar relaciones jerárquicas complejas
    
- Integrar fácilmente con tu sistema base existente
    

**Consejo**: Usa un enfoque de "filtros" para las consultas, por ejemplo:

```php
// En tu modelo base
public function filter_by($column, $value) {
    $this->db->where($column, $value);
    return $this;
}

// Uso en controlador:
$this->Hacienda_model->filter_by('user_id', $current_user_id)->get_all();
```

