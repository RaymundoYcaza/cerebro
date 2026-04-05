---
in:
  - "[[Fast API]]"
---



Pasos para desplegar tu aplicación FastAPI en un servidor de producción con Ubuntu 20.04, partiendo desde un entorno de desarrollo en Windows:
**Preparar el entorno de producción**: Asegúrate de que tu servidor de producción tiene instalado Python 3.6 o superior, pip y venv. Puedes instalarlos con los siguientes comandos:
```
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
**Transferir tu aplicación al servidor de producción**: Puedes usar `scp` (Secure Copy) para transferir tu aplicación desde tu máquina de desarrollo a tu servidor de producción. Asegúrate de reemplazar `yourusername`, `yourserver` y `/path/to/your/app` con tus propios valores:
```
scp -r /path/to/your/app yourusername@yourserver:/path/to/destination
```
**Crear un entorno virtual en el servidor de producción**: Una vez que tu aplicación esté en el servidor de producción, puedes crear un entorno virtual para aislar las dependencias de tu aplicación:
```
python3 -m venv myenv
```
**Activar el entorno virtual e instalar las dependencias**: Activa el entorno virtual e instala las dependencias de tu aplicación. Asegúrate de que el archivo `requirements.txt` de tu aplicación lista todas las dependencias necesarias:
```
source myenv/bin/activate
pip install -r requirements.txt
```
**Ejecutar la aplicación con Uvicorn**: Puedes ejecutar tu aplicación FastAPI con Uvicorn. Asegúrate de reemplazar `main:app` con la ubicación de tu aplicación FastAPI:
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
**Configurar Uvicorn para iniciar al arranque**: Si quieres que tu aplicación se inicie automáticamente cuando se reinicie el servidor, puedes configurar un servicio systemd.
Para que Uvicorn se reinicie automáticamente cuando reinicias tu servidor Ubuntu 20.04, puedes configurar un servicio de systemd. Aquí te dejo los pasos para hacerlo:
**Crea un archivo de servicio systemd para tu aplicación FastAPI**. Puedes hacerlo con el siguiente comando:
```
sudo nano /etc/systemd/system/myfastapi.service
```
**Agrega la siguiente configuración al archivo**. Asegúrate de reemplazar `/path/to/your/fastapi/app` con la ruta a tu aplicación FastAPI y `myenv` con el nombre de tu entorno virtual:
```
[Unit]
Description=FastAPI app running on Uvicorn
After=network.target

[Service]
ExecStart=/path/to/your/fastapi/app/myenv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
WorkingDirectory=/path/to/your/fastapi/app
User=yourusername
Group=www-data
Restart=always

[Install]
WantedBy=multi-user.target
```
**Habilita y inicia el servicio**. Puedes hacerlo con los siguientes comandos:
```
sudo systemctl enable myfastapi
sudo systemctl start myfastapi
```
[Con esta configuración, tu aplicación FastAPI se iniciará automáticamente cuando reinicies tu servidor](https://www.cyberciti.biz/faq/howto-linux-unix-start-restart-cron/)
