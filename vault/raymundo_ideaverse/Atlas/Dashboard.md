
```dataview
TABLE domain, status, topic_key, updated
WHERE type="engram" 
AND !contains(file.path, "Templates")
```


### 📂 Colecciones QMD Activas
Asegúrate de que estas colecciones coincidan con tu terminal:
- [ ] **cheatsheets**: Documentación rápida.
- [ ] **devops**: Infraestructura y despliegue.
- [ ] **notes**: Pensamiento zettelkasten.

> [!TIP] 
> Para buscar en una categoría específica desde la terminal, usa: 
> `qmd query "tu duda" -c nombre_coleccion`