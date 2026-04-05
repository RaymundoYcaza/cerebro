---
in:
  - "[[Logseq]]"
---




## Dynamic Variables
Notice: Macros support dynamic variables too
Syntax: <% something %>
Suported variables:
`today` => `[[Today's journal page]]`
`yesterday` => `[[Yesterday's journal page]]`
`tomorrow` => `[[Tomorrow's journal page]]`
`time` => `Current time`, e.g. 22:44
`current page` => `[[Current page]]`
Natural language date
`Last Friday` => `[[Feb 12th, 2021]]`
## Consultas
### Mostrar los bloques cuyo nombre comienza por 'abc'
```clojure
{:title "Pages that start with abc"
 :query [:find (pull ?p [*])
         :where 
         [?p :block/name ?name]
         [(clojure.string/starts-with? ?name "abc")]]
}
```
### Morfología de consultas avanzadas
#### Consulta para extraer los bloques etiquetados con una decada
```clojure
{ :title [:b "Blocks tagged in the 1970s"]
  :query [
    :find (pull ?b [*]) 
    :in $ ?decade
    :where 
      [?b :block/ref-pages ?p]
      [?p :block/name ?tag]
      [(clojure.string/starts-with? ?tag ?decade)]
  ]
  :collapsed? false
  :breadcrumb-show? true
  :inputs [197]
} 
```
Aquí está el desglose paso a paso:
`:title [:b "Blocks tagged in the 1970s"]`: Este es el título de la consulta. Se mostrará como “Blocks tagged in the 1970s” en la interfaz de usuario de Logseq.
`:query`: Aquí es donde se define la consulta en sí. Está compuesta por varias partes:
`:find (pull ?b [*])`: Esta es la cláusula `find`. Está buscando bloques (representados por `?b`) y quiere extraer todos los atributos de esos bloques (eso es lo que significa `[*]`).
`:in $ ?decade`: Esta es la cláusula `in`. Está diciendo que la consulta tomará una entrada, que es una década (representada por `?decade`).
`:where`: Esta es la cláusula `where`, que define las condiciones que deben cumplir los bloques para ser incluidos en los resultados. Tiene tres condiciones:
`[?b :block/ref-pages ?p]`: Esto significa que estamos buscando bloques (`?b`) que hacen referencia a algunas páginas (`?p`).
`[?p :block/name ?tag]`: Esto significa que las páginas (`?p`) deben tener un nombre (`?tag`).
`[(clojure.string/starts-with? ?tag ?decade)]`: Esto significa que el nombre de la página (`?tag`) debe comenzar con la década de entrada (`?decade`).
`:collapsed? false`: Esto significa que los resultados de la consulta no estarán colapsados en la interfaz de usuario de Logseq.
`:breadcrumb-show? true`: Esto significa que se mostrarán las migas de pan en la interfaz de usuario de Logseq.
`:inputs [197]`: Esto proporciona la entrada para la consulta. En este caso, la década de entrada es “197”.
