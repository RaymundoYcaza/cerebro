---
created: 2024-05-25 
---



Existen casos en los que nos encontramos con estructuras especiales de respuesta JSON, en la que no solo encontramos datos anidados, sino que nos encontramos con la notación de dos puntos (:) y no sabemos cómo acceder a la variable deseada que se encuentra en uno de estos nodos.
![[IJcimage_1707437283016_0.png]]
La estructura de JSON en la que una propiedad tiene un nombre que contiene caracteres especiales como ":" se denomina "JSON con propiedades con nombres especiales". En este caso particular, la propiedad "wp:featuredmedia" tiene un nombre especial debido al ":" que está presente en él.
Cuando trabajas con este tipo de estructura en JSON, es común que las bibliotecas o herramientas que procesan JSON proporcionen una forma de acceder a estas propiedades especiales utilizando una sintaxis específica, como la notación de corchetes.
Esto se debe a que los caracteres especiales pueden tener un significado especial en el lenguaje de programación o en la sintaxis JSON estándar.
Por lo tanto, al trabajar con JSON que tiene propiedades con nombres especiales, es importante consultar la documentación de la biblioteca o herramienta que estés utilizando para comprender cómo acceder correctamente a esas propiedades.
Para acceder a la propiedad "wp:featuredmedia" dentro de "_embedded", puedes utilizar la notación de puntos para acceder a las propiedades anidadas.
Suponiendo que tienes la respuesta JSON almacenada en una variable llamada "post", puedes acceder a "wp:featuredmedia" de la siguiente manera:
```htmlmixed
{{ post._embedded['wp:featuredmedia'][0].source_url }}
```
En este ejemplo, se asume que "wp:featuredmedia" es un array y se accede al primer elemento con el índice [0]. Luego, se accede a la propiedad "source_url" dentro del objeto "wp:featuredmedia".
