---
in:
  - "[[Apuntes]]"
related:
  - "[[Infraestructura Inorizonti - Docker]]"
subtopic: 
tags:
  - "#tags"
  - "#tags
created: 2025-05-15
acr: true
---


```shell
docker run -d \
  --name inorizonti_vpn_tunnel \
  --restart unless-stopped \
  cloudflare/cloudflared:latest tunnel \
  --no-autoupdate run \
  --token eyJhIjoiOTQ1ZGEzN2ZlNzU4MGUwNmFmZjA2NWI3MTFmMzhlMDgiLCJ0IjoiMmE4NTkyMzktN2EyNS00YzBlLThmZWQtOTkzNzQ3YWQyNjUwIiwicyI6Ill6TTRaRFV6WmpNdFlUWXlOQzAwT1Raa0xUazBOall0TUdVNU1EYzRZelpsTXpKbSJ9
```
