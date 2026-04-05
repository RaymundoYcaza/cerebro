---
in:
  - "[[Git]]"
---



**Inicialización del repositorio**:
El líder del equipo inicializa un repositorio Git en el servidor y 
todos los miembros del equipo clonan este repositorio en sus máquinas 
locales.
**Creación de ramas**:
Cada miembro del equipo crea una rama para trabajar en una 
característica o corrección de errores específica. Por ejemplo, si un 
miembro está trabajando en la funcionalidad de inicio de sesión, puede 
crear una rama llamada `feature/login`.
```
git branch feature/login
```
Este
comando creará una nueva rama llamada ‘feature/login’. Sin embargo, ten
en cuenta que este comando no te cambiará a la nueva rama. Para cambiar
a la rama que acabas de crear, necesitarás usar el comando `git checkout` de la siguiente manera:
```
git checkout feature/login
```
Alternativamente, puedes usar el comando `git checkout` con la opción `-b` para crear una nueva rama y cambiar a ella en un solo paso:
```
git checkout -b feature/login
```
**Commits**:
Los miembros del equipo hacen commits regularmente en sus ramas con 
mensajes descriptivos y significativos. Por ejemplo, un buen mensaje de 
commit podría ser `Agrega validación de entrada para el formulario de inicio de sesión`.
```
git commit -m "Agrega validación de entrada para login"
```
**Etiquetas**:
Se pueden usar etiquetas para marcar puntos específicos en la historia 
del proyecto, como una nueva versión. Por ejemplo, cuando se lanza una 
nueva versión de la aplicación, se puede crear una etiqueta con el 
número de versión, como `v1.0`.
```
git tag v1.2.7
```
Este
comando creará una nueva etiqueta llamada ‘v1.2.7’. Las etiquetas, a 
diferencia de las ramas, no avanzan con cada commit que haces. Son 
puntos estáticos en la historia del código que puedes referenciar.

Después
de crear una etiqueta, es común que quieras compartir esta etiqueta con
otros desarrolladores. Para ello, puedes usar el comando `git push` con la opción `--tags`:

```
git push origin --tags
```
Este
comando empujará todas tus etiquetas al repositorio remoto. Si solo 
quieres empujar la etiqueta ‘v1.2.7’, puedes hacerlo especificando la 
etiqueta después de `origin`:

```
git push origin v1.2.7
```
**Revisiones y fusiones**:
Una vez que un miembro del equipo ha terminado su trabajo en una 
característica o corrección de errores, hace un “pull request” para 
fusionar su rama con la rama principal (master o main). Otros miembros 
del equipo revisan el código y, si todo está bien, se fusiona la rama.
Para fusionar una rama en Git, puedes usar el comando `git merge`. Aquí te dejo los pasos para hacerlo:
Primero, necesitas cambiar a la rama en la que quieres fusionar. Por
lo general, esto será tu rama principal o ‘master’. Puedes hacerlo con 
el comando `git checkout`:

```
git checkout master
```
Luego, puedes fusionar tu rama de trabajo (por ejemplo, 
‘feature/login’) en la rama actual (en este caso, ‘master’) con el 
comando `git merge`:

```
git merge feature/login
```
Este
comando fusionará la rama ‘feature/login’ en la rama ‘master’. Si hay 
conflictos entre las dos ramas, Git te lo hará saber y tendrás que 
resolver esos conflictos manualmente.
Después de resolver cualquier conflicto y hacer commit de los 
cambios, puedes empujar la rama fusionada al repositorio remoto con el 
comando `git push`:

```
git push origin master
```
Para crear un “pull request” en un repositorio de Gitea autohospedado es muy similar a hacerlo en GitHub.com.
**Push a tu rama**: Primero, haz push de tu rama (por ejemplo, ‘feature/login’) al repositorio remoto.
```
git push origin feature/login
```
**Abre el repositorio en tu navegador**: Ve al repositorio en tu instancia de GitHub autohospedada en tu navegador web.
**Crea el Pull Request**:
Haz clic en el botón “New pull request”. Selecciona tu rama en el menú 
desplegable “compare” y la rama a la que quieres fusionar (generalmente 
‘master’ o ‘main’) en el menú desplegable “base”. Luego, haz clic en 
“Create pull request”.
**Escribe una descripción**:
Proporciona un título y una descripción detallada para tu “pull 
request” que explique los cambios que has hecho y por qué deberían ser 
incorporados.
**Solicita revisión**:
Puedes solicitar a otros miembros de tu equipo que revisen tus cambios 
haciendo clic en el botón “Reviewers” y seleccionándolos de la lista.
**Merge del Pull Request**:
Una vez que tus cambios han sido revisados y aprobados, alguien con 
permisos de escritura en el repositorio puede hacer clic en “Merge pull 
request” para incorporar tus cambios en la rama base.
**Actualización del repositorio local**:
Después de que se haya fusionado una rama, todos los miembros del 
equipo deben actualizar su repositorio local con los últimos cambios del
servidor.
Es una buena práctica tener una rama separada para el desarrollo de la interfaz de usuario (UI).
**Crea la rama de la UI**: Puedes crear una rama específica para el desarrollo de la UI con el comando `git checkout -b prototype/GUI`. Esto crea una nueva rama llamada ‘prototype/GUI’ y cambia a ella.
**Desarrolla la UI**:
Realiza todos tus cambios relacionados con la UI en esta rama. Esto 
puede incluir cambios en los archivos HTML, CSS, y cualquier otro 
archivo relacionado con la UI.
**Haz commit de tus cambios**: Una vez que estés satisfecho con tus cambios, puedes hacer commit de ellos a la rama ‘prototype/GUI’ con `git commit`.
**Fusiona la rama de la UI**: Si quieres incorporar los cambios de la UI en otra rama (por ejemplo, ‘master’), puedes hacerlo con `git checkout master` seguido de `git merge prototype/GUI`.
**Continúa desarrollando la UI**: Después de fusionar, puedes volver a la rama de la UI con `git checkout prototype/GUI` y continuar desarrollando. Los cambios que hagas no afectarán a otras ramas a menos que los fusiones.
Este
flujo de trabajo te permite desarrollar y probar rápidamente prototipos
de UI sin afectar el desarrollo principal del proyecto. También 
facilita la colaboración entre los miembros del equipo que trabajan en 
diferentes aspectos del proyecto.
