---
up: []
related: []
created: 2026-03-26
---


Un **Makefile** es simplemente un archivo que te permite ejecutar comandos largos con **comandos cortos**.

En vez de escribir:

```bash
pyenv local 3.11.9  
source venv/bin/activate.fish  
python generate_obsidian_books.py
```

Puedes escribir:

```bash
make process
```

Mucho más limpio.

Ejemplo de makefile

```bash
.PHONY: setup process search

setup:
	pyenv local 3.11.9

activate:
	source venv/bin/activate.fish

process:
	python generate_obsidian_books.py

search:
	python smart_library.py

embeddings:
	python build_embeddings.py

duplicates:
	python detect_duplicates.py
```


Con esto puedes usar:

```bash
make process
make search
make duplicates
```