---
up:
  - "[[AHK Script Log]]"
related:
  - "[[AHK Script]]"
created: 2025-05-10
---


Hoy implementé el componente expander para utilizar palabras clave como lanzadores de textos más largos. Comencé con `@queryobsidian` que genera un query `dataview` para obtener todas las notas que en su propiedad `in` enlazan a la nota actual. 

Se utilizó el mismo mecanismo que con  los prompts:

1. Se crea un archivo de texto con el contenido que se enviará.
2. Se vincula un text-expander al archivo creado.
3. Al ejecutar el expander, se busca el texto del archivo vinculado y se almacena en el clipboard su contenido.
4. Se pega el contenido.
5. Se restaura el contenido previo del clipboard.


