

## Resumen ejecutivo

El Mac Mini con chip M4 base (10 núcleos CPU, 10 núcleos GPU, 16 núcleos en Neural Engine) incluye **16 GB de memoria unificada** (ampliable a 24 o 32 GB solo al comprar)【1†L204-L209】【3†L237-L243】. Gracias a la arquitectura unificada de Apple (UMA) no hay costo de transferencia entre CPU y GPU【19†L40-L48】. Sin embargo, **solo ~75 % de la RAM** se asigna al GPU por defecto (≈12 GB útiles en 16 GB totales)【36†L34-L42】. Esto implica que un modelo LLM ocupa buena parte de la memoria. Por ejemplo, un modelo de **7 mil millones de parámetros en 4-bits ocupa ~3.5 GB de memoria** y cabe cómodamente en 16 GB【31†L73-L78】【19†L58-L61】; en cambio un modelo de 13B requiere ~26 GB (FP16) o ~6.5 GB en 4-bits【31†L73-L78】【17†L275-L278】. Según análisis recientes, con 16 GB se pueden ejecutar sin problemas modelos de ~7–8 B (cuantizados a 4 bits) como **Llama2/3 7B–8B, Mistral 7B, Falcon 7B**【14†L43-L45】【17†L275-L278】. Con 24 GB cabrían ~12–14B (Q4) y con 32 GB hasta ~30B (Q4)【17†L275-L279】【17†L279-L283】. Modelos de 70B pueden correrse con 64–96 GB (≈40–45 GB en Q4)【17†L288-L292】. En la práctica, un Mac Mini M4 base (16 GB) permite modelos 7–8B de alto desempeño (incluso en tareas de código)【21†L45-L49】【19†L58-L61】. La cuantización a 4-bits (Q4_K_M) es estándar para ajuste fino de memoria【31†L73-L78】【17†L288-L292】. No es viable atender dos sesiones intensivas simultáneamente, pues duplicar la carga de RAM provoca **swap y caída de rendimiento** (solo ~12 GB GPU disponibles)【36†L34-L42】【36†L80-L86】. Para aprovechar el chip, se recomienda activar la aceleración Metal (MPS/MLX) y configurar apropiadamente los parámetros: p.ej. en llama.cpp usar `-ngl -1` (todas capas en GPU) y un tamaño de contexto y batch moderado【5†L115-L119】【26†L146-L154】. En las siguientes secciones se detallan las especificaciones del M4, requisitos de modelos (Llama2/3, Mistral, Falcon, Vicuna, GPT4All, Alpaca, etc.), tamaños máximos ejecutables (nativo vs cuantizado), soporte de doble usuario, configuraciones óptimas y herramientas recomendadas. 

## Especificaciones de hardware del Mac Mini M4 base

El Mac Mini M4 base integra el chip **Apple M4** de 3 nm, con CPU de 10 núcleos (4 de alto rendimiento a ~4.4 GHz y 6 de alta eficiencia)【1†L204-L209】. El GPU es integrado de 10 núcleos (Apple GPU con ~120 GB/s de ancho de banda de memoria)【1†L204-L209】, y un Neural Engine de 16 núcleos dedicado a AI. Usa **memoria unificada** (CPU, GPU y NE comparten el mismo pool). El modelo básico trae **16 GB** de RAM unificada (también se ofrece en 24 GB o 32 GB, no ampliable tras la compra)【3†L237-L243】. Este RAM tiene 120 GB/s de ancho de banda【1†L204-L209】, similar al VRAM de una GPU media. El almacenamiento SSD es típicamente de 256 GB (PCIe NVMe), ampliable hasta 1–2 TB【3†L286-L291】. Corre macOS 15 “Sonoma” (o superior); para usar aceleración Metal 4 se necesita macOS 15.0+【5†L36-L41】. Debido a UMA, no hay cuello de botella CPU↔GPU en operaciones AI【19†L40-L48】. Sin embargo, **solo ~75% de la memoria física se asigna a la GPU**, por diseño de Apple para no saturar el sistema operativo【36†L34-L42】. En un Mac de 16 GB esto implica ≈12 GB efectivos para el modelo en GPU; el resto queda reservado. 

## Requisitos de memoria de modelos locales populares

Los LLM de varios miles de millones de parámetros tienen demandas que dependen de precisión y context. En líneas generales【17†L274-L278】【31†L73-L78】:
- **3–4B** parámetros: ~8 GB de RAM mínimo. (Ej.: Phi-3.8B, Gemma3-4B)【17†L274-L278】.
- **7–8B** parámetros: ~16 GB mínimo. (Ej.: Llama2/3 7B–8B, Mistral 7B, Vicuna 7B, Falcon 7B)【17†L275-L278】【21†L45-L49】. En 4-bits ocupan unos 3.5–4 GB (7–8B *0.5B/param ≈3.5–4 GB)【31†L73-L78】, ajustables con volatilidad en contexto.
- **12–14B**: ~24 GB mínimo. (Ej.: Llama2/3 13B, CodeLlama 13B, Qwen3 14B)【17†L277-L280】.
- **30–32B**: ~48 GB recomendado. (Ej.: modelos ~32B con cuantización Q4)【17†L279-L282】.
- **70B**: 64–96 GB. En Q4 ocupa ≈40–45 GB【17†L288-L292】. Se recomiendan 64+ GB para margen. 

La cuantización reduce drásticamente los requisitos: por ejemplo, un modelo de 7B en 4-bit ocupa ≈3.5 GB【31†L73-L78】 en memoria, frente a ~14 GB en FP16. Un LLM de 70B cuantizado a 4-bit necesita ~40 GB disco/RAM【17†L288-L292】. Estos valores toman en cuenta el modelo base sin incluir el caché de contexto ni el sistema operativo. Dejar unos 4–6 GB libres para el OS/contexto es prudente. En resumen, un Mac de 16 GB maneja bien modelos de **7–8B** (4-bit)【17†L275-L278】【19†L58-L61】, uno de 24 GB llega a **12–13B**, y un M4 con 32–48 GB puede cargar modelos de **30–32B** (Q4)【17†L277-L282】【17†L288-L292】.

## Tamaños máximos ejecutables en Mac Mini M4

En el Mac Mini M4 *base* con 16 GB, lo realista es correr modelos hasta ≈8B cuantizados. Por ejemplo, se han reportado ejecuciones fluidas de **Mistral-7B, Llama3 8B, Gemma-7B, F3Mini-3.8B, Orca2-7B** (todos Q4) en 8–16 GB【14†L43-L45】【17†L275-L278】. El análisis de la figura adjunta sugiere que 64 GB sería el “sweet spot” para modelos de 70B【14†L58-L61】, pero el modelo base de 16 GB solo permite ~7–9B con fluidez【14†L43-L45】【19†L58-L61】. Con configuración de 24 GB cabrían modelos ~13B (en 4-bit) manteniendo cierto espacio libre. A 32 GB se acercan ~30B en Q4. **Ejemplos prácticos**: Llama-2 7B (FP16≈14 GB; Q4≈3.5 GB) sí cabe, pero Llama-2 13B (≈26 GB FP16; 6.5 GB Q4) queda justo o requiere ≥24 GB. Un modelo Falcon-40B (≈80 GB FP16; 20 GB Q4) es inviable sin una Mac más grande. En Qwen-2.5 de 72B se requieren ≥64 GB【17†L282-L284】. 

Resumiendo: en un **Mac Mini M4 de 16 GB** es factible ejecutar en local eficientemente modelos ~7–8B (Q4) para texto y código. Modelos ≥12B son límite y exigirían cuantización muy agresiva o más RAM. Con 24 GB la frontera sube a ~13B (Q4)【17†L277-L282】; con 48 GB se acercan ~32B【17†L279-L282】; y con 64+ GB se habilitan ~70B quantizados【17†L282-L284】.

## Dos usuarios concurrentes

El Mac Mini comparte la misma memoria unificada entre procesos. Con 16 GB totales, apenas hay ≈12 GB para la GPU según límite Apple【36†L34-L42】. Si un modelo de ~7B ocupa ~4 GB, dos instancias idénticas necesitarían ~8 GB, lo que dejaría poco espacio para el OS. En la práctica **correr dos LLMs grandes simultáneamente provoca uso de swap y severas caídas de rendimiento**【36†L34-L42】【36†L80-L86】. Apple no permite sumar memoria entre dispositivos, por lo que no es viable usar dos Macs en paralelo para un solo modelo. Técnicamente se podría lanzar dos sesiones sencillas (p.ej. dos modelos muy pequeños 3B), pero cualquier carga media saturaría la RAM y dispararía la memoria virtual. Además, usar dos LLMs intensivos simultáneamente elevaría la temperatura del chip; aunque Apple Silicon es eficiente, puede haber *thermal throttling* en cargas largas, reduciendo la velocidad de token. En resumen, un Mac Mini M4 suele atender **una sesión de LLM a la vez** con soltura; intentar dos usuarios codiciosos acabará en intercambio a disco y rendimiento insuficiente.

## Configuraciones recomendadas para mejor rendimiento

Para exprimir el M4 se deben usar optimizaciones:

- **Cuantización:** Emplear modelos en 4 bits (formato GGUF Q4_K_M) siempre que sea posible【31†L73-L78】【17†L288-L292】. Q4 es estándar local; esto reduce el peso ~75%. En llama.cpp y ollama basta añadir `:Q4_K_M` al nombre del modelo【5†L69-L71】. Niveles más bajos (6-bit, 8-bit) ocupan más RAM, menos recomendados si se busca eficiencia.

- **Batch y contexto:** Ajustar `batch_size` moderado (p.ej. 16–64) para balancear latencia vs uso de memoria. Un contexto (`-c`) muy grande consume más memoria de KV cache【5†L117-L119】. Se sugiere comenzar con un tamaño de contexto habitual (p.ej. 1024-2048 tokens) y reducir si falta RAM.

- **Hilos de CPU:** Asignar tantas threads como cores de rendimiento (p.ej. `-t 6` o más) para usar el CPU. En Mac M4 hay 4 cores P; usar 6–8 hilos en llama.cpp suele ser efectivo.

- **Aceleración GPU/Metal:** Aprovechar la GPU integrada via Metal Performance Shaders (MPS) o CoreML. En llama.cpp o su binding Python, activar procesamiento en GPU (parámetro `-ngl -1` en CLI o `n_gpu_layers=-1, f16_kv=True` en llama-cpp-python) 【5†L115-L119】【26†L146-L154】. Alternativamente, usar Apple MLX (“ML Compute”) mediante TensorFlow o PyTorch con soporte `mps`. Según Apple, **MLX puede superar a PyTorch** en algunos casos【19†L122-L129】. En resumen, configuraciones como `llama-cpp -m modelo.gguf -t 8 -b 32 --threads 8 -ngl -1 -c2048` (usando MPS y 16-bit KV) son típicas. 

- **Librerías y frameworks:** Usar versiones recientes de las bibliotecas. Por ejemplo, llama.cpp desde Homebrew【5†L53-L58】 con Metal habilitado, o transformers+optimum con backend Metal/MPS. Core ML Tools permite convertir PyTorch a `.mlmodel` para optimizar aún más. 

El diagrama siguiente ilustra la selección de modelo según RAM disponible:

```mermaid
flowchart TD
    A[RAM disponible] -->|≤ 16 GB| B[Modelos hasta ~8B (Q4)]
    A -->|24 GB| C[Modelos ~12–13B (Q4)]
    A -->|32–48 GB| D[Modelos ~30B (Q4)]
    B --> E[Ejemplos: Llama2-7B, Mistral-7B, Falcon-7B (cuantizados)]
    C --> F[Ejemplos: Llama2-13B, CodeLlama-13B (cuantizados)]
    D --> G[Ejemplos: Llama3-70B (en Q4, límite)]
```

## Tabla comparativa de modelos

A continuación se ofrece una comparación aproximada de distintos modelos (tamaño, memoria) y su **viabilidad** en Mac Mini M4 (16 GB), suponiendo versiones cuantizadas a 4 bits:

| Modelo                 | Parámetros   | Tamaño en disco ≈ | RAM para inferencia ≈ | Tamaño Q4 ≈ | Viabilidad  |
|------------------------|-------------:|-----------------:|----------------------:|------------:|:-----------:|
| LLaMA2-7B              | 7 B          | 14 GB (FP16)     | ~14 GB (FP16)【31†L73-L78】| ~3.5 GB    | Alta        |
| LLaMA2-13B             | 13 B         | 26 GB            | ~26 GB               | ~6.5 GB     | Media       |
| LLaMA3-8B (≈)          | 8 B          | 16 GB            | ~16 GB               | ~4 GB       | Alta        |
| LLaMA3-13B             | 13 B         | 26 GB            | ~26 GB               | ~6.5 GB     | Media       |
| Mistral-7B             | 7.3 B        | 14.6 GB          | ~15 GB               | ~3.7 GB     | Alta        |
| Falcon-7B              | 6.9 B        | 13.8 GB          | ~14 GB               | ~3.4 GB     | Alta        |
| Falcon-40B             | 40 B         | 80 GB            | ~80 GB               | ~20 GB      | Baja        |
| Vicuna-7B              | 7 B          | 14 GB            | ~14 GB               | ~3.5 GB     | Alta        |
| CodeLlama-7B           | 7 B          | 14 GB            | ~14 GB               | ~3.5 GB     | Alta        |
| CodeLlama-13B          | 13 B         | 26 GB            | ~26 GB               | ~6.5 GB     | Media       |
| GPT4All (7B)           | ~7 B         | ~13 GB           | ~14 GB               | ~3.5 GB     | Alta        |
| Alpaca-7B              | ~7 B         | ~13.6 GB         | ~14 GB               | ~3.5 GB     | Alta        |

*Estimaciones basadas en la norma de 2 bytes/parámetro (FP16) y en quantización Q4_K_M【31†L73-L78】【17†L288-L292】. “Viabilidad” alta indica que el modelo (cuantizado) se ejecuta sin problemas en 16 GB; media requiere ajustar cuantización/recursos; baja, no cabría en 16 GB.*

## Herramientas y entornos recomendados

Para ejecutar LLMs localmente en macOS se recomiendan las siguientes herramientas:

- **Homebrew**: facilita la instalación. Por ejemplo `brew install llama.cpp`【5†L53-L58】 y `brew install ollama`【38†L66-L74】. 
- **llama.cpp** (C++ con bindings Python): biblioteca ligera para ejecutar modelos GGUF en CPU/GPU. Soporta MPS/Metal. Se puede compilar con `-DLLAMA_METAL=ON` para activar GPU. Existe también [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) que facilita su uso en Python.
- **Ollama**: interfaz CLI muy sencilla. Instalar con `brew install ollama`【38†L66-L74】. Permite `ollama pull modelo` y `ollama run modelo` fácilmente. Incluye varios LLMs empaquetados optimizados para Apple.
- **Transformers + Optimum**: usar PyTorch con backend MPS o `mlcompute` para acelerar en Apple. Hugging Face Optimum incluye aceleraciones para Apple Silicon.
- **Apple MLX / Core ML**: Apple provee frameworks (ML Compute, CoreML) optimizados para M1/M2/M3/M4. Se puede convertir un modelo PyTorch a formato CoreML (`.mlmodel`) con CoreMLTools y ejecutarlo eficientemente en CPU/GPU/ANE.
- **LM Studio / ULTRA**: apps GUI que simplifican ejecución local (usando llama.cpp o MLX internamente). No son obligatorios pero facilitan la interacción.
- **Docker**: menos recomendado si se quiere usar GPU local (Docker Desktop en macOS no soporta GPU). Solo útil para aislar entornos Python puros.

## Pasos prácticos: ejemplo con Mistral-7B

A modo de ejemplo, estos son los pasos básicos para correr un modelo como *Mistral-7B* en Mac Mini M4:

1. **Instalar dependencias:** Abra Terminal. Actualice brew (`brew update`) y luego instale llama.cpp y Python (si no tiene):  
   ```bash
   brew install llama.cpp
   brew install python
   ```
2. **Descargar el modelo:** En Hugging Face (o LLM-Explorer) elija una variante cuantizada de Mistral 7B. Por ejemplo, use `mistral-ai/Mistral-7B-v0.1` y seleccione la versión *GGUF Q6_K* o *Q4_K*【21†L73-L76】. Descargue el archivo `.gguf` a una carpeta local.
3. **Ejecutar con llama.cpp:** Compile llama.cpp con soporte Metal (si no lo hizo):  
   ```bash
   git clone https://github.com/ggerganov/llama.cpp
   cd llama.cpp && mkdir build && cd build
   cmake .. -DCMAKE_APPLE_SILICON_PROCESSOR=arm64 -DLLAMA_METAL=on
   make -j
   ```
   Luego invoque el modelo:  
   ```bash
   ./build/bin/main --model /ruta/a/mistral-7b.Q4_K_M.gguf -t 8 -b 32 -n 512 -c 2048
   ```
   Esto carga el modelo en Metal/GPU (`-ngl -1` por defecto) con 8 threads CPU y batch 32. Ajuste los valores si falta memoria o rendimiento.
4. **Prueba interactiva:** Alternativamente, puede usar llama-cpp-python en Python:  
   ```python
   pip install llama-cpp-python
   llm = Llama(model_path="/ruta/mistral-7b.Q4_K_M.gguf", n_ctx=2048, n_batch=32,
               n_gpu_layers=-1, f16_kv=True, n_threads=8)
   response = llm("Escribe una función en Python que sume dos números", max_tokens=200)
   print(response['choices'][0]['text'])
   ```
5. **Ollama (opcional):** Con Ollama instalado (`brew install ollama`【38†L66-L74】), simplemente haga:  
   ```bash
   ollama pull mistral-7b-instruct
   ollama run mistral-7b-instruct
   ```
   Esto descarga y ejecuta Mistral-7B con un asistente de chat listo.

Con estas herramientas puede explorar localmente otros modelos (Llama2/3, Gemma, Phi, etc.), siguiendo procesos análogos. 

**Fuentes:** Datos de memoria y benchmarks se han tomado de la documentación de los modelos (Hugging Face), blogs y foros especializados【31†L73-L78】【17†L288-L292】【19†L58-L61】【21†L45-L49】, y sitios técnicos sobre Apple Silicon【36†L34-L42】【19†L122-L129】. Estos sirven de guía para seleccionar el modelo y configuración óptimos en un Mac Mini M4.
