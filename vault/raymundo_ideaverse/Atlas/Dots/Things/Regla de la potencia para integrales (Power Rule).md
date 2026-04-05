---
up:
  - "[[MOC I Cálculo]]"
related:
  - "[[Regla de la potencia para derivadas]]"
aliases:
source: "[[Fuente I Diálogos LLM]]"
source_urls:
  - https://www.perplexity.ai/search/actua-como-mi-companero-de-pen-0cGs7_OASuSYZpF7kJnVIg
created: 2026-02-28
tags:
  - note/evergreen🌲
  - note/commentary🗨
---

## Fórmula

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$$


> [!quote] Integrar es como deshacer una derivada; es el proceso de reconstruir la función original a partir de su tasa de cambio.

## Commentary 
Tomas el exponente de x, le sumas 1; ese resultado es el nuevo exponente Y el denominador. Divide el coeficiente entre ese número. El `+C` solo aplica en integrales indefinidas. Sin él estaríamos afirmando que existe una única función primitiva, cuando en realidad hay infinitas; todas las que difieren en una constante (la que se perdió al derivar).

## Utilidad real 
- Cálculo de físicas y curvas de easing en apps móviles (Ionic) 
- Reconstruir posición a partir de velocidad en gesture tracking 
- Análisis de series de tiempo financieras 

## Colisión conceptual 
|               | Derivar             | Integrar            |
| ------------- | ------------------- | ------------------- |
| ¿Qué hace?    | Mide tasa de cambio | Acumula/reconstruye |
| ¿Pierde info? | Sí (pierde C)       | No                  |
| Analogía      | Velocímetro         | Odómetro            |


## Puntos clave
- Esta regla aplica únicamente para $n \neq -1$

## Temas relacionados
- Esto me recuerda a la [[Regla de la potencia para derivadas]], pero en sentido inverso.
- 
## Preguntas y respuestas
##### ¿Qué pasa si no incluimos la constante de integración +C?
Sin el +C estaríamos diciendo que **solo existe una función** que cumple la condición, cuando en realidad hay infinitas (todas las que difieren en una constante). Ejemplo:
$$  
\frac{d}{dx}(x^2) = 2x  
$$  
  
$$  
\frac{d}{dx}(x^2 + 5) = 2x  
$$  
  
$$  
\frac{d}{dx}(x^2 - 1000) = 2x  
$$  
  
Todas estas funciones tienen la misma derivada.  Entonces, cuando integramos $2x$, debemos escribir:  
$$  
\int 2x \, dx = x^2 + C  
$$

## Ejemplo
Vamos a resolver paso a paso:

$$  
\int x^3 , dx  
$$

---

### 1️⃣ Identificar el tipo de integral

Es una **integral indefinida de una potencia de (x)**.

Usamos la regla general:

$$  
\int x^n , dx = \frac{x^{n+1}}{n+1} + C  
\quad \text{(para } n \neq -1\text{)}  
$$

---

### 2️⃣ Aplicar la regla

Aquí:

$$  
n = 3  
$$

Entonces:

$$  
\int x^3 , dx = \frac{x^{3+1}}{3+1} + C  
$$

---

### 3️⃣ Simplificar

$$  
= \frac{x^4}{4} + C  
$$

---

### ✅ Resultado Final

$$  
\int x^3 , dx = \frac{x^4}{4} + C  
$$

Donde ( C ) es la constante de integración.
## Fuentes adicionales
- https://www.reddit.com/r/learnmath/comments/1647pa1/why_do_we_need_c_for_indefinite_integration/?tl=es-419
- 