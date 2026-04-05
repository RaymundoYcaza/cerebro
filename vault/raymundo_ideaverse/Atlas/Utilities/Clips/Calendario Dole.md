---
created: 2024-09-14
in:
  - "[[Dole]]"
aliases: []
id: Atlas/Utilities/Clips/Calendario Dole
tags: []
---
id: Calendario Dole
tags: []
---

El "calendario 4-4-5" o "calendario fiscal de 13 periodos", común en industrias como la distribución o el retail, donde la planificación se basa en semanas estandarizadas. Este método divide el año en 13 periodos de 4 semanas cada uno, con una estructura de 4-4-5, 4-5-4, o 5-4-4 semanas, según el ciclo.

### Criterios o sistematización

1. **Estructura de 13 periodos**:

    - Cada año tiene 13 periodos, donde la mayoría de los periodos tiene 4 semanas, pero algunos periodos pueden tener 5 semanas para cuadrar el total del año.
    - Los periodos se agrupan en trimestres de 13 semanas (4-4-5). Cada trimestre tiene dos periodos de 4 semanas y uno de 5 semanas.
2. **Ajuste de las semanas**:

    - El total de semanas por año puede variar entre 52 y 53. Esto depende de cuántos días hay en el año (normalmente 365 o 366).
    - Algunos años tienen una semana adicional, lo que se ajusta cada 5 o 6 años para mantener la alineación con el año calendario.
3. **Inicio fijo**:

    - El año no necesariamente comienza el 1 de enero, sino en una fecha fija determinada por la organización, como el primer domingo o lunes de un año fiscal.
4. **Desfase respecto al calendario regular**:

    - Al ajustar las semanas a 13 periodos en lugar de seguir el calendario gregoriano de meses irregulares, las semanas en este calendario suelen no coincidir con las semanas de sistemas convencionales como Excel.
    - Esta discrepancia se debe a que los sistemas convencionales dividen las semanas por un estándar basado en el calendario gregoriano.

### Algoritmo de cálculo

Para calcular estas semanas, puedes:

1. Definir el inicio del año fiscal.
2. Dividir el año en bloques de 4 semanas, con ajustes cada trimestre para incluir un periodo de 5 semanas.
3. Si el año tiene 53 semanas, ajustar el periodo adicional en el trimestre adecuado.

### Implementación con PHP

```php
<?php

  

function getFiscalCalendar($year, $start_date = '2024-01-01')

{

    // Convertimos la fecha de inicio a un objeto DateTime

    $startDate = new DateTime($start_date);

  

    // Ajustamos el inicio al primer lunes de ese año

    if ($startDate->format('N') != 7) {

        $startDate->modify('next sunday');

    }

  

    // Determinamos si el año tiene 52 o 53 semanas

    $endDate = clone $startDate;

    $endDate->modify('+1 year')->modify('-1 day');

  

    $weeksInYear = (int) $startDate->format('W') > 51 ? 53 : 52;

  

    // Iniciamos el calendario con 13 periodos

    $periods = [];

    $currentDate = clone $startDate;

  

    for ($i = 1; $i <= 13; $i++) {

        // Los primeros dos periodos son de 4 semanas, el tercero es de 5 semanas

        $weeksInPeriod = ($i % 3 == 0) ? 5 : 4;

  

        // Ajustamos si estamos en un año de 53 semanas

        if ($i == 13 && $weeksInYear == 53) {

            $weeksInPeriod = 5;

        }

  

        // Calculamos las fechas de inicio y fin de cada periodo

        $periodStart = clone $currentDate;

        $periodEnd = clone $currentDate;

        $periodEnd->modify('+' . ($weeksInPeriod * 7 - 1) . ' days');

  

        $periods[] = [

            'period' => $i,

            'start_date' => $periodStart->format('Y-m-d'),

            'end_date' => $periodEnd->format('Y-m-d')

        ];

  

        // Movemos la fecha actual al inicio del siguiente periodo

        $currentDate->modify('+' . ($weeksInPeriod * 7) . ' days');

    }

  

    return $periods;

}

  

// Ejemplo de uso

$year = 2020;

$fiscalCalendar = getFiscalCalendar($year, '2019-12-29');

  

foreach ($fiscalCalendar as $period) {

    echo "Periodo " . $period['period'] . ": desde " . $period['start_date'] . " hasta " . $period['end_date'] . "<br />";

}

  

?>
```

### Implementación con Python

```python
from datetime import datetime, timedelta

def get_fiscal_calendar(year, start_date='2024-01-01'):
    # Convertir la fecha de inicio a objeto datetime
    start_date = datetime.strptime(start_date, '%Y-%m-%d')

    # Ajustar al primer domingo del año fiscal
    if start_date.weekday() != 6:  # 6 es domingo
        start_date += timedelta(days=(6 - start_date.weekday()))

    # Determinar si el año tiene 52 o 53 semanas
    weeks_in_year = 53 if start_date.isocalendar()[1] > 51 else 52

    periods = []
    current_date = start_date

    for i in range(1, 14):  # 13 periodos
        # Definir periodos de 4-4-5 semanas
        weeks_in_period = 5 if i % 3 == 0 else 4

        # Ajustar si el año tiene 53 semanas y estamos en el último periodo
        if i == 13 and weeks_in_year == 53:
            weeks_in_period = 5

        period_start = current_date
        period_end = current_date + timedelta(days=weeks_in_period * 7 - 1)

        periods.append({
            'period': i,
            'start_date': period_start.strftime('%Y-%m-%d'),
            'end_date': period_end.strftime('%Y-%m-%d')
        })

        # Avanzar al siguiente periodo
        current_date += timedelta(days=weeks_in_period * 7)

    return periods

# Ejemplo de uso
year = 2024
fiscal_calendar = get_fiscal_calendar(year)
for period in fiscal_calendar:
    print(f"Periodo {period['period']}: desde {period['start_date']} hasta {period['end_date']}")

```

### Implementación con JavaScript

```JavaScript
function getFiscalCalendar(year, startDate = '2024-01-01') {
    const start = new Date(startDate);
    
    // Ajustar al primer domingo del año fiscal
    if (start.getDay() !== 0) {
        start.setDate(start.getDate() + (7 - start.getDay()));
    }

    const periods = [];
    let currentDate = new Date(start);
    
    const weeksInYear = (new Date(currentDate.getFullYear() + 1, 0, 1) - currentDate) / (1000 * 60 * 60 * 24 * 7) > 52 ? 53 : 52;

    for (let i = 1; i <= 13; i++) {
        const weeksInPeriod = (i % 3 === 0) ? 5 : 4;

        if (i === 13 && weeksInYear === 53) {
            weeksInPeriod = 5;
        }

        const periodStart = new Date(currentDate);
        const periodEnd = new Date(currentDate);
        periodEnd.setDate(periodEnd.getDate() + (weeksInPeriod * 7 - 1));

        periods.push({
            period: i,
            start_date: periodStart.toISOString().split('T')[0],
            end_date: periodEnd.toISOString().split('T')[0]
        });

        currentDate.setDate(currentDate.getDate() + weeksInPeriod * 7);
    }

    return periods;
}

// Ejemplo de uso
const fiscalCalendar = getFiscalCalendar(2024);
fiscalCalendar.forEach(period => {
    console.log(`Periodo ${period.period}: desde ${period.start_date} hasta ${period.end_date}`);
});

```

### Implementación con TypeScript

```typescript
function getFiscalCalendar(year: number, startDate: string = '2024-01-01'): { period: number, start_date: string, end_date: string }[] {
    const start = new Date(startDate);
    
    // Ajustar al primer domingo del año fiscal
    if (start.getDay() !== 0) {
        start.setDate(start.getDate() + (7 - start.getDay()));
    }

    const periods: { period: number, start_date: string, end_date: string }[] = [];
    let currentDate = new Date(start);
    
    const weeksInYear = (new Date(currentDate.getFullYear() + 1, 0, 1).getTime() - currentDate.getTime()) / (1000 * 60 * 60 * 24 * 7) > 52 ? 53 : 52;

    for (let i = 1; i <= 13; i++) {
        let weeksInPeriod = (i % 3 === 0) ? 5 : 4;

        if (i === 13 && weeksInYear === 53) {
            weeksInPeriod = 5;
        }

        const periodStart = new Date(currentDate);
        const periodEnd = new Date(currentDate);
        periodEnd.setDate(periodEnd.getDate() + (weeksInPeriod * 7 - 1));

        periods.push({
            period: i,
            start_date: periodStart.toISOString().split('T')[0],
            end_date: periodEnd.toISOString().split('T')[0]
        });

        currentDate.setDate(currentDate.getDate() + weeksInPeriod * 7);
    }

    return periods;
}

// Ejemplo de uso
const fiscalCalendar = getFiscalCalendar(2024);
fiscalCalendar.forEach(period => {
    console.log(`Periodo ${period.period}: desde ${period.start_date} hasta ${period.end_date}`);
});

```

### Implementación en MySQL

Para implementar este calendario fiscal en **MySQL**, puedes crear una consulta o una función almacenada que calcule las semanas y periodos según las reglas de 4-4-5 semanas, comenzando desde un domingo. Aquí hay algunos pasos para guiarte:

#### Suposiciones

1. **Inicio del calendario fiscal**: Definir una fecha de inicio, que puede variar cada año o ser fija.
2. **Cálculo de semanas y periodos**: Usar lógica en SQL para dividir el año en 13 periodos, con la estructura de 4-4-5 semanas.
3. **Considerar los años con 53 semanas**: Ajustar la última semana si el año tiene una semana adicional.

#### Estructura de la tabla (si deseas almacenar el calendario)

Puedes crear una tabla donde almacenarás las fechas de inicio y fin de cada periodo, así como el número de semanas que pertenecen a ese periodo.

#### Ejemplo de tabla

```sql
CREATE TABLE fiscal_calendar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    period INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

```

#### Procedimiento almacenado para calcular el calendario

Aquí te dejo un ejemplo de un **procedimiento almacenado** que calcula el calendario fiscal con las semanas comenzando en domingo y siguiendo el patrón 4-4-5:

```sql
DELIMITER $$

CREATE PROCEDURE GenerateFiscalCalendar(IN fiscal_year INT, IN start_date DATE)
BEGIN
    DECLARE current_date DATE;
    DECLARE period INT DEFAULT 1;
    DECLARE weeks_in_period INT;

    -- Ajustar al primer domingo
    SET current_date = start_date + INTERVAL (6 - DAYOFWEEK(start_date)) DAY;

    -- Limpiar la tabla si ya tiene datos para este año fiscal
    DELETE FROM fiscal_calendar WHERE YEAR(start_date) = fiscal_year;

    -- Calcular 13 periodos (4-4-5 semanas)
    WHILE period <= 13 DO
        -- Definir 4 semanas para los primeros dos periodos y 5 para el tercero
        IF period % 3 = 0 THEN
            SET weeks_in_period = 5;
        ELSE
            SET weeks_in_period = 4;
        END IF;

        -- Insertar los datos en la tabla
        INSERT INTO fiscal_calendar (period, start_date, end_date)
        VALUES (
            period,
            current_date,
            current_date + INTERVAL (weeks_in_period * 7 - 1) DAY
        );

        -- Avanzar la fecha al siguiente periodo
        SET current_date = current_date + INTERVAL (weeks_in_period * 7) DAY;
        
        -- Aumentar el periodo
        SET period = period + 1;
    END WHILE;

    -- Manejar años con 53 semanas (si se requiere)
    IF WEEKOFYEAR(current_date) = 53 THEN
        UPDATE fiscal_calendar
        SET end_date = end_date + INTERVAL 7 DAY
        WHERE period = 13;
    END IF;

END$$

DELIMITER ;

```

#### Explicación del procedimiento

1. **Inicio en domingo**: Calcula el primer domingo a partir de la fecha de inicio usando `DAYOFWEEK`.
2. **Bucle para 13 periodos**: Utiliza un bucle `WHILE` para crear los 13 periodos, asignando 4 o 5 semanas a cada uno.
3. **Inserciones**: Inserta cada periodo en la tabla `fiscal_calendar` con las fechas de inicio y fin.
4. **Ajuste para 53 semanas**: Si el año tiene una semana 53, ajusta el último periodo.

#### Ejemplo de ejecución

```sql
CALL GenerateFiscalCalendar(2024, '2024-01-01');

```

Esto te permitirá ver los periodos calculados para el año fiscal.

#### Consideraciones adicionales

- Puedes ajustar el cálculo si necesitas manejar diferentes inicios de año fiscal.
- Si el calendario cambia para diferentes años (por ejemplo, usando otro patrón), puedes modificar el procedimiento almacenado para adaptarse.

### d
