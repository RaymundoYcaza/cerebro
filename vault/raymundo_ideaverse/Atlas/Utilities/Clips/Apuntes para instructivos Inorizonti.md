---
up: []
related: []
created: 2026-03-25
---

## Contabilidad
### Reglas generales
- Cada cargo bancario (con su propio código) debe realizarse en un asiento independiente para que la conciliación bancaria se realice perfectamente al cargar el excel. *Principio: Un asiento por transacción bancaria*

#### Servicios financieros no son objetos de IVA
- 📌 Los servicios financieros prestados por instituciones del sistema financiero (como comisiones bancarias) **no son objeto de IVA** según la Ley de Régimen Tributario Interno. Por eso aplica el código 531 y no genera crédito tributario de IVA. Por ejemplo, el certificado bancario que cuesta $1,00 es deducible como gasto financiero para el IR.

|Campo|Valor|
|---|---|
|**Tipo de Compra**|**531 – Adquisiciones no objeto de IVA**|
|**Sustento Tributario**|**Costo o Gasto para declaración de IR**|

#### Conciliación bancaria
- En la plantilla, hay que tener cuidado de que las columnas *debito* y *credito* tengan los valores correctos (cuidado con que estén invertidas), de lo contrario, el cruce no se realizará. 
- En la plantilla se deben de eliminar las filas que estén en blanco para evitar falsos positivos de registros no cruzados.
- Después de la conciliación con Excel, hay que ir a la opción de consolidación manual y poner el saldo del extracto para verificar que todo está cuadrado sin diferencias y guardar la conciliación.
### Retiro de caja chica

|Cuenta|Descripción|Debe|Haber|DOC. BANCO|#|
|---|---|---|---|---|---|
|`1101001001`|CAJA GENERAL EFECTIVO MATRIZ|$200.00|—|—|—|
|`1101003001`|PRODUBANCO/PROMERICA|—|$200.00|Retiro por ventanilla|`60845084`|

**Glosa sugerida:** _"Retiro por ventanilla para fondo de caja — Junio 2021"_

