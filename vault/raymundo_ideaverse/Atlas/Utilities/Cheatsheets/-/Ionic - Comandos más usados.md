---
created: 2025-02-23 
---

### Crear un nuevo proyecto Ionic

**ionic start**  
Inicia un nuevo proyecto Ionic con una plantilla específica (Angular, React, Vue, etc.).

```
ionic start myApp blank --type=angular  
```

**Variantes del comando start**:

```
ionic start myApp tabs --type=react  # Usa la plantilla "tabs"  
ionic start myApp --capacitor  # Incluye Capacitor por defecto  
```

---

### Ejecutar la aplicación en modo desarrollo

**ionic serve**  
Inicia un servidor de desarrollo con recarga en vivo (live-reload).

```
ionic serve  
```

**Variantes del comando serve**:

```
ionic serve --port 8100  # Puerto específico  
ionic serve --no-open  # No abrir automáticamente el navegador  
```

---

### Compilar el proyecto para producción

**ionic build**  
Genera archivos estáticos optimizados para despliegue en la carpeta `www`.


```
ionic build  
```

**Variantes del comando build**:

```
ionic build --prod  # Compilación de producción (minificación, etc.)  
ionic build --platform=android  # Especificar plataforma (para integración avanzada)  
```

---

### Generar componentes, servicios, páginas, etc.

**ionic generate**  
Crea componentes, páginas, servicios, o módulos siguiendo las mejores prácticas de Ionic.


```
ionic generate page login  
```

**Variantes del command generate**:


```
ionic generate component card  # Componente  
ionic generate service api  # Servicio  
ionic generate module shared  # Módulo  
```

---

### Añadir una plataforma móvil (Android/iOS)

**ionic capacitor add**  
Añade soporte para Android o iOS usando Capacitor (herramienta oficial de Ionic).

```
ionic capacitor add android  
```

**Variantes del comando capacitor add**:

```
ionic capacitor add ios  
```

---

### Sincronizar cambios con Capacitor

**ionic capacitor sync**  
Actualiza las plataformas nativas con los cambios del proyecto web y copia recursos.

```
ionic capacitor sync  
```

**Variantes del comando capacitor sync**:

```
ionic capacitor sync android  # Sincronizar solo Android  
```

---

### Ejecutar la app en un dispositivo o emulador

**ionic capacitor run**  
Compila y ejecuta el proyecto en un dispositivo/emulador conectado.

```
ionic capacitor run android  
```

**Variantes del comando capacitor run**:


```
ionic capacitor run ios --livereload  # Modo live-reload en iOS  
```

---

### Habilitar integraciones (Capacitor, Cordova)

**ionic integrations enable**  
Activa integraciones como Capacitor o Cordova en el proyecto.

```
ionic integrations enable capacitor  
```

---

### Configurar opciones globales de Ionic CLI

**ionic config set**  
Define opciones de configuración globales (proxy, npmClient, etc.).


```
ionic config set -g npmClient yarn  
```

---

### Ver información del entorno de desarrollo

**ionic info**  
Muestra detalles del entorno: versiones de Ionic, Node, OS y dependencias.

```
ionic info  
```

---

### Ejecutar en modo laboratorio (vista multi-dispositivo)

**ionic serve --lab**  
Abre una vista simulando múltiples dispositivos (iOS/Android).

```
ionic serve --lab  
```

---

### Diagnosticar problemas en el proyecto

**ionic doctor check**  
Verifica errores comunes de configuración y sugiere soluciones.

```
ionic doctor check  
```

---

### Copiar cambios web a plataformas nativas

**ionic capacitor copy**  
Copia los archivos web (www/) a las plataformas nativas sin sincronizar.


```
ionic capacitor copy android  
```

---

### Reparar dependencias del proyecto

**ionic repair**  
Reinstala dependencias (node\_modules) y corrige conflictos comunes.

```
ionic repair  
```

---

### Autenticarse en Ionic Cloud (obsoleto en v7+)

**ionic login**  
Inicia sesión en servicios de Ionic (útil para Ionic Appflow).

```
ionic login  
```

---

### Añadir despliegue en vivo (Live Updates)

**ionic deploy add**  
Configura Live Updates para actualizaciones en tiempo real (Ionic Appflow).


```
ionic deploy add  
```

---

### Compilación específica para producción

**ionic build --prod**  
Compila el proyecto con optimizaciones avanzadas (AOT, minificación, etc.).


```
ionic build --prod  
```

---

### Abrir proyecto nativo en IDE (Android Studio/Xcode)

**ionic capacitor open**  
Abre el proyecto nativo en Android Studio o Xcode.


```
ionic capacitor open android  
```

---

### Actualizar Capacitor al core más reciente

**ionic capacitor update**  
Actualiza la versión de Capacitor y las plataformas nativas.

```
ionic capacitor update  
```

---

### Servir aplicación en red local

**ionic serve --external**  
Hace que el servidor de desarrollo sea accesible en la red local.


```
ionic serve --external  
```

---

### Ejecutar pruebas unitarias

**ionic test**  
Ejecuta pruebas unitarias (requiere configuración previa).


```
ionic test  
```

---

### Compilar proyecto nativo (Android/iOS)

**ionic capacitor build**  
Compila el proyecto nativo (requiere Android Studio/Xcode instalado).


```
ionic capacitor build ios  
```

---

### Añadir Capacitor manualmente

**ionic integrations enable capacitor**  
Alternativa para habilitar Capacitor si no se incluyó al iniciar el proyecto.

```
ionic integrations enable capacitor  
```

---

### Verificar requisitos para Cordova

**ionic cordova requirements**  
Verifica que el entorno cumpla con los requisitos para construir con Cordova.

```
ionic cordova requirements  
```

---

### Configurar despliegue en Ionic Appflow

**ionic deploy configure**  
Guía interactiva para configurar Live Updates o canales de despliegue.

```
ionic deploy configure  
```

---

**Nota:** Los comandos de `ionic cordova` son menos frecuentes en Ionic 7+, donde Capacitor es la herramienta recomendada.