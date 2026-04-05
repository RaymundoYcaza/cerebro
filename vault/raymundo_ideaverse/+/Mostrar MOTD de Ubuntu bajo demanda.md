---
up:
  - "[[Índice de Snippets]]"
related: []
created_at: 2025-12-23
din: ID-1766505049161
aliases:
  - motd manual ubuntu
  - mostrar motd ubuntu
tags:
  - z/tipo/snippet
  - z/estado/activo
language: bash
framework: sistema-ubuntu
domain: devops
snippet_type: one-liner
complexity: baja
source: conversacion-llm
dependencies:
  - run-parts
  - update-motd
---

# Mostrar MOTD de Ubuntu bajo demanda

> [!SUMMARY] Resumen Ejecutivo
> Permite mostrar manualmente el Message Of The Day (MOTD) dinámico de Ubuntu sin necesidad de cerrar y abrir sesión.

## 📖 Descripción y Propósito

**¿Qué hace?**  
Ejecuta todos los scripts ubicados en `/etc/update-motd.d/` para generar dinámicamente el mensaje de bienvenida de Ubuntu, incluyendo información de sistema, carga, uso de disco, red y actualizaciones.

**¿Por qué es útil?**  
Permite consultar el estado del sistema bajo demanda sin necesidad de iniciar una nueva sesión SSH o TTY, útil para diagnóstico rápido y verificación operativa.
## 💻 Código

```bash
run-parts /etc/update-motd.d/
```

> [!TIP] Alternativas
> - **Versión Simplificada (snapshot):**
> ```bash
> cat /run/motd.dynamic
> ```
> 
> **Versión Estándar (wrapper oficial):**
> ```bash
> update-motd
> ```

## 🧪 Ejemplo de Uso Real

**Input (Entrada):**

```nginx
Usuario ejecuta el comando en una sesión activa de terminal
```

**Output (Salida):**

```pgsql
System load, memory usage, disk usage, IP, updates, avisos ESM
```

**Escenario:**  
Usado por administradores en servidores Ubuntu 22.04 para validar estado del sistema antes de ejecutar tareas críticas de mantenimiento o despliegue.

## ⚠️ Observaciones y Consideraciones

- **Dependencias:** Requiere `run-parts` (incluido en Ubuntu por defecto).
- **Compatibilidad:** Funciona en Ubuntu 18.04+ con MOTD dinámico habilitado.
- **Limitación:** `cat /run/motd.dynamic` no recalcula métricas en tiempo real.

## 💡 Consejos (Tips & Tricks)

- Puedes crear un alias en `.bashrc`:

```bash
alias motd='run-parts /etc/update-motd.d/'
```

- Desactiva el MOTD automático creando `~/.hushlogin` y ejecútalo solo cuando lo necesites.

## 🔗 Relacionado
