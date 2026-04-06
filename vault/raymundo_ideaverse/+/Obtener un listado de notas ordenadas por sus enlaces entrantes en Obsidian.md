---
up:
  - "[[Obsidian Dataview MOC]]"
related: []
created: 2025-05-11
---

So, basically you need to create a table with all the file notes sorted according to the number of backlinks in each file.  
First, you need to install the plugin **Dataview**.  
Dataview works with ‘metadata’ information: data that you can insert in each file (via frontmatter or inline fiels) or ‘implicit’ data (metadata automatically created by each file, like file name, created date, tags, etc.).  
Your notes files have at least the implicit data. And that is enough for yours intents.  
In this case, you need to use the metadata `file.inlinks` (the backlinks) or `file.outlinks` (the outgoing links).  
You need to create a query like this:

```markdown
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total
FROM "yourfolderinObsidian"
SORT length(file.inlinks) DESC
```

Explaining:

- `file.inlinks` gives you the list/name of all the backlinks. It’s optional. `Backlinks` it’s the name you chose for the table column.
- `length(file.inlinks)` returns the number of backlinks. `Total` it’s the name you chose for the column…
- `"yourfolderinObsidian"` it’s the name of the folder where are your notes. If you want the query for all your vault you can use `""`. (you need to read the plugin documentation to find other options for FROM)
- `SORT length(file.inlinks) DESC` sorts all results by the number of file.inlinks in DESCending order.
