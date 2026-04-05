---
in:
  - "[[Fast API]]"
---



**Ver nueva propuesta**: https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project
Una estructura de organización recomendada para un proyecto FastAPI podría ser la siguiente:
```
.
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── endpoints
│   │   │   ├── __init__.py
│   │   │   ├── endpoint1.py
│   │   │   ├── endpoint2.py
│   │   │   └── ...
│   │   └── middlewares.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── session.py
│   │   └── types.py
│   ├── main.py
│   └── services
│       ├── __init__.py
│       ├── service1.py
│       ├── service2.py
│       └── ...
├── tests
│   ├── __init__.py
│   ├── test_endpoint1.py
│   ├── test_endpoint2.py
│   └── ...
└── .env
```
`app/main.py`: Es el punto de entrada de la aplicación.
`app/api`: Contiene los endpoints de la API y las dependencias.
`app/core`: Contiene la configuración y la configuración de logging.
`app/db`: Contiene todo lo relacionado con la base de datos, como los modelos y las sesiones.
`app/services`: Contiene la lógica de negocio.
`tests`: Contiene las pruebas unitarias y de integración.
Esta estructura permite una separación clara de las responsabilidades y facilita la mantenibilidad del código.
Estructura recomendada
tomado de https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710
FastAPI es un marco de trabajo de Python potente y de alto rendimiento diseñado para construir APIs de manera rápida y eficiente. Utiliza características modernas de Python como anotaciones de tipo y sintaxis async/await para proporcionar una experiencia de desarrollo fluida. [FastAPI ofrece una velocidad y escalabilidad increíbles, lo que lo convierte en una opción preferida para la construcción de aplicaciones web robustas](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
[Cuando se crea una aplicación FastAPI, es importante seguir una organización de proyecto bien estructurada para garantizar la legibilidad, mantenibilidad y escalabilidad](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710). Aquí te dejo una descripción general de la estructura:
[**Servidor**: El directorio del servidor incluye los archivos de la aplicación principal responsables de manejar las solicitudes HTTP y el enrutamiento](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
[**Controlador**: El directorio del controlador alberga los controladores de API responsables de manejar las solicitudes y respuestas](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
[**Adaptador de Datos**: El directorio `data_adapter` contiene módulos responsables de interactuar con la capa de datos, como la base de datos, caché, Elasticsearch, etc](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
[**Modelos**: El directorio de modelos contiene los modelos de datos o esquemas utilizados por la aplicación](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
[**Servicio**: El directorio de servicio contiene la lógica de negocio o servicios utilizados por la aplicación](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
[**Logger**: El directorio de logger consta de módulos relacionados con la configuración y registro de logs](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
[**Config**: El directorio de config contiene varios archivos de configuración necesarios para las configuraciones y variables de entorno de la aplicación](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710)[1](https://medium.com/@ketansomvanshi007/structuring-a-fastapi-app-an-in-depth-guide-cdec3b8f4710).
