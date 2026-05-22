---
up:
  - "[[Crear versión SaaS de Bisstox Agricontrol]]"
related: 
created: 2025-06-11
---
 
# Guía Completa: Hooks para Divisores de Sección en Menús
## 📋 Índice
1. [Sistema de Hooks](#sistema-de-hooks)
2. [Hooks Disponibles](#hooks-disponibles)
3. [Ejemplos Prácticos](#ejemplos-prácticos)
4. [Patrones de Diseño](#patrones-de-diseño)
5. [Mejores Prácticas](#mejores-prácticas)
6. [Casos de Uso Avanzados](#casos-de-uso-avanzados)
## 🔧 Sistema de Hooks
El sistema utiliza **WordPress-style hooks** implementados con la librería **Eventy**:
### Funciones Principales
```php
// Añadir un filter hook
ld_add_filter($hookName, $callback, $priority = 20, $args = 1)
// Aplicar un filter hook (mostrar el contenido)
ld_apply_filters($hookName, $content, $args = null)
// Añadir un action hook
ld_add_action($hookName, $callback, $priority = 20, $args = 1)
// Ejecutar un action hook
ld_do_action($hookName, $args = null)
```
## 🎯 Hooks Disponibles
### Hooks de Grupo de Menú
```php
// Antes de todo el grupo (incluido el título)
'sidebar_menu_group_before_' . Str::slug($groupName)
// Antes del título del grupo
'sidebar_menu_group_heading_before_' . Str::slug($groupName)
// Después del título del grupo
'sidebar_menu_group_heading_after_' . Str::slug($groupName)
// Antes de todos los elementos del menú
'sidebar_menu_before_all_' . Str::slug($groupName)
// Después de todos los elementos del menú
'sidebar_menu_after_all_' . Str::slug($groupName)
// Después de todo el grupo
'sidebar_menu_group_after_' . Str::slug($groupName)
```
### Grupos Disponibles por Defecto
- `main` → `sidebar_menu_group_before_main`
- `agriculture` → `sidebar_menu_group_before_agriculture`
- `more` → `sidebar_menu_group_before_more`
## 🎨 Ejemplos Prácticos
### 1. Divisor Simple con Línea
```php
ld_add_filter('sidebar_menu_group_before_agriculture', function($content) {
    $divider = '
        <div class="menu-divider mb-4 mx-5">
            <hr class="border-gray-200 dark:border-gray-700">
        </div>
    ';
    return $content . $divider;
});
```
### 2. Divisor con Texto Centrado
```php
ld_add_filter('sidebar_menu_group_before_agriculture', function($content) {
    $divider = '
        <div class="menu-section-divider mb-4 px-5">
            <div class="flex items-center">
                <div class="flex-grow border-t border-gray-200 dark:border-gray-700"></div>
                <span class="px-3 text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                    ' . __('Farm Management') . '
                </span>
                <div class="flex-grow border-t border-gray-200 dark:border-gray-700"></div>
            </div>
        </div>
    ';
    return $content . $divider;
});
```
### 3. Divisor con Icono
```php
ld_add_filter('sidebar_menu_group_before_agriculture', function($content) {
    $divider = '
        <div class="menu-section-divider mb-6 px-5">
            <div class="relative">
                <div class="absolute inset-0 flex items-center">
                    <div class="w-full border-t border-gray-200 dark:border-gray-700"></div>
                </div>
                <div class="relative flex justify-center">
                    <span class="bg-white dark:bg-gray-900 px-3 text-sm font-medium text-gray-900 dark:text-white flex items-center">
                        <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z"/>
                        </svg>
                        ' . __('Agriculture') . '
                    </span>
                </div>
            </div>
        </div>
    ';
    return $content . $divider;
});
```
### 4. Card Informativa
```php
ld_add_filter('sidebar_menu_group_before_more', function($content) {
    $card = '
        <div class="menu-info-card mx-3 mb-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-800">
            <div class="flex items-center">
                <div class="flex-shrink-0">
                    <svg class="w-5 h-5 text-blue-600 dark:text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0z"/>
                    </svg>
                </div>
                <div class="ml-3">
                    <p class="text-sm font-medium text-blue-800 dark:text-blue-200">
                        ' . __('System Tools') . '
                    </p>
                    <p class="text-xs text-blue-600 dark:text-blue-300">
                        ' . __('Configuration & utilities') . '
                    </p>
                </div>
            </div>
        </div>
    ';
    return $content . $card;
});
```
### 5. Badge con Estado
```php
ld_add_filter('sidebar_menu_group_heading_after_agriculture', function($content) {
    $badge = '
        <div class="mb-3 px-5">
            <div class="flex items-center justify-between">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300">
                    <span class="w-2 h-2 bg-green-400 rounded-full mr-1.5"></span>
                    ' . __('Active') . '
                </span>
                <span class="text-xs text-gray-500 dark:text-gray-400">
                    4 ' . __('modules') . '
                </span>
            </div>
        </div>
    ';
    return $content . $badge;
});
```
## 🎭 Patrones de Diseño
### Colores Según Grupos
```php
$colorSchemes = [
    'main' => [
        'bg' => 'bg-blue-50 dark:bg-blue-900/20',
        'border' => 'border-blue-200 dark:border-blue-800',
        'text' => 'text-blue-800 dark:text-blue-200'
    ],
    'agriculture' => [
        'bg' => 'bg-green-50 dark:bg-green-900/20',
        'border' => 'border-green-200 dark:border-green-800',
        'text' => 'text-green-800 dark:text-green-200'
    ],
    'more' => [
        'bg' => 'bg-gray-50 dark:bg-gray-900/20',
        'border' => 'border-gray-200 dark:border-gray-800',
        'text' => 'text-gray-800 dark:text-gray-200'
    ]
];
```
### Iconos por Categoría
```php
$icons = [
    'main' => '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77z"/>',
    'agriculture' => '<path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z"/>',
    'analytics' => '<path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2z"/>',
    'settings' => '<path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0"/>',
];
```
## 🏆 Mejores Prácticas
### 1. **Usar Prioridades**
```php
// Prioridad alta (aparece primero)
ld_add_filter('hook_name', $callback, 5);
// Prioridad normal
ld_add_filter('hook_name', $callback, 20);
// Prioridad baja (aparece último)
ld_add_filter('hook_name', $callback, 50);
```
### 2. **Responsive Design**
```php
$divider = '
    <div class="menu-divider mb-4 hidden lg:block">
        <!-- Solo se muestra en pantallas grandes -->
    </div>
';
// O usando CSS
$css = '
    @media (max-width: 1024px) {
        .app-sidebar-minified .menu-section-divider {
            display: none;
        }
    }
';
```
### 3. **Internacionalización**
```php
// Siempre usar función de traducción
__('Farm Management')
trans('modules.agriculture.title')
```
### 4. **Validar Permisos**
```php
ld_add_filter('sidebar_menu_group_before_agriculture', function($content) {
    // Solo mostrar si el usuario tiene permisos
    if (!auth()->user()->can('agriculture.view')) {
        return $content;
    }
    return $content . $divider;
});
```
### 5. **CSS Personalizado**
```php
// En el método boot() del ServiceProvider
ld_add_filter('settings_appearance_tab_before_section_end', function($content) {
    return $content . '<style>/* CSS personalizado */</style>';
});
```
## 🚀 Casos de Uso Avanzados
### 1. **Divisor Dinámico con Contador**
```php
ld_add_filter('sidebar_menu_group_heading_after_agriculture', function($content) {
    $moduleCount = cache()->remember('agriculture_modules_count', 3600, function() {
        return \DB::table('modules')->where('category', 'agriculture')->count();
    });
    $badge = "
        <div class=\"mb-3 px-5\">
            <span class=\"text-xs text-gray-500 dark:text-gray-400\">
                {$moduleCount} " . __('active modules') . "
            </span>
        </div>
    ";
    return $content . $badge;
});
```
### 2. **Divisor Condicional**
```php
ld_add_filter('sidebar_menu_group_before_agriculture', function($content) {
    // Solo mostrar en horario de trabajo
    $currentHour = now()->hour;
    if ($currentHour < 6 || $currentHour > 18) {
        return $content;
    }
    $divider = '
        <div class="menu-time-notice mx-3 mb-4 p-2 bg-yellow-50 dark:bg-yellow-900/20 rounded text-center">
            <span class="text-xs text-yellow-700 dark:text-yellow-300">
                🌅 ' . __('Farm Operations Hours') . '
            </span>
        </div>
    ';
    return $content . $divider;
});
```
### 3. **Divisor con Estado del Sistema**
```php
ld_add_filter('sidebar_menu_group_before_main', function($content) {
    $systemStatus = app('system.health')->check();
    $statusColor = $systemStatus->isHealthy() ? 'green' : 'red';
    $statusBadge = "
        <div class=\"mx-3 mb-4 p-3 bg-{$statusColor}-50 dark:bg-{$statusColor}-900/20 rounded-lg\">
            <div class=\"flex items-center\">
                <div class=\"w-2 h-2 bg-{$statusColor}-400 rounded-full mr-2\"></div>
                <span class=\"text-xs font-medium text-{$statusColor}-800 dark:text-{$statusColor}-200\">
                    " . __('System Status: ') . $systemStatus->message . "
                </span>
            </div>
        </div>
    ";
    return $content . $statusBadge;
});
```
## 📝 Implementación Completa
### En tu ServiceProvider:
```php
<?php
namespace Modules\Farms\app\Providers;
use Illuminate\Support\ServiceProvider;
class MenuDividersServiceProvider extends ServiceProvider
{
    public function register()
    {
        $this->addMenuDividers();
    }
    public function boot()
    {
        $this->addCustomCSS();
    }
    private function addMenuDividers()
    {
        // Divisor principal para Agriculture
        ld_add_filter('sidebar_menu_group_before_agriculture', function($content) {
            return $content . view('partials.menu-divider', [
                'title' => __('Farm Management'),
                'icon' => 'agriculture',
                'color' => 'green'
            ])->render();
        });
        // Badge informativo
        ld_add_filter('sidebar_menu_group_heading_after_agriculture', function($content) {
            return $content . view('partials.menu-badge')->render();
        });
    }
    private function addCustomCSS()
    {
        ld_add_filter('settings_appearance_tab_before_section_end', function($content) {
            return $content . '<style>/* CSS personalizado */</style>';
        });
    }
}
```
### Registrar en FarmsServiceProvider:
```php
public function register()
{
    $this->app->register(MenuDividersServiceProvider::class);
}
```
Esta guía te proporciona todas las herramientas necesarias para implementar divisores HTML personalizados en el sistema de menús usando hooks. ¡El sistema es muy flexible y potente!