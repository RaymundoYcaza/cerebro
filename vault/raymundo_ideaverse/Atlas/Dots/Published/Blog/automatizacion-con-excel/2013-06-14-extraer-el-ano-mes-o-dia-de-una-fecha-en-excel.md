---
title: "Extraer el año, mes o día de una fecha en Excel."
snippet: ""
cluster: false
draft: false
description: "Separar una fecha en Excel, puede serte útil para generar esos reportes separados por meses o por años. En esta entrada te muestro cómo."
publishDate: "2013-06-14"
category: "Fórmulas en Excel"
tags: ["Fecha y Hora", "Fórmulas", "Funciones", "🤖 Automatización con Excel"]
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
slug: automatizacion-con-excel/fecha-en-excel
---

¿Usas mucho las fechas en tus archivos de Excel? Si esto es cierto, lo más seguro es que necesites  segregar estas fechas por mes o incluso por año, usando una columna adicional.

La solución a esto es tan sencillo como usar las fórmulas que Excel nos provee para el efecto. A continuación te muestro rápidamente cómo obtener estos datos desde una fecha en Excel.

## Separando los componentes de una fecha en Excel.

Digamos que tienes en la celda A1 la fecha 6 de junio del 2013. Dependiendo de la configuración que tengas, se escribirá 6/14/2013 o 14/6/2013.

Si quieres extraer el año de esta fecha (el cual sería 2013), puedes hacer uso de la función "Año()". Solo debes escribir la siguiente fórmula en la celda B1

\=AÑO(A1)

En cambio, si lo que deseas es obtener el mes de la fecha indicada, puedes usar la función "Mes()". En la celda C1, escribe la siguiente fórmula:

\=MES(A1)

## ¡Y una más!

Y, si por alguna razón, necesitas solamente obtener el día de la fecha indicada, puedes utilizar la función "Día()". En la celda D1, escribe la siguiente fórmula.

\=DIA(A1)

## Aprovecha estas funciones en tus modelos de Excel.

Al final, debes tener algo similar a lo que te muestro en esta imagen:

[![[fechas-en-excel-300x109.jpg]]](http://raymundoycaza.com/wp-content/uploads/fechas-en-excel.jpg)

En la primera fila, puedes ver el ejercicio que hice yo, mientras que en la segunda fila te muestro las fórmulas utilizadas, para una mejor comprensión del trabajo que debes realizar.

Ahora, **aprovéchate de estas funciones** en tus modelos de Excel y utilízalos en tu día a día, de manera que te ahorren muchas horas de trabajo. Recuerda que el tiempo es oro.

¡Nos vemos!