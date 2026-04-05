---
created: 2025-02-23 
---

## Compilar la aplicación en Android Studio
`ionic capacitor build android`
### Compilar en modo debug:
```bash
ionic capacitor copy android && cd android && ./gradlew assembleDebug && cd ..
```
### Si da problemas de `gradlew permission denied`
Dentro de la carpeta Android:
```bash
chmod +x gradlew
```
### Si da problemas sobre *SDK directory is not writable*, modificar propietario del directorio
```bash
```
El apk deberá estar en
```bash
android/app/build/outputs/apk/debug/app-debug.apk
```
Mover el apk a la carpeta compartida
```bash
sudo mv android/app/build/outputs/apk/debug/app-debug.apk ~/put_apk/
```
Compilar en modo release:
```bash
cd android && 
./gradlew assembleRelease && 
cd app/build/outputs/apk/release &&
jarsigner -keystore YOUR_KEYSTORE_PATH -storepass YOUR_KEYSTORE_PASS app-release-unsigned.apk YOUR_KEYSTORE_ALIAS &&
zipalign 4 app-release-unsigned.apk app-release.apk
```
This will generate `app-release.apk` which should be good to go the play store (see `android/app/build/outputs/apk/release` folder).
You can find your keystore alias by running `keytool -v -list -keystore YOUR_KEYSTORE_PATH`
Ejecutar en dispositivo directamente desde la línea de comandos
```bash
ionic capacitor copy android && cd android && ./gradlew assembleDebug && ./gradlew installDebug && cd ..
```
Si se encuentra conectado algún dispositivo no autorizado:
```bash
adb kill-server
adb connect 192.168.0.5:5555
adb devices
```
