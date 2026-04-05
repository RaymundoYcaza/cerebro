---
title: "¿Cómo Sumar Celdas Visibles en Excel? ¡Sin problema!"
snippet: ""
cluster: false
draft: false
description: "¿Buscas la forma de sumar celdas visibles en Excel? Justamente de eso trato en este artículo."
publishDate: "2012-08-13"
category: "Fórmulas en Excel"
tags: ["Fórmulas", "Funciones", "🤖 Automatización con Excel"]
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
slug: automatizacion-con-excel/sumar-celdas-visibles-en-excel
---

#### ¿Quieres únicamente sumar celdas visibles en Excel, sin complicaciones?

Entonces ésto te interesa.

En este artículo conocerás la forma más sencilla de realizar varias operaciones sobre las celdas que están visibles **sin considerar** las celdas ocultas**,** entre ellas **sumar celdas visibles en Excel.**

Si estás leyendo este artículo, seguramente te ha pasado que al usar la función \SUM()\ sobre los datos de un rango filtrado, **el resultado es diferente al que esperabas** ¿No es así?

![[diferencias-funcion-sum-600x4261.png "Diferencias al usar la función SUM"]]

Pues te cuento que la solución a este problema es la función \SUBTOTAL()\

### Sumando las celdas visibles:

La función  \SUBTOTAL()\ nos permite realizar la suma (y otras operaciones) sin considerar aquellas celdas que están ocultas.

Esto es especialmente útil cuando queremos realizar, por ejemplo, una suma sobre un Rango que está Filtrado.

Esta función es muy versátil ya que te permite realizar varias operaciones, entre ellas: Promedio, Conteo, Conteo de Blancos, Suma, etc.

La función \SUBTOTAL()\ te pide sólo dos cosas:

1. El tipo de operación que quieres realizar.
2. El rango sobre el que vas a realizar la operación.

Por lo tanto, la sintaxis de la fórmula es la siguiente:

\=SUBTOTAL (Tipo de Operación, Rango de Celdas)\

**El parámetro Tipo de Operación** recibe, como su nombre indica, el tipo de operación que quieres realizar. En este ejemplo, vamos a realizar una suma, por lo tanto, colocaremos en éste parámetro el número 9.

![[subtotal-parametros1.png "Función SUBTOTAL"]] **El parámetro Rango de Celdas**, recibe el rango sobre el cual vas a realizar la operación. Y por si fuera poco, puedes agregar más de un rango de celdas. Ya estás pensando en las posibilidades ¿Verdad?

Si utilizamos esta función en el ejemplo anterior, podremos filtrar los datos y esta vez sí obtendremos el resultado esperado:

![[resultado-suma-subtotal-600x4261.png "Resultado de la suma con la función Subtotal(]]")

### Un paso más allá...

Seguramente ya tienes varias ideas sobre como sacarle provecho a esta útil función. En la siguiente imagen puedes ver cómo podrías aprovechar su versatilidad para realizar cálculos dinámicos:

![[subtotal-dinamico-001.gif "Subtotal Dinámico"]]

\Si te interesa averiguar más sobre esta función, visita la siguiente dirección: (http://office.microsoft.com/es-es/excel-help/funcion-subtotales-HP010062463.aspx "Función Subtotales")\

### ¿Y tú? ¿Ya usas la función Subtotal?

La función \SUBTOTAL()\ la utilizo muy seguido en mis trabajos debido a su versatilidad. En combinación con otras fórmulas y técnicas de Excel, es capaz de cubrir los más exigentes escenarios.

¿Y qué me cuentas tú? ¿Usas la función Subtotal? ¿Tienes algún otro consejo que quieras compartir? Por favor no dudes en hacerlo usando los botones de compartir que están más abajo.

\ \