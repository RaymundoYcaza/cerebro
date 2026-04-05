---
up:
  - "[[Obsidian MOC]]"
related: 
created: 2025-05-23
---
 


```clojure
```dataviewjs
// Obtener el valor de 'searchText' de la nota actual
const searchText = dv.current()?.searchText;
const currentFile = dv.current().file;

// 1. Obtener todas las notas que enlazan a la actual
let linkedNotes = dv.pages()
    .where(p => p.file.outlinks.some(link => link.path === currentFile.path))
    .limit(50); // Limitar a 50 resultados

// 2. Filtrar por searchText si existe
if (searchText && searchText.trim() !== "") {
    linkedNotes = linkedNotes
        .where(p => p.file.name.toLowerCase().includes(searchText.toLowerCase()));
}

// 3. Mostrar resultados
if (linkedNotes.length > 0) {
    dv.table(
        ["Nota", "Título"],
        linkedNotes.map(p => [
            p.file.link,
            p.file.name
        ])
    );
} else if (searchText && searchText.trim() !== "") {
    dv.paragraph(`No se encontraron notas que enlacen aquí y contengan **"${searchText}"** en el título.`);
} else {
    dv.paragraph("ℹ️ No hay notas que enlacen a esta. " + 
        (searchText ? "" : "Puedes definir `searchText` en el YAML para filtrar."));
}
```
```