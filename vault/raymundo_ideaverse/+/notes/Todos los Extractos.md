---
up:
  - "[[Sources]]"
related: 
created: 2025-05-22
tags:
  - map/view
  - note/extracts🔖
searchText: responsabilidad
---


```dataviewjs
function normalizeText(text) {
    return text
        .toLowerCase()
        .normalize("NFD")
        .replace(/\p{Diacritic}/gu, "");
}

const currentFile = dv.current().file.name;
const searchTextRaw = dv.page(currentFile)?.searchText || "";
const searchNormalized = normalizeText(searchTextRaw);
const MAX_RESULTS = 25;

let resultCount = 0;

// Modificado para incluir ambas carpetas
for (let page of dv.pages('"Atlas/Notes/Sources" or "Atlas/Notes/People"')) {
    if (resultCount >= MAX_RESULTS) break;

    const file = app.vault.getAbstractFileByPath(page.file.path);
    if (!file || !file.path.endsWith(".md")) continue;

    const content = await app.vault.read(file);
    const match = content.match(/## Extractos([\s\S]*?)(\n##|$)/);
    if (!match) continue;

    const lines = match[1].split('\n');
    dv.header(3, `[[${page.file.name}]]`);

    let currentHeader = null;

    const flushBlock = (blockLines) => {
        if (blockLines.length === 0) return;
        const blockText = blockLines.join('\n');

        if (!searchTextRaw || normalizeText(blockText).includes(searchNormalized)) {
            if (currentHeader) dv.paragraph(currentHeader);
            dv.paragraph("```markdown\n" + blockText + "\n```");
            resultCount++;
        }
    };

    for (let line of lines) {
        const trimmed = line.trim();

        if (/^#{3,}/.test(trimmed)) {
            // actualizar header actual
            currentHeader = trimmed;
        } else if (/^\s*-\s+/.test(line)) {
            // cada item de lista en su propio bloque markdown
            if (resultCount >= MAX_RESULTS) break;
            flushBlock([line]);
        }
        // ignorar otras líneas y espacios en blanco
        if (resultCount >= MAX_RESULTS) break;
    }
}

```



