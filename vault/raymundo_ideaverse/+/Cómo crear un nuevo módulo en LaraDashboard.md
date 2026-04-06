---
up:
  - "[[Crear versión SaaS de Bisstox Agricontrol]]"
related: 
created: 2025-05-26
---



## Crear un módulo usando artisan module

```bash
php artisan module:make NombreModulo
```

Activar el módulo

```bash
php artisan module:enable UserAvatar
```

Agregar la migración

```
php artisan module:make-migration add_avatar_to_users_table UserAvatar
```

Ejecutar la migración del módulo

```
php artisan module:migrate UserAvatar
```




En el `serviceProvider` del módulo, usar el filtro `ld_add_filter()` para agregar las opciones dinámicamente, por ejemplo, en el `FarmsServiceProvider`, dentro del método `boot().

Es necesario incluir al inicio del archivo las líneas:

```php
use Illuminate\Support\Facades\Route;

use App\Services\MenuService\AdminMenuItem;
```

Y dentro del método `boot()` incluir el filtro con el grupo y los items:
```
```
```php
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

            $farmMenuItem->setLabel(__('Farms'))  

                        ->setIcon('tv.svg')  

                        ->setId('farms-submenu')  

                        ->setActive(Route::is('farms.*'))  

                        ->setPriority(25)  

                        ->setPermissions($farmPermissions);  

            // Crear children solo si el usuario tiene los permisos específicos  

            $children = [];  

            if ($user->can('farm.view')) {  

                $allFarmsItem = new AdminMenuItem();  

                $allFarmsItem->setLabel(__('All Farms'))  

                            ->setRoute(route('farms.index'))  

                            ->setActive(Route::is('farms.index') || Route::is('farms.show'))  

                            ->setPriority(10)  

                            ->setPermissions('farm.view');  

                $children[] = $allFarmsItem;  

            }  

            if ($user->can('farm.create')) {  

                $addFarmItem = new AdminMenuItem();  

                $addFarmItem->setLabel(__('Add New Farm'))  

                           ->setRoute(route('farms.create'))  

                           ->setActive(Route::is('farms.create'))  

                           ->setPriority(20)  

                           ->setPermissions('farm.create');  

                $children[] = $addFarmItem;  

            }  

            if ($user->can('farm.view')) {  

                $categoriesItem = new AdminMenuItem();  

                $categoriesItem->setLabel(__('Farm Categories'))  

                              ->setRoute(route('farms.index'))  

                              ->setActive(Route::is('farms.*'))  

                              ->setPriority(30)  

                              ->setPermissions('farm.view');  

                $children[] = $categoriesItem;  

            }  

            $farmMenuItem->setChildren($children);  

            $items[] = $farmMenuItem;  

            return $items;  

        });
```

Para que tu módulo de Farms aparezca en el panel de gestión de permisos, necesitas agregar los permisos de tu módulo al **`PermissionService`** de LaraDashboard.

## **Ubicación del sistema de permisos**

El sistema de permisos está centralizado en PermissionService.php:20-99 , donde se definen todos los grupos de permisos disponibles en la aplicación.

## **Cómo agregar permisos de Farms**

Necesitas modificar el método **`getAllPermissions()`** en el **`PermissionService`** para incluir tu grupo de permisos de farms:

```
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

## **Proceso de creación de permisos**

Una vez agregados al **`PermissionService`**, los permisos se crean automáticamente en la base de datos a través del método PermissionService.php:176-191 , que itera sobre todos los grupos de permisos y los crea usando PermissionService.php:200-210 .

## **Integración con roles predefinidos**

Los nuevos permisos también se pueden incluir automáticamente en los roles predefinidos modificando el **`RolesService`**. Por ejemplo, para que el rol Superadmin tenga todos los permisos de farms automáticamente, el sistema ya está configurado para incluir todos los permisos disponibles.

## **Visualización en la interfaz**

Una vez creados los permisos, aparecerán automáticamente en:

1. **Panel de creación/edición de roles** - create.blade.php:79-102 donde se muestran agrupados por **`group_name`**
2. **Lista de permisos** - index.blade.php:46-80 donde se pueden ver todos los permisos con sus grupos y roles asignados

## **Ejecución de la migración**

Para aplicar los cambios, ejecuta el seeder que creará los nuevos permisos:

```
php artisan db:seed --class=RolePermissionSeeder
```

## Ejecutar los seeders

Para ejecutar los seeders en Laravel tienes varias opciones:

1) Ejecutar todos los seeders registrados en `DatabaseSeeder`:  
   ```
   php artisan db:seed
   ```

2) Refrescar migraciones y ejecutar seeders de golpe:  
   ```
   php artisan migrate:fresh --seed
   ```

3) Correr un seeder concreto por su clase:  
   ```
   php artisan db:seed --class=NombreDelSeeder
   ```

## **Notes**

El sistema está diseñado para ser extensible - solo necesitas agregar tu grupo de permisos al array en **`PermissionService`** y el resto del sistema (interfaz de roles, lista de permisos, verificación de autorización) funcionará automáticamente con los nuevos permisos de farms.

## Implementar vista de frontend

```php
@extends('frontend.layouts.app')

  

@section('content')

    <h1>Hello World</h1>

    <p>Module: {!! config('dashboard.name') !!}</p>

@endsection
```


## Resolución de problemas
### Laravel no encuentra el modelo en un módulo

`Class "Modules\Farms\Models\Farm" not found`

Cuando no se utiliza la carpeta por defecto en `app/Models`, Laravel no encuentra el modelo a menos que se le indique.

En Laravel puro, sólo el directorio **app/** (y los que ya tengas mapeados en tu `composer.json`) se “autocarga” vía PSR-4. Cuando pones archivos en `Modules/...` sin decirle a Composer que los cargue, Laravel no los encontrará y te sale ese “Class … not found”.

Tienes dos caminos:

#### 1) Autocargar `Modules/` vía Composer

1. En tu **`composer.json`** (en la raíz del proyecto), añade dentro de `autoload.psr-4` algo así:

```json
{
  "autoload": {
    "psr-4": {
      "App\\": "app/",
      "Modules\\": "Modules/"
    }
  }
}
```

2. Ejecuta en consola:

```bash
composer dump-autoload
php artisan optimize:clear
```

Ahora Composer sabe que cualquier clase bajo el namespace `Modules\…` vive en `Modules/…`, y podrá cargar tu `Modules\Farms\Models\Farm` sin problemas.

