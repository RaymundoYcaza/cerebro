---
created: 2025-02-23 
---
## Diseño de pantallas
Crear un splash screen y personalizar iconos
https://youtu.be/7cfxvOuDR44
https://capacitorjs.com/docs/apis/splash-screen
https://capacitorjs.com/docs/guides/splash-screens-and-icons
Instalar @capacitor/assets
```bash
npm install @capacitor/assets --save-dev
```
Esto creará una estructura de archivos base que son las imágenes de los iconos que se usarán
```
assets/
├── icon-only.png
├── icon-foreground.png
├── icon-background.png
├── splash.png
└── splash-dark.png
```
Crear una carpeta con el nombre `resources` y colocar en ella las imágenes que se van a utilizar. Tamaño mínimo para los iconos 1024x1024 y para las pantallas 2732x2732. Formato puede ser jpg o png.
icon-background.png 1024x1024
icon-foreground.png 1024x1024
splash.png 2732x2732
splash-dark.png 2732x2732
Una vez listas las imágenes, generar los assets
```bash
npx capacitor-assets generate
```
Editar el archivo `capacitor.config.ts` y agregar la configuración para el splash screen
```jsx
plugins: {
  SplashScreen: {
    launchShowDuration: 2000,
    showSpinner: false,
    androidSpinnerStyle: "small",
    iosSpinnerStyle: "small",
    splashFullScreen: true,
    splashImmersive: true,
    backgroundColor: "#ff0000",
    
  }
}
```
Crear botones con un icono grande y el texto debajo
Para mostrar el icono del botón en grande y debajo el texto, puedes utilizar CSS personalizado para ajustar el tamaño del icono y cambiar la dirección de los elementos dentro del botón.
```html
<ion-col>
  <ion-button class="square-button">
    <ion-icon name="heart" aria-label="Favorite" class="big-icon"></ion-icon>
    <div>Ingresar PM</div>
  </ion-button>
</ion-col>
```
Y en tu archivo CSS:
```css
.square-button {
--border-radius: 0;
--height: 20vw;
--width: 20vw;
flex-direction: column; /* Cambia la dirección de los elementos a vertical */
}
- .big-icon {
font-size: 2em; /* Ajusta el tamaño del icono */
}
```
En este código, `flex-direction: column` hace que los elementos dentro del botón se apilen verticalmente. `font-size: 2em` hace que el icono sea dos veces el tamaño normal. Puedes ajustar estos valores según tus necesidades. Recuerda agregar las clases `square-button` y `big-icon` a los elementos correspondientes.
Cómo cambiar el color de fondo de un botón
Ionic utiliza variables CSS personalizadas para estilizar sus componentes, incluyendo los botones. Para cambiar el color de fondo de un botón en Ionic, debes usar la variable `--background`.
```css
ion-button {
  --background: #ffffff !important;
}
- .square-button {
  border-radius: 0;
  height: 30vw;
  width: 30vw;
  --background: #ffffff !important;
  flex-direction: column;
}
```
En este código, `--background: #ffffff !important;` establece el color de fondo del botón a blanco. La regla `!important` asegura que este estilo tenga prioridad sobre otros estilos aplicados al botón.
Cómo crear un enlace directamente desde html
```htmlmixed
[routerLink]="['/formulario-am']"
```
Pasar datos entre pantallas
https://www.youtube.com/watch?v=C6LmKCSU8eM


