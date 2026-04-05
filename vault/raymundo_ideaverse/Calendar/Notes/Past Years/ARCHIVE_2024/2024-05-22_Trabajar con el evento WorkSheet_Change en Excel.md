---
created: 2024-05-22 
---



- Para detectar el evento en el que se cambian los datos de una celda o rango, se debe usar el evento  `Worksheet_Change`
- Para detectar en qué celda o rango fue el cambio se puede usar la función  `Intersect` :

``` vb
If Not (Intersect(Target, Range("C1:C100000")) Is Nothing) Then
modPO.AddPoNumber (Target.Row)
End If
  ```
