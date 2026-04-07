---
up: []
related: []
created: 2026-04-07
---

# Tareas de documentación Sanagui

Probar el pull por consola:

```bash
curl -s -X GET http://192.168.100.81:8011/api/v2/pull \
  -H "Accept: application/json" \
  -H "Authorization: Bearer 150|FY6t4htfbVix67BuuHZwKJQGgvGptvzkDgVVRN7k02899004" \
  | jq .
```

Consultar los proveedores por consola

```bash
curl -s -X GET http://192.168.100.81:8011/api/proveedores \
  -H "Accept: application/json" \
  -H "Authorization: Bearer 150|FY6t4htfbVix67BuuHZwKJQGgvGptvzkDgVVRN7k02899004" \
  | jq .
```
