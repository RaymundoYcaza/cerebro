---
up:
  - "[[Prompts]]"
related: []
created: 2025-09-14
---


## ALGORITMO DE DECISIÓN:

1. **¿Es accionable?** (requiere que YO haga algo específico)
   - SÍ → Evaluar urgencia → Efforts/[On|Ongoing|Simmering|Sleeping]
   - NO → Continuar al paso 2

2. **¿Es temporal?** (vinculado a fecha específica)
   - SÍ → Calendar/[Logs|Notes]
   - NO → Continuar al paso 3

3. **¿Qué tipo de conocimiento?**
   - **Técnico/Procedimental** ("cómo hacer", comandos, definiciones) → Atlas/Notes/Things
   - **Filosófico/Reflexivo** (interpretable, opiniones, conceptos) → Atlas/Notes/ (raíz)
   - **Sobre personas** → Atlas/Notes/People
   - **Sobre organizaciones/sistemas** → Atlas/Notes/Entities
   - **Afirmaciones/principios** → Atlas/Notes/Statements
   - **Material externo** → Atlas/Notes/Sources/[tipo]
   - **No claro/experimental** → Atlas/Notes/X/

## FORMATO DE SALIDA REQUERIDO:

**CLASIFICACIÓN:** [Carpeta específica]
**TÍTULO SUGERIDO:** [Nombre descriptivo para la nota]

**ESTRUCTURA DE NOTA:**
# [Título]

```markdown
---
up: []
related: []
created: 2025-09-14
---

## [Secciones apropiadas según tipo]

**ETIQUETAS:**
- Etiquetas primarias: #z/procesado/[fecha] #z/tipo/[accion|conocimiento|temporal] #z/area/[trabajo|personal|aprendizaje]
- Etiquetas secundarias: [según contexto específico siempre dentro de #z]
```

**JUSTIFICACIÓN:** [Por qué esta ubicación y no otra]

## CONTEXTO DEL USUARIO:
- Especialista en business intelligence, programador, analista, ingeniero industrial
- Trabaja con animación, tecnología, gestión de negocios
- Necesita separar conocimiento técnico (consultivo) del filosófico (reflexivo)
- Requiere acceso rápido a información técnica sin internet

---

**INSTRUCCIÓN:** Analiza el siguiente texto y proporciona la clasificación completa:

[AQUÍ VA EL TEXTO A ANALIZAR]