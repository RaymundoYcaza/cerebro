# Obsidian Rules

Los frontmatters deben ser planos y compatibles con Obsidian/Dataview.

Los wikilinks en YAML deben quedar como strings:

```yaml
source: '[[Mi nota fuente]]'
related:
  - '[[Otra nota]]'
```

Evitar:

```yaml
source: [[Mi nota fuente]]
```

y evitar valores con triple comilla simple alrededor de wikilinks.

Las notas finales de conocimiento no deben mezclar demasiado proceso reflexivo. El proceso vive en una sesión intermedia.
