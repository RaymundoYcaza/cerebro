---
up: []
related: 
created: 2025-05-21
---



```dataview
list
file.cday
FROM "+" OR "Calendar"
WHERE length(file.outlinks) = 0 AND length(file.inlinks) = 0
SORT file.cday DESC
LIMIT 3
```

