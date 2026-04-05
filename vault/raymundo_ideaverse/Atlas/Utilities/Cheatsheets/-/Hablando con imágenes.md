---
created: 2024-12-18
up:
  - "[[Raymundo Ycaza Morales]]"
---



```dataview
TABLE WITHOUT ID
	file.link as Note,
	image as Source,
	created_at as Created
WHERE
	contains(in,this.file.link) and
	!contains(file.name, "Template")
SORT created desc
```
