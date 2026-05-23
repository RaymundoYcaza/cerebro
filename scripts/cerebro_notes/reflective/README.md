# Reflective Notes

Herramientas para convertir Sparks y extractos en una sesion reflexiva guiada y, cuando aplica, una Thing Note limpia para revisar manualmente.

## Flujo desde nota fuente

`run_reflective_from_note.py` busca una nota Markdown dentro del Inbox configurado, ejecuta extraccion reflexiva con el modelo local, pide validacion humana y genera uno o dos archivos de salida.

Ruta de entrada por defecto:

```text
vault/+
```

Si `paths.inbox_sources_dir` existe en `config.yaml`, esa ruta reemplaza el valor anterior.

Ruta de fuentes procesadas por defecto:

```text
vault/Atlas/Dots/Sources
```

Si `paths.sources_dir` existe en `config.yaml`, esa ruta reemplaza el valor anterior.

## Uso recomendado

Dry-run sin mover ni escribir notas:

```bash
cd /mnt/c/cerebro/scripts/cerebro_notes
python3 run_reflective_from_note.py --config config.yaml --query "texto de busqueda" --dry-run
```

Escritura completa:

```bash
cd /mnt/c/cerebro/scripts/cerebro_notes
python3 run_reflective_from_note.py --config config.yaml --query "texto de busqueda" --write
```

Con `--write`, el comportamiento normal es:

- crear una sesion reflexiva en `output_dir/reflective-session`;
- crear una Thing Note limpia en `output_dir/thing-note`;
- normalizar el frontmatter de la fuente;
- mover la fuente a `Sources`;
- agregar wikilink corto a la fuente movida.

Para escribir las notas sin mover la fuente:

```bash
python3 run_reflective_from_note.py --config config.yaml --query "texto de busqueda" --write --no-move-source
```

## Modos de salida

`--output-mode both` es el valor por defecto. Tambien se puede usar:

- `--output-mode session` para generar solo la sesion reflexiva;
- `--output-mode thing` para generar solo la Thing Note.

La sesion conserva el proceso reflexivo y las respuestas guiadas. La Thing Note debe quedar mas limpia y no mezclar demasiado proceso, para poder moverse luego al Atlas de forma manual.

## Interaccion humana

Despues de que el modelo detecta la senal principal, el script pide tres respuestas:

- validacion de la idea;
- reformulacion en voz propia;
- conexiones con notas, proyectos, experiencias o ideas previas.

Estas respuestas se insertan en la sesion reflexiva. La voz propia y las conexiones tambien alimentan la Thing Note.

## Separacion de responsabilidades

- `core` provee utilidades compartidas como normalizacion de texto, slugs, hashes, rutas unicas y tags.
- `reflective` contiene prompts, renderizado y flujo de notas reflexivas.
- `technical` conserva la carga de configuracion compartida usada por los scripts actuales.

El modelo sugiere senales, titulos, preguntas y tags. Python decide rutas, nombres, frontmatter final, movimientos y escritura.
