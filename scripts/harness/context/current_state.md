# Current State

Estado actual del sistema:

- `scripts/cerebro_notes` fue reorganizado en `core`, `technical` y `reflective`.
- `technical` procesa notas técnicas estructuradas.
- `reflective` procesa Sparks y extractos para generar:
  - sesión reflexiva intermedia
  - Thing Note limpia
- `run_reflective_from_note.py` permite buscar notas fuente con fuzzy search en `+`.
- Las fuentes se mueven por defecto a `Atlas/Dots/Sources`.
- La Thing Note queda en `00_INBOX_IA/thing-note` para ser movida manualmente al Atlas.
- Los wikilinks YAML deben serializarse como strings con comilla simple.
