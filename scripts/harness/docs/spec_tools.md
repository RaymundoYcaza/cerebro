# Spec Tools Documentation

`spec_tools.py` es una herramienta de línea de comandos para gestionar el ciclo de vida de los **specs** markdown en el harness de Cerebro.

## Estados soportados

- `backlog`
- `active`
- `done`
- `cancelled`

## Comandos

### `list`
```
python3 scripts/harness/spec_tools.py list [--state STATE] [--json]
```
Lista los archivos *.md* bajo `specs/`. Con `--state` filtra por estado. Con `--json` devuelve JSON.

### `move`
```
python3 scripts/harness/spec_tools.py move --spec PATH --to STATE [--dry-run]
```
Mueve el spec a la carpeta del estado indicado y actualiza la línea `Estado:` dentro del archivo. `--dry-run` muestra la operación sin escribir.

### `progress`
```
python3 scripts/harness/spec_tools.py progress --spec PATH [--json]
```
Analiza microtareas (encabezados `## MT‑XX`) y casillas de verificación `- [ ]` / `- [x]`. Informa el total, completadas y porcentaje. `--json` devuelve datos estructurados.

### `complete-task`
```
python3 scripts/harness/spec_tools.py complete-task --spec PATH --task MT-XX [--dry-run]
```
Marca como completadas todas las casillas de verificación dentro de la microtarea especificada. No afecta otras microtareas. Usa `--dry-run` para previsualizar.

## Seguridad

- Sólo se operan archivos dentro de `specs/` y con extensión `.md`.
- Los estados deben pertenecer a los valores válidos.
- La herramienta nunca modifica fuera del árbol de specs y rechaza rutas o estados inválidos.

## Salida JSON

Los comandos `list` y `progress` aceptan `--json` y emiten objetos compatibles con JSON para consumo por agentes automatizados.
