---
up:
  - "[[Meta Map]]"
related: 
created: 2025-05-18
---
 

## 1. Notas “People” normales
- **Qué son**: simples notas de persona, creadas a partir de la plantilla básica **People Template**.
- **Metadatos que suelen incluir**:
    - `up:` (enlace al contexto o “padre”)
    - `related:` (conexiones laterales)
    - `created:` (fecha de creación)
- **Cuándo usarlas**:
    - Para **capturar datos biográficos o conceptuales** de alguien (nombre, breve descripción, enlaces a sus obras o citas).
    - Cuando solo necesitas **registrar “quién es”** sin profundizar en su rol o responsabilidades dentro de un proyecto.
        
## 2. Mapas “People ROAR” y plantilla ROAR
- **Qué es “People ROAR”**: un **Map of Content** especializado en personas, llamado “People ROARs” en el kit [paruff.github.io](https://paruff.github.io/).
- **Plantillas relacionadas**:
    - **Master Key (People)(ROAR)**: define la estructura principal del MOC ROAR [paruff.github.io](https://paruff.github.io/?utm_source=chatgpt.com).
    - **People Template (ROAR add‑on)**: extiende la plantilla básica de persona con campos adicionales.
- **Qué significa ROAR** (siglas adaptadas según convenciones de gestión de stakeholders):
    - **R**ole (rol)
    - **O**bjectives (objetivos)
    - **A**uthority/Accountability (autoridad o responsabilidad)
    - **R**elationships (relaciones clave)
- **Metadatos adicionales** (ejemplo de frontmatter):

```yaml
---
in: [[People ROARs]]
role: "Product Owner"
objectives:
  - "Lanzar la versión 2.0"
  - "Alinear expectativas del equipo"
authority: "Decisión final sobre prioridades"
relationships:
  - "[[Equipo de Desarrollo]]"
  - "[[Stakeholders Externos]]"
created: 2025-05-10
---
```

**Cuándo usar “People ROAR”**:
- Al **organizar o visualizar** a los actores de un proyecto, equipo o proceso clave.
- Cuando necesitas **hacer análisis de stakeholders** o clarificar roles y responsabilidades.
- Para que tu MOC “People ROARs” se **autorellene** con todas las notas que usen el campo `in: [[People ROARs]]`, facilitando un mapa dinámico de quién hace qué.
