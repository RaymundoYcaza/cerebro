---
title: "Cómo insertar automáticamente los meses del año en Excel (VÍDEO)"
snippet: ""
cluster: false
draft: false
description: "Aprende cómo insertar automáticamente los meses del año en Excel y olvídate de estarlos escribiendo una y otra vez en tus reportes."
publishDate: "2014-09-22"
category: "Macros en Excel"
tags: ["🤖 Automatización con Excel"]
images: []
resources:
  - name: "featured-image"
image:
  {
    src: "/src/assets/images/2023/ry-portada-generica.png",
    alt: "Raymundo Ycaza",
  }
cover: "/src/assets/images/2023/ry-portada-generica.png"
featuredImage: "images/ry-portada-generica.png"
coverAlt: "Raymundo Ycaza"
domainGroup: automatizacion-con-excel
slug: automatizacion-con-excel/insertar-meses-en-excel
---

Las tareas repetitivas, son las principales responsables de todo ese tiempo perdido en nuestro día a día con Excel.

Un ejemplo de ésto que te cuento, son los listados con los meses del año, que utilizamos generalmente para realizar nuestros reportes o informes.

Así, cuando necesito generar desde cero un listado con los meses debo comenzar a escribir: Enero, febrero, marzo, etc.

### ¿Y qué si quiero autocompletarlos?

Pues, ¡a veces no funciona!

Esto se puede arreglar, con una configuración adicional en tu Excel; pero no es de eso de lo que te voy a hablar ahora.

Quiero proponerte otra solución que puede ser, incluso más cómoda.

Imagina que pulsando un botón... ¡Automáticamente se complete tu listado!

Y no te hablo únicamente de meses. Pueden ser nombres, códigos, productos, maquinaria. ¡Listados de lo que quieras!

¿Te interesa?

Entonces vamos rápidamente a ello.

<iframe width="450" height="230" src="//www.youtube.com/embed/b81hIoUPTN8?modestbranding=1&amp;autohide=1&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>

## Insertar automáticamente los meses del año en Excel

Primero, vas al editor de VBA. Recuerda que en el blog (http://raymundoycaza.com/escribe-tu-primera-macro-en-excel/ "#03 Escribe tu primera Macro en Excel.") si aún no lo tienes claro.

Y luego creamos una rutina, a la que llamaremos **GenerarMeses**.

Aquí colocaremos en la celda activa, el nombre del mes de "Enero".

¡Sencillo!

Ahora, utilizaremos la palabra reservada With con la celda activa, lo que quiere decir que todo lo que utilicemos aquí dentro hará referencia a la celda activa.

Y con el Offset, que significa "desplazar", vamos a bajar una fila; pero sin movernos en las columnas, para escribir allí la palabra "Febrero".

Así, haremos con "Marzo", pero desplazándonos 3 filas. Luego cuatro filas para "Abril", etc.

Al final, habremos completado los doce meses de la misma forma.

Si ejecutas esta macro, verás como automáticamente, aparece el listado en la celda activa. Es decir, en cualquier celda donde esté el cursor en ese momento.

Pero aún nos hace falta darle un poco más de utilidad. Si quieres ejecutar esta macro en cualquier libro que tengas abierto, sin tener que guardarla cada vez, tendrás que colocarla en el libro personal.

Simplemente inserta un módulo en este libro, al que le pondrás el nombre "modMisFunciones".

Ahora, regresa donde tenías el código y córtalo, para luego pegarlo dentro de tu nuevo módulo.

Y no olvides dejarle un comentario para poder saber luego de qué se trata esta función. Recuerda que vas a tener muchas funciones en éste lugar y es bueno saber quién hace qué cosa.

¡Y listo!

Sin embargo, aún podemos hacer algo más para que sea todavía más útil.

¿Qué tal ponerlo a un clic de distancia?

Vamos a insertar un botón aquí en la barra de herramientas de acceso rápido, para que lo tengamos siempre a la mano.

Clic en este botón y luego en "Más comandos".

Ubicamos la sección de las macros...

Buscamos nuestra macro que guardamos en el libro PERSONAL. Si dejas el puntero sobre ella, podrás ver el nombre completo. Recuerda que le pusimos por nombre "GenerarMeses".

Hacemos clic en el botón "Agregar" y verás que se coloca en la columna derecha. Ahora ya podrás ver este botón en la barra de herramientas de acceso rápido, justo al final.

Pero, no nos gusta el icono que aparece por defecto. Así que le hacemos clic en "Modificar".

Seleccionamos un icono que se ajuste a nuestro gusto y le damos clic a aceptar.

Ahora, ya tienes tu botón mágico el cual se encargará de hacer ese trabajo tedioso por ti, cuantas veces quieras.

Ahora, ponlo en práctica y utilízalo para cualquiera que sea la lista que estás repitiendo a diario.

¡Ah! Y déjame tu comentario contándome cómo te fue.

¡Nos vemos!

\