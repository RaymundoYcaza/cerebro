---
up:
  - "[[Home]]"
created: 2015-01-01
tags:
  - map
---

Hi Future Self 👋 Here are "best practices" for managing your PKM system. 

> [!NOTE]+ Notes on this note
> This is a sanitized version of my actual note. 
> - ***Almost all content and links have been removed.***
> - This is stuff covered in the LYT Workshop.
> - Nick, go here [[My PKM MOC]].

- Managing my PKM system
	- [[My PKM Folders]]
	- [[My PKM Tags]]
	- [[My PKM Metadata]]
	- [[My PKM Queries]]
	- [[El uso de tags]]
	- [[Creación de People Notes]]
- Managing my PKM workflows ♽
	- *What are my "best practice" workflows for processing the world of ideas?*
	- [[My PKM Workflows - Global Guidelines]]
	- [[My PKM Workflows - Inputs + Outputs]]
	- [[My PKM Workflows - Outputs]]
- Tipos de Notas
	- [[Las notas People]]
- Etiquetas
	- Etiqueta `#map/view`
		- La etiqueta `#map/view` en el LYT Kit de Nick Milo se reserva para **notas que actúan como “vistas” o dashboards dinámicos**, donde se listan o visualizan otras notas mediante consultas (por ejemplo, Dataview). 
		- No debe usarse en notas de contenido atómico ni en Entities o People, sino únicamente en aquellas páginas que ofrecen una **perspectiva agregada** (Inbox, Outbox, Notebox, etc.). 
		- Estas páginas usan `#map/view` para distinguirse de las notas de contenido o de los MOCs tradicionales.
		- **¿Cuándo NO usar `#map/view`?
			- **Notas de contenido o definición** (Entities, People, Topics): estas van en carpetas específicas (`Entities/`, `People/`, `MOCs/`) y no deben llevar `#map/view`.  
			- **MOCs estáticos**: mapas de contenido que se editan manualmente y no dependen de consultas automáticas usan el tag `MOC` o simplemente no llevan `#map/view` [Linking Your Thinking](https://www.linkingyourthinking.com/resources?utm_source=chatgpt.com).
			- **Notas individuales**: evita etiquetarlas como `#map/view`, pues no ofrecen una perspectiva agregada.
- Metadatos
	- [[Metadatos básicos]]
- ¿Qué son los MOCs (“Maps of Content”) de Entities?
	- **MOC de Entities** (p. ej. “Entities MOC” o “Things MOC”)
		- Es una nota de alto nivel que **lista y organiza** todas las Entity Notes en un solo lugar, usando enlaces y a menudo consultas de Dataview.    
		- Sirve como **índice temático** para navegar rápidamente por todas las entidades de un tipo (p. ej. tecnologías, personas, proyectos).
	- **MOCs específicos de tema** (p. ej. “Docker MOC”)
		- Aunque Docker existe como nota Entity, puedes crear un **Docker MOC** que profundice en subtemas (arquitectura, casos de uso, alternativas) y lo relaciones por `up:` a un MOC padre como “Things” o “Technologies”
- ¿Cuándo una nota será de tipo `entities` o de tipo `people`?
	- En el esquema **ACCESS** de LYT (Linking Your Thinking), conviene distinguir entre:
		1. **Entities**: notas “ligeras” que representan sustantivos concretos (tecnologías, conceptos, organizaciones, objetos, etc.).
		2. **People**: notas dedicadas a personas individuales, donde recoges biografía, rol, relaciones, etc.
- Uso de propiedades
	 -  In
		**Diferenciar “pertenencia” de “vinculación”**
		- `up` genera un enlace al padre jerárquico; `related` sugiere conexiones laterales; `in` funciona como una **etiqueta de pertenencia**: la nota “está en” esa colección.
		- `in` Te ayuda a **mantener separados** los vínculos de navegación estándar de la agrupación temática.
		**Controlar inclusiones en múltiples contextos**
		- Una misma nota puede tener varios `related` o `up`, pero **solo un** `in` (o ninguno, si no quieres que aparezca en ningún índice).
		- Si necesitas que aparezca en más de un MOC, normalmente creas **una nota puente** en cada MOC que transcluya o enlace a la nota original, en lugar de multiplicar `in`.
		**¿Cuándo debes usar `in`?**
		- **Al construir un MOC**: cuando un tema está maduro y quieres que tus notas aparezcan **ordenadas** bajo ese tema sin tener que listarlas manualmente.
		- **Para colecciones dinámicas**: si usas Dataview, puedes hacer queries como `TABLE file.link WHERE in = this.file.name ` y así tu MOC se autorellena con todo lo etiquetado `in: [[MOC – Tema]]`.
			- **Cuando la nota es un “miembro” de un grupo cerrado**: por ejemplo, un conjunto de herramientas, un grupo de lecturas clave o un proyecto concreto.

