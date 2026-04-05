---
in:
  - "[[Git]]"
---



![[GMWrtUTXwAAYucU.jpg]]


- [**Manténlo corto**: Los mensajes de commit deben ser breves, idealmente menos de 150 caracteres](https://initialcommit.com/blog/git-commit-messages-best-practices)[1](https://initialcommit.com/blog/git-commit-messages-best-practices).
	- Ejemplo en inglés: “Add login feature”
	- Traducción al español: “Añade la función de inicio de sesión”
	- (https://initialcommit.com/blog/git-commit-messages-best-practices)[1](https://initialcommit.com/blog/git-commit-messages-best-practices).
- - [**Usa el modo imperativo**: Este es el tono que se debe usar en los mensajes de commit](https://initialcommit.com/blog/git-commit-messages-best-practices)[1](https://initialcommit.com/blog/git-commit-messages-best-practices).
	- Ejemplo en inglés: “Fix bug in payment gateway”
	- Traducción al español: “Corrige error en la pasarela de pago”
- - [**Resume el cambio**: Da una visión general del cambio y cómo lo hiciste](https://www.freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like/)[2](https://www.freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like/).
	- Ejemplo en inglés: “fix: correct typo in user registration form”
	- Traducción al español: “fix: corrige error tipográfico en el formulario de registro de usuario”
- - [**Consistencia**: La consistencia mejora la velocidad de comprensión de la lectura](https://initialcommit.com/blog/git-commit-messages-best-practices)[1](https://initialcommit.com/blog/git-commit-messages-best-practices).
	- Ejemplo en inglés: “Refactor user authentication process”
	- Traducción al español: “Refactoriza el proceso de autenticación de usuario”
- - [**Especifica el tipo de cambio**: Esto ayuda a los demás a entender mejor tu contribución](https://www.freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like/)[2](https://www.freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like/).
	- Ejemplo en inglés: “feat: add search functionality”
	- Traducción al español: “feat: añade funcionalidad de búsqueda”

### Detalle en el título
- De acuerdo con las buenas prácticas, generalmente no es necesario especificar el nombre de los archivos o del módulo donde se realizan los cambios en el título del commit. El título del commit debe ser un resumen conciso de los cambios realizados.
- La descripción del commit, que es opcional, puede proporcionar detalles adicionales sobre los cambios realizados, incluyendo los nombres de los archivos o módulos afectados si es relevante. Sin embargo, la descripción debe centrarse en explicar *el por qué de los cambios, más que el qué*.
- Además, Git proporciona herramientas para ver exactamente qué líneas de código han cambiado en cada archivo, por lo que los detalles específicos de los cambios se pueden inferir a partir de la propia herramienta.


### Tipos de cambio:
- Inglés:
	- `feat` – a new feature is introduced with the changes
	- `fix` – a bug fix has occurred
	- `chore` – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
	- `refactor` – refactored code that neither fixes a bug nor adds a feature
	- `docs` – updates to documentation such as a the README or other markdown files
	- `style` – changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
	- `test` – including new or correcting previous tests
	- `perf` – performance improvements
	- `ci` – continuous integration related
	- `build` – changes that affect the build system or external dependencies
	- `revert` – reverts a previous commit
- Español:
	-
	  | Tipo de cambio | Descripción en español | Ejemplo de uso |
	  |---|---|---|
	  | feat | Se utiliza para describir contribuciones donde se añade información o una nueva funcionalidad a un proyecto de código abierto1. | Si estás añadiendo una nueva funcionalidad de búsqueda a tu proyecto, podrías usar: feat: añade funcionalidad de búsqueda. |
	  | docs | Se utiliza comúnmente para describir revisiones a las versiones actuales o actualizaciones a la documentación de un proyecto de código abierto1. | Si estás actualizando la documentación de tu proyecto, podrías usar: docs: actualiza la documentación del proyecto1. |
	  | fix | Se utiliza típicamente para arreglar errores en la base de código del proyecto o pequeños errores gramaticales en la documentación del proyecto1. | Si estás corrigiendo un error en tu proyecto, podrías usar: fix: corrige error en la función de inicio de sesión. |
	  | chore | Se utiliza a menudo para una contribución que puede llevar más tiempo de lo habitual para terminar1. | Si estás trabajando en una tarea que lleva mucho tiempo, podrías usar: chore: optimiza el rendimiento de la base de datos. |
- Ejemplos de tipos de cambio:
	- feat
		- 1. feat: add login feature
		- 2. feat: implement dark mode
		- 3. feat: introduce multi-language support
		- 4. feat: add drag and drop functionality
		- 5. feat: integrate with third-party API
	- fix
		- 1. fix: resolve null pointer exception in login module
		- 2. fix: correct typo in error message
		- 3. fix: handle edge case in payment gateway
		- 4. fix: improve responsiveness of homepage
		- 5. fix: address memory leak in data processing module
	- chore
		- 1. chore: update dependencies to latest version
		- 2. chore: refactor code for better readability
		- 3. chore: optimize database queries
		- 4. chore: clean up deprecated code
		- 5. chore: improve test coverage
	- docs
		- 1. docs: update README with new feature details
		- 2. docs: correct typo in CONTRIBUTING guide
		- 3. docs: add code of conduct
		- 4. docs: update API documentation
		- 5. docs: improve installation instructions
	- refactor
		- 1. `refactor: simplify login logic`
		- 2. `refactor: extract method for readability`
		- 3. `refactor: move helper functions to utils file`
		- 4. `refactor: update to use new API endpoint`
		- 5. `refactor: improve error handling`
	- style
		- 1. `style: fix indentation in index.js`
		- 2. `style: remove trailing whitespace`
		- 3. `style: add missing semicolons`
		- 4. `style: update code to follow style guide`
		- 5. `style: improve readability of comments`
	- test
		- 1. `test: add unit tests for login module`
		- 2. `test: update integration tests for payment gateway`
		- 3. `test: fix broken test case`
		- 4. `test: improve test coverage for user registration`
		- 5. `test: refactor tests to remove duplication`
	- perf
		- 1. `perf: improve loading speed of homepage`
		- 2. `perf: optimize database queries for faster response`
		- 3. `perf: reduce memory usage in data processing module`
		- 4. `perf: improve efficiency of sorting algorithm`
		- 5. `perf: optimize code for faster execution`
	- ci
		- 1. `ci: add job to run unit tests`
		- 2. `ci: update workflow to deploy to staging`
		- 3. `ci: fix broken build`
		- 4. `ci: add step to publish package`
		- 5. `ci: optimize build for faster execution`
	- build
		- 1. `build: update dependencies`
		- 2. `build: fix error in build script`
		- 3. `build: add script to generate documentation`
		- 4. `build: optimize build for smaller bundle size`
		- 5. `build: configure project for production`
	- revert
		- 1. `revert: undo recent changes to login module`
		- 2. `revert: roll back to previous version of payment gateway`
		- 3. `revert: undo changes to database schema`
		- 4. `revert: remove recently added feature`
		- 5. `revert: undo changes that introduced a bug`

### Reglas generales
- Se utilizará el título del commit más la descripción
- En el título se implementarán las buenas prácticas detalladas anteriormente
- En la descripción se incluirá el código de orden de la que desprende el cambio y otros detalles en caso de ser necesario.

- ### Referencias
	- [How to Write Better Git Commit Messages – A Step-By-Step Guide (freecodecamp.org)](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)
	-

## Resumen
- La especificación de Commits Convencionales es una convención ligera sobre los mensajes de commits.  
- Proporciona un conjunto sencillo de reglas para crear un historial de commits explícito;
  lo que hace más fácil escribir herramientas automatizadas encima del historial.  
- Esta convención encaja con [SemVer](http://semver.org/lang/es/), al describir en los mensajes de los commits las funcionalidades, arreglos, y cambios de ruptura hechos.
- El mensaje del commit debe ser estructurado de la siguiente manera:
  
---
  ```
  <tipo>[ámbito opcional]: <descripción>
  
  [cuerpo opcional]
  
  [nota(s) al pie opcional(es)]
  ```
  
---
- El commit contiene los siguientes elementos estructurales, para comunicar la intención a los consumidores de tu librería:
- **fix:** un commit de _tipo_ `fix` corrige un error en la base del código (se correlaciona con [`PATCH`](http://semver.org/#summary) en el Versionado Semántico).
- **feat:** un commit de _tipo_ `feat` introduce una nueva funcionalidad en la base del código (se correlaciona con [`MINOR`](http://semver.org/#summary) en el Versionado Semántico).
- **BREAKING CHANGE:** un commit que contiene la nota al pie `BREAKING CHANGE:`, o que agrega un `!` después del tipo/ámbito, introduce un cambio de ruptura de API (se correlaciona con [`MAJOR`](http://semver.org/#summary) en el Versionado Semántico).
    
    Un BREAKING CHANGE puede ser parte de commits de cualquier _tipo_.  
    
- _tipos_ distintos a `fix:` y `feat:` están permitidos, por ejemplo [@commitlint/config-conventional](https://github.com/conventional-changelog/commitlint/tree/master/%40commitlint/config-conventional) (basados en [la convención de Angular](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)) que recomienda `build:`, `chore:`, `ci:`, `docs:`, `style:`, `refactor:`, `perf:`, `test:`, y otros.
- _notas al pie_ distintas de `BREAKING CHANGE:` pueden ser añadidas y siguen una convención similar al [formato git trailer](https://git-scm.com/docs/git-interpret-trailers).
    
      
    Tipos adicionales no son obligatorios en la especificación de Commits Convencionales,  
    y no tienen un efecto implícito en el Versionado Semántico (al menos que incluyan un BREAKING CHANGE).  
      
    Un ámbito puede ser añadido al tipo de un commit, para proveer  
    información adicional contextual y debe ser contenido entre paréntesis,  
    ej., `feat(parser): add ability to parse arrays`.


## Ejemplos
- ### Mensaje de commit con descripción y cambio de ruptura en la nota al pie
  
  ```
  feat: allow provided config object to extend other configs
  
  BREAKING CHANGE: `extends` key in config file is now used for extending other config files
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con--para-llamar-la-atención-al-cambio-de-ruptura) Mensaje de commit con  `!`  para llamar la atención al cambio de ruptura
  
  ```
  refactor!: drop support for Node 6
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con-ambos--y-breaking-change-en-la-nota-al-pie) Mensaje de commit con ambos  `!`  y BREAKING CHANGE en la nota al pie
  
  ```
  refactor!: drop support for Node 6
  
  BREAKING CHANGE: refactor to use JavaScript features not available in Node 6.
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-sin-cuerpo) Mensaje de commit sin cuerpo
  
  ```
  docs: correct spelling of CHANGELOG
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con-ámbito) Mensaje de commit con ámbito
  
  ```
  feat(lang): added polish language
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con-cuerpo-multi-párrafo-y-múltiples-notas-al-pie) Mensaje de commit con cuerpo multi-párrafo y múltiples notas al pie
  
  ```
  fix: correct minor typos in code
  
  see the issue for details
  
  on typos fixed.
  
  Reviewed-by: Z
  Refs #133
  ```


##  Ejemplos
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con-descripción-y-cambio-de-ruptura-en-la-nota-al-pie) Mensaje de commit con descripción y cambio de ruptura en la nota al pie
  
  ```
  feat: allow provided config object to extend other configs
  
  BREAKING CHANGE: `extends` key in config file is now used for extending other config files
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con--para-llamar-la-atención-al-cambio-de-ruptura) Mensaje de commit con  `!`  para llamar la atención al cambio de ruptura
  
  ```
  refactor!: drop support for Node 6
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con-ambos--y-breaking-change-en-la-nota-al-pie) Mensaje de commit con ambos  `!`  y BREAKING CHANGE en la nota al pie
  
  ```
  refactor!: drop support for Node 6
  
  BREAKING CHANGE: refactor to use JavaScript features not available in Node 6.
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-sin-cuerpo) Mensaje de commit sin cuerpo
  
  ```
  docs: correct spelling of CHANGELOG
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con-ámbito) Mensaje de commit con ámbito
  
  ```
  feat(lang): added polish language
  ```
- ### [](https://www.conventionalcommits.org/es/v1.0.0/#mensaje-de-commit-con-cuerpo-multi-párrafo-y-múltiples-notas-al-pie) Mensaje de commit con cuerpo multi-párrafo y múltiples notas al pie
  
  ```
  fix: correct minor typos in code
  
  see the issue for details
  
  on typos fixed.
  
  Reviewed-by: Z
  Refs #133
  ```



