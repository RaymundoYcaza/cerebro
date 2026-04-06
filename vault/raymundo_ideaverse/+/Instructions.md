---
up: 
related: 
created: 2025-06-12
tags:
  - map/instructions
---
# Cómo organizar la información
Una vez implementada la metodología ACE (Atlas, Calendar, Efforts) que sugiere tener tres ejes: Conocimiento, Tiempo, Proyectos; puedo establecer una regla general para organizar la información de mi cerebro digital, como se expone a continuación:

## Memoria histórica (🗓 Calendar/Logs)
En esta sección guardaré los eventos que han sucedido a nivel personal (Diario) o a nivel de entidades (Straffic, Inorizonti, Maria Morales, Server Maximax, Laptop RY, etc.) o a nivel local/regional (Noticias).

## Conocimiento

### 1. **Conocimiento Estable (📘 / `Atlas/Notes`)**
Es el **conocimiento conceptual, profundo o filosófico**, relativamente atemporal, que moldea mi forma de pensar y decidir. Aquí vive mi "cerebro estratégico".
**Ejemplos:**
- Definición de inteligencia artificial
- Análisis histórico de Jesús
- Fundamentos de epistemología
- Teorías sobre toma de decisiones
- Filosofía organizacional de tu empresa
**Ubicación:**
- Carpeta: `Atlas/Notes`

### 2. **Conocimiento Operativo (🛠️ / `Atlas/Notes/X`)**
Son las **notas prácticas**, procedimientos, comandos, cómo hacer algo. Este contenido es mutable, con fecha de caducidad, y muy orientado a la acción inmediata.
**Ejemplos:**
- Comandos de Artisan o Tinker
- Cómo crear contenedores Docker
- Sintaxis para consultas SQL específicas
- Pasos para configurar Rclone o NGINX
**Ubicación:**
- Carpeta: `Atlas/Notes/X` 

### 🗂️ Alternativa aún más clara (si quiero ir un paso más allá)
Agregar a la subcarpeta `X` un nombre semántico como:
- `Atlas/Notes/X/Procedimientos/`
- `Atlas/Notes/X/Operativas/`
- `Atlas/Notes/X/Playbook/`
- `Atlas/Notes/X/Acciones/`

### 🧩 COMPARATIVA DE CRITERIOS
| Nombre             | Criterio Principal                     | Enfoque Semántico               | Casos de Uso Comunes                                | Ventajas                                |
| ------------------ | -------------------------------------- | ------------------------------- | --------------------------------------------------- | --------------------------------------- |
| **Procedimientos** | Documentación paso a paso reutilizable | Formal, técnico, tipo ISO o BPM | Instructivos detallados, SOPs, onboarding           | Precisión, orden, trazabilidad          |
| **Operativas**     | Conocimiento técnico práctico          | Cotidiano, técnico-pragmático   | Comandos, configuraciones, cheatsheets              | Rapidez de acceso, útil en desarrollo   |
| **Playbook**       | Estrategias recurrentes con decisiones | Estrategia práctica, ágil       | Flujos de resolución, guías de acción con criterios | Acción contextual, adaptable, reflexiva |
| **Acciones**       | Tareas concretas y atómicas            | Ejecutable, directo             | “Cómo hacer X”, scripts, microtareas                | Claridad inmediata, ejecución rápida    |


### 🧠 Recomendación práctica para ti

Dado tu perfil técnico y estratégico, puedes combinar dos niveles:

```r
Atlas/
├── Notes/
│   ├── 📘 (notas permanentes conceptuales)
│   ├── Playbook/         ← Para decisiones tipo “si pasa esto, haz esto”
│   └── Operativas/       ← Para cómo ejecutar técnicamente (comandos, sintaxis, etc.)

```

## Proyectos (Esfuerzos)
