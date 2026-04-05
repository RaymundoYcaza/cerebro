---
created: 2024-05-21 
---


- # Actividades

-
- ## Astro
  collapsed:: true
	- ## Know-How
		- ### Crear asides o admonitions
			- ![image.png](../assets/image_1710211947073_0.png)
			- ```jsx
			  <Aside type='note' title='Empieza ahora'>
			      Accede a mi **curso "[Domina Excel, paso a paso](curso-de-excel)"** que estará en constante actualización.
			  </Aside>
			  ```
		- ### Crear un post-preview
		  collapsed:: true
			- ![image.png](../assets/image_1710211993346_0.png)
			- ```jsx
			  import img from '../2023-06-27-curso-de-excel/images/curso-de-excel_portada.png';
			  ```
			- ```jsx
			  <PostPreview       
			        postName="curso-de-excel"
			        title="Domina Excel, paso a paso: 'Curso de Excel'"
			        footer="#Cursos #Excel #Formación">
			        <Picture src={img} alt="" slot="picture"/>
			        <span slot="title">Si deseas comenzar desde cero con Excel, esto es para ti.</span>
			        <span slot="description">lorem impsun dolor</span>
			  </PostPreview>
			  ```
	- ## Documentación
		- ### Componentes
		  collapsed:: true
			- https://docs.astro.build/es/basics/astro-components/
		- ### Componente Picture
		  collapsed:: true
			- https://astro-imagetools-docs.vercel.app/en/components/Picture/
		- ### Varios
			- https://markjames.dev/blog/dynamically-importing-images-astro
			- https://techsquidtv.com/blog/generating-open-graph-images-for-astro/
		-