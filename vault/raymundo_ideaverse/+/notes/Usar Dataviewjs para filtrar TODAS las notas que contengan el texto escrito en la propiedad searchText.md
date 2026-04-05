---
up:
  - "[[Snippets]]"
  - "[[Obsidian MOC]]"
related: 
created: 2025-05-23
---
 


```clojure
```dataviewjs
// 1. Obtener el valor de 'searchText' de la nota actual
const searchText = dv.current().searchText;

// 2. Si existe, buscar notas que contengan ese texto en el título
if (searchText) {
    const notasCoincidentes = dv.pages()
        .where(p => p.file.name.includes(searchText));

    // 3. Mostrar resultados
    if (notasCoincidentes.length > 0) {
        dv.table(
            ["Nota", "Título"],
            notasCoincidentes.map(p => [
                p.file.link,
                p.file.name
            ])
        );
    } else {
        dv.paragraph(`No se encontraron notas con **"${searchText}"** en el título.`);
    }
} else {
    dv.paragraph("ℹ️ Define una propiedad `searchText` en el YAML de esta nota para buscar.");
}
```
```