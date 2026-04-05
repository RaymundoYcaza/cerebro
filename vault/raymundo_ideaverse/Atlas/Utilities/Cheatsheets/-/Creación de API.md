---
up:
  - "[[Crear versión SaaS de Bisstox Agricontrol]]"
related: 
created: 2025-06-17
---

# 📚 Guía Completa para Crear APIs Seguras en BanaControl
## 🎯 Filosofía y Arquitectura
### Ubicación de Archivos
- **Ubicar controladores API en la raíz de `application/controllers/`**
- **Razón:** Simplifica el enrutamiento y evita conflictos con subdirectorios
- **Convención de nombres:** `[Modulo]_api.php` (ej: `Personnel_api.php`, `Inventory_api.php`)
### Herencia y Reutilización
- **Todos los APIs deben heredar de `Secure_base_api`**
- **Beneficios:** Autenticación automática, respuestas estandarizadas, logging, CORS
## 🔐 Implementación de Autenticación
### 1. Métodos de Autenticación Soportados
#### A. Sesión Web (Ion Auth) - Para AJAX desde aplicaciones web
```javascript
// Frontend JavaScript - Automático si el usuario está logueado
fetch('/personnel_api/employees', {
    method: 'GET',
    credentials: 'include' // Incluye cookies de sesión
})
```
#### B. API Key en Header - Para aplicaciones móviles y herramientas
```bash
# Método recomendado para aplicaciones externas
curl -H "X-API-Key: YOUR_API_KEY" "http://domain.com/personnel_api/employees"
```
#### C. API Key en Parámetro - Para desarrollo y herramientas simples
```bash
# Para Power BI, Power Query, herramientas que no soportan headers customizados
curl "http://domain.com/personnel_api/employees?api_key=YOUR_API_KEY"
```
#### D. Bearer Token - Para aplicaciones OAuth2
```bash
# Para sistemas con autenticación basada en tokens
curl -H "Authorization: Bearer YOUR_TOKEN" "http://domain.com/personnel_api/employees"
```
### 2. Configuración para Clientes Específicos
#### Power BI / Power Query
```m
// En Power Query M
let
    url = "http://domain.com/personnel_api/employees?api_key=YOUR_API_KEY",
    source = Json.Document(Web.Contents(url))
in
    source
```
#### Aplicaciones Móviles (React Native/Flutter)
```javascript
// React Native
const response = await fetch('http://domain.com/personnel_api/employees', {
    headers: {
        'X-API-Key': 'YOUR_API_KEY',
        'Content-Type': 'application/json'
    }
});
```
#### Aplicaciones Web (AJAX)
```javascript
// jQuery/JavaScript - Usuario ya logueado
$.ajax({
    url: '/personnel_api/employees',
    method: 'GET',
    success: function(response) {
        console.log(response.data);
    }
});
```
## 🏗️ Estructura de Controlador API
### Plantilla Base para Nuevo Controlador
```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');
// Cargar el controlador base seguro
require_once(APPPATH . 'controllers/Secure_base_api.php');
/**
 * [Modulo] API Controller
 *
 * API para el módulo de [descripción].
 * Proporciona endpoints para operaciones AJAX y aplicaciones móviles.
 * Incluye autenticación y autorización.
 *
 * @author BanaControl Development Team
 * @version 1.0
 * @date 2025-06-18
 */
class [Modulo]_api extends Secure_base_api
{
    public function __construct()
    {
        // El constructor padre ya maneja la autenticación
        parent::__construct();
        // Cargar modelos específicos del módulo
        $this->load->model('[modulo]/[Modelo]_model', 'modelo');
    }
    /**
     * Endpoint principal del módulo
     *
     * @method GET
     * @url /[modulo]_api/[endpoint]
     */
    public function [endpoint]()
    {
        try {
            // 1. Obtener y validar parámetros
            $param1 = $this->input->get('param1');
            $param2 = $this->input->get('param2') ?: 'default_value';
            // 2. Validaciones
            if (empty($param1)) {
                $this->_send_error_response('Parameter "param1" is required', 400);
                return;
            }
            // 3. Lógica de negocio
            $data = $this->_get_data($param1, $param2);
            // 4. Log de actividad
            $this->_log_api_activity('get_data', [
                'param1' => $param1,
                'total_returned' => count($data)
            ]);
            // 5. Respuesta exitosa
            $this->_send_success_response($data, 'Data retrieved successfully', [
                'pagination' => [
                    'total' => count($data),
                    'param1' => $param1
                ]
            ]);
        } catch (Exception $e) {
            log_message('error', 'API Error in [endpoint](): ' . $e->getMessage());
            $this->_send_error_response('Error retrieving data: ' . $e->getMessage(), 500);
        }
    }
    /**
     * Método privado para lógica de negocio
     */
    private function _get_data($param1, $param2)
    {
        // Implementar lógica aquí
        return [];
    }
}
```
## 📋 Estructura JSON Estandarizada
### Respuesta Exitosa
```json
{
    "success": true,
    "message": "Data retrieved successfully",
    "data": [
        {
            "id": "1",
            "field1": "value1",
            "field2": "value2"
        }
    ],
    "pagination": {
        "total": 150,
        "limit": 50,
        "offset": 0,
        "count": 50,
        "has_more": true
    },
    "filters": {
        "search": "term",
        "category": "active"
    },
    "timestamp": "2025-06-18 12:00:00"
}
```
### Respuesta de Error
```json
{
    "success": false,
    "error": "API Error",
    "message": "Parameter 'id' is required",
    "timestamp": "2025-06-18 12:00:00"
}
```
### Respuesta de Autenticación Requerida (401)
```json
{
    "success": false,
    "error": "Unauthorized",
    "message": "Authentication required. Please provide valid credentials.",
    "authentication_methods": {
        "session": "Login through web interface",
        "bearer_token": "Authorization: Bearer YOUR_TOKEN",
        "api_key_header": "X-API-Key: YOUR_API_KEY",
        "api_key_param": "?api_key=YOUR_API_KEY"
    },
    "examples": {
        "api_key_param": "?api_key=test_key",
        "header_example": "X-API-Key: test_key"
    },
    "timestamp": "2025-06-18 12:00:00"
}
```
## 🔧 Métodos Estandarizados Disponibles
### En tu controlador tienes acceso a:
#### Respuestas
```php
// Respuesta exitosa
$this->_send_success_response($data, $message, $extra_data);
// Respuesta de error
$this->_send_error_response($message, $http_code, $extra_data);
```
#### Autenticación
```php
// Verificar permisos específicos
if (!$this->_has_permission('read_employees')) {
    $this->_send_error_response('Insufficient permissions', 403);
    return;
}
// Obtener usuario autenticado
$user = $this->_get_authenticated_user();
// Deshabilitar autenticación para endpoints públicos (usar con cuidado)
$this->_disable_auth();
```
#### Logging
```php
// Log automático de actividad
$this->_log_api_activity('action_name', [
    'param1' => $value1,
    'result_count' => count($data)
]);
```
## 📊 Logging Automático
### Qué se registra automáticamente:
- **Usuario:** Nombre del usuario autenticado o método de autenticación usado
- **Acción:** Nombre del endpoint y operación realizada
- **Datos:** Parámetros principales y resultados
- **IP:** Dirección IP del cliente
- **Timestamp:** Fecha y hora exacta
### Ejemplo de log generado:
```
INFO - API Activity - User: juan.perez, Action: get_employees, Data: {"limit":50,"offset":0,"total_returned":25}, IP: 192.168.1.100
```
### Configuración de logs:
```php
// En application/config/config.php
$config['log_threshold'] = 1; // 0=off, 1=errors, 2=debug, 3=info, 4=all
```
## 🚀 Escalabilidad y Reutilización
### 1. Patrón Reutilizable
- **Un controlador base:** `Secure_base_api.php`
- **Múltiples controladores específicos:** `Personnel_api.php`, `Inventory_api.php`, etc.
- **Funcionalidad heredada:** Autenticación, respuestas, logging
### 2. Adición de Nuevos Módulos
```bash
# Pasos para agregar nuevo módulo API:
1. Crear archivo: application/controllers/New_module_api.php
2. Heredar de Secure_base_api
3. Implementar endpoints siguiendo la plantilla
4. Agregar rutas en application/config/routes.php (opcional)
5. Crear pruebas en public/test_new_module_api.php
```
### 3. Extensión de Autenticación
```php
// En Secure_base_api.php - Agregar nuevos métodos de auth
private function _validate_custom_auth($custom_token) {
    // Implementar nueva lógica de autenticación
    return true/false;
}
```
## 🧪 Validación y Pruebas
### Crear Script de Pruebas
```php
// public/test_[module]_api.php
<?php
function test_endpoint($url, $expected_code = 200) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    echo "URL: $url\n";
    echo "Expected: $expected_code, Got: $http_code\n";
    echo "Response: " . substr($response, 0, 200) . "...\n\n";
}
// Tests sin autenticación (debe devolver 401)
test_endpoint('http://localhost/module_api/endpoint', 401);
// Tests con API key (debe devolver 200)
test_endpoint('http://localhost/module_api/endpoint?api_key=test_key', 200);
?>
```
## ⚠️ Mejores Prácticas y Errores Comunes
### ✅ Hacer:
- Siempre heredar de `Secure_base_api`
- Usar `$this->_send_success_response()` y `$this->_send_error_response()`
- Validar todos los parámetros de entrada
- Logear actividad importante con `$this->_log_api_activity()`
- Usar try-catch en todos los endpoints
- Documentar parámetros y respuestas en comentarios PHPDoc
### ❌ No Hacer:
- No usar `echo json_encode()` directamente
- No heredar de `CI_Controller` directamente
- No omitir validación de parámetros
- No olvidar el manejo de excepciones
- No usar `exit()` o `die()` directamente
- No crear endpoints sin autenticación (salvo casos muy específicos)
## 🔑 Configuración de API Keys en Producción
### Actualizar en Secure_base_api.php:
```php
private function _validate_api_key($api_key) {
    $valid_api_keys = [
        'prod_key_mobile_app' => [
            'name' => 'Mobile Application',
            'permissions' => ['read', 'write']
        ],
        'prod_key_powerbi' => [
            'name' => 'Power BI Integration',
            'permissions' => ['read']
        ],
        'prod_key_external_system' => [
            'name' => 'External System Integration',
            'permissions' => ['read', 'write', 'admin']
        ]
    ];
    if (isset($valid_api_keys[$api_key])) {
        $this->authenticated_user = (object) $valid_api_keys[$api_key];
        return true;
    }
    return false;
}
```
Esta guía proporciona todo lo necesario para crear APIs seguras, escalables y consistentes en el sistema BanaControl.