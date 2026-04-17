---
up: []
related: []
created: 2026-04-13
---

# Como configurar el theme en nvim de Gentleman Programming

````markdown
# Neovim / LazyVim Theme Cheatsheet (Especialmente para Gentleman.Dots)

Guía rápida para **diagnosticar, instalar y configurar themes** en Neovim + LazyVim + Gentleman.Dots.

---

# 1. Ver Theme Actual

Dentro de nvim:

```vim
:echo g:colors_name
```
````

Ejemplo:

```
everforest
```

---

# 2. Ver Themes Disponibles

```vim
:colorscheme <TAB>
```

o con Telescope:

```vim
:Telescope colorscheme
```

---

# 3. Dónde se Configuran los Themes en LazyVim

LazyVim carga automáticamente:

```
~/.config/nvim/lua/plugins/*.lua
```

Esto significa que **puedes tener múltiples archivos de theme**:

```
lua/plugins/
├── colorscheme.lua
├── theme.lua
├── ui.lua
└── user/
    └── theme.lua
```

El **último que se carga sobrescribe** los anteriores.

---

# 4. Configurar Theme por Defecto

Ejemplo:

Crear archivo:

```
~/.config/nvim/lua/plugins/theme.lua
```

Contenido:

```lua
return {
  {
    "neanias/everforest-nvim",
    priority = 1000,
  },

  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "everforest",
    },
  },
}
```

---

# 5. Método Recomendado (Configuración Personal)

Crear carpeta:

```
~/.config/nvim/lua/plugins/user/
```

Luego:

```
~/.config/nvim/lua/plugins/user/theme.lua
```

Esto evita conflictos al actualizar dotfiles.

---

# 6. Instalar Nuevo Theme

Ejemplo Everforest:

```lua
return {
  {
    "neanias/everforest-nvim",
    priority = 1000,
  },

  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "everforest",
    },
  },
}
```

Luego:

```vim
:Lazy sync
```

Reiniciar nvim.

---

# 7. Buscar Dónde Está Definido un Theme

Desde terminal:

```bash
grep -R "everforest" ~/.config/nvim
```

o

```bash
grep -R "colorscheme" ~/.config/nvim
```

Esto ayuda cuando:

- Un theme aparece sin saber por qué
- Hay overrides ocultos
- Migras entre entornos (WSL / Ubuntu)

---

# 8. Forzar Theme Temporalmente

Dentro de nvim:

```vim
:colorscheme everforest
```

(No es persistente)

---

# 9. Actualizar Plugins

```vim
:Lazy sync
```

o

```vim
:Lazy update
```

---

# 10. Diagnóstico Completo

Ver salud:

```vim
:checkhealth
```

Ver plugins:

```vim
:Lazy
```

---

# 11. Ubicaciones Importantes

Config principal:

```
~/.config/nvim/
```

Plugins Lazy:

```
~/.local/share/nvim/lazy/
```

Estado:

```
~/.local/state/nvim/
```

Cache:

```
~/.cache/nvim/
```

---

# 12. Problemas Comunes

## Theme no aparece

Ejecutar:

```vim
:Lazy sync
```

---

## Theme no se aplica

Buscar override:

```bash
grep -R "colorscheme" ~/.config/nvim
```

---

## Theme diferente entre WSL y Ubuntu

Verificar:

- Plugins instalados
- Archivos `plugins/*.lua`
- Terminal diferente
- Nerd Font diferente

---

# 13. Themes Recomendados (LazyVim)

Muy populares:

- everforest
- catppuccin
- tokyonight
- kanagawa
- gruvbox
- rose-pine
- nightfox

---

# 14. Ver Orden de Carga

Usar prioridad:

```lua
priority = 1000
```

Más alto = carga primero.

---

# 15. Configuración Limpia Recomendada

```
lua/plugins/
├── core/
├── ui/
└── user/
    └── theme.lua
```

Mantener personalizaciones en:

```
lua/plugins/user/
```

---

# 16. Reinicio Completo (Si algo falla)

rm -rf ~/.local/share/nvim
rm -rf ~/.cache/nvim
rm -rf ~/.local/state/nvim

````

Luego abrir:

```bash
nvim
````

---

# 17. Verificar Configuración Activa

Dentro de nvim:

```vim
:scriptnames
```

Muestra todos los archivos cargados.

Muy útil para debugging.
