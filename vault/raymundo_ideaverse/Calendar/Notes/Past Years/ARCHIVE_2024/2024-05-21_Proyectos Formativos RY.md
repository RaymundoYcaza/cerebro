---
created: 2024-05-21 
---
- #+BEGIN_QUOTE
  "He aquí el ojo de Jehová sobre los que le temen, Sobre los que esperan en su misericordia, **Para librar sus almas de la muerte, Y para darles vida en tiempo de hambre**. Nuestra alma espera a Jehová; Nuestra ayuda y nuestro escudo es él.''
  — ( Salmos 33:18-20 )
  #+END_QUOTE
- 📙 [[Guía Zettelkasten]] | [[Conocimiento]]
- Categorías: [[creatividad 🎭]] [[tecnologia 👨‍💻]] [[negocios 💼]] [[Desarrollo Personal 👤]]
- # Proyectos de Formación
	- ## Estadística
	- ## Finanzas
	- ## Álgebra lineal
		- Fundamentos de álgebra
		  collapsed:: true
			- Álgebra de **Aurelio Baldor**
			- Álgebra y Trigonometría con Geometría Analítica de **Earl W. Swokowski**
		- Álgebra Lineal
		  collapsed:: true
			- “Fundamentos De Álgebra Lineal” de Ron Larson: Este libro presenta de manera clara, y con mucho detalle cada uno de los temas2.
			  “Introducción al álgebra lineal” de Gilbert Strang: Este libro es una excelente introducción al álgebra lineal.
			- “Álgebra Lineal” de David C. Lay: Este libro explica los conceptos de manera clara y detallada, con ejemplos útiles y prácticos. Es uno de los libros más solicitados de álgebra lineal.
			- “Álgebra Lineal para estudiantes de ciencias e ingenierías” de Eduardo Espinoza Ramos1: Este libro es uno de los más buscados por los estudiantes de ciencias e ingenierías.
			- “Álgebra Lineal – 7ma edición” de Stanley I. Grossman: Este libro abarca una gran cantidad de temas de álgebra lineal y es muy solicitado por estudiantes de nivel superior.
	- ## Desarrollo Backend
	- ## Automatización de Procesos de Negocio
-
- # Producción de Contenido
	- ## Procedimiento Zettelkasten
	  collapsed:: true
		- La organización del conocimiento el Zettelkasten se realizaba en tarjetas. Lo que fallaba en mi sistema de Logseq, era que yo pensaba que cada bloque era una nota; pero no lo era mientras no creara propiedades para cada uno de esos bloques. Al crear propiedades consistentes en cada bloque, este se convierte en una tarjeta con datos que puedo clasificar, correlacionar y filtrar en las consultas para mostrarlas de forma estructurada.
		- En los [[Extractos 📜]] "atrapo" las ideas que me han llamado la atención;
		- Luego, las proceso convirtiéndolas en [[notasBibliograficas 🌰]] , para lo que necesito también haber creado [[notasReferencia 📝]]
		- Las [[notasBibliograficas 🌰]] son el lugar donde dejo testimonio de la tormenta de ideas que surge en mi mente y que me lleva a sintetizar la idea final.
		- Las [[notasPermanentes 🌱]] son la versión "pulida" de la idea final resultante de las [[notasBibliograficas 🌰]]
		-
	- ## Tipos de fuentes de referencia
	  collapsed:: true
		- [[Libros]]
		- [[Cursos]]
		- [[Videos]]
		- [[Conversaciones]]
		- [[Blogs]]
		- [[RRSS]]
		- [[Prensa]]
		- [[Tesis]]
		- [[Artículos]]
		- [[Videojuegos]]
	- ## Fuentes de referencia
	  collapsed:: true
		- {{query (and [[Conocimiento]] (not [[Templates]]) (property :categoria))}}
		  query-table:: true
		  query-properties:: [:captura :page :categoria :estado]
		-
		-
	- ## Extractos pendientes
	  collapsed:: true
		- {{query (and [[Extractos 📜]] [[pendientes]] (not [[Templates]]))}}
		  query-table:: true
		  query-properties:: [:page :extracto :fuente :referencia :estado]
		-
		-
	- ## Notas bibliográficas pendientes
	  collapsed:: true
		- {{query (and [[🌰notasBibliograficas]] [[pendientes]] (not [[Templates]]))}}
		  query-table:: true
		  query-properties:: [:nota :page :etiquetas]
		-
-