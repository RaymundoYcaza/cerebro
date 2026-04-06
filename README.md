# Proyecto Cerebro – README

## Visión general

Cerebro es un "Second Brain" autónomo construido sobre el vault de Obsidian de Raymundo, con Git como base de datos y agentes LLM que ejecutan tareas en background mientras el usuario duerme.[memory:189] El sistema indexa notas, repara frontmatter, actualiza MOCs, responde consultas vía agentes (Kai, Vault Manager), y provee captura rápida de notas por SSH, todo de forma reproducible en Ubuntu 24.

---

## Objetivo general

Construir un Second Brain autónomo que:

- Use el vault de Obsidian como única fuente de verdad.
- Use Git como base de datos (historial, respaldo, audit log).
- Permita a agentes LLM (Kai, Vault Manager, futuros agentes) procesar notas, reparar estructura y ejecutar tareas nocturnas.
- Soporte captura rápida de notas (spark, source, contact) vía SSH, sin abrir la interfaz gráfica de Obsidian.[memory:189]

---

## Objetivos específicos

1. **Infraestructura base reproducible**
   - Mantener el vault en un directorio fijo en Ubuntu 24.
   - Automatizar qmd (motor semántico) y systemd timers para reindexar el vault sin intervención.
   - Mantener scripts de recuperación (`restore-setup.sh`) para volver a levantar todo tras un formateo.[memory:190]

2. **Agentes LLM integrados con el vault**
   - Agente **Kai** como asistente primario para el vault (búsqueda, síntesis, planificación).[memory:191]
   - Agente **Vault Manager** para reparar frontmatter y, en el futuro, reubicar notas.
   - Skills de OpenCode: `/recall`, `/atomize`, `/deep-research`, `/daily-summary`, `/vault-manager`.

3. **Manejo del Inbox y frontmatter LYT/ACE**
   - Estandarizar el frontmatter de notas en `+` (Inbox) con propiedades base `up`, `related`, `created`, siguiendo el método ACE de Linking Your Thinking.[memory:190]
   - Proveer scripts que reparen inconsistencias de frontmatter de forma controlada.

4. **Captura rápida vía CLI/SSH**
   - Implementar scripts de captura rápida (`scripts/capture/`) para crear notas de tipo `spark`, `source` y `contact` usando plantillas del vault.
   - Permitir seleccionar modo de captura manual u OpenAI (IA), dejando OpenAI listo para fases posteriores.[memory:189]

5. **Automatización nocturna** (futuro)
   - Orquestar qmd reindex, Vault Manager, y sincronización Git mediante systemd timers y scripts nocturnos.
   - Integrar acceso móvil (p.ej. Telegram + tmux) para interactuar con el sistema desde el celular.

---

## Arquitectura actual

### Componentes principales

- **Vault de Obsidian**: `vault/raymundo_ideaverse/` – estructura LYT con Atlas, Inbox `+`, Efforts, Calendar, etc.[memory:190]
- **Motor semántico `qmd`**: indexa el contenido del vault y expone búsqueda semántica via MCP.
- **OpenCode**: framework de agentes con:
  - Agente `kai` (modelo configurado via `model: provider/model-id`).
  - Agente `vault-manager` para tareas de mantenimiento.
  - Skills: `/recall`, `/atomize`, `/deep-research`, `/daily-summary`, `/vault-manager`.
- **Vault Manager (scripts/vault_manager/)**:
  - `repair.py`: repara frontmatter de notas en `+`.
  - `repair-ui.sh`: interfaz TUI con `gum` + `jq` para filtrar y aceptar reparaciones sin recordar parámetros.[memory:191]
  - `relocate.py`: placeholder (para mover notas según reglas futuras, actualmente no hace cambios).[memory:190]
- **Captura CLI (scripts/capture/)**:
  - `main.py`: punto de entrada para captura interactiva.
  - `config.py`: carga configuración YAML.
  - `profiles.py`: define perfiles soportados (`spark`, `source`, `contact`).
  - `templates.py`: carga y renderiza plantillas desde el vault.
  - `manual_prompt.py`: preguntas guiadas para cada perfil.
  - `ai_prompt.py`: stub para integración con OpenAI Responses API.
  - `engine.py`: orquesta datos + plantilla + escritura de archivo.
  - `utils.py`: utilidades (slug, fecha, escritura, nombres de archivo).[memory:189]

---

## Estructura de directorios relevante

```text
cerebro/
├── scripts/
│   ├── vault_manager/
│   │   ├── repair.py
│   │   ├── repair-ui.sh
│   │   └── relocate.py
│   └── capture/
│       ├── main.py
│       ├── config.py
│       ├── profiles.py
│       ├── templates.py
│       ├── manual_prompt.py
│       ├── ai_prompt.py
│       ├── engine.py
│       └── utils.py
└── vault/
    └── raymundo_ideaverse/
        ├── +/                 # Inbox
        ├── Atlas/
        ├── Efforts/
        ├── Calendar/
        └── Templates/
            └── capture/
                ├── spark.md
                ├── source.md
                └── contact.md
```

---

## Vault Manager – Sprint 2 (Acción controlada)

### Objetivo

Reparar el frontmatter de notas en `+` sin moverlas y sin cambios automáticos masivos. Todas las decisiones de reparación pasan por el usuario (o por una UI TUI). Esto respeta el principio de sensemaking de LYT/ACE: la fricción de procesar la nota es parte del aprendizaje.[memory:190]

### `repair.py`

- Escanea el directorio `+` (Inbox) en el vault.
- Extrae el frontmatter si existe (`---` o `***`).
- Verifica que existan las claves:
  - `up` (lista)
  - `related` (lista)
  - `created` (fecha)
- Si faltan, propone añadirlas y genera una `Proposal` por archivo.
- Puede operar en modo:
  - `--dry-run`: solo muestra propuestas (humano o JSON).
  - `--apply`: aplica cambios con confirmación por archivo.
  - `--apply --yes`: aplica sin preguntar (pensado para ser llamado por una UI que ya filtró/confirmó).[memory:191]

### `repair-ui.sh`

- Script Bash con TUI sobre `repair.py` usando:
  - `gum filter --no-limit` para buscar/seleccionar notas.
  - `jq` para procesar la salida JSON de `repair.py`.
- Flujo:
  1. Llama a `repair.py --dry-run --format json`.
  2. Extrae `relative_path` y `action_summary` a TSV.
  3. Usa `gum filter` para seleccionar múltiples notas.
  4. Muestra un resumen de selección.
  5. Pregunta confirmación global.
  6. Ejecuta `repair.py --apply --yes` por cada nota seleccionada.[memory:191]

Esta interfaz permite procesar lotes grandes de notas sin recordar parámetros ni comandos complejos.

### `relocate.py` (Placeholder)

- Pensado para un futuro Sprint.
- Responsabilidad futura:
  - Mover notas desde `+` a `Atlas/Dots`, `Efforts`, `Calendar`, etc., cuando cumplan reglas de madurez (p.ej. `up` no vacío, `type: effort`, títulos con fechas, etc.).
- Actualmente solo imprime un mensaje y no hace cambios.

---

## Captura rápida – Sprint Fase 1 (spark, source, contact)

### Objetivo

Permitir captura rápida de notas vía SSH/CLI, sin abrir Obsidian, usando plantillas del vault y asegurando el frontmatter base (`up`, `related`, `created`).[memory:189]

### Configuración (`scripts/capture/config.yaml`)

- Define rutas y plantillas sin hardcodear en Python.
- Ejemplo de campos clave:
  - `vault_root`: ruta absoluta al vault.
  - `templates_root`: ruta a `Templates/capture/`.
  - `defaults`: formato de fecha, longitud máxima de nombre de archivo, modelo OpenAI por defecto.
  - `profiles`: configuración por perfil:
    - `spark`: `output_dir: "+"`, `template: spark.md`, `filename_strategy: timestamp-title`.
    - `source`: `output_dir: "Sources"`, `template: source.md`, `filename_strategy: title`.
    - `contact`: `output_dir: "Contacts"`, `template: contact.md`, `filename_strategy: title`.

Cambiar la ubicación de `Sources` o `Contacts` se hace editando `config.yaml`, sin modificar código.[web:220]

### Perfiles soportados

1. **spark**
   - Captura ultrarrápida de ideas.
   - Pregunta: título opcional, cuerpo.
   - Escribe en `+/` usando plantilla `spark.md`.

2. **source**
   - Para fuentes (libro, blog, video, curso, conversación, reflexión).
   - Pregunta: subtipo, título, autor, URL, fecha de la fuente, notas rápidas.
   - Escribe en `Sources/` con plantilla `source.md`.

3. **contact**
   - Para contactos/personas.
   - Pregunta: nombre, cumpleaños (`birthday`), dirección, teléfono, email, organización, rol y notas.
   - Escribe en `Contacts/` con plantilla `contact.md`.

### Propiedades base y específicas

- Todas las notas creadas por `capture` incluyen:
  - `up: []`
  - `related: []`
  - `created: YYYY-MM-DD` (por defecto la fecha actual, pero se planea permitir override manual en los prompts).
- Contactos incluyen además:
  - `birthday`, `address`, `phone`, `email`, `organization`, `role`.

### Integración con plantillas del vault

- Las plantillas viven en `vault/raymundo_ideaverse/Templates/capture/`.
- Ejemplos:
  - `spark.md`: encabezado con `up`, `related`, `created` y cuerpo con `{{title}}`, `{{body}}`.
  - `source.md`: añade `type: source`, `subtype`, `author`, `url`, `source_date`, `notes`.
  - `contact.md`: añade `type: contact` y los campos de persona.
- `templates.py` se encarga de cargar el `.md` correspondiente y reemplazar placeholders `{{campo}}` con datos proporcionados por el usuario o calculados.

### Flujo de ejecución (`scripts/capture/main.py`)

1. Mostrar lista de perfiles disponibles (`spark`, `source`, `contact`).
2. Preguntar modo de captura (`manual` / `openai`), siendo `manual` el default.
3. Recoger datos vía `manual_prompt.py` (preguntas en CLI).
4. Combinar datos con campos comunes (`up`, `related`, `created`).
5. Renderizar la plantilla adecuada.
6. Guardar la nota en la ruta configurada.
7. Imprimir la ruta final de la nota.

`ai_prompt.py` implementa un stub para OpenAI (Responses API), listo para evolucionar cuando se quiera delegar parte de la captura al LLM en lugar de preguntas manuales.[web:201][web:208]

---

## Bugs encontrados y decisiones tomadas

1. **Bug qmd MCP ignorando `--index`**
   - qmd en modo MCP ignoraba el argumento `--index` y usaba internamente `index.sqlite`.
   - Solución: crear un symlink `index.sqlite → portable.sqlite` dentro del wrapper `qmd-mcp`.
   - Decisión: encapsular este fix en un wrapper para que la reproducibilidad no dependa de recordar el bug.

2. **Modelo por defecto inválido en agentes OpenCode**
   - `model: default` en `kai.md` y `vault-manager.md` generaba "Agent kai's configured model default/ is not valid".
   - Solución: cambiar `model` a un identificador real `provider/model-id` (ej. `opencode/gpt-5.1-codex`) según la configuración de `opencode.json`.[conversation_history:193]

3. **`tkinter` no disponible**
   - Un intento inicial de crear una UI con `tkinter` falló porque Python no fue compilado con soporte Tcl/Tk.
   - Decisión: abandonar GUI y adoptar TUI con `gum` + `jq`, alineado con el flujo natural de trabajo en terminal.

4. **Desfase entre `repair-ui.sh` y `repair.py`**
   - Tras actualizar `repair.py` para soportar `--format`, el wrapper seguía llamando a la versión anterior.
   - Diagnóstico: diferencia de rutas/Python entre `fish` y `bash` (p.ej. Pythons distintos en PATH).
   - Solución: forzar rutas absolutas y/o el mismo intérprete Python que se usa en `fish`.

5. **Desalineación de columnas en resumen TUI**
   - `repair-ui.sh` asumía columnas `relative_path`, `type`, `destination`, `actions`, pero `repair.py` cambió a `relative_path`, `action_summary`.
   - Resultado: el resumen mostraba `destino: add:up,add:related,add:created` y `acciones` vacío.
   - Solución: reescribir `repair-ui.sh` para usar solo `relative_path` y `action_summary` y renombrar a `faltan: ...`.

---

## Respaldo y restauración del proyecto

### Respaldo

1. **Git como base de datos**
   - El vault está versionado en Git.
   - Para guardar el estado:
     - `git status`
     - `git add .`
     - `git commit -m "Mensaje descriptivo"`
     - `git push origin main`

2. **Respaldo externo del vault**
   - Copia del directorio `vault/raymundo_ideaverse/` a otra ubicación o disco externo.

3. **Configuración de scripts y timers**
   - Asegurarse de que `scripts/`, `.opencode/`, y configuraciones de systemd user units (p.ej. `~/.config/systemd/user/qmd-embed.service`) estén bajo control de Git o documentados para recrearlos.

### Restauración

1. **Clonar el repositorio**
   - `git clone git@github.com:RaymundoYcaza/cerebro.git`.

2. **Ejecutar script de recuperación**
   - Hay un script `scripts/restore-setup.sh` encargado de restaurar dependencias y configuración tras un formateo (instalar qmd, crear symlinks, configurar MCPs, etc.).[memory:190]
   - Revisar y actualizar este script para que incluya:
     - instalación de dependencias de Python (`pyyaml`, `openai` si se usa),
     - instalación de `gum`, `jq`,
     - configuración de systemd timers para qmd y, en el futuro, tareas nocturnas.

3. **Reconstruir índices semánticos**
   - Volver a ejecutar el indexado de qmd para el vault.

4. **Verificar agentes OpenCode**
   - Comprobar que `kai`, `vault-manager`, y los skills están correctamente referenciados y que los modelos configurados existen.

---

## Cómo ejecutar los componentes principales

### Vault Manager

- Ver propuestas de reparación en modo humano:

  ```bash
  python3 scripts/vault_manager/repair.py --dry-run
  ```

- Ver propuestas de reparación en JSON:

  ```bash
  python3 scripts/vault_manager/repair.py --dry-run --format json
  ```

- Aplicar cambios con confirmación por archivo:

  ```bash
  python3 scripts/vault_manager/repair.py --apply
  ```

- Procesar por lotes con TUI (`gum` + `jq`):

  ```bash
  bash scripts/vault_manager/repair-ui.sh
  ```

### Captura rápida de notas (spark, source, contact)

- Ejecutar el capturador:

  ```bash
  python3 scripts/capture/main.py
  ```

- Flujo típico:
  1. Elegir perfil (`spark`, `source`, `contact`).
  2. Elegir modo (`manual`, `openai` – actualmente manual es el camino estable).
  3. Responder a las preguntas.
  4. Ver la ruta de la nota generada.

### OpenAI (opcional / futuro cercano)

- Requisitos:
  - `pip install openai`
  - `export OPENAI_API_KEY="tu_api_key"`

- El stub actual en `ai_prompt.py` se puede extender para que:
  - Tome un "brain dump" textual del usuario.
  - Llame a `client.responses.create(...)` con un prompt que exija JSON.[web:201][web:208]
  - Parse ese JSON y lo use como `profile_data` para `engine.py`.

---

## Futuro roadmap

1. **Fase 2 captura**
   - Integrar `gum` en el flujo de captura para selección de perfil y asistente.
   - Agregar prompts de fecha custom para `created` cuando el usuario quiera registrar notas de fechas distintas a la actual.

2. **Relocate Manager**
   - Implementar reglas para mover notas según su estado de madurez (e.g. `up` no vacío → `Atlas/Dots`).
   - Integrar con MOCs y Atlas/Maps.

3. **Nightly Runner**
   - Script `nightly-sync.sh` que ejecute:
     - reindexado qmd,
     - Vault Manager (en modo seguro),
     - commit/push git,
     - otras tareas nocturnas.
   - Timer systemd (`nightly-sync.timer`).

4. **Acceso móvil (CCBot)**
   - Bot de Telegram que hable con Kai y con los scripts de captura vía tmux/SSH.

5. **Integración LLM avanzada**
   - OpenAI/Anthropic para:
     - clasificar notas,
     - sugerir `up` y `related`,
     - generar resúmenes diarios (`/daily-summary`).

Este README está diseñado para que tanto un LLM como un analista humano puedan retomar el proyecto, entender el contexto y continuar implementando el roadmap sin perder la visión original.

## Log de sesiones

Cada sesión de trabajo se documenta aquí para mantener un historial claro de avances y decisiones. El formato está pensado para que tanto LLMs como analistas humanos puedan retomar el proyecto.

---

### 2026-04-06 — Sesión de pulido de captura rápida y ajustes de Aurora

En esta sesión se avanzó en la pulida de la funcionalidad de captura rápida y en el ajuste de la plantilla Aurora para que sea robusta y coherente con el resto del sistema. [cite:189]

#### Objetivo de la sesión

- Mejorar el flujo de captura, haciéndolo más estable y fácil de usar.
- Ajustar la plantilla Aurora para que acepte correctamente los campos `up`, `related`, `created`, `title` y `body`.
- Asegurar que el programa vuelva al menú tras guardar una nota, en lugar de cerrarse.

#### Actividades realizadas

- Corregir la plantilla `aurora.md` para que los placeholders sean `{{related}}` y `{{created}}` sin espacios internos, resolviendo el problema de no reemplazo de valores.
- Mejorar `templates.py` para soportar placeholders con espacios, usando expresiones regulares en lugar de reemplazo literal.
- Añadir `gum write` para capturas multilínea, evitando que Enter envíe el texto de forma incorrecta.
- Hacer que el flujo de `main.py` vuelva al menú tras guardar una nota, en lugar de cerrarse; añadir una opción de salir explícita en los menús.

#### Detalles técnicos

- `gum write` ahora se usa para capturar el cuerpo de notas, permitiendo pegado de texto largo sin interrupciones.
- La plantilla `aurora.md` incluye `up`, `related`, `created`, `aliases` y `tags` con placeholders correctos.
- `templates.py` usa regex para reemplazar placeholders, soportando variantes con espacios (`{{ created }}`, `{{  created  }}`).
- `main.py` vuelve al menú principal tras guardar una nota, pidiendo confirmación para salir.

#### Resultados obtenidos

- La captura de notas `spark`, `source`, `contact` y `aurora` es ahora más estable y robusta.
- La plantilla Aurora acepta correctamente los campos `up`, `related`, `created`, `title` y `body`.
- El flujo de trabajo es más intuitivo, con menús claros y opción de salir explícita.

#### Tabla resumen de estado actual

| Objetivo / Funcionalidad                 | Estado actual    | Detalle                                                                                                                                                                        |
| ---------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ✅ Infraestructura base reproducible     | 🟢 ✔️            | Configuración en restore-setup.sh, config.yaml y perfiles organizados. Todo es reproducible desde cero.                                                                        |
| 🔄 Agentes LLM integrados                | 🟡 En desarrollo | Kai y Vault Manager ya van en el repositorio, pero la integración con IA es solo el stub (ai_prompt.py) sin conectividad real.                                                 |
| 🔄 Manejo del Inbox y frontmatter ACE    | 🟡 En desarrollo | spark y aurora capturan correctamente, pero vault-manager es solo un script de reparación que no reubica notas. Falta el relocate real.                                        |
| ✅ Captura rápida CLI/SSH                | ✅ Funciona      | main.py y manual_prompt.py permiten captura rápida de spark, source, contact y aurora desde terminal, con menú gum y salida de notas en + / Sources / Contacts / Atlas/Dots/X. |
| 🟡 Validación básica de fechas           | 🟡 En desarrollo | ask_profile_data valida created, source_date y birthday como YYYY-MM-DD, pero es solo validación; no hay lógica de faltas ni bloqueo fuerte.                                   |
| 🟢 Frontmatter base (up/related/created) | ✅ Funciona      | Todas las notas generadas mantienen up, related y created en el frontmatter, gracias al renderizado de plantillas.                                                             |
| 🔴 Aurora con plantilla robusta          | 🟢 Según versión | La plantilla aurora.md ahora incluye up, related y created con placeholders {{related}} y {{created}} correctamente, sin espacios internos.                                    |
| 🔴 Interacción IA (OpenAI) real          | 🔴 Por hacer     | ai_prompt.py es solo un stub con openai_capture_stub; falta implementar llamada real a OpenAI y parsear la salida JSON para alimentar engine.py.                               |
| 🔴 Gestión avanzada de notes             | 🔴 Por hacer     | spark captura, pero no hay mover las notas a Atlas/Dots ni Efforts según reglas de madurez; eso es el fututo relocate.py.                                                      |
| 🟢 Respaldo y restauración               | ✅ Funciona      | Git respalda el vault y scripts; restore-setup.sh restaura la configuración de forma programada tras formateo o reinstalación.                                                 |
