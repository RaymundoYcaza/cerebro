### CalloutNumbered.astro


---
import CalloutNumbered from '/src/components/CalloutNumbered.astro';

---


```html
<CalloutNumbered
  type="default"
  number={1}
  title="Configuración inicial"
>
  <p>Instala todas las dependencias necesarias antes de continuar.</p>
</CalloutNumbered>
```


### ExcelFormula.astro

---
import ExcelFormula from '../components/ExcelFormula.astro';

---

```html
<ExcelFormula
  name="SUMA"
  params={[
    { label: "número1", description: "Primer valor a sumar" },
    { label: "número2", description: "Segundo valor a sumar" }
  ]}
/>
```


### ExcelFunctionCard.astro

---
import ExcelFunctionCard from '../components/ExcelFunctionCard.astro';

---

```html
<ExcelFunctionCard
  name="SUMA"
  params={[
    { label: "número1" },
    { label: "número2" }
  ]}
/>
```


```html
<ExcelFunctionCard
  name="BUSCARV"
  params={[
    { label: "valor_buscado" },
    { label: "tabla" },
    { label: "columna" },
    { label: "ordenado", optional: true }
  ]}
/>
```


```html
<ExcelFunctionCard
  name="SI"
  params={[
    { label: "condición", color: "blue" },
    { label: "valor_si_verdadero", color: "green" },
    { label: "valor_si_falso", color: "red" }
  ]}
/>
```


```html
<ExcelFunctionCard
  name="HOY"
/>
```

#### Tamaños

```html
<ExcelFunctionCard
  name="PROMEDIO"
  size="sm"
  params={[
    { label: "rango" }
  ]}
/>
```


Opciones:

- sm
- md
- lg (default)
- xl


#### Ejemplo tipo documentación

```html
<section>
  <h3 class="text-xl font-semibold mb-4">Función SI</h3>

  <ExcelFunctionCard
    name="SI"
    params={[
      { label: "condición" },
      { label: "valor_si_verdadero" },
      { label: "valor_si_falso", optional: true }
    ]}
  />

  <p class="mt-4 text-gray-600">
    Permite evaluar una condición lógica y devolver un resultado.
  </p>
</section>
```


### Firma.astro

---
import Firma from '../components/Firma.astro';

---


```html
<Firma />
```



### KeyboardShortcut.astro

---
import KeyboardShortcut from '../components/KeyboardShortcut.astro';

---

<KeyboardShortcut
  keys={["Ctrl", "Shift", "P"]}
  title="Abrir paleta de comandos"
  description="Permite ejecutar comandos rápidamente"
/>


<KeyboardShortcut
  keys={["⌘", "C"]}
  title="Copiar"
  description="Copia el contenido seleccionado"
/>


```html
<section>
  <h3 class="text-lg font-semibold mb-4">Atajos esenciales</h3>

  <KeyboardShortcut
    keys={["Ctrl", "S"]}
    title="Guardar"
  />

  <KeyboardShortcut
    keys={["Ctrl", "Z"]}
    title="Deshacer"
  />

  <KeyboardShortcut
    keys={["Ctrl", "Shift", "Z"]}
    title="Rehacer"
  />

  <KeyboardShortcut
    keys={["Alt", "Tab"]}
    title="Cambiar ventana"
    description="Alterna entre aplicaciones abiertas"
  />
</section>
```


```html
<article class="prose mx-auto">

  <h2>Atajos en VS Code</h2>

  <KeyboardShortcut
    keys={["Ctrl", "P"]}
    title="Ir a archivo"
    description="Busca archivos rápidamente por nombre"
  />

  <KeyboardShortcut
    keys={["Ctrl", "Shift", "F"]}
    title="Buscar en todo el proyecto"
  />

</article>
```



### PostCard.astro

---
import PostCard from '../components/PostCard.astro';

---

```html
<PostCard slug="excel/funcion-suma" />
```

```html
<PostCard 
  slug="excel/tablas-dinamicas"
  variant="horizontal-reverse"
/>
```

```html
<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
  <PostCard slug="excel/si-condicional" variant="card" />
  <PostCard slug="excel/promedio" variant="card" />
  <PostCard slug="excel/contar-si" variant="card" />
</div>
```

```html
<PostCard 
  slug="excel/macros-basico"
  label="Avanzado"
/>
```

