---
created_at: 2024-10-06
up:
  - "[[Tecnología MOC]]"
tags: []
description: 
---



```php
<?php
// Obtener la hora actual en formato de 24 horas
$horaActual = date("H");
$minutosActuales = date("i");

// Calcular los minutos transcurridos desde la medianoche
$minutosTranscurridos = ($horaActual * 60) + $minutosActuales;

echo "Minutos transcurridos hoy: " . $minutosTranscurridos;
?>
```