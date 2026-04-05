---
up:
  - "[[Home]]"
in:
  - "[[Raymundo Ycaza Morales]]"
related:
subtopic:
tags:
---



```dataview
TABLE WITHOUT ID
	file.link as Note, 
	created_at as Created
WHERE
	contains(this.file.inlinks, file.link) and
	!contains(file.name, "Template")
SORT created desc
```






