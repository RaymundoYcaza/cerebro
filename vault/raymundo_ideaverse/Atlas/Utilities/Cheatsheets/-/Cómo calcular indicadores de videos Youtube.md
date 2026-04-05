---
created: 2025-03-21
in:
  - "[[Negocios MOC]]"
---
Aquí tienes cinco perspectivas / indicadores, ordenados de los que suelen tener mayor relevancia a los de menor importancia:

1. **Tasa de Interacción Global**  
    Calcula el nivel de engagement sumando likes y comentarios, y dividiéndolo entre el total de visitas:

    $$
    \text{Tasa de interacción} = \frac{\text{Likes + Comentarios}}{Visitas}
    $$
    
​
	Este indicador muestra cuán activamente se involucra la audiencia con el contenido.
    
2. **Visitas Diarias**  
    Ajusta las visitas teniendo en cuenta la antigüedad del video. Divides el número total de visitas entre el número de días transcurridos desde la publicación:

	$$
\text{Visitas Diarias} = \frac{\text{Visitas}}{\text{Días de publicación}}
$$
    Permite comparar videos antiguos y recientes en función de su rendimiento diario.

3. **Puntuación de Popularidad Compuesta**  
Combina los tres elementos clave (visitas, likes y comentarios) asignando distintos pesos según su importancia. Por ejemplo:

$$
\text{Puntuación} = 0.5 (\text{Visitas Normalizadas}) + 0.3(\text{Likes Normalizados}) + 0.2(\text{Comentarios Normalizados})
$$
- Con “normalizados” se entiende ajustar cada métrica a una escala comparable (por ejemplo, entre 0 y 1) para poder sumarlas. Este indicador ofrece una visión integral del éxito del video.
    
- 4. **Ratio de Likes por Visita**  
    Mide la proporción de visitas que terminan en un “like”:
    
$$
\text{Ratio Likes/Visitas} = \frac{\text{Likes}}{\text{Visitas}}
$$

- Un valor alto indica que muchos espectadores valoran positivamente el contenido.

5. **Ratio de Comentarios por Visita**  
Similar al anterior, se centra en el feedback a través de comentarios:

$$
\text{Ratio Comentarios/Visitas} = \text{Comentarios}/\text{Visitas}
$$

Este indicador puede ser útil para identificar videos que, aunque puedan tener menos likes, generan conversaciones o debates significativos.

Estas perspectivas te permitirán analizar el éxito de los videos desde distintos ángulos: el engagement global, la rapidez de captación de audiencia, una visión compuesta de popularidad y, de manera más específica, la efectividad en generar reacciones positivas y comentarios.

## Normalización de métricas
Para **normalizar** métricas como Visitas, Likes o Comentarios y poder compararlas en la misma escala, normalmente se utilizan dos métodos principales:

## 1. Normalización Min-Máx (Escala 0 a 1)

Es el método más sencillo para llevar todos los valores a una escala entre **0** y **1**. La fórmula general es:

$$
\text{Valor normalizado} = \frac{\text{Valor - Min(columna)}}{\text{Max(columna) - Min(Columna)}}
$$​

**Ejemplo en Excel** (suponiendo que los datos de “Visitas” están en la columna `F`, desde la fila 2 hasta la 9, y deseas colocar el resultado en la columna `I`):

1. En la celda `I2` (primera fila de datos):
    
```
= (F2 - MIN($F$2:$F$9)) / (MAX($F$2:$F$9) - MIN($F$2:$F$9))    
```

1. Copias esta fórmula hacia abajo para todas las filas de tu rango (de la 2 a la 9).

Repite un proceso similar para **Likes** y **Comentarios** (ajustando referencias a columnas/filas según corresponda).

## 2. Normalización tipo Z-score (Estandarización)

Convierte los valores a desviaciones estándar respecto a la media, quedando con valores centrados en 0. La fórmula es:

$$
\text{Z-score} = \frac{\text{Valor - } \mu}{\sigma}
$$
donde μ es la media de la columna y σ es la desviación estándar.

**Ejemplo en Excel** (para “Visitas” en la columna `F`):

En la celda `I2`:

```
= (F2 - PROMEDIO($F$2:$F$9)) / DESVEST($F$2:$F$9)
```

Copias la fórmula hacia abajo.

En este caso, un valor **positivo** indica que está por encima de la media, y uno **negativo** que está por debajo de la media. Cuanto más grande sea el valor en positivo, más se aleja por arriba de la media, y viceversa.

### ¿Cuál método elegir?

- **Min-Máx** (0 a 1) es más **intuitivo** para indicadores compuestos, ya que todos los valores se sitúan en la misma franja y resulta fácil ponderarlos.
- **Z-score** es útil si te interesa ver **cuán lejos** de la media se encuentra cada valor en términos de desviaciones estándar.

Si lo que buscas es comparar los videos de forma sencilla y combinar métricas (por ejemplo, hacer una “Puntuación de Popularidad”), lo más habitual es usar **Min-Máx** para luego sumar o ponderar las métricas normalizadas (visitas, likes y comentarios) en una única columna.

