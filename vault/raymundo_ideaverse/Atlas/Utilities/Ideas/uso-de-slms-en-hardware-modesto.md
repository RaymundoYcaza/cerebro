---
up: []
related: []
created: 2026-04-12
---

# Uso de SLMs en hardware modesto

Continuar chat: <https://www.perplexity.ai/search/que-tan-cierta-es-la-noticia-d-Vd4KWLMwR_mR_EttZ_fy1Q>

Sí: **ya estamos en una etapa útil**, pero todavía no en una etapa “plug-and-play” donde un modelo pequeño sirva solo para todo. La situación actual favorece justo tu enfoque: **varios modelos pequeños, cada uno con una tarea estrecha, prompts fijos, salida estructurada y cambio manual u orquestado según el caso**. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

## Dónde estamos hoy

Hoy los modelos pequeños ya son suficientemente buenos para piezas concretas de un sistema, especialmente cuando la tarea está acotada y el contexto viene dado por tu aplicación. Eso encaja bien con tu stack actual, porque ya vienes probando modelos locales livianos en Ollama sobre una máquina con **4 GB de VRAM** y priorizas automatización, RAG y agentes austeros en recursos. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

## Lo que ya funciona

El patrón que mejor está funcionando hoy es este: **modelo pequeño + instrucciones rígidas + contexto externo + validación**. En ese esquema, un SLM ya puede hacer bien cosas como resumir notas, convertir texto a JSON, extraer campos, redactar borradores, clasificar entradas y asistir en scripting guiado. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

## Familias prometedoras

Ahora mismo hay dos señales fuertes en esa dirección. Por un lado, **Gemma 4 E2B y E4B** están diseñados explícitamente para dispositivos móviles, edge y navegador, con soporte para agentes, system prompts y llamada a funciones; por otro, **Qwen2.5** ya ofrece una familia separada para lenguaje general, coding y matemáticas, lo que encaja casi exactamente con la idea de “copilotos intercambiables”. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)

## Gemma 4

Gemma 4 ya expone un diseño muy alineado con tu visión: modelos pequeños de **2B y 4B efectivos**, ventana de contexto de **128K**, compatibilidad nativa con instrucciones del sistema y soporte integrado para **function calling**. Además, Google publica que los requisitos aproximados en **Q4_0** son de **3.2 GB para E2B** y **5 GB para E4B**, aunque advierte que eso cubre solo los pesos base y no toda la sobrecarga real de inferencia ni el KV cache. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

## Qwen como suite

Qwen2.5 está particularmente bien posicionado para especialización porque no solo tiene tamaños pequeños, sino también ramas dedicadas como **Qwen2.5-Coder** y **Qwen2.5-Math**. El propio equipo destaca mejoras en **structured outputs, JSON, system prompts, tool calling** y soporte de hasta **128K** tokens, que son exactamente las capacidades que hacen viable un orquestador sencillo basado en tareas. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)

## Qué significa “especializado”

Hoy “especializado” no suele significar un fine-tune profundo por tarea en todos los casos, sino más bien una combinación de tres capas. Primera, escoger un modelo que ya venga sesgado hacia el dominio —por ejemplo coder o math—; segunda, usar prompts fijos y contratos estrictos de salida; tercera, si hace falta, aplicar LoRA o ajuste ligero sobre ejemplos de tu flujo. [hatchworks](https://hatchworks.com/blog/gen-ai/small-language-models/)

## Casos ya maduros

Los casos más maduros para modelos pequeños especializados hoy son:

- **Extracción y estructuración** de texto a JSON o tablas. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)
- **RAG local** sobre documentación o vaults, si el modelo responde solo con contexto recuperado. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)
- **Resumen y transformación** de contenido, como reuniones, correos o notas. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)
- **Asistencia de código** en tareas acotadas, como debugging, explicación, refactors pequeños y generación de funciones cortas. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)

## Casos aún débiles

Siguen siendo flojos cuando les pides una mezcla de razonamiento abierto, memoria de trabajo larga, múltiples pasos implícitos y libertad creativa total. También fallan si les das demasiado margen semántico, que es justo lo que ya detectaste con modelos muy pequeños al intentar preguntas generales fuera de una tarea estrecha. [perplexity](https://www.perplexity.ai/search/555d17f1-3f46-4d9f-8734-bdbe6f49c834)

## Lo que ha cambiado de verdad

Lo que cambió en los últimos ciclos no es solo que el modelo “sepa más”, sino que ahora los pequeños vienen mejor preparados para **salidas estructuradas, system prompts, tool calling y contexto largo**. Eso vuelve más realista construir una arquitectura como la tuya: varios microcopilotos manuales hoy, y mañana un enrutador simple por tipo de tarea. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

## Tu visión es correcta

Tu idea de intercambiarlos manualmente primero y orquestarlos después es probablemente la estrategia más sensata para hardware modesto. De hecho, ya investigaste algo muy cercano a eso con agentes ligeros sobre Ollama, Qwen2.5-Coder y un cerebro local con Qdrant, así que no estás apostando a futuro especulativo: estás bastante alineado con la frontera práctica actual.

## Cómo se ve hoy en arquitectura

Una arquitectura realista en 2026 para esta visión sería:

- **Modelo general pequeño** para clasificar intención o elegir tarea, por ejemplo 1B–3B. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)
- **Modelo de extracción/redacción** para JSON, emails, formularios y resúmenes. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)
- **Modelo coder** para scripting y cambios pequeños en repositorios. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)
- **RAG/local search** fuera del modelo, con embeddings y recuperación documental.
- **Validador simple** con reglas o un segundo modelo pequeño cuando el error cuesta caro. [hatchworks](https://hatchworks.com/blog/gen-ai/small-language-models/)

## El límite real

El límite no es tanto “faltan modelos pequeños”, sino que aún falta más estandarización para componerlos sin fricción. Los modelos ya existen; lo más inmaduro sigue siendo el pegamento: routing, evaluación, caching, observabilidad y control de calidad por tarea. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

## Mi lectura práctica

Si lo que preguntas es si **ya vale la pena** trabajar así, mi respuesta es sí. Hoy ya tiene sentido montar un conjunto de **SLMs especializados** para tareas cotidianas, especialmente en tu caso, donde privacidad, costo, control local y modularidad pesan más que tener un único modelo brillante pero pesado. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

Si quieres, en el siguiente mensaje te puedo proponer un **catálogo concreto de 6 microcopilotos locales** para tu caso —PKM/Obsidian, correo, resumen, extracción JSON, scripting y clasificación— con qué modelo pequeño usar en cada uno y cómo enrutar en[Itre ellos manualmente al inicio.

# Cuáles serían los SLMs más apropiados para el equipo disponible en Inorizonti?

Sí: para tu caso, el catálogo más sensato es un conjunto de **microcopilotos por tarea**, no un solo modelo “todista”. Con tu hardware y tu forma de trabajar, lo ideal es separar entre **copilotos de texto/negocio**, **copilotos de PKM/RAG** y **copilotos de código** para Laravel e Ionic.

## Catálogo base

| Microcopiloto           | Tarea principal                                                 | Modelo sugerido                                                                                                                                                                                                  | Por qué encaja                                                                                                                                                                                                                                                                  |
| ----------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Router ligero           | Clasificar intención y decidir qué copiloto usar                | **llama3.2:1b** o similar 1B–2B                                                                                                                                                                                  | Un modelo muy pequeño basta para enrutar si le pides solo etiquetas y no razonamiento abierto. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)                                                                                                                           |
| Extractor estructurado  | Convertir texto a JSON, campos, tablas, entidades               | **Qwen2.5-3B-Instruct** [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)                                                                                                                           | Qwen2.5 destaca en salidas estructuradas y JSON, justo lo que más importa aquí. [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)                                                                                                                                  |
| Redactor operativo      | Correos, respuestas cortas, reformulación y tono                | **Gemma 4 E2B** [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)                           | Tiene 128K de contexto y está pensado para edge; sirve bien para redacción guiada con contexto fijo. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)     |
| Resumidor               | Reuniones, notas largas, changelogs, artículos internos         | **Gemma 4 E4B** si cabe; si no, **E2B** [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)   | Gemma 4 trae contexto largo y enfoque agentic, útil para resumir bloques extensos. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)                       |
| PKM/RAG                 | Consultar Obsidian, vaults y documentos con respuestas ancladas | **Gemma 4 E2B** o **Qwen2.5-3B-Instruct** [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent) | Para RAG lo decisivo no es tanto el tamaño, sino obedecer contexto y no salirse del material recuperado. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent) |
| Clasificador de negocio | Etiquetar tickets, correos, leads, documentos y flujos          | **granite3-dense:2b** o Qwen2.5-3B [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)                                                                                                                        | Estas tareas suelen ir muy bien con modelos pequeños si el esquema de salida está cerrado. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)                                                                                                                               |

## Copilotos de código

| Microcopiloto        | Tarea principal                                            | Modelo sugerido                                                                             | Por qué encaja                                                                                                                                                               |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Coder general        | Explicar código, escribir funciones, refactors pequeños    | **Qwen2.5-Coder 3B** [arxiv](https://arxiv.org/html/2409.12186v3)                           | La familia Qwen2.5-Coder fue diseñada específicamente para coding en varios tamaños. [arxiv](https://arxiv.org/html/2409.12186v3)                                            |
| Laravel backend      | CRUD, rutas, validación, Eloquent, controladores simples   | **Qwen2.5-Coder 3B** [arxiv](https://arxiv.org/html/2409.12186v3)                           | Te conviene un coder pequeño, pero con prompt muy alineado a tus convenciones PSR-12 y controladores simples. [arxiv](https://arxiv.org/html/2409.12186v3)                   |
| Ionic frontend       | Componentes, servicios, formularios, consumo API, fixes UI | **Qwen2.5-Coder 3B** o **Gemma 4 E4B** si cabe [arxiv](https://arxiv.org/html/2409.12186v3) | Ionic mezcla TypeScript, Angular y UI; ahí Qwen coder encaja mejor, y Gemma 4 puede ayudar en tareas de comprensión más largas. [arxiv](https://arxiv.org/html/2409.12186v3) |
| Shell/devops pequeño | Bash, Docker Compose, systemd, scripts utilitarios         | **Qwen2.5-Coder 3B** [arxiv](https://arxiv.org/html/2409.12186v3)                           | Este tipo de scripting acotado es uno de los usos más sólidos de un coder pequeño local. [arxiv](https://arxiv.org/html/2409.12186v3)                                        |
| Revisor de patch     | Revisar diff, detectar riesgos y pedir cambios mínimos     | **Qwen2.5-3B-Instruct** [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)      | Para revisar un diff corto, pesa más la disciplina del prompt y la estructura de salida que el tamaño bruto. [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)  |

## Recomendación concreta para ti

Como ya tienes **4 GB de VRAM** y vienes usando modelos como **llama3.2:1b** y **codeqwen**, yo lo montaría en dos niveles. Nivel 1: mantener un set ultraestable que casi seguro corre en tu equipo; nivel 2: dejar modelos algo más pesados para probar cuando tengas margen o offload a RAM. [perplexity](https://www.perplexity.ai/search/b753bc36-f113-4e22-a40a-642e196a0069)

## Set mínimo viable

Tu set mínimo viable podría ser este:

- **Router:** llama3.2:1b.
- **Extractor/JSON:** Qwen2.5-3B-Instruct. [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
- **PKM/RAG:** Gemma 4 E2B o Qwen2.5-3B-Instruct. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)
- **Coder Laravel/Ionic:** Qwen2.5-Coder 3B. [arxiv](https://arxiv.org/html/2409.12186v3)
- **Redactor corto:** Gemma 4 E2B. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)

## Laravel específico

Para Laravel, el microcopiloto no debería ser “programa todo”, sino algo más estrecho y confiable. Yo lo dividiría en cuatro modos de prompt: **crear endpoint**, **diagnosticar bug**, **generar migración/modelo/controlador simple**, y **proponer feature test básico**, porque eso se parece mucho más a tu forma real de trabajar que pedirle arquitectura compleja. [perplexity](https://www.perplexity.ai/search/1105f1c1-3075-4f3e-87e4-7cb8340b57cc)

## Ionic específico

Para Ionic, haría otro copiloto distinto del de Laravel, aunque use el mismo modelo base. Los modos útiles serían: **crear página/componente**, **conectar servicio HTTP al backend**, **arreglar formularios/reactive forms**, y **resolver errores de tipado o build**, porque mezclar backend y frontend en un solo prompt degrada bastante la precisión en modelos pequeños. [arxiv](https://arxiv.org/html/2409.12186v3)

## Cómo separarlos bien

Aunque uses el mismo modelo base para varias tareas, siguen siendo microcopilotos distintos si cambias tres cosas:

- **Prompt del sistema** fijo por rol. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)
- **Formato de salida** obligatorio, por ejemplo JSON, diff o checklist. [qwen.readthedocs](https://qwen.readthedocs.io/en/latest/framework/function_call.html)
- **Contexto filtrado** solo a los archivos o documentos relevantes.

## Qué modelo usaría por prioridad

Si tuviera que dejarte una prioridad simple, sería esta:

1. **Qwen2.5-Coder 3B** para Laravel, Ionic, bash y scripting. [arxiv](https://arxiv.org/html/2409.12186v3)
2. **Qwen2.5-3B-Instruct** para extracción, clasificación y revisión estructurada. [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
3. **Gemma 4 E2B** para redacción, RAG y resumen ligero con contexto largo. [ollama](https://ollama.com/library/gemma4:e2b)
4. **Gemma 4 E4B** solo si en tu entorno realmente cabe y responde con estabilidad. [ai.google](https://ai.google.dev/gemma/docs/core)

## Qué evitar

Evitaría usar modelos de 1B–2B para coding serio en Laravel o Ionic más allá de routing, snippets muy cortos o clasificación. También evitaría pedirle a un único modelo pequeño que haga a la vez análisis del requerimiento, planificación, edición multiarchivo, validación y commit message, porque ese flujo todavía rompe fácil en hardware modesto. [perplexity](https://www.perplexity.ai/search/555d17f1-3f46-4d9f-8734-bdbe6f49c834)

## Cómo se vería el catálogo final

Tu catálogo práctico, hoy, quedaría así:

- **MC-01 Router:** llama3.2:1b, clasifica tarea y elige copiloto.
- **MC-02 Struct:** Qwen2.5-3B-Instruct, texto a JSON/tablas/campos. [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
- **MC-03 Mail:** Gemma 4 E2B, redacta y reescribe correos. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)
- **MC-04 Summary:** Gemma 4 E2B/E4B, resume reuniones y documentos. [ai.google](https://ai.google.dev/gemma/docs/core)
- **MC-05 Vault:** Gemma 4 E2B o Qwen2.5-3B, responde solo con contexto RAG. [tomshardware](https://www.tomshardware.com/pc-components/gpus/benchmarking-nvidias-rtx-neural-texture-compression-tech-that-can-reduce-vram-usage-by-over-80-percent)
- **MC-06 BizFlow:** granite3-dense:2b o Qwen2.5-3B, clasifica y llena flujos. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)
- **MC-07 Laravel:** Qwen2.5-Coder 3B, backend y refactors chicos. [arxiv](https://arxiv.org/html/2409.12186v3)
- **MC-08 Ionic:** Qwen2.5-Coder 3B, componentes, servicios y formularios. [arxiv](https://arxiv.org/html/2409.12186v3)
- **MC-09 ShellOps:** Qwen2.5-Coder 3B, bash/docker/systemd. [arxiv](https://arxiv.org/html/2409.12186v3)
- **MC-10 Review:** Qwen2.5-3B-Instruct, revisión de diff y checklist de riesgos. [huggingface](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)

## Mi recomendación final de implementación

Para empezar, yo no construiría aún un orquestador complejo. Haría primero un **launcher manual** con nombres fijos de tarea —por ejemplo `task=laravel`, `task=ionic`, `task=summary`, `task=extract`— y un prompt del sistema distinto para cada uno; eso te dará señal clara sobre qué combinación funciona antes de automatizar routing. [youtube](https://www.youtube.com/watch?v=WKWvoZUyyjM)

Si quieres, en el siguiente mensaje te puedo entregar esto ya convertido en algo operativo:

- **los prompts de sistema exactos** para cada microcopiloto,
- una **convención de nombres** tipo `mc-laravel`, `mc-ionic`, `mc-vault`,
- y un **esqueleto de implementación con Ollama + Laravel** para invocarlos por API local.
