## 3 Reglas de aprendizaje en los procesos de calculo,

- **Realizar preferentemente una visita técnica en planta** antes de automatizar cualquier proceso, con el objetivo de comprender cómo se ejecuta actualmente de forma manual, identificar variaciones operativas y detectar reglas implícitas que no suelen estar documentadas.
    
    En los casos donde la visita presencial no sea posible —por razones de seguridad, paro nacional, limitaciones de viáticos o distancia geográfica— se deberán aplicar mecanismos alternativos para recopilar la información necesaria, tales como:
    
    - Reuniones virtuales con el personal operativo y administrativo
    - Solicitud de videos del proceso manual completo
    - Recolección de tickets, reportes y documentos reales de operación
    - Entrevistas estructuradas con los responsables del proceso
    - Validación paso a paso mediante casos de prueba reales
    - Sesiones de revisión y confirmación de cálculos con el cliente
    
    El objetivo es asegurar, independientemente del medio utilizado, que el proceso manual quede completamente entendido y documentado antes de su automatización.
    
- **Definir explícitamente la lógica de cálculo utilizada por el cliente**, incluyendo:
    
    - Método de cálculo aplicado
    - Cantidad de decimales utilizados
    - Tipo de redondeo (redondeo tradicional, hacia arriba, hacia abajo)
    - Uso de truncamiento o corte de decimales
    - Momento del redondeo dentro del proceso (por operación, por subtotal o resultado final)
- **Establecer desde el inicio del proyecto las unidades de medida oficiales**, dejándolo documentado en los criterios de aceptación, incluyendo:
    
    - Unidades de peso (kg, libras, quintales, toneladas)
    - Unidades monetarias
    - Formato de decimales
    - Conversión entre unidades (si aplica)
    - Nivel de precisión requerido para cálculos de costo, precio y pesaje

Estas definiciones deben quedar formalmente documentadas para evitar inconsistencias entre el proceso manual y el sistema automatizado, así como prevenir diferencias en auditorías y validaciones operativas.