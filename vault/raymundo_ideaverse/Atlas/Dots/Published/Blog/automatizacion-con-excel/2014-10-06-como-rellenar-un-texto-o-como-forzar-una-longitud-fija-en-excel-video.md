---
title: "Cómo rellenar un texto o cómo forzar una longitud fija en Excel (Vídeo)"
snippet: ""
cluster: false
draft: false
description: "Cómo rellenar un texto, cuando quieres que éste siempre se mantenga en una cantidad fija de caracteres. ¿Te interesa? ¡Empecemos!"
publishDate: "2014-10-06"
category: "Fórmulas en Excel"
tags: ["Funciones", "Trucos Excel", "🤖 Automatización con Excel"]
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
slug: automatizacion-con-excel/como-rellenar-un-texto
---

Hace unos días recibí un mensaje de Noé, uno de mis suscriptores, en el que me pedía que explicara cómo hacer para que Excel “rellenara” automáticamente un texto, para que éste siempre se mantenga en 40 caracteres.

**¿Qué significa esto?**

Quiere decir que si escribo la palabra “Hola”, que tiene cuatro caracteres, automáticamente se completen, por ejemplo, 40 caracteres.

Es decir, en palabras sencillas, ¿cómo hago para rellenar un texto con espacios o cualquier otra cosa?

¿Te interesa?

¡Empecemos!

<iframe width="450" height="230" src="//www.youtube.com/embed/V3WyFF8T8M4?modestbranding=1&amp;autohide=1&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>

### A partir de aquí, te dejo la transcripción del vídeo

Imagina que tienes la siguiente lista. Como ves, cada item es una palabra diferente y, obviamente, la cantidad de letras en cada una es diferente.

Lo que haremos será crear una columna auxiliar aquí, en la que haremos una copia del texto de la columna original y lo “rellenaremos” con guiones por delante, hasta completar 40 caracteres.

Primero, tenemos que saber cuántos caracteres tiene la palabra en cuestión. Así que utilizamos la función LARGO.

La copiamos hacia abajo y ves cómo te muestra la longitud de cada palabra o cuántas letras tiene cada palabra.

Una vez que ya conocemos la longitud de cada palabra, ya podemos saber cuánto le falta para completar 40 caracteres. Simplemente, vamos a restar de 40 la longitud de la palabra.

Hacemos la operación:

```
40 - LARGO de la palabra.
```

¿Ves? Ya sabemos cuántos guiones debemos rellenar para completar los 40 caracteres.

Ahora, vamos a generar esos guiones con la función REPETIR.

<script>(function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0]; if (d.getElementById(id)) return; js = d.createElement(s); js.id = id; js.src = "//connect.facebook.net/en_US/all.js#xfbml=1"; fjs.parentNode.insertBefore(js, fjs); }(document, 'script', 'facebook-jssdk'));</script>

[Post](https://www.facebook.com/raymundo.ycaza/posts/720926877980154) by [Raymundo Ycaza](https://www.facebook.com/raymundo.ycaza).

Utilizamos la función REPETIR, abrimos paréntesis y le colocamos el caracter que se va a repetir, en este caso el guión. Recuerda que debes especificarlo entre comillas.

El siguiente parámetro será toda la fórmula que hicimos para calcular la cantidad de caracteres que necesitamos y cerramos el paréntesis por el otro lado.

Ahora, puedes ver que se generan los guiones, en función del largo de cada palabra.

El paso final, será concatener esos guiones con la propia palabra, para que se muestre tal y como queremos.

Si quieres que se complete por delante, la concatenas así:

```
=REPETIR(” “;40-LARGO(D2))&D2
```

Pero si quieres que se complete por detrás, la concatenas así:

```
=D2 & REPETIR(” “;40-LARGO(D2))
```

## [](#y-listo)Y listo!

Ya tienes tu propio sistema para auto-rellenar códigos o cualquier otro tipo de texto que necesites, con una sencilla combinación de fórmulas.

Esto puede servirte para ciertos tipos de codificaciones en inventarios o generación de tickets, órdenes de trabajo, etc.

Anímate y pónlo en práctica. Cuéntame cómo te fue y en qué piensas aplicar este truco.

¡Ah! Y si el vídeo te gustó, por favor dale un “me gusta” y compártelo con tus amigos. También agrégate a mis redes sociales para estar al tanto de mis publicaciones.

Y si quieres estar en contacto conmigo a través del correo, suscríbete al boletín. Allí comparto información y promociones exclusivas que no publico en el blog.

¡Nos vemos!

\