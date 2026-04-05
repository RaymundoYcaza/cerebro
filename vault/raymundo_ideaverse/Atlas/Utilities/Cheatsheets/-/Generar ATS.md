---
created: 2024-09-12
in:
  - "[[Tecnología MOC]]"
---

>[!Warning] # Atención
>Para ejecutar estos scripts, necesitarás instalar la librería `pandas`
>
>```bash
>pip install pandas openpyxl
>```

- **Script 1**:
    - Lee un archivo Excel con la estructura correcta (pestañas: `Informante`, `Compras`, `Ventas`, `VentasEstablecimiento`).
    - Extrae los datos y genera un archivo XML con la misma estructura que proporcionaste.
- **Script 2**:
    - Genera una plantilla Excel con las pestañas y columnas necesarias para que puedas llenarla con los datos.

### Script 1: Generar XML desde Excel

Este script toma un archivo Excel y genera un archivo XML con la estructura necesaria.

```python
import pandas as pd

import xml.etree.ElementTree as ET

  

def generar_xml_desde_excel(excel_file, output_xml):

    # Leer el archivo Excel

    df = pd.read_excel(excel_file, sheet_name=None)

    # Crear la estructura del XML

    iva = ET.Element('iva')

    # Información principal

    TipoIDInformante = ET.SubElement(iva, 'TipoIDInformante')

    TipoIDInformante.text = str(df['Informante'].iloc[0]['TipoIDInformante'])

    IdInformante = ET.SubElement(iva, 'IdInformante')

    IdInformante.text = str(df['Informante'].iloc[0]['IdInformante'])

    razonSocial = ET.SubElement(iva, 'razonSocial')

    razonSocial.text = str(df['Informante'].iloc[0]['razonSocial'])

    Anio = ET.SubElement(iva, 'Anio')

    Anio.text = str(df['Informante'].iloc[0]['Anio'])

    Mes = ET.SubElement(iva, 'Mes')

    Mes.text = str(df['Informante'].iloc[0]['Mes'])

    numEstabRuc = ET.SubElement(iva, 'numEstabRuc')

    numEstabRuc.text = str(df['Informante'].iloc[0]['numEstabRuc'])

    totalVentas = ET.SubElement(iva, 'totalVentas')

    totalVentas.text = str(df['Informante'].iloc[0]['totalVentas'])

    codigoOperativo = ET.SubElement(iva, 'codigoOperativo')

    codigoOperativo.text = str(df['Informante'].iloc[0]['codigoOperativo'])

    # Compras

    compras = ET.SubElement(iva, 'compras')

    for _, row in df['Compras'].iterrows():

        detalleCompras = ET.SubElement(compras, 'detalleCompras')

        for col in df['Compras'].columns:

            elem = ET.SubElement(detalleCompras, col)

            elem.text = str(row[col])  # Convertir a cadena

    # Ventas

    ventas = ET.SubElement(iva, 'ventas')

    for _, row in df['Ventas'].iterrows():

        detalleVentas = ET.SubElement(ventas, 'detalleVentas')

        for col in df['Ventas'].columns:

            elem = ET.SubElement(detalleVentas, col)

            elem.text = str(row[col])  # Convertir a cadena

    # Ventas Establecimiento

    ventasEstablecimiento = ET.SubElement(iva, 'ventasEstablecimiento')

    for _, row in df['VentasEstablecimiento'].iterrows():

        ventaEst = ET.SubElement(ventasEstablecimiento, 'ventaEst')

        for col in df['VentasEstablecimiento'].columns:

            elem = ET.SubElement(ventaEst, col)

            elem.text = str(row[col])  # Convertir a cadena

  

    # Generar el archivo XML

    tree = ET.ElementTree(iva)

    # Guardar el archivo XML

    with open(output_xml, "wb") as files:

        tree.write(files, encoding='UTF-8', xml_declaration=True)

    # Llamar a la función para eliminar las etiquetas vacías

    eliminar_etiquetas_vacias(output_xml)

    print(f"Archivo XML generado: {output_xml}")

  

def eliminar_etiquetas_vacias(output_xml):

    # Cargar el archivo XML generado

    tree = ET.parse(output_xml)

    root = tree.getroot()

  

    # Lista de etiquetas a eliminar si están vacías

    etiquetas_vacias = ['compras', 'ventas', 'ventasEstablecimiento']

  

    # Función recursiva para eliminar etiquetas vacías

    def eliminar_vacias(elemento):

        for child in list(elemento):

            eliminar_vacias(child)  # Recursivamente eliminar en los subelementos

            # Eliminar la etiqueta si está vacía y es una de las etiquetas objetivo

            if child.tag in etiquetas_vacias and (child.text is None or child.text.strip() == "") and len(child) == 0:

                elemento.remove(child)

  

    # Ejecutar la función de eliminación a partir de la raíz

    eliminar_vacias(root)

  

    # Guardar el archivo XML limpio

    tree.write(output_xml, encoding='UTF-8', xml_declaration=True)

  

# Uso

generar_xml_desde_excel('datos.xlsx', 'resultado.xml')

```


### Script 2: Generar Plantilla Excel Vacía

Este script genera una plantilla Excel con las hojas y columnas necesarias para que puedas llenarla y generar el XML después.

```python
import pandas as pd

def generar_plantilla_excel(output_excel):
    # Crear DataFrames vacíos con las columnas necesarias
    df_informante = pd.DataFrame({
        'TipoIDInformante': [''],
        'IdInformante': [''],
        'razonSocial': [''],
        'Anio': [''],
        'Mes': [''],
        'numEstabRuc': [''],
        'totalVentas': [''],
        'codigoOperativo': ['']
    })

    df_compras = pd.DataFrame({
        'codSustento': [''],
        'tpIdProv': [''],
        'idProv': [''],
        'tipoComprobante': [''],
        'parteRel': [''],
        'fechaRegistro': [''],
        'establecimiento': [''],
        'puntoEmision': [''],
        'secuencial': [''],
        'fechaEmision': [''],
        'autorizacion': [''],
        'baseNoGraIva': [''],
        'baseImponible': [''],
        'baseImpGrav': [''],
        'baseImpExe': [''],
        'montoIce': [''],
        'montoIva': [''],
        'valRetBien10': [''],
        'valRetServ20': [''],
        'valorRetBienes': [''],
        'valRetServ50': [''],
        'valorRetServicios': [''],
        'valRetServ100': [''],
        'valorRetencionNc': [''],
        'totbasesImpReemb': [''],
        'pagoLocExt': [''],
        'paisEfecPago': [''],
        'aplicConvDobTrib': [''],
        'pagExtSujRetNorLeg': ['']
    })

    df_ventas = pd.DataFrame({
        'tpIdCliente': [''],
        'idCliente': [''],
        'parteRelVtas': [''],
        'tipoComprobante': [''],
        'tipoEmision': [''],
        'numeroComprobantes': [''],
        'baseNoGraIva': [''],
        'baseImponible': [''],
        'baseImpGrav': [''],
        'montoIva': [''],
        'montoIce': [''],
        'valorRetIva': [''],
        'valorRetRenta': [''],
        'formaPago': ['']
    })

    df_ventas_est = pd.DataFrame({
        'codEstab': [''],
        'ventasEstab': [''],
        'ivaComp': ['']
    })

    # Crear un archivo Excel con múltiples hojas
    with pd.ExcelWriter(output_excel) as writer:
        df_informante.to_excel(writer, sheet_name='Informante', index=False)
        df_compras.to_excel(writer, sheet_name='Compras', index=False)
        df_ventas.to_excel(writer, sheet_name='Ventas', index=False)
        df_ventas_est.to_excel(writer, sheet_name='VentasEstablecimiento', index=False)
    
    print(f"Plantilla Excel generada: {output_excel}")

# Uso
generar_plantilla_excel('plantilla_vacia.xlsx')
```




a