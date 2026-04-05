---
up:
  - "[[Obsidian MOC]]"
related: 
created: 2025-06-03
---
 


### 📄 **Descripción del Query - Resumen de Referencias a esta Nota**

**Propósito:**  
Este script en **DataviewJS** genera una tabla con notas que _referencian a la nota actual (usando la propiedad `up`)_, excluyendo aquellas dentro de la carpeta `Efforts`. Para cada nota encontrada, muestra cuántas notas la referencian y cuántas de esas referencias están marcadas como completadas o pendientes.

**Columnas mostradas:**
1. **Note:** Enlace a la nota que referencia a la actual.
2. **Pending:** Cantidad de backlinks (referencias entrantes) a esa nota que **no están completadas** (`completed !== true`).
3. **Completed:** Cantidad de backlinks a esa nota que **sí están completadas** (`completed === true`).
4. **Total:** Total de referencias entrantes.
**Criterios clave:**
- Solo se muestran notas cuyo campo `up` contenga un enlace a esta nota.
- Se excluyen notas ubicadas en carpetas que comiencen con `Efforts`.
- Se cuenta el estado `completed` de las notas que enlazan a cada una de estas notas (inlinks).

**Uso sugerido:**  
Ideal para revisar el estado de avance de tareas o notas hijas relacionadas con esta nota, especialmente útil en sistemas de planificación jerárquica o documentación en red.

```js
const currentFile = dv.current().file;
const pages = dv.pages()
    .where(p => !p.file.folder.startsWith("Efforts"))
    .where(p => p.up && dv.array(p.up).some(link => link.path === currentFile.path))
    .map(p => [
        p.file.link,
        p.file.inlinks.filter(link => dv.page(link.path)?.completed !== true).length,
        p.file.inlinks.filter(link => dv.page(link.path)?.completed === true).length,
        p.file.inlinks.length
    ]);

dv.table(["Note", "Pending", "Completed", "Total"], pages);
```
