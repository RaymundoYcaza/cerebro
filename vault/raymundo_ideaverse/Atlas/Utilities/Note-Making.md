---
up:
  - "[[Home]]"
related: []
created: 2026-02-24
---

>[!quote]  ### Y, si me equivoqué al escribir algo, te pido que me lo digas porque el error es humano.

## Unresolved notes
### Versión DQL
```dataview
TABLE WITHOUT ID key AS "Nota no creada", rows.file.link AS "Referenciada desde"
FROM "Atlas/Dots" AND #note 
FLATTEN file.outlinks as outlinks
WHERE !outlinks.file
  AND !contains(meta(outlinks).path, ".png")
  AND !contains(meta(outlinks).path, ".jpg")
  AND !contains(meta(outlinks).path, ".jpeg")
  AND !contains(meta(outlinks).path, ".gif")
  AND !contains(meta(outlinks).path, ".svg")
  AND !contains(meta(outlinks).path, ".webp")
  AND !contains(meta(outlinks).path, ".pdf")
GROUP BY outlinks
LIMIT 100
```


## ¿Cómo pasar una nota de spark a evergreen paso a paso?
El proceso de transformar una **"spark"** (chispa) en una nota **"evergreen"** (madura o perenne) es el núcleo del marco de trabajo **ARC** (Añadir, Relacionar, Comunicar) y se basa en los niveles de **emergencia de ideas**.

Aquí tienes el paso a paso detallado según las fuentes:

1. Captura de la "Spark" (Emergencia Nivel 1)

Todo comienza con la creación de una **"thing note"** o nota de concepto sobre algo que consideres interesante o importante.

• **Acción:** Captura la idea rápidamente usando una nota nueva.

• **Estado:** En este punto, la nota es una **"spark"** que vive en tu espacio de **"ADD"** (Añadir). Es una idea atómica que acaba de "evaporarse del éter" para volverse algo sólido.

2. Clasificación y Reentrada (Relacionar)

Una vez capturada, debes mover la nota de la carpeta de entrada al **Atlas** para empezar a trabajar con ella.

• **Etiquetado:** Si la nota está aislada, puedes etiquetarla como `note/boat` (una idea solitaria en el océano) o `note/develop` si estás listo para "hincarle el diente" y desarrollarla más.

• **Nota-making:** En lugar de solo "tomar" la nota pasivamente, empiezas a **"hacer" la nota** añadiendo tus propios comentarios (`commentary`) sobre por qué la idea es relevante.

3. Conexión Atómica (Emergencia Nivel 2)

El siguiente paso es vincular esta chispa con lo que ya conoces.

• **Disparador mental:** Utiliza la frase **"Esto me recuerda a..."** para forzar a tu cerebro a encontrar relaciones con otras notas existentes.

• **Enlaces:** Crea vínculos (links) entre estas notas atómicas. Al hacerlo, las ideas empiezan a comportarse como un ecosistema vivo.

4. Ensamblaje en un MOC (Emergencia Nivel 3)

Cuando acumulas varias notas relacionadas y sientes un "apretón mental" por el desorden, es momento de crear un **Mapa de Contenido (MOC)**.

• **Reunión de ideas:** Reúne los enlaces de tus chispas relacionadas en una sola nota (el MOC).

• **Fase de colisión:** Aquí es donde ocurre el trabajo duro. Empiezas a reorganizar las notas, comparándolas entre sí para afilar los argumentos.

5. Maduración a "Evergreen"

La nota se convierte en **evergreen** a través de un proceso de "colisión de ideas" similar a un acelerador de partículas.

• **Refinamiento:** Durante la fase de colisión en el MOC, cortas lo que no sirve, combinas ideas y editas hasta que el contenido sea de **alta calidad, claro y nítido**.

• **Resultado:** Las notas que sobreviven a este proceso de pensamiento profundo y síntesis son tus **notas evergreen**. Estas notas ya no son solo información externa, sino pensamientos sólidos y propios listos para ser comunicados o utilizados en creaciones mayores.

6. Compuestos de Valor (Emergencia Nivel 4)

Finalmente, tus notas evergreen pueden conectarse con otros MOCs (por ejemplo, relacionar un MOC de "Hábitos" con uno de "Modelos Mentales") para generar **conocimiento compuesto** y nuevas creaciones.





## ¿Cuál es la estructura de una nota?
| Sección                 | Función              |
| ----------------------- | -------------------- |
| **Núcleo**              | Qué dijo el spark    |
| **Statement**           | Qué piensas tú       |
| **Notas relacionadas**  | Dónde vive en tu red |
| **Pregunta generativa** | Qué queda abierto    |
| **Fuentes**             | De dónde viene       |
| **Comunicar**           | A dónde va           |

**FASE 1 — CAPTURAR** _(qué dice el spark)_

1. Aislar lo que resonó
    
2. Transformarlo en Núcleo formal
    

**FASE 2 — PENSAR** _(qué piensas tú)_  
3. Hacerte preguntas sobre el tema central → Pregunta generativa  
4. Identificar subtemas implícitos no definidos → Notas semilla pendientes  
5. Relacionar con otros temas → Notas relacionadas  
6. Crear el Statement

**FASE 3 — PROYECTAR** _(a dónde va)_  
7. Decidir qué Comunicar
	1. **¿Esto cambia algo en cómo actúo?** → anota una decisión o hábito  
	2. **¿Esto tiene valor para alguien más?** → anota un formato: post, conversación, video  
	3. **¿Esto abre un proyecto o tarea concreta?** → anota el siguiente paso con verbo de acción

No necesitas responder las tres siempre. Pero sí necesitas responder **al menos una** — si no puedes, la nota todavía no está madura y debería quedarse en `note/boat🚤`.

#### Mover una nota a través de los niveles de emergencia de ideas: Fase RELATE

- Paso 1: Mover al Atlas.
Mover la nota de la carpeta ADD a Atlas/Notes. Esto indica que ya no es solo algo que "cae" en tu sistema, sino parte de tu cuerpo de conocimiento.


- Paso 2: Note-making (Hacer la nota): No debe quedar la fórmula copiada de un libro (fuente). Se debe traducir al propio sabor, gramática y sintaxis.

> Ejemplo de comentario propio: "Integrar es como deshacer una derivada; es el proceso de reconstruir la función original a partir de su tasa de cambio".

- Paso 3: Establecer vínculos (Relate): Utilizar el disparador mental "Esto me recuerda a..." para conectar la nota con lo que ya se conoce.

> Escribe en la nota: "Esto me recuerda a la `[[Regla de la potencia para derivadas]]`, pero en sentido inverso". Al crear este enlace, estás cableando tu cerebro.

- Paso 4: Ensamblaje en un MOC (Nivel 3 de Emergencia): Si empiezas a tener varias notas sobre matemáticas, crea un MOC (Map of Content) llamado `[[Cálculo MOC]]`

> En este mapa, coloca el enlace a tu nota de integrales junto a otras chispas relacionadas.

- Paso 5: Colisión y Refinamiento: Dentro del MOC, haz que las ideas "choquen". Revisa tu nota de integrales junto a la de derivadas. Quizás te das cuenta de que falta mencionar la "constante C". Editas la nota para hacerla más nítida, limpia y crujiente

## ¿Cómo procesar una nota spark en tres pasos?

### 1) Qué hago con el texto original

No copiarlo en tu nota “Thing” significa: no convertir la nota en un _clon_ del spark. Puedes manejarlo así:

- Crear una nota en **Sources** con el texto completo (o el enlace / captura / referencia), y desde tu Thing Note solo apuntas a esa fuente. Esto preserva el material original separado de tu pensamiento.​
    
- En tu Thing Note, escribir solo: (a) tu formulación del núcleo en tus palabras, (b) 2–3 frases de reacción/interpretación, (c) un enlace a la nota fuente.
    
- Si lo quieres “recordable” sin copiar: guarda 1–2 citas _muy_ cortas (fragmentos mínimos) solo como ancla, no como contenido principal.
    

Pregunta: ¿quieres conservar el spark como “evidencia” (para revisitarlo) o solo como detonante (y luego descartarlo)?

### 2) Relate vs Communicate (cómo diferenciarlos)

**Relate** = crear _posibles conexiones_ (ganchos) para que la idea pueda vivir en una red, aunque hoy esas notas estén vacías. En otras palabras: “¿con qué otras ideas podría chocar o conversar esto?”

**Communicate** = producir una _salida propia_ y utilizable (una mini-tesis, una regla, una pregunta guía, una decisión o experimento). Es donde la nota deja de ser “interesante” y se vuelve “operativa”.

Un test rápido:

- Si lo que escribes empieza con “Esto se parece a… / Esto conecta con…”, es Relate.
    
- Si empieza con “Para mí significa… / A partir de esto voy a… / Mi postura es…”, es Communicate.
    

### 3) Dónde coloco la nota en tu Atlas

Viendo tu estructura (Atlas → Dots → People/Sources/Statements/Things), yo lo haría así:

- El texto original completo: **Atlas/Dots/Sources/** (una nota tipo “Fuente: [título]”). Esto calza con separar material capturado de tus notas propias.​
    
- Tu nota principal (tu núcleo): **Atlas/Dots/Things/** porque es una idea/“thing” que quieres desarrollar y enlazar.​
    
- Si en Communicate terminas con una postura tipo “Regla/Principio”: puedes además crear (o derivar) una nota en **Atlas/Dots/Statements/** con esa frase como statement, enlazada desde la Thing. (Solo si realmente queda como afirmación estable, no si aún está verde)​
    
### Siguiente paso (mínimo)

1. “Lo guardo como Source + Thing (sin Statement todavía)”
    
2. “Quiero que salga un Statement desde ya”
    
3. “Solo quiero la Thing Note y nada más por ahora”
## Preguntas frecuentes

### ¿Por qué funciona ARC?
• **Evita el "Collector's Fallacy":** Al obligarte a interactuar, evita que simplemente acumules notas que no entiendes (over-collecting).

• **Fomenta la Emergencia:** Ayuda a que la estructura "se gane" (earned structure) a través del esfuerzo mental del operador en el nivel 1 y 2 de emergencia.

• **Mantiene el Control Humano:** El sistema LYT enfatiza que cuando **tú** haces las conexiones, el conocimiento se vuelve permanente y útil para el futuro.


### “Salidas” (Communicate): ¿misma nota o notas aparte?

Usa esta regla:

- Si la salida es **un primer borrador**, dependiente del contexto, o todavía estás pensando: déjala en la _misma_ Thing Note en una sección tipo “Communicate / Mi take / Implicaciones / Experimento”.
    
- Si la salida se convierte en una **frase-principio** que quieres reutilizar en muchos lugares (una regla, definición, heurística, postura): crea una nota aparte en **Atlas/Dots/Statements/** y enlázala desde la Thing Note.​
    

Otra regla práctica (muy simple): “¿Lo citaría yo mismo en 3 meses sin re-leer toda esta nota?”

- Si sí → promuévelo a Statement.
    
- Si no → se queda dentro de la Thing.

### ¿Una nota por cada idea?

Evita hacerlo “por cada idea” al inicio: crea **1 Thing Note** con 1–2 salidas máximo, y solo separa en notas cuando algo se vuelva reutilizable o empiece a atraer enlaces desde varias partes (señal de que merece independizarse). Esto reduce la sobre-atomización y deja que la estructura emerja con el uso.




