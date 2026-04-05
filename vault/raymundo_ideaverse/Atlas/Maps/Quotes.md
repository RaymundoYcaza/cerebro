---
up: []
related: []
created: 2026-02-24
tags:
  - note/quotes💬
  - map/view
---

## Summary
```dataview 
LIST length(rows)
FROM #note/quotes 
WHERE topics
FLATTEN topics as topic
GROUP BY topic
SORT key asc
```


