# Spec — Menú interactivo auxiliar para spec_tools

Estado: backlog

## Objetivo

Crear un script auxiliar interactivo para usar las funciones existentes de `scripts/harness/spec_tools.py` sin tener que recordar rutas ni pasar argumentos largos como `--spec specs/backlog/...`.

El menú deberá permitir navegar specs por estado, seleccionar archivos disponibles y ejecutar acciones comunes: listar, ver progreso, completar microtarea y mover specs entre estados.

Ruta objetivo sugerida:

```text
specs/backlog/20260523153000_spec-tools-interactive-menu.md
```

## Contexto

Ya existe o está planificada la herramienta CLI `scripts/harness/spec_tools.py`, con comandos por argumentos como:

```bash
python3 scripts/harness/spec_tools.py progress --spec specs/backlog/20260523141512_discard-working-tree-git-tools.md
```

Ese flujo es útil para agentes, pero incómodo para uso humano frecuente porque obliga a copiar rutas completas. Para no tocar ni romper lo ya hecho, se propone crear un script auxiliar interactivo que use la herramienta existente como backend operativo.

## Alcance

Crear un script nuevo:

```bash
python3 scripts/harness/spec_menu.py
```

Comportamiento mínimo:

- Abrir en estado `backlog` por defecto.
- Mostrar specs disponibles del estado actual.
- Permitir cambiar de estado: `backlog`, `active`, `done`, `cancelled`.
- Permitir seleccionar un spec por número.
- Sobre un spec seleccionado, permitir:
  - ver progreso
  - completar microtarea
  - mover a otro estado
  - volver a lista
- Reutilizar `scripts/harness/spec_tools.py` mediante subprocess o import seguro.
- No duplicar lógica compleja de movimiento, progreso o modificación de specs.
- Mantener interfaz simple compatible con terminal estándar.

Comandos esperados:

```bash
python3 scripts/harness/spec_menu.py
python3 scripts/harness/spec_menu.py --state backlog
python3 scripts/harness/spec_menu.py --state active
```

## Fuera de alcance

- No reemplazar `spec_tools.py`.
- No modificar el comportamiento actual de `spec_tools.py`.
- No implementar interfaz TUI avanzada con dependencias externas.
- No usar librerías externas como `rich`, `textual`, `questionary` o `fzf`.
- No implementar búsqueda fuzzy.
- No ejecutar microtareas automáticamente.
- No hacer commit, push, merge, rebase ni modificar Git.
- No modificar `vault/raymundo_ideaverse`.

## Requisitos EARS

### Ubiquitous

El sistema deberá exponer un script auxiliar `scripts/harness/spec_menu.py`.

El sistema deberá iniciar en el estado `backlog` por defecto.

El sistema deberá usar estados válidos: `backlog`, `active`, `done`, `cancelled`.

El sistema deberá reutilizar `spec_tools.py` para operaciones de specs siempre que sea posible.

El sistema deberá operar únicamente sobre archivos dentro de `specs/`.

### Event-driven

Cuando el usuario ejecute `python3 scripts/harness/spec_menu.py`, el sistema deberá mostrar los specs de `backlog`.

Cuando el usuario seleccione otro estado, el sistema deberá mostrar los specs disponibles en ese estado.

Cuando el usuario seleccione un spec, el sistema deberá mostrar un menú de acciones para ese spec.

Cuando el usuario elija ver progreso, el sistema deberá ejecutar o reutilizar la funcionalidad equivalente a `spec_tools.py progress --spec`.

Cuando el usuario elija completar microtarea, el sistema deberá pedir el ID de microtarea y ejecutar o reutilizar `spec_tools.py complete-task`.

Cuando el usuario elija mover spec, el sistema deberá pedir estado destino y ejecutar o reutilizar `spec_tools.py move`.

### State-driven

Mientras no haya specs en el estado actual, el sistema deberá mostrar un mensaje claro y permitir cambiar de estado o salir.

Mientras un spec esté seleccionado, las acciones deberán aplicarse solo sobre ese spec.

Mientras una operación modificadora sea solicitada, el sistema deberá pedir confirmación simple antes de ejecutarla.

Mientras el usuario cancele una acción, el sistema deberá volver al menú anterior sin modificar archivos.

### Unwanted behavior

Si `spec_tools.py` no existe, el sistema deberá fallar con un mensaje claro indicando que primero debe implementarse `spec_tools.py`.

Si el usuario introduce una opción inválida, el sistema deberá mostrar error y volver a pedir opción.

Si el usuario intenta mover a un estado inválido, el sistema deberá rechazar la operación.

Si `spec_tools.py` devuelve error, el sistema deberá mostrar el error y no ocultarlo.

Si no hay terminal interactiva disponible, el sistema deberá fallar de forma clara.

### Optional

Donde se use `--state <estado>`, el sistema deberá abrir directamente en ese estado.

Donde `spec_tools.py` soporte `--json`, el menú podrá usar esa salida para listar y calcular opciones de forma más robusta.

## Archivos esperados

- `scripts/harness/spec_menu.py`
- `scripts/harness/docs/spec_tools.md`
- `scripts/harness/README.md`
- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`

## Tareas

1. Crear script auxiliar `spec_menu.py`.
2. Implementar navegación por estados.
3. Implementar selección de spec.
4. Integrar acciones con `spec_tools.py`.
5. Agregar confirmaciones para acciones modificadoras.
6. Documentar flujo interactivo.
7. Actualizar changelog y repo map.
8. Ejecutar checks del harness.

## Microtareas

## MT-01 — Verificar spec_tools.py existente

### Tipo

- setup

### Archivos permitidos

- `scripts/harness/spec_tools.py`
- `scripts/harness/context/repo_map.md`

### Objetivo

Confirmar que `spec_tools.py` existe y conocer los comandos disponibles antes de crear el menú auxiliar.

### Pasos

- [ ] Verificar existencia de `scripts/harness/spec_tools.py`.
- [ ] Ejecutar `python3 scripts/harness/spec_tools.py --help`.
- [ ] Ejecutar `python3 scripts/harness/spec_tools.py list --help`.
- [ ] Ejecutar `python3 scripts/harness/spec_tools.py progress --help`.
- [ ] No modificar archivos.

### Check local

```bash
test -f scripts/harness/spec_tools.py
python3 scripts/harness/spec_tools.py --help
python3 scripts/harness/spec_tools.py list --help
python3 scripts/harness/spec_tools.py progress --help
```

### Criterio de aceptación

- [ ] `spec_tools.py` existe.
- [ ] Los comandos mínimos necesarios están disponibles.
- [ ] Se confirma que el menú puede reutilizar la herramienta existente.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-02 — Crear CLI base de spec_menu.py

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Crear el script auxiliar con estructura básica, parser de argumentos y validación de estado inicial.

### Pasos

- [ ] Crear `scripts/harness/spec_menu.py`.
- [ ] Usar solo librerías estándar de Python.
- [ ] Definir estados válidos: `backlog`, `active`, `done`, `cancelled`.
- [ ] Agregar argumento opcional `--state`.
- [ ] Hacer que el estado por defecto sea `backlog`.
- [ ] Agregar función `main()`.

### Check local

```bash
python3 scripts/harness/spec_menu.py --help
python3 -m py_compile scripts/harness/spec_menu.py
```

### Criterio de aceptación

- [ ] El script existe.
- [ ] `--help` funciona.
- [ ] El script compila sin errores.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-03 — Implementar helper para invocar spec_tools.py

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Centralizar la ejecución de `spec_tools.py` para no duplicar lógica de specs.

### Pasos

- [ ] Crear helper `run_spec_tools(args)`.
- [ ] Ejecutar `python3 scripts/harness/spec_tools.py` usando `subprocess.run`.
- [ ] Capturar stdout, stderr y returncode.
- [ ] Mostrar errores de forma clara.
- [ ] No usar shell=True.
- [ ] Preparar soporte para comandos que retornan JSON si está disponible.

### Check local

```bash
python3 -m py_compile scripts/harness/spec_menu.py
```

### Criterio de aceptación

- [ ] Existe helper aislado para invocar `spec_tools.py`.
- [ ] No se duplica lógica de mover/progreso/completar.
- [ ] No se usa `shell=True`.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-04 — Implementar listado de specs por estado

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Mostrar en el menú los specs disponibles para el estado actual.

### Pasos

- [ ] Implementar lectura de specs desde `specs/<estado>/*.md`.
- [ ] Ordenar archivos por nombre.
- [ ] Mostrar lista numerada.
- [ ] Mostrar opción para cambiar estado.
- [ ] Mostrar opción para salir.
- [ ] Manejar carpeta inexistente o vacía sin fallar.

### Check local

```bash
python3 scripts/harness/spec_menu.py --state backlog
```

### Criterio de aceptación

- [ ] El menú abre en backlog.
- [ ] Muestra archivos `.md` disponibles si existen.
- [ ] Si no hay archivos, permite cambiar estado o salir.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-05 — Implementar navegación entre estados

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Permitir cambiar entre carpetas de estado desde el menú interactivo.

### Pasos

- [ ] Agregar opción `cambiar estado`.
- [ ] Mostrar estados válidos.
- [ ] Permitir elegir estado por número o nombre.
- [ ] Actualizar estado actual.
- [ ] Volver a listar specs del nuevo estado.
- [ ] Rechazar entradas inválidas.

### Check local

```bash
python3 scripts/harness/spec_menu.py
```

### Criterio de aceptación

- [ ] El usuario puede navegar entre `backlog`, `active`, `done`, `cancelled`.
- [ ] Las opciones inválidas no cierran el programa.
- [ ] El menú vuelve a mostrar la lista correcta.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-06 — Implementar selección de spec y submenú de acciones

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Permitir seleccionar un spec y mostrar acciones disponibles para ese archivo.

### Pasos

- [ ] Permitir seleccionar spec por número.
- [ ] Mostrar ruta relativa del spec seleccionado.
- [ ] Agregar submenú con acciones:
  - ver progreso
  - completar microtarea
  - mover a otro estado
  - volver
- [ ] Validar entradas inválidas.
- [ ] Evitar que una acción opere sobre otro archivo.

### Check local

```bash
python3 scripts/harness/spec_menu.py --state backlog
```

### Criterio de aceptación

- [ ] Se puede seleccionar un spec por número.
- [ ] El submenú muestra acciones claras.
- [ ] Volver regresa al listado del estado actual.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-07 — Integrar acción ver progreso

### Tipo

- integración

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Ejecutar la funcionalidad de progreso desde el menú sobre el spec seleccionado.

### Pasos

- [ ] En acción `ver progreso`, invocar `spec_tools.py progress --spec <ruta>`.
- [ ] Mostrar stdout de la herramienta.
- [ ] Mostrar stderr si falla.
- [ ] Volver al submenú del spec seleccionado.

### Check local

```bash
python3 scripts/harness/spec_menu.py --state backlog
```

### Criterio de aceptación

- [ ] Ver progreso no requiere escribir la ruta manualmente.
- [ ] El resultado coincide con ejecutar `spec_tools.py progress --spec <ruta>`.
- [ ] Si falla, el error se muestra claramente.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-08 — Integrar acción completar microtarea

### Tipo

- integración

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Permitir completar una microtarea del spec seleccionado sin escribir la ruta completa.

### Pasos

- [ ] Pedir ID de microtarea, por ejemplo `MT-01`.
- [ ] Validar formato mínimo `MT-`.
- [ ] Pedir confirmación antes de modificar.
- [ ] Invocar `spec_tools.py complete-task --spec <ruta> --task <MT-XX>`.
- [ ] Mostrar resultado.
- [ ] Volver al submenú.

### Check local

```bash
python3 scripts/harness/spec_menu.py --state backlog
```

### Criterio de aceptación

- [ ] Completar microtarea no requiere escribir la ruta del spec.
- [ ] La acción pide confirmación antes de modificar.
- [ ] Solo se modifica el spec seleccionado.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-09 — Integrar acción mover spec entre estados

### Tipo

- integración

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Permitir mover el spec seleccionado a otro estado desde el menú.

### Pasos

- [ ] Mostrar estados destino válidos.
- [ ] Permitir elegir estado por número o nombre.
- [ ] Rechazar mover al mismo estado con mensaje claro.
- [ ] Pedir confirmación antes de mover.
- [ ] Invocar `spec_tools.py move --spec <ruta> --to <estado>`.
- [ ] Después de mover, regresar al listado del estado actual o del destino.
- [ ] Mostrar la nueva ruta del spec si `spec_tools.py` la informa.

### Check local

```bash
python3 scripts/harness/spec_menu.py --state backlog
```

### Criterio de aceptación

- [ ] Mover spec no requiere escribir la ruta.
- [ ] La acción pide confirmación.
- [ ] El spec termina en la carpeta de destino.
- [ ] La línea `Estado:` queda sincronizada por `spec_tools.py`.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-10 — Agregar manejo de cancelación y entradas vacías

### Tipo

- implementación

### Archivos permitidos

- `scripts/harness/spec_menu.py`

### Objetivo

Hacer el menú tolerante a errores humanos comunes.

### Pasos

- [ ] Permitir `q` para salir.
- [ ] Permitir `b` para volver.
- [ ] Manejar `Ctrl+C` con salida limpia.
- [ ] Rechazar entradas vacías sin traceback.
- [ ] Mostrar mensajes breves y claros.

### Check local

```bash
python3 scripts/harness/spec_menu.py
```

### Criterio de aceptación

- [ ] `q` sale limpiamente.
- [ ] `b` vuelve cuando aplica.
- [ ] `Ctrl+C` no muestra traceback largo.
- [ ] Entradas inválidas no rompen el menú.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-11 — Documentar menú interactivo

### Tipo

- docs

### Archivos permitidos

- `scripts/harness/docs/spec_tools.md`
- `scripts/harness/README.md`

### Objetivo

Documentar el nuevo flujo interactivo sin duplicar toda la documentación de `spec_tools.py`.

### Pasos

- [ ] Agregar sección `Menú interactivo`.
- [ ] Documentar comando `python3 scripts/harness/spec_menu.py`.
- [ ] Explicar estado por defecto `backlog`.
- [ ] Explicar navegación entre estados.
- [ ] Explicar acciones disponibles.
- [ ] Indicar que usa `spec_tools.py` por debajo.

### Check local

```bash
grep -R "spec_menu" scripts/harness/docs scripts/harness/README.md
```

### Criterio de aceptación

- [ ] La documentación explica cuándo usar `spec_menu.py`.
- [ ] La documentación indica que no reemplaza `spec_tools.py`.
- [ ] Hay ejemplos mínimos.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-12 — Actualizar CHANGELOG y repo_map

### Tipo

- docs

### Archivos permitidos

- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`

### Objetivo

Registrar el nuevo script auxiliar en el historial y mapa del repo.

### Pasos

- [ ] Agregar entrada en `scripts/harness/CHANGELOG.md`.
- [ ] Agregar `scripts/harness/spec_menu.py` al repo map.
- [ ] Agregar comando principal nuevo si existe sección de comandos.

### Check local

```bash
grep -R "spec_menu" scripts/harness/CHANGELOG.md scripts/harness/context/repo_map.md
```

### Criterio de aceptación

- [ ] Changelog menciona `spec_menu.py`.
- [ ] Repo map menciona `spec_menu.py`.

### Límite

No continuar a la siguiente microtask si este check falla.

---

## MT-13 — Checks finales del harness

### Tipo

- check

### Archivos permitidos

- `scripts/harness/CHANGELOG.md`

### Objetivo

Validar el harness completo y registrar el cambio.

### Pasos

- [ ] Ejecutar checks del harness.
- [ ] Ejecutar scan del repo.
- [ ] Registrar cambio con `log-change`.

### Check local

```bash
python3 scripts/harness/spec_menu.py --help
python3 -m py_compile scripts/harness/spec_menu.py
python3 scripts/harness/harness.py check
python3 scripts/harness/harness.py scan-repo
python3 scripts/harness/harness.py log-change \
  --summary "Add interactive spec menu" \
  --details "Adds scripts/harness/spec_menu.py as an interactive helper that reuses spec_tools.py to navigate specs by state, view progress, complete microtasks, and move specs without manually passing file paths." \
  --files "scripts/harness/spec_menu.py,scripts/harness/docs/spec_tools.md,scripts/harness/README.md,scripts/harness/CHANGELOG.md,scripts/harness/context/repo_map.md"
```

### Criterio de aceptación

- [ ] `spec_menu.py --help` funciona.
- [ ] `spec_menu.py` compila.
- [ ] `harness.py check` pasa.
- [ ] `harness.py scan-repo` pasa.
- [ ] El cambio queda registrado.

### Límite

No cerrar la spec si estos checks fallan.

## Criterios de aceptación

- [ ] Existe `scripts/harness/spec_menu.py`.
- [ ] `python3 scripts/harness/spec_menu.py --help` funciona.
- [ ] El menú abre en `backlog` por defecto.
- [ ] `--state active`, `--state done` y `--state cancelled` funcionan.
- [ ] El menú lista specs del estado actual.
- [ ] El usuario puede cambiar de estado desde el menú.
- [ ] El usuario puede seleccionar spec por número.
- [ ] El usuario puede ver progreso sin escribir ruta.
- [ ] El usuario puede completar microtarea sin escribir ruta.
- [ ] El usuario puede mover spec entre estados sin escribir ruta.
- [ ] Las acciones modificadoras piden confirmación.
- [ ] El menú reutiliza `spec_tools.py` y no duplica lógica compleja.
- [ ] No se modifica `spec_tools.py` salvo que sea estrictamente necesario.
- [ ] Documentación, changelog y repo map actualizados.
- [ ] Checks del harness ejecutados.

## Checks

```bash
python3 scripts/harness/spec_menu.py --help
python3 -m py_compile scripts/harness/spec_menu.py
python3 scripts/harness/harness.py check
python3 scripts/harness/harness.py scan-repo
python3 scripts/harness/harness.py log-change \
  --summary "Add interactive spec menu" \
  --details "Adds scripts/harness/spec_menu.py as an interactive helper that reuses spec_tools.py to navigate specs by state, view progress, complete microtasks, and move specs without manually passing file paths." \
  --files "scripts/harness/spec_menu.py,scripts/harness/docs/spec_tools.md,scripts/harness/README.md,scripts/harness/CHANGELOG.md,scripts/harness/context/repo_map.md"
```

## Documentación a actualizar

- `scripts/harness/docs/spec_tools.md`
- `scripts/harness/README.md`
- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`

## Riesgos

- Duplicar lógica de `spec_tools.py` puede generar divergencia.
- Parsear salida humana de `spec_tools.py list` puede ser frágil; preferir filesystem directo para listar o `--json` si existe.
- Un menú interactivo puede ser menos útil para agentes no interactivos; por eso debe mantenerse `spec_tools.py` como interfaz principal automatizable.
- Acciones de movimiento y completado modifican archivos; deben pedir confirmación.
- Si el usuario mueve un spec incorrecto, el seguimiento operativo puede desordenarse.

## Dependencias

- `scripts/harness/spec_tools.py` implementado.
- Python 3 disponible.
- Convención de specs en `specs/<estado>/`.
- Terminal interactiva estándar.
- Specs en Markdown.

## Prompt corto para agente ejecutor

Crea `scripts/harness/spec_menu.py` como script auxiliar interactivo. Debe abrir en `backlog` por defecto, listar specs disponibles, permitir cambiar entre `backlog`, `active`, `done`, `cancelled`, seleccionar un spec por número y ejecutar acciones sobre ese spec: ver progreso, completar microtarea y mover a otro estado. Reutiliza `scripts/harness/spec_tools.py` para `progress`, `complete-task` y `move`, usando `subprocess.run` sin `shell=True`. No reemplaces ni reescribas `spec_tools.py`. Usa solo librerías estándar. Agrega confirmación antes de acciones modificadoras. Actualiza docs, changelog y repo_map. No hagas commit, push, merge ni modifiques el vault.

