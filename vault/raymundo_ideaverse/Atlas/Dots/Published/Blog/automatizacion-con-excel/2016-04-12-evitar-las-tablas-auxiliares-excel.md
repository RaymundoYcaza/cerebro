---
title: "Cómo evitar las Tablas Auxiliares en Excel"
snippet: ""
cluster: false
draft: false
description: "Descubre cómo evitar el abuso de las Tablas Auxiliares en Excel y mejora la calidad de tus informes."
publishDate: "2016-04-12"
category: "Herramientas en Excel"
tags: ["Trucos Excel", "🤖 Automatización con Excel"]
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
slug: automatizacion-con-excel/tablas-auxiliares
---

Cuando utilizamos las Tablas Auxiliares en Excel y no hacemos un análisis previo, podemos fácilmente llegar a cometer un abuso de ellas y convertirlas en auténtica basura para nuestros reportes.

Un lindo archivo de Excel puede verse plagado de hojas y rangos con tablas auxiliares, muchas de ellas innecesarias.

Como parte de este plan para erradicar el uso indiscriminado de Tablas Auxiliares en Excel, he decidido mostrarte una idea para que puedas evitarlas y, de paso, un truco te ayudará a lucirte ante tus compañeros.

## Evitando el Uso de Tablas Auxiliares en Excel

<iframe style="width: 560px !important; margin: 0 auto;" src="https://www.youtube.com/embed/SWUJ42heHEc?showinfo=0" allowfullscreen="allowfullscreen" width="560" height="315" frameborder="0"></iframe>

Haz clic en la imagen para ver el vídeo. o [Haz clic aquí para verlo en Youtube](https://youtu.be/SWUJ42heHEc).

### Transcripción del vídeo

A veces tenemos que realizar búsquedas en una tabla para “traducir’ un código y obtener su nombre. Por ejemplo, a veces tenemos el número de un mes y lo que necesitamos es su nombre.

Hasta este punto, nada nuevo; pero ¿por qué meter tantas tablas auxiliares? ¿No sería estupendo que pudiéramos hacer nuestros archivos un poco más elegantes?

Soy Raymundo Ycaza y esto es “Exprimiendo Excel”.

¡Empecemos!

Nos encontramos aquí con un caso típico: Tenemos una tabla con algunas columnas. Una de ellas es la fecha y en la segunda columna necesitamos obtener el día de la semana.

Como puedes ver, yo ya lo he conseguido, a través de la función “DIASEM”.

Y por ahora, todo bien. Con un ligero ejercicio mental, puedo saber qué día de la semana es, revisando el número que me arroja la función.

Pero queremos hacer aún más claro y, por qué no, más elegante el archivo.

Así que utilizamos la función “BUSCARV” para buscar en nuestra tabla auxiliar cuál es el nombre del día de la semana que le corresponde a cada número de los que tenemos aquí.

Bien, hasta este momento, no hemos hecho nada nuevo.

Pero ¿y qué hago con esta tabla auxiliar?

Mmm… Bueno, la puedo poner en una hoja independiente y luego esconderla.

O puedo esconder las columnas…

¡Pero sigue siendo un estorbo!

¿Entonces, cómo nos deshacemos de ella?

Pues meteremos todo ese rango, con sus valores incluidos, dentro de la fórmula.

Primero, utilizaremos el truco de la función “TRANSPONER”.

Una vez que tenemos la función lista y hemos llegado a este punto, no presiones la tecla “Enter”.

En lugar de eso, presiona la tecla “F9”.

Verás que la referencia se ha convertido en sus valores referenciados, dentro de la matriz.

Aunque, claro, como usamos la función “TRANSPONER” ya no están en la misma posición. Recuerda eso.

Ahora, el truco es que puedes seleccionar toda esta parte de aquí, con las llaves incluidas, y lo usarás en lugar de la referencia a la tabla.

Seleccionas todo el rango y lo borras. Ahora pegas los valores que acabamos de copiar… Y presionas la tecla “Enter”.

Verás que te ha dado un error. ¿Por qué?

Pues porque los valores ya no están como al principio. ¿Recuerdas que usamos la función “TRANSPONER”?

Entonces, si los valores están ordenados horizontalmente, utilizaremos una función que realice la búsqueda en horizontal.

¡Sí! La función “BUSCARH”.

Pero como ya teníamos escriba la función “BUSCARV”, entonces solo tenemos que cambiar una letra… ¡Y ahora sí!

Funciona a la perfección.

Con este truco hemos eliminado la necesidad de utilizar tablas auxiliares y nuestro libro tendrá menos basura acumulando polvo por ahí, sin que nos demos cuenta.

Espero que el consejo te sirva y lo apliques a tus nuevos trabajos.

¡Nos vemos! \