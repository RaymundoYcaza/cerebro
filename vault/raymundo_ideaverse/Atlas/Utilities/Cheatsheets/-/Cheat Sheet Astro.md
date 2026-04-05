---
in:
  - "[[Astro]]"
---



## Iniciar servidor dev
```
# start the development server

npx astro dev
```
## Conocer la versión de Astro
Puedes verificar la versión de Astro en tu proyecto ejecutando el siguiente comando en la terminal de tu proyecto:
```
npx astro --version
```
## Insertar imágenes en los posts
**Solo es necesario insertar las imágenes siguiendo la estructura:** `![Ruleta con PowerPoint](./images/ruleta-con-powerpoint_portada.png)`
Para insertar imágenes en los posts de tu blog en Astro, cuando la estructura de carpetas está en paquetes, puedes seguir estos pasos:
Almacenar las imágenes localmente: Astro recomienda que las imágenes locales se guarden en src / para que Astro pueda transformarlas, optimizarlas y agruparlas. Las imágenes pueden almacenarse en cualquier carpeta, incluso junto a tu contenido.
Importar las imágenes: En los archivos .astro, las imágenes locales deben importarse al archivo para poder utilizarse. Aquí tienes un ejemplo de cómo hacerlo:
```jsx
- import { Image } from 'astro:assets';
- import localImage from './images/localImage.png';
- <Image src={localImage} alt="Descripción de la imagen" />
```
Usar imágenes en el frontmatter de Markdown: Para usar imágenes en el frontmatter de Markdown con la función de activos de Astro, necesitas usar el ayudante de imagen en tu esquema de colección de contenido. Aquí tienes un ejemplo de cómo hacerlo:
```jsx
- // src/content/config.ts
- import { defineCollection, z } from "astro:content";
- export const collections = {
	- posts: defineCollection({
		- schema: ({ image }) => z.object({
			- cover: image(),
		- }),
	- }),
- };
```
Con esto, podrás pasar post.data.cover directamente al componente <Image>.
## Crear componentes
**Crea un nuevo archivo de componente en Astro**. En la carpeta de tu proyecto, crea un nuevo archivo `.astro` en la carpeta de componentes. Por ejemplo, puedes llamarlo `HolaMundo.astro`. El camino podría ser algo como `src/components/HolaMundo.astro`.
**Añade el contenido estático al componente**. Abre el archivo `HolaMundo.astro` y añade el siguiente código:
```
---
// Aquí puedes añadir lógica de JavaScript/TypeScript si es necesario
---

<h3>Hola mundo</h3>
```
**Utiliza el componente en tu post**. Ahora, puedes utilizar este componente en tu post. Abre el archivo `index.mdx` de tu post que se encuentra en `content/blog/nombre-categoria/post/index.mdx` y añade el componente de la siguiente manera:
```
---
// Aquí estarán los metadatos de tu post
---

import HolaMundo from '../../../src/components/HolaMundo.astro';

<HolaMundo />
```
**No usar llaves para importar el componente**
En JavaScript y otros lenguajes similares, `import { HolaMundo }` se utiliza para importar una **exportación con nombre** de un módulo. Esto significa que el módulo está exportando múltiples cosas, y quieres importar solo una de ellas, en este caso `HolaMundo`.
Por otro lado, `import HolaMundo` se utiliza para importar la **exportación predeterminada** de un módulo. Esto significa que el módulo está exportando una sola cosa, y quieres importar esa cosa.
En el caso de los componentes de Astro, cada archivo `.astro` exporta un solo componente como su exportación predeterminada. Por lo tanto, cuando importas un componente de Astro, utilizas `import HolaMundo` en lugar de `import { HolaMundo }`.
