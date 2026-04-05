---
created: 2024-05-25 
---



## Conceptos de programación
Manejo de Excepciones
**Modelo**: Aquí es donde debes lanzar la mayoría de las excepciones. El modelo es responsable de la lógica de negocio y la interacción con la base de datos. Por lo tanto, cualquier error relacionado con estas operaciones (como errores de base de datos, violaciones de reglas de negocio, etc.) debe resultar en una excepción que se lanza desde el modelo.
**Vista**: En general, la vista no debería lanzar ni manejar excepciones. Su trabajo es presentar los datos al usuario de una manera amigable. Si ocurre un error en la vista, probablemente sea un error de programación y no algo que deba manejarse en tiempo de ejecución.
**Controlador**: Este es el lugar donde debes capturar y manejar las excepciones. El controlador actúa como intermediario entre el modelo y la vista. Puede capturar las excepciones lanzadas por el modelo, decidir qué hacer con ellas (por ejemplo, registrarlas, mostrar un mensaje de error al usuario, etc.) y luego pasar los datos apropiados a la vista.
Lógica de negocio
La lógica de negocio, que es el conjunto de reglas y procedimientos que determinan cómo se manejan, procesan y presentan los datos en una aplicación, generalmente reside en el **modelo** en el patrón de diseño Modelo-Vista-Controlador (MVC).
Aquí es donde se realizan las operaciones de la base de datos, se aplican las reglas de negocio y se lanzan las excepciones cuando algo va mal. Por ejemplo, si tienes una aplicación de comercio electrónico, la lógica de negocio podría incluir cosas como calcular el total de un carrito de compras, verificar si un artículo está en stock antes de añadirlo al carrito, o aplicar un descuento a un pedido.
Es importante mantener la lógica de negocio en el modelo y no en el controlador o la vista. Esto mantiene la aplicación bien organizada y facilita la realización de pruebas y la reutilización del código. Además, al mantener la lógica de negocio en el modelo, puedes asegurarte de que las reglas de negocio se apliquen de manera consistente cada vez que se acceda a los datos, independientemente de la interfaz de usuario que se esté utilizando.
Responsabilidades de cada componente en el patrón de diseño MVC
**Modelo**: El modelo es responsable de la lógica de negocio y la gestión de los datos. Esto incluye interactuar con la base de datos, aplicar reglas de negocio, validar datos y lanzar excepciones cuando algo va mal. El modelo es independiente de la interfaz de usuario y no sabe nada sobre cómo se presentan los datos.
**Vista**: La vista es responsable de la presentación de los datos al usuario. Toma los datos del modelo y los muestra de una manera que tiene sentido para el usuario. La vista no contiene ninguna lógica de negocio y no interactúa directamente con la base de datos.
**Controlador**: El controlador actúa como intermediario entre el modelo y la vista. Maneja la entrada del usuario (por ejemplo, clics de botones, entradas de texto, etc.), actualiza el modelo en consecuencia, y luego actualiza la vista para reflejar cualquier cambio en el modelo. El controlador también es donde se manejan las excepciones lanzadas por el modelo.
A manera de resumen, el modelo maneja los datos y la lógica de negocio, la vista maneja la presentación de los datos, y el controlador maneja la interacción entre el modelo y la vista. Esta separación de responsabilidades hace que el código sea más fácil de mantener y probar.
Uso de Value Objects
Un código de clase que tiene muchas responsabilidades, puede ser difícil de mantener sobre todo cuando se tienen muchas propiedades.
![image.png](../assets/image_1707586455108_0.png){:height 457, :width 774}
Usando value objects (que yo entendería como "valores como objetos" o el uso de objetos en lugar de valores primitivos), conseguimos que cada propiedad -solo si la propiedad es relevante y lo requiere- puede ser una clase, con sus respectivas validaciones.
Esto genera que podamos tener separada la lógica por cada propiedad, facilitando el mantenimiento por tener un código más claro y responsabilidades más atómicas.
*¿Cómo diferenciar una entidad de un value object?*
La entidad va a ser todo mutable, menos el id.
![image.png](../assets/image_1707586656562_0.png)
![image.png](../assets/image_1707586730639_0.png)
![image.png](../assets/image_1707586804200_0.png)
![image.png](../assets/image_1707587091133_0.png)
Uso de repositorios
sfsafd
![image.png](../assets/image_1707587530944_0.png)
Usando repositorio
![image.png](../assets/image_1707587518414_0.png)
