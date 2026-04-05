---
in:
  - "[[Git]]"
---



## Prompts
Generar un commit
```
Prompt para generar un commit
```

## Comandos básicos

### Descartar todos los cambios y volver exactamente al último commit (como si no hubieras tocado nada)
Esto se puede hacer cuando se han hecho cambios en los archivos, pero el staging está limpio.
```bash
git restore .
```

Si además se quiere eliminar archivos y carpetas no rastreadas
```bash
git clean -fd
```
### Creating a new repository on the command line
```bash
git init
git commit -m "first commit"
git remote add origin https://github.com/VijayNew/NewExample.git
git push -u origin master
```

### Pushing an existing repository from the command line

```bash

git remote add origin https://git.inorizonti.com/Bisstox/InorizontiEmaApp.git

git push -u origin main

```

### Gitignore
#### Ignora todos los archivos y carpetas
*

#### No ignorar archivos .mp4
!*.mp4

#### No ignorar carpetas (necesario si hay archivos .mp4 dentro de carpetas)
!*/

#### No ignorar archivos .mp4 dentro de cualquier subcarpeta
!**/*.mp4

### Crear una rama
Crear la rama
`git branch nueva_rama`
Cambiar a la rama
`git checkout nueva_rama`

### Encontrar el hash de un commit

Para encontrar el hash de tu commit en Git, puedes usar el comando `log`. Este comando muestra el historial de commits en tu repositorio. Aquí te dejo un ejemplo:
  `git log`

Este comando te mostrará una lista de todos los commits en tu rama actual, empezando por el más reciente. Cada commit se muestra con su hash completo, el autor del commit, la fecha del commit y el mensaje del commit.
Si estás buscando un commit específico, puedes agregar algunas opciones al comando `log` para ayudarte a encontrarlo. Por ejemplo, puedes usar la opción `-p` para mostrar la diferencia introducida en cada commit. También puedes limitar el número de commits que se muestran utilizando `-n`, donde `n` es el número de commits que deseas ver.
  `git log -p -2`

Este comando te mostrará los últimos 2 commits junto con las diferencias introducidas en cada commit.
Para obtener una versión más corta de los logs en Git, puedes usar la opción `--oneline` con el comando `log`. Aquí te dejo un ejemplo:
  `git log --oneline`

Este comando te mostrará una lista de todos los commits en tu rama actual, empezando por el más reciente. Cada commit se muestra con su hash corto (los primeros 7 caracteres del hash completo) y el mensaje del commit en una sola línea.

### Regresar a un estado anterior en Git
Para regresar a un commit específico en Git, puedes usar el comando `checkout` junto con el hash del commit al que deseas regresar. 
```
git checkout <hash_del_commit>
```
Donde `<hash_del_commit>` es el identificador único del commit al que deseas regresar. Este hash usualmente se compone de una cadena de caracteres y números.

Al hacer esto, te moverás a una nueva rama sin nombre que apunta a ese commit. Si deseas mantener tus cambios en una nueva rama, puedes crearla al mismo tiempo que haces el checkout, así:
-
```
git checkout -b <nombre_de_la_nueva_rama> <hash_del_commit>
```
Donde `<nombre_de_la_nueva_rama>` es el nombre que deseas darle a la nueva rama. Recuerda reemplazar `<hash_del_commit>` con el hash del commit al que deseas regresar.
#### ¿PUEDO REGRESAR A UN COMMIT ESPECÍFICO, MANTENIÉNDOME EN MI RAMA MAIN?
Sí, puedes regresar a ese punto en tu rama `main`, pero debes tener en cuenta que esto modificará el historial de tu rama. Para hacerlo, puedes usar el comando `reset` de Git. Aquí te dejo un ejemplo:
-
  ```
  git checkout main
  git reset --hard <hash_del_commit>
  ```

Donde `<hash_del_commit>` es el identificador único del commit al que deseas regresar.
Por favor ten en cuenta que el comando `reset --hard` es destructivo, lo que significa que **perderás cualquier cambio no comprometido** que tengas en tu rama `main`. Asegúrate de haber guardado o comprometido cualquier cambio que desees conservar antes de ejecutar este comando.
Si deseas mantener los cambios realizados después del commit al que deseas regresar, puedes usar el comando `git revert`. Este comando crea un nuevo commit que deshace los cambios realizados en el commit especificado, sin alterar el historial de la rama.


  ```
  git checkout main
  git revert <hash_del_commit>
  ```
-

### Mostrar la etiqueta actual
```git
git describe --tags
```

### Corregir el último commit
```git
git commit --amend
```

## Cómo trabajar con orígenes en Git
Para ver el origen del repositorio actual en Git, puedes usar el comando `git remote -v`. Este comando muestra todas las conexiones remotas que tienes con otros repositorios. Aquí te dejo cómo sería:
```bash
git remote -v
```
Este comando te mostrará algo como esto:
```bash
origin  https://github.com/usuario/repositorio.git (fetch)
origin  https://github.com/usuario/repositorio.git (push)
```
Este comando te mostrará algo como esto:
```bash
origin  https://github.com/usuario/repositorio.git (fetch)
origin  https://github.com/usuario/repositorio.git (push)
```
En este ejemplo, ‘origin’ es el nombre predeterminado que Git da al  servidor desde donde clonaste el repositorio, y la URL que sigue es la   dirección del repositorio. Los términos ‘(fetch)’ y ‘(push)’ indican que  esta dirección se utiliza tanto para traer (fetch) como para enviar   (push) commits.








## Cómo deshacer cambios en Git
Obtener la clave del commit al que se desea retroceder
```git
git log --oneline
```
Retroceder al commit deseado
```bash
git reset --mixed <clave>
```
## Modificar un repositorio
### Cambiar el URL remoto de un repositorio.
**In order to change the URL of a Git remote, you have to use the “git remote set-url” command and   specify the name of the remote as well as the new remote URL to be   changed.**  
```bash
git remote set-url <remote_name> <remote_url>
```
- For example, let’s say that you want to **change the URL of your [Git origin remote](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)**.
- In order to achieve that, you would use the “set-url” command on the “origin” remote and you would specify the new URL.
```bash
git remote set-url origin https://git-repo/new-repository.git
```
- In order to verify that the changes were made, you can use the “git remote” command with the “-v” option (for verbose)
```bash
git remote -v
```
## Cómo eliminar un repositorio local Git sin eliminar los archivos
- Para eliminar un repositorio local de
Git sin eliminar los archivos, puedes simplemente eliminar la carpeta   ".git" del directorio principal del repositorio. La carpeta ".git" es la  carpeta oculta que almacena toda la información del control de   
versiones de Git, incluyendo la información del historial de cambios y   la configuración.  

Para hacer esto, sigue los siguientes pasos:  
- Abre la terminal o línea de comandos en tu computadora.
- Navega hasta el directorio principal del repositorio de Git que deseas eliminar. Por ejemplo, si el repositorio está en el directorio   "MiProyecto", ingresa el siguiente comando:  
```bash
cd MiProyecto  
```  

- Verifica que estás en el directorio correcto ingresando el comando:
```bash
ls -a  
```

Esto mostrará una lista de todos los archivos y carpetas, incluyendo la carpeta oculta ".git".  
- Para eliminar la carpeta ".git", ingresa el siguiente comando:  

```bash
rm -rf .git  
```

Nota: Este comando es peligroso, ya  que eliminará la carpeta ".git" y todos sus subdirectorios y archivos   
sin confirmación adicional. Asegúrate de estar en el directorio correcto  antes de ejecutar este comando.  

Una vez que hayas eliminado la   carpeta ".git", ya no podrás realizar ninguna operación de control de   
versiones de Git en el repositorio, pero todos los archivos permanecerán  en su lugar. Si deseas crear un nuevo repositorio de Git en el mismo   directorio en el futuro, simplemente inicializa un nuevo repositorio con  el comando "git init".
## Gitea
Crear nuevo repositorio
```git
touch README.md
git init
git checkout -b main
git add README.md
git commit -m "first commit"
git remote add origin https://git.inorizonti.com/Bisstox/deleteme.git
git push -u origin main
```
Asignar repositorio local existente a gitea
```
git remote add origin https://git.inorizonti.com/Bisstox/deleteme.git
git push -u origin main
```
Remover origen remoto
```git
git remote remove origin
```
Ver repositorio remoto
```git
git remote -v
```








