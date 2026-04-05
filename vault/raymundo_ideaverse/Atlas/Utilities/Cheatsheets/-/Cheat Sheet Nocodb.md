---
in:
  - "[[Nocodb]]"
---



## Obtener el dia del año (day of year)
```
DATETIME_DIFF({CreatedAt}, CONCAT(LEFT({CreatedAt},4),"-01-01"), "d")+1
```
## Generar DIN Nuevo formato 2024
Está formato por un prefijo de texto, el año de la fecha propuesta, seguido del número del día del año según la fecha propuesta, seguido de la marca temporal calculada. Todos los componentes están separados por un guión.
`SO-YYYY-000-0000`

```
CONCAT(

    "SO-",

    LEFT({Fecha}, 4),

    "-",

    LEFT(

        "000",

        (3 - LEN(

            (DATETIME_DIFF({Fecha}, CONCAT(LEFT({Fecha}, 4), "-01-01"), "d") + 1)

        ))

    ),

    INT(

        (DATETIME_DIFF({Fecha}, CONCAT(LEFT({Fecha}, 4), "-01-01"), "d") + 1)

    ),

    "-",

    ADD(

        INT(

        VALUE(      

            LEFT(

        INT(DATETIME_DIFF({Fecha}, "1970-01-01 00:00:00", "ms")),

        10

            ))),{id}    

    )

)
```

## Generar código de identificación
Está formato por un prefijo de texto, el año de la fecha propuesta, seguido del número del registro actual, seguido de los últimos 3 dígitos de la marca temporal calculada. Todos los componentes están separados por un guión.

`SO-YYYY-000-000`

```
CONCAT("SO-", LEFT({Fecha}, 4), "-",LEFT("000", (3 - len({Id}))),{Id},"-", right(left(int(DATETIME_DIFF({CreatedAt}, "1970-01-01 00:00:00", "ms")),10),3))
```

## Crear columna secuencial

```python
concat("XXX-", LEFT("000000000", (9 - len({id}))), {id})
```

## Crear relaciones

Cuando se crean relaciones de muchos a muchos, no aparece la descripción de los registros relacionados, sino el conteo. Se debe analizar si realmente se requiere una relación muchos a muchos o si se requiere una relación 1 a muchos, ya que esta última sí permite visualizar directamente el registro vinculado.
