---
up:
  - "[[Raymundo Ycaza Morales]]"
created: 2024-06-09
---


```dataview
TABLE WITHOUT ID
	file.link as Note,
	created as Created
WHERE
	contains(in,this.file.link) and
	!contains(file.name, "Template")
SORT created desc
```
