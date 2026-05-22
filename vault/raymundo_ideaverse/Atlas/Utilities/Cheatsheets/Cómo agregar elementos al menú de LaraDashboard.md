---
up: []
related: []
created: 2025-06-11
---


 1. Definir los permisos en `PermissionService.php`

Ejemplo:

```php
<?php
[  
    'group_name' => 'farm',  
    'permissions' => [  
        'farm.create',  
        'farm.view',   
        'farm.edit',  
        'farm.delete',  
        'farm.reports',  
    ],  
], 
```


2. Configurar el menú en un archivo [Modulo]ServiceProvider.php

Ejemplo FarmsServiceProvider.php:

```php
<?php
// Usar filtros que se ejecutan cuando se renderiza el menú  
ld_add_filter('sidebar_menu_main', function($items) {  
    // Verificar que el usuario esté autenticado  
    if (!auth()->check()) {  
        return $items;  
    }  

    // Verificar explícitamente si el usuario tiene al menos uno de los permisos de farm  
    $user = auth()->user();  
    $farmPermissions = ['farm.view', 'farm.create', 'farm.edit', 'farm.delete'];  
    $hasAnyFarmPermission = false;  
      
    foreach ($farmPermissions as $permission) {  
        if ($user->can($permission)) {  
            $hasAnyFarmPermission = true;  
            break;  
        }  
    }  

    // Solo agregar el menú si el usuario tiene permisos  
    if (!$hasAnyFarmPermission) {  
        return $items;  
    }  

    // Crear objetos AdminMenuItem manualmente  
    $farmMenuItem = new AdminMenuItem();  
    $farmMenuItem->setLabel(__('Haciendas'))  
                ->setIcon('tv.svg')  
                ->setId('farms-submenu')  
                ->setActive(Route::is('farms.*'))  
                ->setPriority(25)  
                ->setPermissions($farmPermissions);  

    // Crear children solo si el usuario tiene los permisos específicos  
    $children = [];  

    if ($user->can('farm.view')) {  
        $allFarmsItem = new AdminMenuItem();  
        $allFarmsItem->setLabel(__('Listado Haciendas'))  
                    ->setRoute(route('farms.index'))  
                    ->setActive(Route::is('farms.index') || Route::is('farms.show'))  
                    ->setPriority(10)  
                    ->setPermissions('farm.view');  
        $children[] = $allFarmsItem;  
    }  

    if ($user->can('farm.create')) {  
        $addFarmItem = new AdminMenuItem();  
        $addFarmItem->setLabel(__('Crear Hacienda'))  
                   ->setRoute(route('farms.create'))  
                   ->setActive(Route::is('farms.create'))  
                   ->setPriority(20)  
                   ->setPermissions('farm.create');  
        $children[] = $addFarmItem;  
    }  

    // ... más submenús ...

    $farmMenuItem->setChildren($children);  
    $items[] = $farmMenuItem;  
    return $items;  
});  
```

3. Ejecutar el seeder para insertar los permisos en la base de datos
cd /var/www/html && php artisan db:seed --class=RolePermissionSeeder

4. Vistas con control de permisos

Las vistas que usan directivas de control de permisos para mostrar u ocultar elementos, usan código como:

```php
<?php
@can('owner.create')
<a href="{{ route('farms.owners.create') }}" class="btn-primary">Nuevo Propietario</a>
@endcan
```

## Cómo verificar los permisos que existen en la base de datos?
cd /var/www/html && php artisan tinker --execute="dump(\Spatie\Permission\Models\Permission::pluck('name')->toArray());"

## Agregar encabezados antes de un elemento

```php
        ld_add_filter('sidebar_menu_before_farms-submenu', function($html) {  

            return $html . '<div class="my-3 border-t border-gray-200 dark:border-gray-700"><h3 class="mb-4 text-xs uppercase leading-[20px] text-gray-400 px-5">Haciendas</h3></div>';  

        });
```


## Cómo eliminar los permisos que se han removido de PermissionService?

 Cuando removes un grupo de permisos del [PermissionService.php](vscode-file://vscode-app/c:/Users/raymundo/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html), esos permisos quedan "huérfanos" en la base de datos. Te muestro varias formas de eliminarlos:

## 1. **Verificar qué permisos están huérfanos**
Vamos a verificar si aún están en la BD:

```php
cd /var/www/html && php artisan tinker --execute="

// Obtener permisos definidos en código

\$service = app(\App\Services\PermissionService::class);

\$definedPermissions = collect(\$service->getAllPermissions())->pluck('permissions')->flatten()->toArray();

  

// Obtener permisos en BD

\$dbPermissions = \Spatie\Permission\Models\Permission::pluck('name')->toArray();

  

// Encontrar huérfanos

\$orphanPermissions = array_diff(\$dbPermissions, \$definedPermissions);

  

echo 'Permisos definidos en código: ' . count(\$definedPermissions) . PHP_EOL;

echo 'Permisos en BD: ' . count(\$dbPermissions) . PHP_EOL;

echo 'Permisos huérfanos: ' . count(\$orphanPermissions) . PHP_EOL;

dump(\$orphanPermissions);

"
```

## 2. **Métodos para eliminar permisos huérfanos**

### **Método 1: Comando Artisan directo**

Run command in terminal

```bash
cd /var/www/html && php artisan tinker --execute="

// Eliminar permisos del grupo 'hola'

\$deletedCount = \Spatie\Permission\Models\Permission::where('group_name', 'hola')->delete();

echo 'Permisos eliminados: ' . \$deletedCount;

"
```

### **Método 2: Crear un comando para limpiar permisos huérfanos**

`CleanOrphanPermissionsCommand.php`

```php
<?php

  

namespace App\Console\Commands;

  

use App\Services\PermissionService;

use Illuminate\Console\Command;

use Spatie\Permission\Models\Permission;

  

class CleanOrphanPermissionsCommand extends Command

{

    protected $signature = 'permissions:clean-orphans {--dry-run : Show what would be deleted without actually deleting}';

    protected $description = 'Remove permissions from database that are not defined in PermissionService';

  

    public function __construct(

        private readonly PermissionService $permissionService

    ) {

        parent::__construct();

    }

  

    public function handle()

    {

        $isDryRun = $this->option('dry-run');

        // Obtener permisos definidos en código

        $definedPermissions = collect($this->permissionService->getAllPermissions())

            ->pluck('permissions')

            ->flatten()

            ->toArray();

  

        // Obtener permisos en BD

        $dbPermissions = Permission::all();

  

        // Encontrar huérfanos

        $orphanPermissions = $dbPermissions->filter(function ($permission) use ($definedPermissions) {

            return !in_array($permission->name, $definedPermissions);

        });

  

        if ($orphanPermissions->isEmpty()) {

            $this->info('No se encontraron permisos huérfanos.');

            return 0;

        }

  

        $this->info("Se encontraron {$orphanPermissions->count()} permisos huérfanos:");

        $tableData = $orphanPermissions->map(function ($permission) {

            return [

                $permission->name,

                $permission->group_name ?? 'N/A',

                $permission->roles()->count() . ' roles',

                $permission->users()->count() . ' usuarios'

            ];

        })->toArray();

  

        $this->table(

            ['Permiso', 'Grupo', 'Roles asignados', 'Usuarios'],

            $tableData

        );

  

        if ($isDryRun) {

            $this->warn('Modo dry-run activado. No se eliminará nada.');

            return 0;

        }

  

        if (!$this->confirm('¿Estás seguro de que quieres eliminar estos permisos?')) {

            $this->info('Operación cancelada.');

            return 0;

        }

  

        $deletedCount = 0;

        foreach ($orphanPermissions as $permission) {

            $permission->delete();

            $deletedCount++;

        }

  

        $this->info("Se eliminaron {$deletedCount} permisos huérfanos.");

        // Limpiar caché de permisos

        if (function_exists('cache')) {

            cache()->forget(config('permission.cache.key'));

            $this->info('Caché de permisos limpiado.');

        }

  

        return 0;

    }

}
```

Ahora vamos a probar el comando en modo dry-run (sin eliminar nada):

cd /var/www/html && php artisan permissions:clean-orphans --dry-run

El comando necesita ser reconocido. Vamos a verificar si está bien registrado:

cd /var/www/html && php artisan config:clear && php artisan cache:clear

cd /var/www/html && php artisan list | grep permission

## Agregar elementos al menú
### Múltiples puntos de extensión

El sistema proporciona numerosos hooks para personalizar cada parte del sidebar: menu-item.blade.php:7-9

Los hooks disponibles incluyen:

- `sidebar_menu_group_before_{group_slug}`
- `sidebar_menu_group_after_{group_slug}`
- `sidebar_menu_group_heading_before_{group_slug}`
- `sidebar_menu_group_heading_after_{group_slug}`
- `sidebar_menu_before_all_{group_slug}`
- `sidebar_menu_after_all_{group_slug}`
## Agregar HTML al menú

### Agregar HTML a continuación del menú principal

```php
        ld_add_filter('sidebar_menu_group_after_main', function ($html) {  

            return $html . '<div class="my-3 border-t border-gray-200 dark:border-gray-700"><h3 class="mb-4 text-xs uppercase leading-[20px] text-gray-400 px-5">Haciendas</h3></div>';  

        });
```

### Agregar HTML antes de un grupo 


```php
// Agregar encabezado personalizado antes de un grupo  
ld_add_filter('sidebar_menu_group_before_mi-grupo-personalizado', function ($html) {  
    return $html . '<div class="px-5 py-2 text-xs font-semibold text-gray-500 uppercase">Sección Especial</div>';  
});
```