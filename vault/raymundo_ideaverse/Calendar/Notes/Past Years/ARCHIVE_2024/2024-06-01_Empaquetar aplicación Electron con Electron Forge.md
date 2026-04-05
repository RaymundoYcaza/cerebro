---
created: 2024-06-01
in:
  - "[[Electron]]"
---
1. **Instala Electron Forge:**
    
    - Asegúrate de tener **Node.js** y **npm** instalados en tu sistema.
        
    - Luego, instala **Electron Forge** en tu proyecto ejecutando el siguiente comando en la terminal:
        
        ```bash
        npm install --save-dev @electron-forge/cli
        ```
        
2. **Importa tu proyecto a Electron Forge:**
    
    - Después de instalar Electron Forge, puedes importar tu proyecto existente. Ejecuta el siguiente comando:
        
        ```bash
        npx electron-forge import
        ```
        
    - Esto agregará algunos scripts a tu archivo `package.json` y creará un archivo `forge.config.js` con una configuración predefinida.
        
3. **Crea un distribuible:**
    
    - Utiliza el script `make` para crear un distribuible de tu aplicación. Ejecuta:
        
        ```bash
        npm run make
        ```
        
    - Este comando realizará dos pasos:
        
        - Primero, ejecutará `electron-forge package`, que agrupa el código de tu aplicación junto con el binario de Electron. El código empaquetado se generará en una carpeta.
        - Luego, utilizará esta carpeta de aplicaciones empaquetadas para crear un distribuible separado para cada fabricante configurado (por ejemplo, macOS, Windows, Linux).
4. **Verifica la carpeta de salida:**
    
    - Después de ejecutar el comando, deberías ver una carpeta llamada `out` en tu directorio de proyecto. Dentro de ella, encontrarás los distribuibles generados para cada plataforma.

Por ejemplo, en macOS, verás una estructura similar a esta:

```
out/
├── out/make/zip/darwin/x64/my-electron-app-darwin-x64-1.0.0.zip
├── ...
└── out/my-electron-app-darwin-x64/my-electron-app.app/Contents/MacOS/my-electron-app
```

El distribuible en la carpeta `out/make` estará listo para ejecutarse.