---
up: []
related: []
created: 2026-04-16
---

# Como buscar con fzf

Sí. **`fzf` en PowerShell puede buscar por contenido**, pero **no lo hace solo**. Necesita combinarse con herramientas como:

* `rg` (ripgrep) — recomendado (rápido)
* `grep`
* `Select-String` (PowerShell nativo)

La forma más común y eficiente es usar **ripgrep + fzf**.

---

# Opción recomendada (rápida): `ripgrep + fzf`

```powershell
rg --line-number --no-heading --color=always "" | fzf
```

Pero normalmente se usa así:

```powershell
rg "texto_a_buscar" | fzf
```

Ejemplo:

```powershell
rg "database" | fzf
```

Esto:

* Busca **"database" dentro de archivos**
* `fzf` te deja **filtrar interactivo**
* Seleccionas con Enter

---

# Búsqueda interactiva en vivo (más potente)

Esto permite escribir dentro de `fzf` y que vaya buscando contenido:

```powershell
fzf --bind "change:reload:rg {q} || rem" --ansi --disabled
```

Esto hace:

* Escribes algo
* `rg` busca dentro de archivos
* `fzf` muestra resultados dinámicos

Muy potente 🔥

---

# Si no tienes `ripgrep`

Puedes usar PowerShell nativo:

```powershell
Select-String -Path * -Pattern "texto" -Recurse | fzf
```

Pero es:

* Más lento
* Menos cómodo

---

# Bonus: Abrir archivo seleccionado

Muy útil:

```powershell
rg "texto" | fzf | ForEach-Object {
    code ($_ -split ":")[0]
}
```

Esto:

* Busca contenido
* Seleccionas
* Abre en Visual Studio Code

---

# Mi recomendación

Instala:

```powershell
winget install BurntSushi.ripgrep
winget install fzf
```

Es la combinación más potente para:

* Buscar archivos
* Buscar contenido
* Navegar proyectos grandes

---

Si me dices:

* si usas Windows puro
* PowerShell 5 o PowerShell 7
* Windows Terminal / WezTerm / Alacritty

Te doy una configuración más avanzada (tipo fuzzy search estilo LazyVim).
