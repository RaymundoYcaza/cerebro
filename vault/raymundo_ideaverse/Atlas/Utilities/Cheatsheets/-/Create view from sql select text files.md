---
created: 2024-09-10
up:
  - "[[Python Scripts]]"
---

Este script recorre todos los archivos txt del directorio actual e inserta el comando 'create view xxx as', donde xxx es el nombre del archivo, sin la extensión.

```python
import os

  

# Función para modificar el contenido del archivo

def modify_file_content(file_path, view_name):

    with open(file_path, 'r') as file:

        content = file.read()

    # Modificamos el contenido anteponiendo el texto "CREATE VIEW XXX AS"

    new_content = f"CREATE VIEW {view_name} AS\n{content}"

    with open(file_path, 'w') as file:

        file.write(new_content)

  

# Obtenemos todos los archivos .txt del directorio actual

current_directory = os.getcwd()

txt_files = [f for f in os.listdir(current_directory) if f.endswith('.txt')]

  

# Modificamos cada archivo

for txt_file in txt_files:

    view_name = os.path.splitext(txt_file)[0]  # Nombre del archivo sin extensión

    file_path = os.path.join(current_directory, txt_file)

    modify_file_content(file_path, view_name)

  

print("Archivos modificados correctamente.")
```

