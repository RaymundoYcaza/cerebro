---
up:
  - "[[Codeigniter 3 Snippets MOC]]"
related: []
created: 2025-05-07
---


Una técnica común es crear un modelo padre  `application/core/MY_Model.php` que encapsule la preferencia por el formato de los datos devueltos:

```PHP
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class MY_Model extends CI_Model {
    /** 
     * 'array' o 'object'
     */
    protected $returnType = 'array';

    public function __construct()
    {
        parent::__construct();
    }

    protected function formatResult($query)
    {
        if ($this->returnType === 'object') {
            return $query->result();
        }
        return $query->result_array();
    }

    public function getAll($table)
    {
        $q = $this->db->get($table);
        return $this->formatResult($q);
    }

    public function getById($table, $id)
    {
        $q = $this->db->get_where($table, ['id' => $id]);
        return $this->returnType === 'object'
            ? $q->row()
            : $q->row_array();
    }
}
```

Luego cada modelo concreto hereda de `MY_Model`:

```php
class User_model extends MY_Model {
    protected $returnType = 'object';  // este modelo devuelve objetos
}
```

De esta forma se puede centralizar la lógica de conversión y solo se configura `$returntype` donde se necesite distinto comportamiento.
#### Recomendaciones prácticas
1. Definir una política global (arrays vs. objetos)
2. Documentar en la guía de estilo (puede usarse la [[PHP Style Guide — CodeIgniter 3.1.13 documentation]])
3. Usar el modelo base _MY_Model_ para no repetir lógica.
4. Validar con `num_row()` antes de iterar, independientemente del formato.
5. Para responses JSON, arrays suelen mapear directamente sin conversión adicional.