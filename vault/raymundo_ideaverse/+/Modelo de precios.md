---
up:
  - "[[Crear versión SaaS de Bisstox Agricontrol]]"
related: 
created: 2025-06-12
cssclasses:
  - wide-page
---
### 1 │ Por qué necesitamos un **modelo escalonado**

- **Competidores** orientados a pequeñas fincas muestran precios de **US-$19/mes (Agrivi)** y **US-$30/mes (Agrimap)** para 1 usuario, con más funciones y usuarios bajo cotización.[rua.ua.es](https://rua.ua.es/dspace/bitstream/10045/96744/1/Aplicacion_movil_para_la_gestion_de_viveros_Cayo_Guachamin_Dennis_Alfredo.pdf)
    
- Para grandes haciendas (tu nicho), las soluciones locales como AGRI publican planes con 3-6 usuarios pero sin precio público (“cotización personalizada”), lo que indica márgenes holgados para ofertas superiores.[agrit.us](https://www.agrit.us/precios/)
    
- Tu estructura **de costos fijos** es reducida (≈ US-$305/mes) y el **costo variable** real por cliente es el hosting (US-$17/mes).
    
- La meta es **cubrir costes con el menor número de clientes** y, a la vez, parecer razonable frente a los precios “de entrada” que ven los agricultores en la red (19-30 US-$ por 1 usuario).
    

---

## 2 │ Propuesta de planes mensuales (suscripción SaaS)
| Plan           | Usuarios incluidos | Tarifa mensual    | Usuario extra   | Soporte / SLA       | Reportes                                         | Personalización incluida           | Objetivo de cliente                      |
| -------------- | ------------------ | ----------------- | --------------- | ------------------- | ------------------------------------------------ | ---------------------------------- | ---------------------------------------- |
| **Starter**    | 3                  | **US-$150**       | 25 US-$/usuario | e-mail 1 día        | 5 plantillas estándar                            | Básica (logo, colores)             | Finca mediana que quiere salir del papel |
| **Growth**     | 10                 | **US-$300**       | 20 US-$/usuario | WhatsApp 8 h        | 10 plantillas + 1 reporte a medida/mes           | Básica + 2 ajustes intermedios/año | Hacienda de 40-80 ha que ya exporta      |
| **Pro**        | 25                 | **US-$450**       | 15 US-$/usuario | Teléfono/WA 4 h     | Reportería ilimitada (simples) + 3 avanzadas/año | • Básica • 10 h intermedia incl.   | Operador multihacienda / exportador      |
| **Enterprise** | Ilimitados         | **Desde US-$900** | —               | Línea directa (2 h) | Todo ilimitado + BI API                          | 20 h intermedia + 40 h avanzada    | Grupo agro-industrial                    |

**Notas clave**
1. **Precio de usuario adicional** decrece a propósito para empujar el salto de plan.
2. En todos los casos el _hosting_ por instancia (US-$17) va incluido en la cuota.
3. Se ofrecen **10 % de descuento** por pago anual anticipado (mejora flujo de caja).
4. Contrato mínimo recomendado: **6 meses Starter / 12 meses demás planes**.
5. Cada plan viene con **prueba piloto sin costo de 30 días (1 usuario)**: reduce fricción.

## 3 │ Break-even y número mínimo de clientes

| Plan          | Margen bruto por cliente* | Clientes necesarios para cubrir US-$305 fijos |
| ------------- | ------------------------- | --------------------------------------------- |
| Starter 150 $ | 133 $                     | **3**                                         |
| Growth 300 $  | 283 $                     | **2**                                         |
| Pro 450 $     | 433 $                     | **1**                                         |

* Margen = Tarifa – 17 $ hosting.  
→ **Escenario conservador**: 2 clientes Growth (o 3 Starter) ya pagan todos los gastos y dejan utilidad; cualquier cliente Pro o Enterprise coloca la operación muy por encima de break-even.

## 4 │ Límites y condiciones sugeridas
### Recursos técnicos
- **Almacenamiento**: 10 GB / 50 GB / 200 GB / ilimitado (se puede vender GB extra a 0,10 US-$/GB).
- **APIs**: acceso sólo en Pro + Enterprise.
- **Instancias**: una por cliente; multi-empresa sólo Pro +.

Soporte y capacitación

|Plan|Capacitación incluida|Horas de soporte extra|
|---|---|---|
|Starter|Video-biblioteca|30 US-$/h|
|Growth|2 sesiones online iniciales|25 US-$/h|
|Pro|1 onsite + 1 online/mes|20 US-$/h|
|Enterprise|ilimitado (acuerdo marco)|Incluido SLA|

## 5 │ Gestión de personalizaciones
