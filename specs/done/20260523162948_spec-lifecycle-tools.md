# Spec — Herramientas de ciclo de vida y seguimiento de specs

Estado: done

## Objetivo

Crear una herramienta operativa para gestionar el ciclo de vida de specs Markdown dentro del harness, permitiendo mover specs entre carpetas de estado, actualizar la línea `Estado:`, listar specs por estado y consultar progreso básico por microtareas/checklists.

Ruta objetivo sugerida:

```text
specs/backlog/20260523150000_spec-lifecycle-tools.md
```

## Contexto

Actualmente las specs pueden quedar en `specs/backlog/` aun después de ser implementadas y validadas. También falta una forma simple de seguimiento de microtareas realizadas, pendientes y programadas.

El repo `cerebro` usa un harness en `scripts/harness`, con documentación humana, `CHANGELOG.md`, `repo_map`, checks y herramientas operativas. Esta spec debe crear una herramienta pequeña, segura y usable tanto por el usuario como por un LLM/agente de código pequeño.

## Alcance

Crear una herramienta nueva:

```bash
python3 scripts/harness/spec_tools.py
```

Comandos mínimos:

```bash
python3 scripts/harness/spec_tools.py list
python3 scripts/harness/spec_tools.py list --state backlog
python3 scripts/harness/spec_tools.py move --spec specs/backlog/NOMBRE.md --to done
python3 scripts/harness/spec_tools.py progress --spec specs/done/NOMBRE.md
python3 scripts/harness/spec_tools.py complete-task --spec specs/active/NOMBRE.md --task MT-01
```

Estados soportados:

```text
backlog
active
done
cancelled
```

Directorios esperados:

```text
specs/backlog/
specs/active/
specs/done/
specs/cancelled/
```

Comportamiento principal:

- `move` mueve el archivo de una carpeta de estado a otra.
- `move` actualiza la línea `Estado: <estado>`.
- `list` muestra specs agrupadas o filtradas por estado.
- `progress` muestra microtareas detectadas, completadas y pendientes.
- `complete-task` marca una microtarea como completada cuando exista una línea compatible.
- La herramienta no ejecuta implementación de tareas.
- La herramienta no hace commit, push, merge, rebase ni modifica el vault.

## Fuera de alcance

- No implementar tablero Kanban visual.
- No integrar todavía con una base SQLite.
- No ejecutar microtareas automáticamente.
- No modificar código fuera del harness salvo los archivos de specs.
- No crear automatización con Git.
- No inferir éxito real de implementación; solo registrar estado operativo indicado por el usuario/agente.
- No modificar `vault/raymundo_ideaverse`.

## Requisitos EARS

### Ubiquitous

El sistema deberá exponer una herramienta CLI `scripts/harness/spec_tools.py`.

El sistema deberá reconocer los estados `backlog`, `active`, `done` y `cancelled`.

El sistema deberá mantener sincronizada la carpeta del spec con la línea `Estado:` del Markdown.

El sistema deberá operar solo sobre archivos `.md` dentro de `specs/`.

### Event-driven

Cuando el usuario ejecute `list`, el sistema deberá listar specs disponibles por estado.

Cuando el usuario ejecute `list --state <estado>`, el sistema deberá listar solo los specs de ese estado.

Cuando el usuario ejecute `move --spec <ruta> --to <estado>`, el sistema deberá mover el archivo al directorio correspondiente y actualizar `Estado:`.

Cuando el usuario ejecute `progress --spec <ruta>`, el sistema deberá mostrar conteo de microtareas totales, completadas y pendientes.

Cuando el usuario ejecute `complete-task --spec <ruta> --task MT-XX`, el sistema deberá marcar como completada la microtarea indicada si existe una línea compatible.

### State-driven

Mientras el directorio `specs/<estado>/` no exista, el sistema deberá crearlo cuando sea necesario para una operación válida.

Mientras un spec esté en `specs/backlog/`, su línea `Estado:` deberá ser `backlog`.

Mientras un spec esté en `specs/done/`, su línea `Estado:` deberá ser `done`.

Mientras existan checkboxes `- [ ]` o `- [x]` relacionados con microtareas, `progress` deberá contarlos.

### Unwanted behavior

Si el usuario intenta mover un archivo fuera de `specs/`, el sistema deberá rechazar la operación.

Si el usuario indica un estado no soportado, el sistema deberá fallar con un mensaje claro.

Si el archivo destino ya existe, el sistema deberá cancelar salvo que se implemente un flag explícito futuro.

Si el spec no contiene línea `Estado:`, el sistema deberá agregarla cerca del inicio del documento de forma segura.

Si `complete-task` no encuentra la microtarea solicitada, el sistema deberá cancelar sin modificar el archivo.

### Optional

Donde se use `--dry-run`, el sistema deberá mostrar lo que haría sin modificar archivos.

Donde se use `--json`, el sistema deberá devolver salida estructurada para consumo por agentes.

## Archivos esperados

- `scripts/harness/spec_tools.py`
- `scripts/harness/docs/spec_tools.md`
- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`
- Opcional: `scripts/harness/tests/smoke/test_spec_tools.py`

## Tareas

1. Crear herramienta CLI aislada `spec_tools.py`.
2. Implementar comandos `list` y `move`.
3. Implementar comando `progress`.
4. Implementar comando `complete-task`.
5. Agregar validaciones de seguridad.
6. Documentar uso.
7. Actualizar changelog y repo map.
8. Ejecutar checks del harness.

## Microtareas

## MT-01 — Inspeccionar estructura de harness y specs

### Tipo

- setup

### Archivos permitidos

- `scripts/harness/context/repo_map.md`
- `scripts/harness/docs/harness_usage.md`

### Objetivo

Confirmar convenciones actuales del harness antes de crear la nueva herramienta.

### Pasos

- [ ] Revisar si existe carpeta `specs/`.
- [ ] Revisar si existen documentos que mencionen specs.
- [ ] Confirmar estilo de scripts CLI existentes en `scripts/harness`.
- [ ] No modificar archivos en esta microtarea.

### Check local

```bash
ls scripts/harness
find specs -maxdepth 2 -type f 2>/dev/null | head
python3 scripts/harness/harness.py check
```

### Criterio de aceptación

- [ ] Se conoce si `specs/` existe.
- [ ] Se conoce el patrón CLI que debe seguir `spec_tools.py`.
- [ ] No hubo modificaciones de archivos.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-02 — Crear CLI base spec_tools.py

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Crear el archivo base de la herramienta con parser de argumentos y ayuda.

### Pasos

- [ ] Crear `scripts/harness/spec_tools.py`.
- [ ] Usar `argparse`.
- [ ] Agregar subcomandos vacíos o mínimos: `list`, `move`, `progress`, `complete-task`.
- [ ] Definir constantes de estados válidos.
- [ ] Agregar función `main()`.
- [ ] Asegurar ejecución directa con `python3`.

### Check local

```bash
python3 scripts/harness/spec_tools.py --help
python3 scripts/harness/spec_tools.py list --help
python3 scripts/harness/spec_tools.py move --help
python3 scripts/harness/spec_tools.py progress --help
python3 scripts/harness/spec_tools.py complete-task --help
```

### Criterio de aceptación

- [ ] El script existe.
- [ ] Todos los comandos muestran ayuda.
- [ ] No hay errores de sintaxis.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-03 — Implementar validación segura de rutas y estados

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Evitar que la herramienta modifique archivos fuera de `specs/` o use estados inválidos.

### Pasos

- [ ] Crear helper para resolver rutas relativas al repo.
- [ ] Validar que `--spec` esté dentro de `specs/`.
- [ ] Validar extensión `.md`.
- [ ] Validar estados permitidos: `backlog`, `active`, `done`, `cancelled`.
- [ ] Preparar creación segura de directorios `specs/<estado>/`.

### Check local

```bash
python3 scripts/harness/spec_tools.py move --spec README.md --to done
```

### Criterio de aceptación

- [ ] La operación sobre `README.md` es rechazada.
- [ ] El error explica que solo se permiten specs dentro de `specs/`.
- [ ] Estados inválidos son rechazados.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-04 — Implementar comando list

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Listar specs existentes por estado o filtrados por un estado específico.

### Pasos

- [ ] Implementar `list`.
- [ ] Agregar flag opcional `--state`.
- [ ] Buscar archivos `.md` en `specs/backlog`, `specs/active`, `specs/done`, `specs/cancelled`.
- [ ] Mostrar ruta relativa y estado.
- [ ] Manejar carpetas inexistentes sin fallar.

### Check local

```bash
python3 scripts/harness/spec_tools.py list
python3 scripts/harness/spec_tools.py list --state backlog
```

### Criterio de aceptación

- [ ] Lista specs sin error aunque falte alguna carpeta.
- [ ] `--state backlog` filtra correctamente.
- [ ] La salida es legible para usuario y LLM.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-05 — Implementar actualización de línea Estado

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Crear helper para actualizar o insertar la línea `Estado:` dentro del Markdown.

### Pasos

- [ ] Detectar línea que empiece con `Estado:`.
- [ ] Reemplazarla por `Estado: <estado>`.
- [ ] Si no existe, insertarla después del primer título `# ...`.
- [ ] Preservar el resto del archivo sin reformatear.
- [ ] Mantener encoding UTF-8.

### Check local

```bash
python3 -m py_compile scripts/harness/spec_tools.py
```

### Criterio de aceptación

- [ ] Existe helper aislado.
- [ ] No altera contenido no relacionado.
- [ ] El archivo compila correctamente.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-06 — Implementar comando move

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Mover specs entre carpetas de estado y actualizar `Estado:`.

### Pasos

- [ ] Implementar `move --spec <ruta> --to <estado>`.
- [ ] Crear `specs/<estado>/` si no existe.
- [ ] Rechazar si el archivo destino ya existe.
- [ ] Actualizar contenido con `Estado: <estado>`.
- [ ] Mover archivo al directorio destino.
- [ ] Mostrar ruta anterior y nueva.
- [ ] Agregar `--dry-run` para mostrar operación sin escribir.

### Check local

```bash
python3 scripts/harness/spec_tools.py move --spec specs/backlog/archivo-inexistente.md --to done
```

### Criterio de aceptación

- [ ] Archivo inexistente produce error claro.
- [ ] Estado inválido produce error claro.
- [ ] `--dry-run` no modifica archivos.
- [ ] En caso real, mueve archivo y actualiza `Estado:`.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-07 — Implementar comando progress

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Reportar progreso de microtareas y checkboxes dentro de un spec.

### Pasos

- [ ] Implementar `progress --spec <ruta>`.
- [ ] Detectar headings `## MT-XX`.
- [ ] Detectar checkboxes `- [ ]` y `- [x]`.
- [ ] Reportar total de microtareas detectadas.
- [ ] Reportar checkboxes completados y pendientes.
- [ ] Reportar porcentaje simple si hay datos suficientes.
- [ ] No modificar archivos.

### Check local

```bash
python3 scripts/harness/spec_tools.py progress --spec specs/backlog/archivo-inexistente.md
```

### Criterio de aceptación

- [ ] Archivo inexistente produce error claro.
- [ ] En un spec real, muestra microtareas y progreso.
- [ ] No modifica el spec.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-08 — Implementar complete-task

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Permitir marcar una microtarea como completada de forma controlada.

### Pasos

- [ ] Implementar `complete-task --spec <ruta> --task MT-XX`.
- [ ] Buscar el heading `## MT-XX`.
- [ ] Marcar como completadas las líneas `- [ ]` dentro de esa microtarea hasta el siguiente `## MT-`.
- [ ] No modificar otras microtareas.
- [ ] Si la microtarea no existe, cancelar sin cambios.
- [ ] Agregar `--dry-run`.

### Check local

```bash
python3 scripts/harness/spec_tools.py complete-task --spec specs/backlog/archivo-inexistente.md --task MT-01
```

### Criterio de aceptación

- [ ] Archivo inexistente produce error claro.
- [ ] Microtarea inexistente produce error claro.
- [ ] En un spec real, solo marca checkboxes de la microtarea indicada.
- [ ] `--dry-run` no modifica archivos.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-09 — Agregar salida JSON opcional

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_tools.py`

### Objetivo

Permitir que agentes consuman la salida de `list` y `progress` de forma estructurada.

### Pasos

- [ ] Agregar flag `--json` a `list`.
- [ ] Agregar flag `--json` a `progress`.
- [ ] Emitir JSON válido.
- [ ] Mantener salida humana por defecto.
- [ ] No agregar dependencias externas.

### Check local

```bash
python3 scripts/harness/spec_tools.py list --json
```

### Criterio de aceptación

- [ ] La salida de `--json` puede parsearse como JSON.
- [ ] La salida humana sigue funcionando.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-10 — Crear documentación de spec_tools

### Tipo

- docs

### Archivos permitidos

- `scripts/harness/docs/spec_tools.md`
- `scripts/harness/README.md`

### Objetivo

Documentar el flujo operativo de specs para usuario y LLM.

### Pasos

- [ ] Crear `scripts/harness/docs/spec_tools.md`.
- [ ] Explicar estados soportados.
- [ ] Documentar comandos
