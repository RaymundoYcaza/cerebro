---
up:
  - "[[Decision Frameworks MOC]]"
  - "[[Process Improvement & Control MOC]]"
  - "[[Academic Writing MOC]]"
related: []
created: 2026-02-28
aliases:
source: "[[Fuente I Diálogos LLM]]"
source_urls:
  - https://www.perplexity.ai/search/como-puedo-aplicar-el-metodo-r-fYOVBasHTbirqLyULFlA7A
tags:
  - "#note/commentary🗨"
  - note/evergreen🌲
---


> [!abstract] Definición en una línea
> _RICE es un método de priorización que usa cuatro variables medibles, para una rápida toma de decisiones._

## Fórmula / Definición
$$`\text{Puntuación} = \frac{\text{Alcance} \times \text{Impacto} \times \text{Confianza}}{\text{Esfuerzo}}`$$

## Commentary
> RICE es un método de priorización que asigna una *ponderación estimativa* usando datos más o menos definidos para tomar decisiones rápidamente. A diferencia de una matriz de ponderación libre, RICE impone siempre las mismas cuatro variables (Reach, Impact, Confidence, Effort), lo que permite comparar proyectos heterogéneos sin necesidad de construir un vector de variables ad hoc para cada decisión. Su mayor ventaja es la velocidad: reduce el debate subjetivo a números justificables.

## Utilidad real
- Features en proyectos de software y multimedia 
- Iniciativas de mejora en procesos internos 
- Selección de temas para artículos y papers

## Colisión conceptual
RICE vs. Matriz de Ponderación:

- La Matriz de Ponderación es flexible: tú defines las variables según el contexto (ubicación, costo, riesgo…). Ideal cuando los proyectos son muy distintos en naturaleza.

- RICE es estandarizado: siempre las mismas 4 variables. Ideal cuando comparas iniciativas del mismo tipo (features, mejoras de proceso, artículos).


> Regla de oro: Si tardas más de 5 minutos definiendo las variables, usa RICE.

## Puntos clave
- Confianza penaliza, no premia: Un proyecto con Impacto alto pero Confianza del 50% queda automáticamente a la mitad. No subestimes este divisor.

- Esfuerzo en meses-persona, no en días: Si usas días, los números se disparan y pierden sentido comparativo. Usa 0.5 como mínimo para tareas pequeñas.

- Impacto no es continuo: Usa solo los valores fijos 3 / 2 / 1 / 0.5 / 0.25. Inventar un "2.7" rompe la comparabilidad entre proyectos.

- Alcance es por período, no total: Siempre especifica el horizonte de tiempo (ej. usuarios/mes o transacciones/trimestre). Cambiar el período cambia el score dramáticamente.

## Temas relacionados
- Esto me recuerda a la [[Matriz de ponderación]] porque también se utiliza para priorizar opciones, como la selección de una ubicación para instalar una planta industrial.
- También me recuerda a la [[Matriz Eisenhower]] que es una herramienta de priorización un poco más simple, que puede ser usado en situaciones puntuales.

## Q&A


## Ejemplo
Escenario: Tienes que elegir entre dos mejoras para tu sistema de facturación.

| Iniciativa                      | Alcance    | Impacto | Confianza | Esfuerzo | **Score** |
| ------------------------------- | ---------- | ------- | --------- | -------- | --------- |
| Automatizar envío de XML al SRI | 200 tx/mes | 3       | 80%       | 1 mes    | **480**   |
| Módulo de reportes por cliente  | 200 tx/mes | 2       | 50%       | 3 meses  | **67**    |

Aunque los reportes suenan útiles, la automatización al SRI gana por lejos: menor esfuerzo, mayor confianza y mayor impacto directo.

## Fuentes adicionales


