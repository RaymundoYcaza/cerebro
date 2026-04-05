---
title: "Cómo Obtener el Nombre de Archivo en Excel, usando macros."
snippet: ""
cluster: false
draft: false
description: "Aprende a obtener el nombre de archivo en Excel mediante macros. Simplifica la gestión de tus archivos y procesos."
publishDate: "2016-02-17"
category: "Macros en Excel"
tags: ["Macros (VBA)", "🤖 Automatización con Excel"]
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
slug: automatizacion-con-excel/obtener-el-nombre-de-archivo-en-excel
---

Cuando trabajamos con Excel y empezamos a manejar las macros, se nos vienen muchas ideas nuevas para mejorar nuestros archivos. Y esas nuevas ideas, muchas veces nos llevan a buscar nuevos conocimientos para poder realizarlas.

Un ejemplo de esto, puede verse cuando llega el momento en el que necesitas **obtener el nombre del archivo en Excel**, para colocarlo en una celda.

¿Te interesa descubrir cómo hacerlo?

¡Pues, empecemos!

<iframe src="https://www.youtube.com/embed/Ah9Oj-CRFuI?showinfo=0" allowfullscreen="allowfullscreen" width="560" height="315" frameborder="0"></iframe>

## ¿Cómo Obtener el Nombre de Archivo en Excel, usando macros?

(TRANSCRIPCIÓN DEL VÍDEO)

Lo primero que vamos a hacer, será acceder a la ventana del editor de código de visual basic, y vamos a insertar un nuevo módulo.

Dentro de este módulo, crearemos una función cuyo nombre será “ObtenerNombreLibro”. Esta función realizará la tarea de “escribir” en la celda activa, el nombre que tenga el libro activo. Es decir, el libro que está activo en el momento de ejecutarse la macro.

Si ejecutamos la macro, veremos que donde sea que esté la celda activa, se escribirá en ella el nombre del libro. En mi caso, el nombre del archivo es “Obtener el Nombre del Archivo.xlsm”.

Pero ¿y qué hago si necesito escribirlo en una celda específica? Por ejemplo, en mi caso, quiero escribirlo en la celda C4 de la Hoja2.

Para eso voy a escribir otra función y de esta manera me evito borrar la función anterior.

A esta nueva función le daré el nombre “insertarNombreLibro”. En su interior, le diré que escriba en la celda C4, pero de la Hoja2. Esto se consigue utilizando el objeto “Range”, al cual le pasaré el nombre de la hoja, seguido de la referencia a la celda. No olvides separarlos por un signo de admiración, como estoy haciendo yo.

Entonces, una vez listo esto, cerramos el paréntesis y le decimos que el valor de este punto en la hoja, será igual al nombre del libro activo, que ya vimos cómo lo obtenemos.

Ahora, si probamos la función, veremos cómo no importa dónde nos ubiquemos, siempre se escribirá el nombre del libro, en la celda C4 de la hoja 2.

Pero, pongamos un último ejemplo. ¿Qué tal si quiero hacerlo con un nombre de rango? Es decir, utilizar una celda con nombre, en lugar de escribir su referencia.

En mi caso, la celda C4 ya tiene un nombre de rango, el cual es “defNombreArchivo”. Y lo que quiero es escribir en esa celda el nombre del archivo, utilizando el nombre definido. Para esto, crearé otra función, que llamaré “mostrarNombreLibro”. En esta función, la única diferencia que tendrá respecto de la anterior, es que ya no usaremos el objeto “Range”, sino que directamente escribiremos, entre paréntesis angulares o corchetes, el nombre de la celda. En este caso, “\”.

Fíjate que aquí ya no usamos el atributo “.value”, sino que directamente asignamos con el igual el nombre del libro, tal y como lo hemos venido haciendo en los casos anteriores.

Si probamos nuevamente el código, veremos que se comporta exactamente igual que si lo hubiéramos realizado con referencias, solo que al usar celdas con nombre, se facilita mucho la escritura y el mantenimiento a futuro de nuestros archivos.

Y eso es todo por hoy. Espero que con estos consejos puedas comenzar a crear tus archivos mejorados y te inspire a crear nuevas herramientas que potencien tu productividad con Excel.

¡Nos vemos!

\