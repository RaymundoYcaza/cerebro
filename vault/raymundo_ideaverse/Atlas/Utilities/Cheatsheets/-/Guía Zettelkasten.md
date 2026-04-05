---
created: 2025-01-28
---


### **1. Estructura de Carpetas en Obsidian**

Organiza tus notas en carpetas para mantener un flujo ordenado:

```
📁 Zettelkasten  
├── 📁 0-Inbox (Notas fugaces)  
├── 📁 References (Notas de referencia)  
├── 📁 Literature (Notas literarias)  
├── 📁 Permanent (Notas permanentes)  
└── 📁 Maps of Content (MOCs)  
```

### **2. Flujo de Trabajo Paso a Paso**

#### **A. Captura Inicial: Notas Fugaces (Fleeting Notes)**

- **Qué son**: Ideas rápidas, pensamientos espontáneos, preguntas o insights que surgen en el momento.
    
- **Cómo usarlas**:
    
    1. Crea una nota en la carpeta `0-Inbox` con un título breve (ej: `20231005-idea-sobre-neuroplasticidad`).
        
    2. Escribe la idea en 1-2 frases sin preocuparte por el formato.
        
    3. Usa etiquetas como `#fleeting` o `#inbox` para filtrar después.
        
- **Ejemplo**:

```markdown
# Idea: La neuroplasticidad no es exclusiva de la juventud  
- Estudio reciente muestra que adultos mayores pueden generar nuevas conexiones neuronales con estimulación cognitiva.  
#fleeting #neurociencia
```

#### **B. Notas de Referencia (Reference Notes)**

- **Qué son**: Metadatos de fuentes externas (libros, artículos, podcasts) con información bibliográfica.
    
- **Cómo usarlas**:
    
    1. Al leer/consumir contenido, crea una nota en `References` con:
        
        - Título: `Referencia: [Título del recurso]` (ej: `Referencia: El cerebro plástico - Doidge`).
            
        - Metadata: Autor, año, URL, tipo de recurso.
            
        - Resumen breve (1-2 líneas) del tema general.
            
    2. Vincula esta nota a las **notas literarias** asociadas.
        
- **Ejemplo**:

```markdown
---
author: Norman Doidge  
year: 2007  
type: Libro  
url: ---  
---  
# Referencia: El cerebro plástico  
Explora casos de neuroplasticidad en adultos mediante terapias innovadoras.  
```

#### **C. Notas Literarias (Literature Notes)**

- **Qué son**: Resúmenes o citas clave **de una fuente específica**, en tus propias palabras.
    
- **Cómo usarlas**:
    
    1. Mientras lees/estudias, crea notas en `Literature` vinculadas a su `Referencia`.
        
    2. Estructura:
        
        - **Contexto**: ¿Qué parte del recurso resume (capítulo, página)?
            
        - **Ideas clave**: Parafraseadas (¡sin copiar!).
            
        - **Citas importantes**: Entre comillas si es textual.
            
        - Enlaces a `[[Referencia: Título]]` y a notas relacionadas.
            
- **Ejemplo**:

```markdown
# Literatura: Neuroplasticidad en adultos - Doidge  
**Referencia**: [[Referencia: El cerebro plástico]]  
**Páginas**: Capítulo 3  
**Ideas clave**:  
- La terapia de movimiento forzado en pacientes con ACV reactiva redes neuronales inactivas.  
- La plasticidad requiere atención focalizada y repetición.  
Relacionado: [[Permanent/Neuroplasticidad y edad]]  
```

#### **D. Procesar el Inbox: Convertir a Notas Permanentes**

- **Qué son**: Ideas depuradas, autocontenidas y conectadas a tu red de conocimiento.
    
- **Cómo crearlas**:
    
    1. Revisa diariamente/semanalmente la carpeta `0-Inbox`.
        
    2. Para cada nota fugaz:
        
        - **Si es válida**: Desarróllala en una nota permanente (carpeta `Permanent`).
            
        - **Si es incompleta**: Investiga más o combínala con otras notas.
            
        - **Si es irrelevante**: Archívala o elimínala.
            
    3. Reglas clave:
        
        - **Atomicidad**: 1 idea por nota.
            
        - **Conexiones**: Enlaza a notas existentes con `[[ ]]` y explica la relación.
            
        - **Claridad**: Escribe como si fuera para otro lector.
            
- **Ejemplo**:
```markdown
# La neuroplasticidad en adultos mayores  
Contrario al mito, el cerebro adulto puede remodelarse significativamente bajo condiciones específicas:  
- **Estimulación cognitiva**: Ejercicios desafiantes (ej: [[Aprendizaje de idiomas en adultos]]).  
- **Movimiento forzado**: Terapias como la usada en ACV ([[Referencia: El cerebro plástico]]).  
---  
> Relacionado: [[Neurodegeneración]], [[Plasticidad y envejecimiento saludable]]  
```

### **3. Conectar y Expandir el Conocimiento**

- **Enlaces bidireccionales**: Usa `[[ ]]` para vincular notas. Obsidian mostrará relaciones en la gráfica.
    
- **Maps of Content (MOCs)**: Crea notas índice para temas amplios (ej: `MOC Neurociencia`) que enlacen a subtemas y notas permanentes.
    
- **Etiquetas estratégicas**: Usa pocas etiquetas generales (ej: `#filosofía`, `#aprendizaje`) para filtrar, pero prioriza enlaces.
    

---

### **4. Mantenimiento y Mejora**

- **Revisión semanal**:
    
    - Fusiona notas redundantes.
        
    - Actualiza enlaces rotos.
        
    - Refina notas permanentes con nuevos insights.
        
- **Búsqueda activa**: Usa `Ctrl+O` en Obsidian para encontrar conexiones al crear nuevas notas.
    

---

### **5. Ejemplo de Flujo Completo**

1. **Nota fugaz** en Inbox: "¿La meditación afecta la neuroplasticidad?"
    
2. **Investigas**: Creas `Referencia: Estudio Lutz 2014` y `Literatura: Meditación y materia gris`.
    
3. **Conviertes a permanente**:

```markdown
# Meditación y neuroplasticidad  
Estudio de Lutz ([[Referencia: Estudio Lutz 2014]]) muestra aumento de materia gris en córtex prefrontal tras 8 semanas de mindfulness.  
Relacionado: [[Estrés y plasticidad]], [[Técnicas de meditación]]  
```

### **6. Tips para Obsidian**

- **Templates**: Crea plantillas predefinidas para cada tipo de nota (ve a `Settings > Core plugins > Templates`).
    
- **Backlinks**: Usa el panel de backlinks para ver cómo se conectan las notas.
    
- **Graph View**: Visualiza conexiones inesperadas para descubrir relaciones nuevas.


# Ejemplos variados
### **1. Lectura de Libro/Artículo/Blog/Noticias/Posts de RRSS**

**Ejemplo con un libro de neurociencia**:

#### **a. Nota de Referencia**


```markdown
---
author: David Eagleman  
title: "Incógnito: Las vidas secretas del cerebro"  
year: 2011  
type: Libro  
url: ---  
---  
# Referencia: Incógnito - Eagleman  
Explora el subconsciente y cómo el cerebro toma decisiones sin participación consciente.  
```


#### **b. Nota Literaria** (mientras lees el Capítulo 4)

```markdown
# Literatura: Toma de decisiones inconscientes - Eagleman  
**Referencia**: [[Referencia: Incógnito - Eagleman]]  
**Páginas**: Capítulo 4 (p. 89-112)  
**Ideas clave**:  
- El cerebro inconsciente procesa 11 millones de bits/segundo vs. 50 bits/segundo de la mente consciente.  
- Los juicios morales complejos (ej: dilemas éticos) se originan en redes subcorticales.  
**Cita**:  
> "Somos una junta directiva operada por fuerzas competidas de las que no somos conscientes".  
**Relacionado**: [[Toma de decisiones]], [[Sesgos cognitivos]]  
```

#### **c. Nota Permanente** (idea procesada)

```markdown
# El cerebro como sistema de comités inconscientes  
El cerebro no tiene un "centro de mando", sino múltiples subsistemas que compiten ([[Referencia: Incógnito - Eagleman]]).  
- **Ejemplo**: Al elegir entre opciones A y B, el tálamo actúa como "mediador" entre circuitos emocionales y racionales.  
- **Implicación**: La "decisión consciente" es solo la punta del iceberg (relacionado: [[Ilusión de agencia]]).  
```

### **2. Consumo de Video/Curso/Película/Serie/Videojuego**

**Ejemplo con un videojuego (Portal 2)**:

#### **a. Nota Fugaz**

```markdown
# Idea: Portal 2 y la teoría de incentivos en el aprendizaje  
- El juego recompensa la experimentación con puzzles, reforzando la persistencia.  
#fleeting #gamificación
```  

#### **b. Nota de Referencia**

```markdown
---
title: "Portal 2"  
creator: Valve Corporation  
year: 2011  
type: Videojuego  
---  

# Referencia: Portal 2  
Juego de puzzles que usa mecánicas de física y recompensas incrementales para enseñar lógica espacial.  
```

#### **c. Nota Literaria**


```markdown
# Literatura: Diseño de niveles en Portal 2  
**Referencia**: [[Referencia: Portal 2]]  
**Momento clave**: Nivel 7 ("Cámara de desafío")  
- **Mecánica**: El jugador debe fallar 3-5 veces antes de descubrir la solución, generando "frustración positiva".  
- **Principio psicológico**: [[Curva de dificultad óptima]] (Vygotsky).  
```

#### **d. Nota Permanente**

```markdown
# Aprendizaje mediante fracaso controlado  
Contextos como los videojuegos ([[Referencia: Portal 2]]) enseñan que:  
1. El error debe tener consecuencias **reversibles** para evitar desmotivación.  
2. La retroalimentación debe ser inmediata y vinculada a la acción ([[Leyes de Thorndike]]).  
> **Aplicación**: Diseñar entrenamientos corporativos con desafíos "reseteables".  
```

---

### **3. Extracto de Charla/Clase/Conferencia/Conversación/Reflexión**

**Ejemplo con una conversación espontánea**:

#### **a. Nota Fugaz**

```markdown
# Charla con María (CEO): "La toma de decisiones bajo estrés"  
- Su regla: "Si es irreversible, espero 24h; si es reversible, actúo con 70% de información".  
#fleeting #liderazgo  
```
#### **b. Nota de Referencia** (si la fuente es formal, ej: conferencia)

```markdown
---
speaker: Dra. Elena Ruiz  
event: "Conferencia sobre liderazgo en incertidumbre"  
date: 2023-09-15  
type: Conferencia  
---  
# Referencia: Conferencia Liderazgo - Ruiz  
Aborda estrategias para decidir en entornos VUCA (Volátiles, Inciertos, Complejos, Ambiguos).  
```

#### **c. Nota Literaria**

```markdown
# Literatura: Regla 24h/70% - Conferencia Ruiz  
**Referencia**: [[Referencia: Conferencia Liderazgo - Ruiz]]  
**Contexto**: Minuto 34: "Cuando la ansiedad por decidir nubla el juicio".  
- **Técnica**:  
  1. Clasificar decisiones en **irreversibles** (ej: despidos) vs. **reversibles** (ej: prueba de mercado).  
  2. Irreversibles → Analizar 24h con checklist de riesgos.  
  3. Reversibles → Actuar con 70% de datos para evitar "parálisis por análisis".  
**Relacionado**: [[Sesgo del costo hundido]], [[Heurísticos en management]]  
```

#### **d. Nota Permanente**

```markdown
# Toma de decisiones estratégicas: Irreversible vs. Reversible  
Framework usado por líderes en entornos VUCA ([[Referencia: Conferencia Liderazgo - Ruiz]]):  
- **Irreversible**:  
  - Ejemplo: Fusión de empresas.  
  - Acción: Espera estructurada + simulación de escenarios ([[Modelo de Montecarlo]]).  
- **Reversible**:  
  - Ejemplo: Lanzar feature en beta.  
  - Acción: "Minimum Viable Decision" → Implementar rápido, iterar después.  
---  
> **Link**: [[Mentalidad antifrágil]], [[Gestión de riesgos ágil]]  
---
```
### **Claves Transversales para Todos los Casos**

1. **Jerarquía de notas**:
    
    - **Fugaces**: Breves + etiquetas.
        
    - **Literatura**: Vinculadas a su Referencia + citas/páginas/minutos.
        
    - **Permanentes**: Autocontenidas + enlaces bidireccionales.
        
2. **Enlaces contextualizados**: No uses solo `[[Nota]]`, explica **por qué** se relacionan:
    
        
```markdown
La regla 70% de Ruiz complementa el concepto de [[Mentalidad antifrágil]], donde la acción rápida permite aprender del error.  
```
    
3. **Plantillas en Obsidian**:
    
    - Crea templates para cada tipo de nota (Reference, Literature, etc.) con campos predefinidos.
        
    - Usa plugins como **QuickAdd** para capturar fugaces sin romper el flujo.
        
4. **Multimedia**: En videos/podcasts, anota el minuto exacto (`02:15: Teoría X`). En juegos, captura pantallas y vincúlalas con el plugin `![[ ]]`



