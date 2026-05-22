---
tags: [draft, blog]
created: 2026-03-29
---

Hola automatizadores,

Hoy quiero compartir contigo cómo crear una herramienta en Python para extraer facturas y detalles de todos los XML firmados del SRI Ecuador a un Excel. La tecnología bien aplicada, no reemplaza personas, potencia talentos.

Paso 1: Instala las bibliotecas necesarias con `pip install pyexcel`, `pyexcel-xls` y `xml.etree.ElementTree`.

Paso 2: Crea una función que abre los archivos XML firmados del SRI, extrae la información de facturas y detalles usando ElementTree.

Paso 3: Usa PyExcel para escribir en un archivo Excel el contenido extraído.

Con este script podrás automatizar procesos, optimizando tiempo y recursos. ¡Pruébalo!

```python
import pyexcel as p
import xml.etree.ElementTree as ET

def extraer_facturas_xml(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()
    
    datos_factura = []
    for factura in root.findall('factura'):
        detalle = []
        for item in factura.find('detalles').findall('item'):
            detalle.append({
                'producto': item.find('nombre').text,
                'cantidad': item.find('cantidad').text,
                'precio': item.find('precio').text
            })
        
        datos_factura.append({
            'numero_factura': factura.find('numDoc').text,
            'fecha': factura.find('fechaEmision').text,
            'detalle': detalle
        })

    return datos_factura

def exportar_a_excel(datos, archivo):
    p.save_book_as(records=datos, dest_file_name=archivo)

# Ejemplo de uso
archivos_xml = ['factura1.xml', 'factura2.xml']
datos_facturas = [extraer_facturas_xml(archivo) for archivo in archivos_xml]
exportar_a_excel(datos_facturas, 'facturas.xlsx')
```

¡Hasta la próxima! La tecnología bien aplicada, no reemplaza personas, potencia talentos.