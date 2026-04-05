---
up:
  - "[[Library]]"
related: 
created: 2024-07-11
---
 



[[COMUNICACIÓN - Tabla auxiliar de Números Ordinales]]

[[Inglés MOC]]
[[Dole]]

[[Cómo calcular indicadores de videos Youtube]]



## Apuntes sueltos

> [!bug]+ Mtgs pointing to this note
> All notes linking as related to `This note`
> ```dataview
> LIST
> 
> FROM ""
> 
> WHERE contains(related,this.file.link)  AND !contains(in,[[Collections]]) AND !contains(in,[[Entities]]) AND !contains(in,[[Concepts]])
> 
> SORT file.name desc
> LIMIT 10
> ```
## Collecciones

> [!example]+ Mtgs pointing to this note
> All notes linking as related to `This note`
> ```dataview
> LIST
> 
> FROM ""
> 
> WHERE contains(related,this.file.link) AND contains(in,[[Collections]])
> 
> SORT file.name desc
> LIMIT 10
> ```

## Conceptos

> [!abstract]+ Mtgs pointing to this note
> All notes linking as related to `This note`
> ```dataview
> LIST
> 
> FROM ""
> 
> WHERE contains(related,this.file.link) AND contains(in,[[Concepts]])
> 
> SORT file.name desc
> LIMIT 10
> ```

## Entidades

> [!user]+ Mtgs pointing to this note
> All notes linking as related to `This note`
> ```dataview
> LIST
> 
> FROM ""
> 
> WHERE contains(related,this.file.link) AND contains(in,[[Entities]])
> 
> SORT file.name desc
> LIMIT 10
> ```

