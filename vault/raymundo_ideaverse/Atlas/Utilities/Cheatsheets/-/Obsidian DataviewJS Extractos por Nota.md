---
up:
  - "[[Obsidian MOC]]"
related: 
created: 2025-05-22
---


```clojure
for (let page of dv.pages('"Atlas/Notes/Sources"')) {
    let file = app.vault.getAbstractFileByPath(page.file.path);

    if (file && file.path.endsWith(".md")) {
        let content = await app.vault.read(file);
        let match = content.match(/## Extractos([\s\S]*?)(\n##|$)/);

        if (match) {
            let extractos = match[1]
                .split('\n')
                .filter(line => line.trim().startsWith('- '))
                .map(line => line.replace(/^- /, '').trim());

            if (extractos.length > 0) {
                dv.header(3, page.file.name);
                dv.list(extractos);
            }
        }
    }
}
```

### ✅ Qué hace este script:

- Recorre todas las notas dentro de `Atlas/Notes/Sources`.
- Lee el contenido completo del archivo Markdown.
- Busca el bloque bajo el encabezado `## Extractos`.
- Extrae solo las líneas que comienzan con `-` .
- Las muestra con el nombre del archivo como subtítulo.

### 🧪 Prueba rápida

En una nota llamada `Ejemplo.md` dentro de `Atlas/Notes/Sources`, agrega:
```markdown
## Extractos
- Primer punto.
- Segundo punto.
```

## 🔗 Versión actualizada del script con enlaces a la nota original

Aquí el mismo script, pero ahora los extractos aparecerán como **enlaces al archivo fuente**, agregando claridad y trazabilidad:

```js
for (let page of dv.pages('"Atlas/Notes/Sources"')) {
    let file = app.vault.getAbstractFileByPath(page.file.path);

    if (file && file.path.endsWith(".md")) {
        let content = await app.vault.read(file);
        let match = content.match(/## Extractos([\s\S]*?)(\n##|$)/);

        if (match) {
            let extractos = match[1]
                .split('\n')
                .filter(line => line.trim().startsWith('- '))
                .map(line => line.replace(/^- /, '').trim());

            if (extractos.length > 0) {
                dv.header(3, `[[${page.file.name}]]`);
                dv.list(extractos.map(e => `[[${page.file.name}]]: ${e}`));
            }
        }
    }
}
```

## 🔗 Script con enlaces _limpios_ (alias)

```js
for (let page of dv.pages('"Atlas/Notes/Sources"')) {
    let file = app.vault.getAbstractFileByPath(page.file.path);

    if (file && file.path.endsWith(".md")) {
        let content = await app.vault.read(file);
        let match = content.match(/## Extractos([\s\S]*?)(\n##|$)/);

        if (match) {
            let extractos = match[1]
                .split('\n')
                .filter(line => line.trim().startsWith('- '))
                .map(line => line.replace(/^- /, '').trim());

            if (extractos.length > 0) {
                dv.header(3, `[[${page.file.name}]]`);
                dv.list(extractos.map(e => `[[${page.file.name}|${e}]]`));
            }
        }
    }
}
```

## 🔁 Script actualizado con enlaces al encabezado `## Extractos`

```js
for (let page of dv.pages('"Atlas/Notes/Sources"')) {
    let file = app.vault.getAbstractFileByPath(page.file.path);

    if (file && file.path.endsWith(".md")) {
        let content = await app.vault.read(file);
        let match = content.match(/## Extractos([\s\S]*?)(\n##|$)/);

        if (match) {
            let extractos = match[1]
                .split('\n')
                .filter(line => line.trim().startsWith('- '))
                .map(line => line.replace(/^- /, '').trim());

            if (extractos.length > 0) {
                dv.header(3, `[[${page.file.name}]]`);
                dv.list(
                    extractos.map(e =>
                        `[[${page.file.name}#Extractos|${e}]]`
                    )
                );
            }
        }
    }
}

```

## ✅ Script actualizado con filtro por `searchText`

```js
const currentFile = dv.current().file.name;
const searchText = dv.page(currentFile)?.searchText || "";
const searchLower = searchText.toLowerCase();

for (let page of dv.pages('"Atlas/Notes/Sources"')) {
    let file = app.vault.getAbstractFileByPath(page.file.path);

    if (file && file.path.endsWith(".md")) {
        let content = await app.vault.read(file);
        let match = content.match(/## Extractos([\s\S]*?)(\n##|$)/);

        if (match) {
            let extractos = match[1]
                .split('\n')
                .filter(line => line.trim().startsWith('- '))
                .map(line => line.replace(/^- /, '').trim());

            // Aplica filtro solo si searchText tiene contenido
            let filtrados = searchText
                ? extractos.filter(e => e.toLowerCase().includes(searchLower))
                : extractos;

            if (filtrados.length > 0) {
                dv.header(3, `[[${page.file.name}]]`);
                dv.list(filtrados.map(e => `[[${page.file.name}#Extractos|${e}]]`));
            }
        }
    }
}
```

## ✅ Script con normalización (ignorar tildes y mayúsculas) y paginado 

```js
function normalizeText(text) {
    return text
        .toLowerCase()
        .normalize("NFD")
        .replace(/\p{Diacritic}/gu, "");
}

const currentFile = dv.current().file.name;
const searchTextRaw = dv.page(currentFile)?.searchText || "";
const searchNormalized = normalizeText(searchTextRaw);

let count = 0;
const MAX_RESULTS = 25;

for (let page of dv.pages('"Atlas/Notes/Sources"')) {
    if (count >= MAX_RESULTS) break;

    let file = app.vault.getAbstractFileByPath(page.file.path);

    if (file && file.path.endsWith(".md")) {
        let content = await app.vault.read(file);
        let match = content.match(/## Extractos([\s\S]*?)(\n##|$)/);

        if (match) {
            const lines = match[1].split('\n');

            // Agrupar en bloques de lista de primer nivel y sus subelementos
            const blocks = [];
            let currentBlock = [];

            for (let line of lines) {
                if (line.trim().startsWith('- ')) {
                    if (currentBlock.length > 0) blocks.push(currentBlock);
                    currentBlock = [line];
                } else if (line.trim().startsWith('  -') || line.trim().startsWith('\t-')) {
                    currentBlock.push(line);
                } else if (line.trim() === '') {
                    continue;
                } else {
                    // Línea que no pertenece a ningún bloque
                    if (currentBlock.length > 0) {
                        blocks.push(currentBlock);
                        currentBlock = [];
                    }
                }
            }
            if (currentBlock.length > 0) blocks.push(currentBlock);

            // Filtrar por texto de búsqueda
            const filteredBlocks = searchTextRaw
                ? blocks.filter(block =>
                    block.some(line => normalizeText(line).includes(searchNormalized))
                )
                : blocks;

            if (filteredBlocks.length > 0) {
                const remaining = MAX_RESULTS - count;
                const shownBlocks = filteredBlocks.slice(0, remaining);
                count += shownBlocks.length;

                dv.header(3, `[[${page.file.name}]]`);

                for (let block of shownBlocks) {
                    dv.paragraph("```markdown\n" + block.join('\n') + "\n```");
                }
            }
        }
    }
}

```



