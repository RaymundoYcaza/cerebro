---
title: "Cómo limitar el área de trabajo en Excel"
snippet: ""
cluster: false
draft: false
description: "Aprende a limitar el área de trabajo en Excel para enfocarte en una zona específica de tu hoja de cálculo."
publishDate: "2013-06-24"
category: "Herramientas en Excel"
tags:
  [
    "Excel Avanzado",
    "Presentación",
    "Trucos Excel",
    "🤖 Automatización con Excel",
  ]
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
slug: automatizacion-con-excel/area-de-trabajo-en-excel
---

Cuando te hablo de limitar el área de trabajo en Excel, me refiero a definir una zona de tu hoja de trabajo en la que el usuario pueda trabajar, sin poder ver nada más.

## ¿Y para que me interesa limitar el área de trabajo?

Si necesitas esconder fórmulas de la vista de tus usuarios / clientes (especialmente aquellas que realizan cálculos delicados) o si necesitas darle un formato más al estilo formulario, esta técnica te resultará interesante.

[![[como-limitar-el-area-de-trabajo-en-excel-000067-300x300.jpg]]](http://raymundoycaza.com/wp-content/uploads/como-limitar-el-area-de-trabajo-en-excel-000067.jpg)

## Ocultando lo que sobra

Ya te mostre cómo (http://raymundoycaza.com/como-proteger-un-rango-de-celdas-en-una-hoja-de-excel/) de tu hoja de trabajo. Esto también te ayudaría a proteger tus fórmulas; pero las celdas aún quedarian visibles.

La idea es esconder todo lo que sobre, de manera que, vas a elegir aquellas columnas y filas que no te interesa mostrar y procederas de la siguiente forma:

- Seleccionando las primera columna “en blanco” utiliza el atajo **CTRL + Mayúsculas + Flecha derecha**, de manera que se seleccionen todas las columnas de aquí en adelante. [![[como-limitar-el-area-de-trabajo-en-excel-000069-300x300.jpg]]](http://raymundoycaza.com/wp-content/uploads/como-limitar-el-area-de-trabajo-en-excel-000069.jpg) Luego, harás un clic derecho sobre el encabezado de cualquiera de estas columnas y elige la opción ‘Ocultar’. [![[como-limitar-el-area-de-trabajo-en-excel-000071-298x300.jpg]]](http://raymundoycaza.com/wp-content/uploads/como-limitar-el-area-de-trabajo-en-excel-000071.jpg)
- Ahora… Sí, ¡exacto! Harás lo mismo con las filas. [![[como-limitar-el-area-de-trabajo-en-excel-000072-300x300.jpg]]](http://raymundoycaza.com/wp-content/uploads/como-limitar-el-area-de-trabajo-en-excel-000072.jpg) Solo selecciona la primera fila en blanco y, esta vez, con la combinación de teclas **CTRL + Mayúsculas + Flecha abajo**, seleccionarás todas las filas que no quieres mostrar. Con un clic derecho sobre su encabezado y eliges la opción ‘Ocultar’. [![[como-limitar-el-area-de-trabajo-en-excel-000073-300x300.jpg]]](http://raymundoycaza.com/wp-content/uploads/como-limitar-el-area-de-trabajo-en-excel-000073.jpg)

### Y para terminar…

Ya tienes delimitada tu área de trabajo. Con esto es muy difícil que tus usuarios se pierdan en la inmensidad de una hoja de trabajo y también ((http://raymundoycaza.com/10-tips-excel-para-mejorar-tus-archivos); pero… para evitar que puedan moverse de esta área desplazándose con las barras de desplazamiento, vas a decirle a Excel que no se mueva más allá de los límites que tú quieres.

Esto se consigue realizando los siguientes pasos:

1. Dirígete a la ficha programador. Si no la encuentras, (http://raymundoycaza.com/ficha-programador).
2. En el apartado ‘Controles’, pincha sobre la opción ‘Propiedades’. [![[como-limitar-el-area-de-trabajo-en-excel-000074-300x234.jpg]]](http://raymundoycaza.com/wp-content/uploads/como-limitar-el-area-de-trabajo-en-excel-000074.jpg)
3. Verás que se abre una pequeña ventana. En ella, busca la propiedad llamada ‘ScrollArea’ y en ella escribe el rango del cual no quieres que Excel se mueva.[![[como-limitar-el-area-de-trabajo-en-excel-000075-300x123.jpg]]](http://raymundoycaza.com/wp-content/uploads/como-limitar-el-area-de-trabajo-en-excel-000075.jpg)

Ahora, verás que no puedes desplazarte del área que tú has definido. ¿Interesante, verdad?

### ¡Y ya está!

Con esta técnica y algo de formato, ya estás listo/a para desarrollar tus formularios personalizados en Excel. Imagínate si lo combinas con (http://raymundoycaza.com/macros-de-excel)… ¡El resultado puede ser impresionante!

Ahora te dejo a solas con tus ideas. A partir de aquí, puedes expandir tus opciones para tus modelos en Excel y darle rienda suelta a tu imaginación. No dejes de poner en práctica este consejo.

Si te ha gustado este artículo, ayúdame a difundirlo pinchando en los iconos de las redes sociales.

¡Nos vemos!