---
created: 2024-05-31
in:
  - "[[Python MOC]]"
---
er



```
python -m PyInstaller -F --noconsole .\darwin.py
```

Con icono personalizado

```
python -m PyInstaller -F --icon=C:\pathtoyouricon\icon.ico --noconsole .\darwin.py
```

Agregar las carpetas que usa la aplicación y serán redistribuidas

```
python -m PyInstaller -F --noconsole --add-data="commands/*;commands" --add-data="data/*;data" --add-data="gui/*;gui" darwin.py
```

