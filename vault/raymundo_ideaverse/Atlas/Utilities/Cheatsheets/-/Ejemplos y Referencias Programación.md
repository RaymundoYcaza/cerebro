---
in:
  - "[[Tecnología MOC]]"
---



¿Qué es TDD?
TDD, o Test-Driven Development (Desarrollo Guiado por Pruebas), es una metodología de desarrollo de software que enfatiza escribir pruebas automatizadas antes de escribir el código de producción. El ciclo de desarrollo en TDD sigue tres pasos principales: escribir una prueba, escribir código para pasar la prueba y refactorizar el código.
Aquí hay una explicación más detallada de cada paso:
**Escribir una prueba (Test):**
En este paso, escribes una prueba automatizada que define el comportamiento deseado de una pequeña parte de tu código. Esta prueba fallará inicialmente, ya que el código de producción aún no existe.

Por ejemplo, supongamos que estás construyendo una función para sumar dos números. La prueba podría ser algo como:
```jsx
test('sumar 2 números', () => {
    expect(sumar(3, 5)).toBe(8);
});
```
Aquí, `sumar()` es una función que aún no has implementado. La prueba espera que la suma de 3 y 5 sea igual a 8.
**Escribir código de producción para pasar la prueba:**
En este paso, escribes el código mínimo necesario para que la prueba pase. No te preocupes por la calidad o la eficiencia en este punto; solo haz que la prueba pase.

Usando el ejemplo anterior, podrías escribir una función `sumar()` simple así:
```jsx
function sumar(a, b) {
    return a + b;
}
```
Esta función simplemente suma dos números y devuelve el resultado.
**Refactorizar el código:**
Después de que la prueba pase, es el momento de refactorizar el código para mejorar su calidad, claridad y eficiencia. Asegúrate de que la funcionalidad siga siendo la misma, pero mejora la estructura del código si es posible.

Por ejemplo, podrías refactorizar la función `sumar()` para manejar argumentos de tipos diferentes, o para ser más legible:
```jsx
function sumar(a, b) {
    return Number(a) + Number(b);
}
```
Ahora la función `sumar()` manejará argumentos de cualquier tipo y los convertirá a números antes de sumarlos.
Este ciclo se repite continuamente a medida que desarrollas tu código, escribiendo pruebas para cada pequeña funcionalidad y refactorizando según sea necesario.

TDD promueve un diseño de software más sólido, ya que las pruebas automatizadas garantizan que el código cumpla con los requisitos y funcione como se espera, incluso después de futuras modificaciones. También ayuda a mantener el código más limpio y modular, ya que se enfoca en pequeñas unidades de funcionalidad a la vez.
### Canales de Youtube
https://www.youtube.com/@aDevSays569/videos
