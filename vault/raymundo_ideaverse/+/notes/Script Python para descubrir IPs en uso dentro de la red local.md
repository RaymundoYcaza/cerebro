---
up:
  - "[[Python Scripts]]"
related: 
created: 2025-05-19
---

Este script de Python permite descubrir cuáles son las IP que están activas dentro de la red local, haciendo un "ping" a todas dentro del rango `192.168.100.3` a `192.168.100.100`.

```python
import subprocess

import platform

from concurrent.futures import ThreadPoolExecutor

  

# Configuración de ping

is_windows = platform.system().lower() == "windows"

param = "-n" if is_windows else "-c"

ping_count = "1"

timeout_param = "-w" if is_windows else "-W"

timeout = "1000" if is_windows else "1"  # milisegundos para Windows, segundos para Unix

  

# Rango de IPs

base_ip = "192.168.100."

start = 2

end = 100

  

def ping(ip):

    try:

        result = subprocess.run(

            ["ping", param, ping_count, timeout_param, timeout, ip],

            capture_output=True,

            text=True

        )

        output = result.stdout.lower()

        # Buscar indicadores de respuesta

        if is_windows:

            return ip if "ttl=" in output else None

        else:

            return ip if "ttl=" in output or "bytes from" in output else None

    except Exception:

        return None

  

def scan_ips():

    ips = [f"{base_ip}{i}" for i in range(start, end + 1)]

    live_hosts = []

  

    print("Escaneando IPs...")

  

    with ThreadPoolExecutor(max_workers=20) as executor:

        results = executor.map(ping, ips)

  

    for ip in results:

        if ip:

            live_hosts.append(ip)

  

    print("\nIPs activas:")

    for ip in live_hosts:

        print(ip)

  

if __name__ == "__main__":

    scan_ips()
```
