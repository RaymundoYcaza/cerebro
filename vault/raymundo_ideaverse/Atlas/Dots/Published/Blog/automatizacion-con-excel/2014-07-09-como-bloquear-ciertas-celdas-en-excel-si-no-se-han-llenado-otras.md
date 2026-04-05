---
title: "Cómo bloquear ciertas celdas en Excel, si no se han llenado otras."
snippet: ""
cluster: false
draft: false
description: "Ayer me hicieron una pregunta en Twitter: ¿ Cómo bloquear ciertas celdas en Excel, si no se han llenado otras? Aquí te dejo la respuesta."
publishDate: "2014-07-09"
category: "Macros en Excel"
tags: ["Consultas", "Excel 911", "Macros (VBA)", "🤖 Automatización con Excel"]
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
slug: automatizacion-con-excel/bloquear-ciertas-celdas-en-excel
---

Imagen cortesía de [Freeimages](http://www.freeimages.com/ "Freeimages")

Jonn_Rosales me preguntaba en Twitter sobre cómo podría hacer para bloquear ciertas celdas en Excel, cuando aún el usuario no ha terminado de rellenar otras.

<blockquote class="twitter-tweet" lang="es"><a href="https://twitter.com/RaymundoYcaza">@RaymundoYcaza</a> hola Ray buen dia, una consulta: puedo bloquear de alguna forma la columna "B" si aun no lleno lo de la columna "A"??<div></div>— jon (@jonn_rosales) <a href="https://twitter.com/jonn_rosales/statuses/486549406531854336">julio 8, 2014</a></blockquote>¿Es esto posible?

Pues sí. Como siempre, hay más de una respuesta, pero hoy te daré una de las más simples y con esa base, tu podrás ir experimentando por tu cuenta.

Primero, vas a guardar tu archivo con extensión xlsm.

Luego, en el objeto "Hoja1" vas a insertar el código que te muestro más abajo.

¿Que no recuerdas cómo trabajar con macros?

Entonces pásate de nuevo por la entrada ["escribe tu primera macro en Excel"](http://raymundoycaza.com/escribe-tu-primera-macro-en-excel/ "Escribe tu primera macro en Excel").

¿Listo?

¡Bien! Ahora, vas a insertar el siguiente código dentro de el evento WorkSheet_Change de tu hoja:

Private Sub Worksheet_Change(ByVal Target As Range)

    If Not Intersect(ActiveCell, Range("B1:B10")) Is Nothing Then

        If (\ \= "" Or \ \= "" Or \ \= "" Or \ \= "" Or \ \= "") And Target.Value <> "" Then

            Target.Value \= ""
            MsgBox "No has terminado con la columna A. Debes llenar todos los datos antes de continuar.", vbCritical + vbOKOnly, "RaymundoYcaza.com"

        End If

    End If

End Sub

## ¿Qué es lo que he conseguido con este código?

Cada vez que trates de escribir en cualquier celda de la columna B, dentro del rango B1:B10, Excel borrará cualquier texto que trates de escribir ahí a menos que hayas completado todas las celdas indicadas en la columna A.

### Intersect

Con esta línea, lo que hago es preguntarle a Excel: "¿El cambio se hizo dentro del rango B1:B10?"

Si la respuesta es sí, entonces continúo con la revisión.

### If (\ = "" Or \ = "" ...

Con esta línea estoy preguntando, celda a celda, si está vacía. Es decir, si la celda A2 está vacía o la celda A3 está vacía o la celda A4 está vacía o...

Bueno, ya entiendes la idea.

Si cualquiera de esas condiciones se cumple, entonces proceso a invalidar la acción.

**Mucho ojo:** También considero que el valor asignado no sea vacío ( "" )

Si no hicieras esto, tu programa caería en un bucle infinito.

### Target.Value

Target es el objeto que contiene el valor de la celda que ha cambiado. O mejor dicho, es una referencia a esta celda, por lo que manipular el objeto target, sería casi como estar manipulando la celda misma.

Aquí lo que he hecho es asignarle una cadena vacía en caso de que se cumpla que hay algún dato faltante y con eso obtengo el efecto de "celda bloqueada" que Jonn andaba buscando.

## El archivo terminado

Haz clic en el siguiente botón para obtener el archivo terminado.

[Descargar](http://raymundoycaza.com/wp-content/uploads//bloquear-si-no-esta-completo.xlsm "Descargar el archivo.").

## ¿Qué te parece?

A que no pensabas que era tan sencillo, ¿qué dices?

Claro, esta es una validación básica. Ya queda en ti que la mejores y adaptes a tus necesidades.

Cuéntame, ¿cómo y en qué lo has implementado tú?

Te espero en los comentarios.

¡Nos vemos!

\