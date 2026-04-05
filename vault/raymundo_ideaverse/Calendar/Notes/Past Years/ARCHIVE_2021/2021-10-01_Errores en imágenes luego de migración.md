- Descubro que durante el cambio a Webempresa, mis imágenes no fueron migradas completamente y existen varias entradas que no muestran imágenes de portada. En algunos casos puntuales, no muestran imágenes internas. 
    - Existen 9978 archivos en el directorio wp-contents/uploads
    - Se cambian los permisos de los archivos bajo el directorio wp-content/uploads a 644
    - Se cambian los permisos de los subdirectorios bajo el directorio wp-content/uploads a 744
    - Fue un error cambiar los permisos de los subdirectorios a 744. Según el Codex de Wordpress a día de hoy 2021-10-01 los permisos ideales par directorios son 755 o 750.
    - De acuerdo con el mismo Codex de WordPress, los archivos deben tener permisos 644, por lo que no es necesario realizar ningún cambio.
    - Procedo a descargar las imágenes faltantes desde el hosting viejo, manualmente, y las cargo al nuevo hosting, en la carpeta uploads.
    - Cambio la estructura de los enlaces permanentes a %nombre%/%id%/
    - Resultado de revisión preliminar: Siendo las 2:16 del 2021-10-02 todas las imágenes destacadas de las entradas se muestran sin problemas. Falta revisar nuevamente y revisar las imágenes internas de cada entrada.

