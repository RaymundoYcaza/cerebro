---
up:
  - "[[Redes e Internet Ubuntu Linux]]"
related: 
created: 2025-05-19
---
 

Sí, **es ideal** para tu caso porque:
- Quieres que el servidor **tenga siempre la misma IP** dentro de tu red local.
- Necesitas que funcione **sin conexión a internet**.
- Deseas que otras computadoras **puedan acceder al servidor internamente** (por IP estática es más fácil).

#### 1. Identifica tu interfaz de red

```bash
ip a
```

Busca un nombre como `enp3s0`, `eth0`, `ens33`, etc. (evita `lo`, que es la interfaz de loopback).

- % En el caso de Maximax la interfaz de red usada fue **enp2s0**
#### 2. Edita el archivo de configuración de Netplan

Los archivos están en `/etc/netplan/`. Puede haber uno llamado `00-installer-config.yaml` o similar.

Ejemplo de configuración estática:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp2s0:  # reemplaza por el nombre de tu interfaz
      dhcp4: no
      addresses:
        - 192.168.100.81/24
      gateway4: 192.168.100.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 1.1.1.1
```

#### 3. Aplica la configuración

```shell
sudo netplan apply
```

#### Verifica que funciona

- Usa `ip a` para verificar que la IP se ha asignado.
- Desde otra computadora en la red, prueba:
	- `ping 192.168.1.100`
- O accede vía SSH si está habilitado:
	- `- O accede vía SSH si está habilitado:`
