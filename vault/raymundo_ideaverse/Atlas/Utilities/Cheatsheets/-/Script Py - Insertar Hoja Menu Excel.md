---
created: 2024-09-10
up:
  - "[[Python Scripts]]"
---

**Propósito**: Este script permitirá modificar un archivo Excel agregando una hoja con un menú y enlaces para navegar entre las hojas fácilmente.

**Descripción:** Script en Python que utiliza la biblioteca `openpyxl` para modificar un archivo de Excel, insertando una hoja llamada "MENU" con enlaces a las otras hojas, y añadiendo un enlace de "Volver al menú" en cada hoja:

```python
import openpyxl
import os
from tkinter import Tk
from tkinter import filedialog

def create_menu(workbook, sheet_names):
    """Crea una hoja llamada 'MENU' con enlaces a las demás hojas."""
    # Crear la hoja MENU al principio
    menu_sheet = workbook.create_sheet('MENU', 0)
    
    # Insertar los nombres de las hojas en mayúsculas como enlaces
    for i, sheet_name in enumerate(sheet_names, start=1):
        cell = menu_sheet.cell(row=i, column=1)
        cell.value = sheet_name.upper()
        # Crear un hipervínculo a la hoja correspondiente
        cell.hyperlink = f"#{sheet_name}!A1"
        cell.style = "Hyperlink"

def add_back_to_menu_link(workbook, sheet_names):
    """Inserta un enlace en cada hoja para volver a la hoja 'MENU'."""
    for sheet_name in sheet_names:
        sheet = workbook[sheet_name]
        # Insertar una fila completa al principio
        sheet.insert_rows(1)
        # Insertar el enlace en la celda A1
        cell = sheet.cell(row=1, column=1)
        cell.value = "Volver al menú"
        cell.hyperlink = "#MENU!A1"
        cell.style = "Hyperlink"

def modify_excel(file_path, output_folder):
    # Cargar el archivo de Excel
    workbook = openpyxl.load_workbook(file_path)
    # Obtener los nombres de las hojas (excepto MENU si ya existe)
    sheet_names = [sheet for sheet in workbook.sheetnames if sheet != 'MENU']

    # Crear la hoja MENU
    create_menu(workbook, sheet_names)

    # Insertar los enlaces para volver al menú en cada hoja
    add_back_to_menu_link(workbook, sheet_names)

    # Generar el nombre del archivo resultante
    file_name = os.path.basename(file_path)
    output_path = os.path.join(output_folder, file_name)

    # Guardar el archivo modificado en la carpeta seleccionada
    workbook.save(output_path)
    print(f"Archivo modificado y guardado en: {output_path}")

if __name__ == "__main__":
    # Ocultar la ventana principal de tkinter
    root = Tk()
    root.withdraw()

    # Abrir diálogo para seleccionar el archivo de Excel
    file_path = filedialog.askopenfilename(
        title="Selecciona el archivo de Excel",
        filetypes=[("Archivos de Excel", "*.xlsx *.xls")]
    )

    if not file_path:
        print("No se ha seleccionado ningún archivo. Saliendo del programa.")
        exit()

    # Abrir diálogo para seleccionar la carpeta de destino
    output_folder = filedialog.askdirectory(title="Selecciona la carpeta donde guardar el archivo modificado")

    if not output_folder:
        print("No se ha seleccionado ninguna carpeta. Saliendo del programa.")
        exit()

    # Modificar el archivo de Excel
    modify_excel(file_path, output_folder)
```

### ¿Cómo funciona el script?

1. **`create_menu`**: Crea una nueva hoja llamada "MENU" y genera una lista con enlaces a las demás hojas en mayúsculas.
2. **`add_back_to_menu_link`**: Inserta una fila al principio de cada hoja existente, y en la celda A1 coloca un enlace de "Volver al menú".
3. **`modify_excel`**: Es la función principal que carga el archivo de Excel, ejecuta las dos funciones anteriores y guarda el archivo con los cambios.

### Dependencias:

- Se necesita tener instalada la biblioteca `openpyxl`:

```bash
pip install openpyxl
```

