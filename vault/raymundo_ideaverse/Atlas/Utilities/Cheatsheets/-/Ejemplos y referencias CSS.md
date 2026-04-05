---
in:
  - "[[CSS]]"
---



Cómo agregar un efecto  sobre un fondo usando 
https://webdevetc.com/blog/how-to-add-a-gradient-overlay-to-a-background-image-using-just-css-and-html/
## Animaciones con CSS
  con cajas y teléfono lector de 
[https://codepen.io/zack_frost/details/RKQXgm](https://codepen.io/zack_frost/details/RKQXgm)
  usando 
[https://www.sliderrevolution.com/resources/css-animated-background/](https://www.sliderrevolution.com/resources/css-animated-background/)
[https://alvarotrigo.com/blog/animated-backgrounds-css/](https://alvarotrigo.com/blog/animated-backgrounds-css/)
Cómo crear un efecto  sobre un elemento con 
```css
<style>

.scroll-wrapper {text-align:center;}

.scroll {   

    font-size: 50px;

    color: #000;

    

    

   -webkit-animation: scrolling 3s ease infinite;

   -moz-animation: scrolling 3s ease infinite;

   -o-animation: scrolling 3s  ease infinite;

   animation: scrolling 3s ease infinite;

}



@keyframes scrolling {

  0% {

    transform: translate(0);

  }

 

  50% {

    transform: translate(0,40px);}



 

  100% {

     transform: translate(0);

  }

}

</style>
```
## Estilos enlaces
Cómo dar un estilo para diferenciar los   y 
Para diferenciar los enlaces externos de los enlaces internos utilizando CSS, se puede utilizar el atributo href de los enlaces. Normalmente, los enlaces internos apuntan a páginas dentro del mismo sitio web y tienen una ruta relativa, mientras que los enlaces externos apuntan a páginas fuera del sitio web y tienen una ruta absoluta.
Puedes utilizar el siguiente código CSS para darle un estilo diferente a los enlaces externos:
```css
a[href^="http"]:not([href*="tu_sitio_web.com"]) {
  /* Estilos para enlaces externos */
  color: #0072c6;
  font-weight: bold;
  text-decoration: underline;
}
```
