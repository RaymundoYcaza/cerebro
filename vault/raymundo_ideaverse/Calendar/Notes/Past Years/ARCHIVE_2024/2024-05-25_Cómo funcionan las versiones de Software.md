---
created: 2024-05-25 
---



{{video(https://www.youtube.com/watch?v=lC73oir6mrE)}}
Los tres números principales que se usan en el versionado semántico se deonominan: versión mayor, versión menor y parche.
1.2.3

El número de parche se aumenta 
cuando ha sido corregido un error en el programa, sin la necesidad de 
modificar la funcionalidad existente.

La versión menor se aumenta cuando se agrega funcionalidad nueva que es retrocompatible, es decir, que no modifica la actual.

La versión mayor se aumenta 
cuando los cambios que se han hecho en la funcionalidad no es 
recompatible. Por ejemplo cuando se elimina funcionalidad antigua. 
Cuando el usuario tiene que realizar ciertos cambios en su información /
datos para adaptarsee a los cambios o a la funcionalidad nueva.

Cada vez que un número de la 
versión se actualiza, todos los números de su derecha, se deben 
reiniciar (poner a cero nuevamente).

A la hora de comenzar con el desarrollo de una aplicación, se debe comenzar con la versión 0.1.0

Cuando se envia el software a producción , se debe actualizar a la versión 1.0.0

Adicionalmente, se pueden agregar etiquetas a la versión. Por ejemplo:

Alpha.- Es inestable o incompleta. Tiene errores que corregir.

Beta.- Más estable que Alpha. 
Funcionalidad completa pero aun tiene que realizarse pruebas en busca de
errores o problemas de rendimiento.

Pre-release.- O prelanzamiento, prácticamente lista para ser lanzada.
## Selección de versiones
Cuando se utilizan gestores de 
paquetes como npm o Composer, se pueden usar los simbolos > < 
> = o <= para seleccionar una versión mayor / igual a la indicada.

<= 3.0.2

Un signo de acento circunflejo ^ 
indica que se use una versión mayor a la indicada, siempre y cuando sea 
retrocompatible. Esto es, manteniendose dentro de la versión mayor 
actual, mientras se asegura que el software se encuentra actualizado.

^1.5.0
## Ejemplo
[Versioning | Ionic Documentation (ionicframework.com)](https://ionicframework.com/docs/reference/versioning)
