---
title: "Cómo ejecutar una macro de Excel N veces o cómo repetir una macro varias veces sin tener que hacerlo una por una."
snippet: ""
cluster: false
draft: false
description: "En esta entrada te explico cómo ejecutar una macro de Excel N veces o cómo repetir una macro varias veces sin tener que hacerlo una por una. ¡Empecemos!"
publishDate: "2015-10-27"
category: "Macros en Excel"
tags:
  [
    "Excel Avanzado",
    "Macros (VBA)",
    "Productividad",
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
slug: automatizacion-con-excel/ejecutar-una-macro
---

En un entorno tan ajetreado como el nuestro y en una época en la que el tiempo cada vez parece más escaso, se hace necesario (y mucho) contar con herramientas, técnicas o inclusive trucos bajo la manga que sean capaces de ayudarnos a realizar nuestras tareas cotidianas en el menor tiempo que sea posible.

¿O tú eres la excepción?

Incluso, cuando ya hemos logrado encontrar esa herramienta, ese truco, o esa (http://raymundoycaza.com/las-macros-en-excel/) que nos ayuda a realizar un montón de trabajo en poco tiempo, podemos sorprendernos a nosotros mismos aún realizando tareas repetitivas que podríamos sacarnos de encima para que la solución sea completa.

Un claro ejemplo de esto, es el tener que repetir dos, tres, cinco, diez o hasta cincuenta veces una macro que hace un montón de trabajo; pero que necesita ser ejecutada más de una vez, por la razón que sea.

Imagínate poder decirle a Excel que ejecute esa macro que hace todo el cuadre y la repita 49 veces, mientras tú vas por un café a relajarte o te diriges al otro piso a buscar ese informe para tu siguiente tarea.

¿Verdad que suena bien?

En esta entrada voy a mostrarte cómo puedes ejecutar tu macro una cantidad indeterminada de veces, sin que tengas que estar en esa silla haciendo clics toda la tarde.

<iframe src="https://www.youtube.com/embed/EymBYsHmLLc?showinfo=0" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

**CLIC EN LA IMAGEN PARA VER EL VÍDEO**

## ¿Cómo entrar en un ciclo repetitivo? Conociendo a los bucles.

Bien, quedemos de acuerdo en algo. Ya tenemos una idea de (http://raymundoycaza.com/curso-macros-en-excel/) y estamos utilizando una (esa es la idea de esta entrada).

Ahora, lo que necesitamos es que esa macro que ya estamos utilizando, se ejecute la primera vez, cuando tú la actives, y además se repita un número 'n' de veces.

Pero ¿cómo se logra esto?

Pues colocando a una macro dentro de una porción de código que se ejecute una y otra vez, tantas veces como tú lo quieras.

A estas porciones de código se las conoce como **bucles**.

Lo único que necesitas es colocar el nombre de la macro dentro de un bucle, indicarle cuántas veces quieres que se ejecute el bucle y el resto es cruzarse de brazos hasta que termine.

## Creando mi primer bucle.

Comenzaremos con algo sencillo. Vamos a mostrar la leyenda: "Estoy escribiendo la línea " y le vamos a poner al final un número que indicará el número de veces que se ha ejecutado la macro.

Para escribir la línea, usaremos la instrucción 'Debug.Print' seguida del texto entre comillas.

Utilizaremos la variable i (la llamaremos 'i' por aquello de que iteración comienza con i) de manera que nos sirva como una especie de 'contador de vueltas' para cada ejecución del bucle.

Luego, utilizaremos la estructura de control FOR, para ejecutar un bucle que realizará el mismo trabajo un total de diez veces.

Para esto, en la estructura FOR, le indicamos que la variable 'i', tomará el valor desde 1 hasta 10 y quedará entendido que aumentará de uno en uno hasta llegar a su valor máximo.

El código quedaría como éste:

Sub MiPrimerBucle()

Dim i As Integer

For i \= 1 To 10
Debug.Print "Estoy escribiendo la línea " & i
Next i

End Sub

Fíjate como estoy utilizando FOR para iniciar el bucle y NEXT para cerrarlo e indicarle a Excel que todo lo que esté entre estas dos marcas, deberá repetirse tantas veces como indique la línea FOR.

El código que estamos ejecutando es sencillo. Con Debug.Print estamos escribiendo un texto que luego concatenamos con la variable 'i', para lo cual usamos el operador de concatenación '&'.

Una vez terminada la ejecución, en la **ventana 'Inmediato'** se mostrará el resultado del bucle, es decir, 10 líneas que se diferencian únicamente por el número al final:

`Estoy escribiendo la línea 1 Estoy escribiendo la línea 2 Estoy escribiendo la línea 3 Estoy escribiendo la línea 4 Estoy escribiendo la línea 5 Estoy escribiendo la línea 6 Estoy escribiendo la línea 7 Estoy escribiendo la línea 8 Estoy escribiendo la línea 9 Estoy escribiendo la línea 10`

¿Ves? Tan sencillo como eso.

Pero claro, tú quieres ejecutar una macro. ¡Vamos por ello!

## ¿Cómo implementar una macro dentro de un bucle?

En realidad, ya hicimos todo el trabajo. Aquí lo único que debes hacer es reemplazar la línea Debug.Print por el nombre de la macro que quieres ejecutar.

¿Así de fácil?

Sí, ¡así de fácil!

Entonces, imaginemos que lo que quieres es ejecutar 10 veces la macro llamada 'CuadreMensual', utilizando el mismo código que te mostré anteriormente:

Sub MiPrimerBucle()

Dim i As Integer

For i \= 1 To 10
CuadreMensual
Next i

End Sub

Como ves, lo único que hice fue reemplazar la parte que se encargaba de escribir la línea en la ventana inmediato y puse el nombre de la macro que quiero ejecutar.

Por supuesto, si has declarado a tu macro como privada y la tienes en otro módulo, entonces no podrás ejecutarla. Ten en cuenta eso.

## ¿Cómo hacer que el número de repeticiones sea variable?

¡Claro! No siempre vas a necesitar ejecutar la macro diez veces. Puede que necesites que se repita siete veces o hasta cincuenta... ¡o más!

Entonces, necesitamos una forma de decirle a Excel justo en el momento en que se va a ejecutar la macro, el número de veces que necesitamos que se ejecute la misma.

Esto lo vamos a hacer utilizando la instrucción 'InputBox', de esta forma:

`intVeces = InputBox("Ingresa el número de veces a repetir:", "Mi Sistema", 10)`

La instrucción 'InputBox', se encarga de mostrar una ventana en la que te pide que escribas un valor y luego lo coloca en una variable. En este caso, en la variable 'intVeces'.

El primer (http://raymundoycaza.com/que-son-los-argumentos-en-excel/), es el texto que servirá de referencia para el usuario, es decir, la isntrucción para que la persona sepa qué es lo que está pidiendo Excel.

El segundo argumento es el título que quieres que aparezca en la ventana.

El tercer argumento es el valor que aparecerá por defecto, para que incluso te ahorres de escribirlo si vas a usar ese valor muchas veces.

Luego, para terminar, ajustamos nuestro código anterior de la siguiente forma:

Sub MiPrimerBucle()

Dim i As Integer
Dim intVeces As Integer

intVeces \= InputBox("Ingresa el número de veces a repetir:", "Mi Sistema", 10)

For i \= 1 To intVeces

    CuadreMensual

Next i

End Sub

Como ves en el código anterior, luego de darle el valor deseado a la variable 'intVeces', la colocamos en el bucle en lugar del número 10 y así tendremos un valor máximo que será variable y se ajustará a lo que necesitemos en cada caso y podremos manejar esas excepciones o variantes de las que no nos libramos nunca al ciento por ciento.

## Conclusión.

Los bucles son estructuras realmente importantes en la programación de macros y le dan una potencia tremenda a nuestros trabajos, dándonos también la flexibilidad que necesitamos como te he mostrado en este caso. No dejes de poner entre tus pendientes el estudio de las estructuras y por supuesto, no dejes de poner en práctica este ExcelConsejo que seguramente va servirte para que puedas agilizar varios de tus trabajos en la oficina.

## ¿Te ha gustado esta entrada?

Si quieres recibir más tutoriales y consejos como éste, entonces no dejes de (#) y si ya lo has hecho, entonces puedes ayudarme a compartir esta entrada en las redes sociales para que otras personas encuentren esa solución que andan buscando.

¡Nos vemos!

\