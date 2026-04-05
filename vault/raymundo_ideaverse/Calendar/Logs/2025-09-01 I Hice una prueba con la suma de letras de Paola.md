---
up:
  - "[[Aurora MOC]]"
related: []
created: 2025-09-01
automatic: true
aliases:
tags:
  - note/aurora✨
---


Utilizando la herramienta de Python que implementé para sumar letras (sumar los valores de los números ordinales de cada letra de un texto dado) obtuve los siguientes resultados:


PS W:\> py .\sumar-letras.py
Ingresa la cadena: paola
Texto procesado: PAOLA
Desglose: P(16) + A(1) + O(15) + L(12) + A(1)
Suma total: 45
Reducción a 2 dígitos (<=99): 45
Reducción a 1 dígito (<=9): 9


PS W:\> py .\sumar-letras.py
Ingresa la cadena: paola alejandra
Texto procesado: PAOLAALEJANDRA
Desglose: P(16) + A(1) + O(15) + L(12) + A(1) + A(1) + L(12) + E(5) + J(10) + A(1) + N(14) + D(4) + R(18) + A(1)
Suma total: 111
Reducción a 2 dígitos (<=99): 3
Reducción a 1 dígito (<=9): 3


PS W:\> py .\sumar-letras.py
Ingresa la cadena: paola tapia
Texto procesado: PAOLATAPIA
Desglose: P(16) + A(1) + O(15) + L(12) + A(1) + T(20) + A(1) + P(16) + I(9) + A(1)
Suma total: 92
Reducción a 2 dígitos (<=99): 92
Reducción a 1 dígito (<=9): 2


PS W:\> py .\sumar-letras.py
Ingresa la cadena: paola alejandra tapia leturne
Texto procesado: PAOLAALEJANDRATAPIALETURNE
Desglose: P(16) + A(1) + O(15) + L(12) + A(1) + A(1) + L(12) + E(5) + J(10) + A(1) + N(14) + D(4) + R(18) + A(1) + T(20) + A(1) + P(16) + I(9) + A(1) + L(12) + E(5) + T(20) + U(21) + R(18) + N(14) + E(5)
Suma total: 253
Reducción a 2 dígitos (<=99): 10
Reducción a 1 dígito (<=9): 1


PS W:\> py .\sumar-letras.py
Ingresa la cadena: alejandra
Texto procesado: ALEJANDRA
Desglose: A(1) + L(12) + E(5) + J(10) + A(1) + N(14) + D(4) + R(18) + A(1)
Suma total: 66
Reducción a 2 dígitos (<=99): 66
Reducción a 1 dígito (<=9): 3


PS W:\> py .\sumar-letras.py
Ingresa la cadena: pao
Texto procesado: PAO
Desglose: P(16) + A(1) + O(15)
Suma total: 32
Reducción a 2 dígitos (<=99): 32
Reducción a 1 dígito (<=9): 5
