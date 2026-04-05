---
up:
  - "[[Sources]]"
related: []
created: 2022-01-01
---


This note passively looks at the properties of all notes.

If a note has an `in` property that includes a link to `Books`, it will show up below.


> [!context]+ Unrequited Notes
> These notes point directly to this note. But this note doesn't point back.
> 
> ```dataview  
> LIST 
> 
> FROM [[Books]] and !outgoing([[Books]])
> 
> SORT file.name asc  
> ```  

