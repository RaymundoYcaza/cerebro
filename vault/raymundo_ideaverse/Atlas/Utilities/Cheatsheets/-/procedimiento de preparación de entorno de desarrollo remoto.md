---
created: 2025-01-08
---


Primero asegurar la conexión al servidor sin contraseña (o con contraseña propia, sin comprometer la contraseña del usuario del servidor) [[cómo acceder al servidor linux sin contraseña usando ssh]] 

Luego, instalar en Visual Studio Code el plugin Remote SSH


## Requisitos

- **Must Have**:
    - Acceso remoto al servidor para desarrollo con Visual Studio Code.
    - Soporte para contenedores Docker con bases de datos y aplicaciones.
    - Seguridad en las conexiones remotas mediante SSH o túneles seguros.
    - Compatibilidad con las tecnologías requeridas (Ionic, Laravel, Node.js, etc.).
    - Capacidad de exponer servicios del servidor a través de subdominios personalizados.
- **Should Have**:
    - Configuración que minimice el esfuerzo de mantenimiento.
    - Opciones para futuras expansiones (como CI/CD).
- **Could Have**:
    - Entorno preconfigurado para análisis de datos con herramientas como Jupyter Notebook.
    - Opciones de escalabilidad en caso de requerir más potencia.
- **Won't Have**:
    - Soluciones basadas en servicios de nube con costos recurrentes.

