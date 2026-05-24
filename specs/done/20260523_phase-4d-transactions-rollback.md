# Spec — Fase 4D: Transacciones y rollback seguro

Estado: done

## Objetivo

Agregar seguridad transaccional a operaciones de escritura y movimiento de notas para evitar pérdida de información cuando falle la creación, escritura o movimiento de archivos.

## Contexto

El sistema `cerebro_notes` procesa notas y puede mover notas fuente después de generar contenido derivado. Actualmente se requiere proteger esas operaciones con escritura atómica, movimiento seguro y rollback simple.

La implementación debe ser suficientemente pequeña para que un modelo local mediano pueda ejecutarla por microtareas. Debe evitar tocar el vault real durante pruebas y debe integrarse de forma mínima en `run_reflective_from_note.py`.

## Alcance

- Crear `scripts/cerebro_notes/core/transactions.py`.
- Implementar `atomic_write_text`.
- Implementar `safe_move_file`.
- Implementar un contexto transaccional simple para rollback.
- Integrar el contexto transaccional en `scripts/cerebro_notes/run_reflective_from_note.py`.
- Crear smoke tests con `tempfile`.
- Actualizar documentación humana.
- Ejecutar checks del harness.
- Registrar `log-change`.

## Fuera de alcance

- No modificar `vault/raymundo_ideaverse`.
- No cambiar el diseño general del pipeline reflexivo.
- No agregar dependencias externas.
- No implementar transacciones distribuidas.
- No implementar base de datos de transacciones.
- No hacer commit, push, merge ni rebase automático.
- No modificar otros flujos técnicos salvo que sea estrictamente necesario.

## Requisitos EARS

### Ubiquitous

El sistema deberá proveer utilidades transaccionales en `scripts/cerebro_notes/core/transactions.py`.

El sistema deberá escribir archivos de texto usando escritura atómica cuando se use `atomic_write_text`.

El sistema deberá mover archivos usando una operación segura cuando se use `safe_move_file`.

El sistema deberá permitir registrar acciones de rollback en un contexto transaccional simple.

### Event-driven

Cuando una escritura atómica se complete correctamente, el sistema deberá reemplazar el archivo destino solo al final de la operación.

Cuando una escritura atómica falle, el sistema deberá conservar el archivo destino previo sin corrupción parcial.

Cuando un archivo fuente sea movido dentro de una transacción, el sistema deberá registrar una acción de rollback para restaurarlo.

Cuando ocurra una excepción dentro del contexto transaccional, el sistema deberá ejecutar las acciones de rollback registradas en orden inverso.

### State-driven

Mientras una transacción esté activa, el sistema deberá acumular acciones de rollback.

Mientras la creación de notas falle antes de mover la fuente, el sistema no deberá mover la fuente.

Mientras falle una operación después de mover la fuente, el sistema deberá intentar restaurar la fuente.

Mientras se ejecuten smoke tests, el sistema deberá usar directorios temporales y no tocar el vault real.

### Unwanted behavior

Si falla la creación de notas, el sistema deberá evitar mover la nota fuente.

Si falla después de mover la fuente, el sistema deberá restaurar la fuente cuando sea posible.

Si el rollback falla, el sistema deberá reportar el error sin ocultar la excepción original.

Si el archivo destino ya existe y no se permite overwrite, el sistema deberá fallar de forma explícita.

### Optional

Donde se habilite un modo dry-run existente, el sistema deberá evitar escrituras y movimientos reales.

## Archivos esperados

- `scripts/cerebro_notes/core/transactions.py`
- `scripts/cerebro_notes/run_reflective_from_note.py`
- `scripts/cerebro_notes/tests/smoke/test_transactions.py`
- `scripts/cerebro_notes/core/README.md`
- `scripts/harness/context/current_state.md`
- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`

## Tareas

- [ ] Crear módulo transaccional.
- [ ] Implementar escritura atómica.
- [ ] Implementar movimiento seguro.
- [ ] Implementar contexto transaccional simple.
- [ ] Crear smoke tests con `tempfile`.
- [ ] Integrar transacciones en `run_reflective_from_note.py`.
- [ ] Actualizar documentación humana.
- [ ] Ejecutar checks.
- [ ] Registrar `log-change`.

## Microtareas

## MT-01 — Inspeccionar flujo actual de escritura y movimiento

### Tipo

- setup

### Archivos permitidos

- `scripts/cerebro_notes/run_reflective_from_note.py`
- `scripts/cerebro_notes/core/transactions.py`

### Objetivo

Identificar dónde se crean notas y dónde se mueve la nota fuente antes de implementar el rollback.

### Pasos

- [ ] Abrir `scripts/cerebro_notes/run_reflective_from_note.py`.
- [ ] Localizar operaciones de escritura de notas.
- [ ] Localizar operación de movimiento de nota fuente.
- [ ] Verificar si ya existe `scripts/cerebro_notes/core/transactions.py`.
- [ ] No modificar archivos en esta microtarea.

### Check local

```bash
test -f scripts/cerebro_notes/run_reflective_from_note.py
grep -n "move\|rename\|replace\|write_text\|open(" scripts/cerebro_notes/run_reflective_from_note.py || true
```

### Criterio de aceptación

- [ ] Se identificó el punto de integración mínimo.
- [ ] Se confirmó si `transactions.py` existe o debe crearse.
- [ ] No se modificaron archivos.

### Límite

No continuar a la siguiente microtask si no se identifica dónde integrar.

---

## MT-02 — Crear módulo base transactions.py

### Tipo

- implementación

### Archivos permitidos

- `scripts/cerebro_notes/core/transactions.py`

### Objetivo

Crear el módulo transaccional base sin integrarlo todavía en el flujo.

### Pasos

- [ ] Crear `scripts/cerebro_notes/core/transactions.py` si no existe.
- [ ] Agregar imports estándar necesarios: `Path`, `tempfile`, `shutil`, `os`, `contextlib` si aplica.
- [ ] Agregar docstring breve del módulo.
- [ ] Definir API inicial exportable:
  - `atomic_write_text`
  - `safe_move_file`
  - `FileTransaction`
- [ ] Dejar implementaciones mínimas o stubs seguros si es necesario.

### Check local

```bash
python3 -m py_compile scripts/cerebro_notes/core/transactions.py
```

### Criterio de aceptación

- [ ] El archivo existe.
- [ ] El módulo compila.
- [ ] La API esperada está declarada.

### Límite

No continuar a la siguiente microtask si el módulo no compila.

---

## MT-03 — Implementar atomic_write_text

### Tipo

- implementación

### Archivos permitidos

- `scripts/cerebro_notes/core/transactions.py`

### Objetivo

Implementar escritura atómica de texto para evitar archivos parcialmente escritos.

### Pasos

- [ ] Implementar `atomic_write_text(path, text, encoding="utf-8")`.
- [ ] Crear el directorio padre si no existe.
- [ ] Escribir primero en un archivo temporal dentro del mismo directorio.
- [ ] Hacer flush/fsync si se implementa de forma sencilla y segura.
- [ ] Reemplazar destino final usando `os.replace`.
- [ ] Eliminar temporal si ocurre error antes del replace.
- [ ] Mantener solo librerías estándar.

### Check local

```bash
python3 -m py_compile scripts/cerebro_notes/core/transactions.py
python3 - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from scripts.cerebro_notes.core.transactions import atomic_write_text

with TemporaryDirectory() as tmp:
    p = Path(tmp) / "note.md"
    atomic_write_text(p, "hola")
    assert p.read_text(encoding="utf-8") == "hola"
print("atomic_write_text ok")
PY
```

### Criterio de aceptación

- [ ] Escribe texto correctamente.
- [ ] Crea directorio padre si falta.
- [ ] No deja temporal visible en caso normal.
- [ ] Usa reemplazo atómico final.

### Límite

No continuar a la siguiente microtask si el check falla.

---

## MT-04 — Implementar safe_move_file

### Tipo

- implementación

### Archivos permitidos

- `scripts/cerebro_notes/core/transactions.py`

### Objetivo

Implementar movimiento seguro de archivos con validaciones explícitas.

### Pasos

- [ ] Implementar `safe_move_file(src, dst, overwrite=False)`.
- [ ] Validar que `src` exista.
- [ ] Crear directorio padre de `dst` si no existe.
- [ ] Si `dst` existe y `overwrite=False`, fallar explícitamente.
- [ ] Usar `shutil.move` o `Path.replace` según sea más compatible.
- [ ] Devolver ruta destino como `Path`.

### Check local

```bash
python3 - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from scripts.cerebro_notes.core.transactions import safe_move_file

with TemporaryDirectory() as tmp:
    root = Path(tmp)
    src = root / "a.md"
    dst = root / "archive" / "a.md"
    src.write_text("x", encoding="utf-8")
    safe_move_file(src, dst)
    assert not src.exists()
    assert dst.exists()
    assert dst.read_text(encoding="utf-8") == "x"
print("safe_move_file ok")
PY
```

### Criterio de aceptación

- [ ] Mueve archivo existente.
- [ ] Crea carpeta destino.
- [ ] No sobreescribe por defecto.
- [ ] Falla claramente si `src` no existe.

### Límite

No continuar a la siguiente microtask si el check falla.

---

## MT-05 — Implementar FileTransaction con rollback LIFO

### Tipo

- implementación

### Archivos permitidos

- `scripts/cerebro_notes/core/transactions.py`

### Objetivo

Crear un contexto transaccional simple que ejecute rollback en orden inverso si ocurre una excepción.

### Pasos

- [ ] Implementar clase `FileTransaction`.
- [ ] Soportar uso con `with FileTransaction() as tx:`.
- [ ] Agregar método `add_rollback(callable, *args, **kwargs)`.
- [ ] Ejecutar rollbacks en orden LIFO si ocurre excepción.
- [ ] No ejecutar rollbacks si no ocurre excepción.
- [ ] Preservar la excepción original.
- [ ] Si un rollback falla, reportarlo por stderr o acumularlo sin ocultar la excepción original.

### Check local

```bash
python3 - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from scripts.cerebro_notes.core.transactions import FileTransaction

with TemporaryDirectory() as tmp:
    p = Path(tmp) / "x.txt"
    try:
        with FileTransaction() as tx:
            p.write_text("movido", encoding="utf-8")
            tx.add_rollback(p.unlink)
            raise RuntimeError("fallo simulado")
    except RuntimeError:
        pass
    assert not p.exists()
print("FileTransaction rollback ok")
PY
```

### Criterio de aceptación

- [ ] Ejecuta rollback si hay excepción.
- [ ] No ejecuta rollback si todo sale bien.
- [ ] Ejecuta rollback en orden inverso.
- [ ] No oculta la excepción original.

### Límite

No continuar a la siguiente microtask si el check falla.

---

## MT-06 — Agregar helpers transaccionales para escritura y movimiento

### Tipo

- implementación

### Archivos permitidos

- `scripts/cerebro_notes/core/transactions.py`

### Objetivo

Facilitar la integración con funciones pequeñas que registren rollback cuando se escriba o mueva un archivo.

### Pasos

- [ ] Agregar método o helper para registrar restauración de archivo existente antes de sobrescribir.
- [ ] Agregar método o helper para mover archivo y registrar rollback inverso.
- [ ] Mantener nombres claros, por ejemplo:
  - `tx.write_text(path, text)`
  - `tx.move_file(src, dst)`
- [ ] Evitar lógica específica de notas reflexivas en este módulo.
- [ ] Mantener el módulo genérico para futuras integraciones.

### Check local

```bash
python3 -m py_compile scripts/cerebro_notes/core/transactions.py
```

### Criterio de aceptación

- [ ] Existen helpers transaccionales reutilizables.
- [ ] El módulo sigue siendo genérico.
- [ ] Compila sin errores.

### Límite

No continuar a la siguiente microtask si el módulo no compila.

---

## MT-07 — Crear smoke test de atomic_write_text con tempfile

### Tipo

- test

### Archivos permitidos

- `scripts/cerebro_notes/tests/smoke/test_transactions.py`

### Objetivo

Validar escritura atómica sin tocar el vault real.

### Pasos

- [ ] Crear o actualizar `scripts/cerebro_notes/tests/smoke/test_transactions.py`.
- [ ] Usar `tempfile.TemporaryDirectory`.
- [ ] Probar que `atomic_write_text` crea el archivo.
- [ ] Probar que sobrescribe contenido correctamente.
- [ ] Asegurar que el test no usa rutas del vault.

### Check local

```bash
python3 scripts/cerebro_notes/tests/smoke/test_transactions.py
```

### Criterio de aceptación

- [ ] El smoke test pasa.
- [ ] Usa solo directorios temporales.
- [ ] No toca `vault/raymundo_ideaverse`.

### Límite

No continuar a la siguiente microtask si el test falla.

---

## MT-08 — Crear smoke test de safe_move_file con tempfile

### Tipo

- test

### Archivos permitidos

- `scripts/cerebro_notes/tests/smoke/test_transactions.py`

### Objetivo

Validar movimiento seguro sin tocar el vault real.

### Pasos

- [ ] Agregar test para mover archivo a subdirectorio temporal.
- [ ] Verificar que fuente desaparece.
- [ ] Verificar que destino existe.
- [ ] Verificar que no sobreescribe si destino existe y `overwrite=False`.
- [ ] Mantener todo dentro de `TemporaryDirectory`.

### Check local

```bash
python3 scripts/cerebro_notes/tests/smoke/test_transactions.py
```

### Criterio de aceptación

- [ ] El test de movimiento pasa.
- [ ] El test de no overwrite pasa.
- [ ] No toca rutas reales.

### Límite

No continuar a la siguiente microtask si el test falla.

---

## MT-09 — Crear smoke test de rollback después de mover

### Tipo

- test

### Archivos permitidos

- `scripts/cerebro_notes/tests/smoke/test_transactions.py`

### Objetivo

Validar que si falla una operación después de mover un archivo, el rollback restaura la fuente.

### Pasos

- [ ] Crear fuente temporal.
- [ ] Mover fuente a destino usando helper transaccional.
- [ ] Simular excepción después del movimiento.
- [ ] Verificar que la fuente vuelve a existir.
- [ ] Verificar que el destino no queda como movimiento final exitoso.
- [ ] No tocar vault.

### Check local

```bash
python3 scripts/cerebro_notes/tests/smoke/test_transactions.py
```

### Criterio de aceptación

- [ ] Si falla después de mover, restaura fuente.
- [ ] No deja estado inconsistente en el caso probado.
- [ ] Test usa solo `tempfile`.

### Límite

No continuar a la siguiente microtask si el test falla.

---

## MT-10 — Integrar transacción en run_reflective_from_note.py

### Tipo

- integración

### Archivos permitidos

- `scripts/cerebro_notes/run_reflective_from_note.py`
- `scripts/cerebro_notes/core/transactions.py`

### Objetivo

Usar el contexto transaccional en el flujo real para proteger creación de notas y movimiento de fuente.

### Pasos

- [ ] Importar `FileTransaction` o helpers necesarios desde `core.transactions`.
- [ ] Envolver la sección mínima de escritura/movimiento con `with FileTransaction() as tx:`.
- [ ] Usar escritura transaccional para notas generadas si aplica.
- [ ] Usar movimiento transaccional para mover la fuente si aplica.
- [ ] Asegurar que la fuente no se mueva si falla la creación de notas.
- [ ] Mantener el cambio mínimo y localizado.

### Check local

```bash
python3 -m py_compile scripts/cerebro_notes/run_reflective_from_note.py
python3 scripts/cerebro_notes/tests/smoke/test_transactions.py
```

### Criterio de aceptación

- [ ] El archivo compila.
- [ ] El test transaccional sigue pasando.
- [ ] La integración es mínima.
- [ ] No se modifican rutas del vault durante tests.

### Límite

No continuar a la siguiente microtask si compila o tests fallan.

---

## MT-11 — Agregar prueba de no mover fuente si falla creación

### Tipo

- test

### Archivos permitidos

- `scripts/cerebro_notes/tests/smoke/test_transactions.py`
- `scripts/cerebro_notes/run_reflective_from_note.py`

### Objetivo

Cubrir el criterio de aceptación: no mover fuente si falla creación de notas.

### Pasos

- [ ] Crear una prueba aislada con archivos temporales.
- [ ] Simular fallo antes del movimiento de fuente.
- [ ] Verificar que la fuente sigue en su ubicación original.
- [ ] Evitar invocar rutas reales de Obsidian/vault.
- [ ] Si la integración directa es difícil, probar el helper transaccional equivalente.

### Check local

```bash
python3 scripts/cerebro_notes/tests/smoke/test_transactions.py
```

### Criterio de aceptación

- [ ] Si falla la creación previa, la fuente no se mueve.
- [ ] El test no toca vault.
- [ ] El test pasa de forma determinística.

### Límite

No continuar a la siguiente microtask si el test falla.

---

## MT-12 — Actualizar documentación humana

### Tipo

- docs

### Archivos permitidos

- `scripts/cerebro_notes/core/README.md`
- `scripts/harness/context/current_state.md`

### Objetivo

Documentar el uso y propósito de las utilidades transaccionales.

### Pasos

- [ ] Documentar `atomic_write_text`.
- [ ] Documentar `safe_move_file`.
- [ ] Documentar `FileTransaction`.
- [ ] Explicar que los tests deben usar `tempfile`.
- [ ] Explicar que el vault no debe tocarse en tests.
- [ ] Mencionar integración en flujo reflexivo.

### Check local

```bash
grep -R "FileTransaction\|atomic_write_text\|safe_move_file" scripts/cerebro_notes/core/README.md scripts/harness/context/current_state.md
```

### Criterio de aceptación

- [ ] La documentación menciona las tres utilidades.
- [ ] La documentación explica el rollback seguro.
- [ ] La documentación advierte no tocar vault en tests.

### Límite

No continuar a la siguiente microtask si la documentación no queda localizable.

---

## MT-13 — Actualizar CHANGELOG y repo_map

### Tipo

- docs

### Archivos permitidos

- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`

### Objetivo

Registrar la Fase 4D en historial y mapa del repo.

### Pasos

- [ ] Agregar entrada en `scripts/harness/CHANGELOG.md`.
- [ ] Actualizar `scripts/harness/context/repo_map.md` para incluir `core/transactions.py`.
- [ ] Confirmar que `test_transactions.py` aparece en el repo map si corresponde.
- [ ] No registrar como done si los checks finales no han pasado.

### Check local

```bash
grep -R "transactions.py\|FileTransaction\|rollback" scripts/harness/CHANGELOG.md scripts/harness/context/repo_map.md
```

### Criterio de aceptación

- [ ] Changelog menciona transacciones y rollback.
- [ ] Repo map menciona `transactions.py`.
- [ ] Repo map refleja test nuevo si aplica.

### Límite

No continuar a la siguiente microtask si no hay registro documental.

---

## MT-14 — Ejecutar checks finales y registrar log-change

### Tipo

- check

### Archivos permitidos

- `scripts/harness/CHANGELOG.md`

### Objetivo

Validar la Fase 4D completa y registrar el cambio en el harness.

### Pasos

- [ ] Ejecutar smoke test de transacciones.
- [ ] Ejecutar check general del harness.
- [ ] Ejecutar scan del repo.
- [ ] Registrar `log-change`.

### Check local

```bash
python3 scripts/cerebro_notes/tests/smoke/test_transactions.py
python3 scripts/harness/harness.py check
python3 scripts/harness/harness.py scan-repo
python3 scripts/harness/harness.py log-change \
  --summary "Add transactional file operations for reflective notes" \
  --details "Adds atomic_write_text, safe_move_file and FileTransaction rollback helpers, integrates them into run_reflective_from_note.py, and adds tempfile-based smoke tests to ensure source notes are not lost on failures." \
  --files "scripts/cerebro_notes/core/transactions.py,scripts/cerebro_notes/run_reflective_from_note.py,scripts/cerebro_notes/tests/smoke/test_transactions.py,scripts/cerebro_notes/core/README.md,scripts/harness/context/current_state.md,scripts/harness/CHANGELOG.md,scripts/harness/context/repo_map.md"
```

### Criterio de aceptación

- [ ] Smoke tests pasan.
- [ ] `harness.py check` pasa.
- [ ] `harness.py scan-repo` pasa.
- [ ] `log-change` queda registrado.

### Límite

No cerrar la spec si cualquier check falla.

## Criterios de aceptación

- [ ] Existe `scripts/cerebro_notes/core/transactions.py`.
- [ ] Existe `atomic_write_text`.
- [ ] Existe `safe_move_file`.
- [ ] Existe contexto transaccional simple `FileTransaction`.
- [ ] No mueve fuente si falla creación de notas.
- [ ] Si falla después de mover, restaura fuente.
- [ ] Tests usan `tempfile`.
- [ ] Tests no modifican `vault/raymundo_ideaverse`.
- [ ] `run_reflective_from_note.py` usa la transacción en el punto mínimo necesario.
- [ ] Documentación humana actualizada.
- [ ] `harness check` pasa.
- [ ] `harness scan-repo` pasa.
- [ ] `log-change` registrado.

## Checks

```bash
python3 -m py_compile scripts/cerebro_notes/core/transactions.py
python3 -m py_compile scripts/cerebro_notes/run_reflective_from_note.py
python3 scripts/cerebro_notes/tests/smoke/test_transactions.py
python3 scripts/harness/harness.py check
python3 scripts/harness/harness.py scan-repo
python3 scripts/harness/harness.py log-change \
  --summary "Add transactional file operations for reflective notes" \
  --details "Adds atomic_write_text, safe_move_file and FileTransaction rollback helpers, integrates them into run_reflective_from_note.py, and adds tempfile-based smoke tests to ensure source notes are not lost on failures." \
  --files "scripts/cerebro_notes/core/transactions.py,scripts/cerebro_notes/run_reflective_from_note.py,scripts/cerebro_notes/tests/smoke/test_transactions.py,scripts/cerebro_notes/core/README.md,scripts/harness/context/current_state.md,scripts/harness/CHANGELOG.md,scripts/harness/context/repo_map.md"
```

## Documentación a actualizar

- `scripts/cerebro_notes/core/README.md`
- `scripts/harness/context/current_state.md`
- `scripts/harness/CHANGELOG.md`
- `scripts/harness/context/repo_map.md`

## Riesgos

- Integrar rollback en un flujo existente puede mover o restaurar archivos incorrectamente si se selecciona mal el punto de integración.
- Un rollback incompleto puede dejar duplicados o archivos en estado inconsistente.
- La escritura atómica puede comportarse distinto entre sistemas de archivos si se cruza de partición; por eso el temporal debe estar en el mismo directorio destino.
- Los tests no deben tocar el vault real.
- Si se mezcla integración con refactor amplio, la tarea puede exceder la capacidad de un modelo pequeño.

## Dependencias

- Python 3.
- `scripts/cerebro_notes/run_reflective_from_note.py` existente.
- Estructura `scripts/cerebro_notes/core/`.
- Harness funcional.
- Smoke tests ejecutables como scripts Python directos.

## Prompt corto para agente ejecutor

Implementa la Fase 4D en microcambios. Crea `scripts/cerebro_notes/core/transactions.py` con `atomic_write_text`, `safe_move_file` y `FileTransaction` con rollback LIFO. Agrega smoke tests con `tempfile` en `scripts/cerebro_notes/tests/smoke/test_transactions.py`; no toques `vault/raymundo_ideaverse`. Integra de forma mínima en `scripts/cerebro_notes/run_reflective_from_note.py` para que no se mueva la fuente si falla la creación de notas y para que se restaure si falla después de mover. Actualiza documentación, changelog y repo_map. Ejecuta smoke tests, `harness.py check`, `harness.py scan-repo` y registra `log-change`. No hagas commit, push, merge ni rebase.
