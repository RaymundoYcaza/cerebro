# Clasificador PARA + Obsidian - Fase 2

## Instalacion

```powershell
cd C:\cerebro\scripts\para
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python clasificador_para.py
```

## Que hace

- Procesa solo archivos/carpetas de primer nivel en `P:\PARA\00-INBOX`.
- Permite busqueda por texto o difusa.
- Pregunta clasificacion en modo rapido o logica completa.
- Pide confirmacion antes de mover.
- Mueve el archivo/carpeta a la estructura PARA.
- Crea nota Markdown en `zResources`.
- Registra movimientos en CSV, Markdown y JSON.
- Permite deshacer el ultimo movimiento, incluyendo eliminar la nota creada.

## Rutas configurables

Edita `config.yaml` si cambia la letra del disco o la ubicacion del vault.
