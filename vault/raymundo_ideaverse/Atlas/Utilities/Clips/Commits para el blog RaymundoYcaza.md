---
up: []
related: []
created: 2026-03-23
---


# COMMIT STANDARD FOR ASTRO CONTENT (BLOG POSTS)

  

## General Rules

- Use Conventional Commits format:(scope):

- Always include the post slug as identifier: post-slug-

- Write messages in English

- Use imperative mood (e.g., "update", "fix", "add")

- Keep subject line ≤ 72 characters

- Add body only when context adds value

  

---

  

## 1. Inline Images (images داخل del contenido del post)


  

When updating, replacing, optimizing, or correcting images داخل del contenido:

  

feat(post): update inline images for -post-slug-

  

Alternative (no functional impact):

chore(post): update inline images for -post-slug-

  

Body (optional):

- Replaced outdated images with improved versions

- Optimized image size and format

- Updated paths and alt attributes

  

---

  

## 2. Post Content (text, markdown, structure)

  

For text edits, corrections, or improvements:

  

docs(post): update content for -post-slug-

  

If restructuring or major rewrite:

  

docs(post): revise and restructure content for -post-slug-

  

Body (optional):

- Improved clarity and readability

- Fixed grammar and typos

- Updated or expanded sections

  

---

  

## 3. Cover Image (featured / hero image)

  

When updating the main post image:

  

feat(post): update cover image for -post-slug-

  

Alternative (no functional impact):

chore(post): update cover image for -post-slug-

  

Body (optional):

- Replaced cover image with new version

- Optimized dimensions and compression

- Updated metadata reference

  

---

  

## 4. Multiple Changes in Same Post

  

If combining changes:

  

feat(post): update content and assets for -post-slug-

  

Body:

- Updated inline images

- Revised content sections

- Replaced cover image

  

---

  

## 5. Slug Format

  

- Use lowercase

- Use hyphens as separators

- Example: how-to-build-kanban-tauri

  

---

  

## 6. Scope Definition

  

Always use:

(post)

  

Optional extensions if needed:

(post/images)

(post/content)

(post/seo)

  

Example:

feat(post/images): update inline images for -post-slug-

  

---

  

## 7. Do Not Use

  

- "update stuff"

- "fix things"

- Empty commit messages

- Mixed languages

- Missing post identifier


# Aplicación práctica

Ejemplos de pciones alineadas con **Conventional Commits** (claro, mantenible y compatible con CI/CD). Asumo que manejas posts tipo blog y assets asociados.

---

## 1) Actualización de imágenes dentro de un post

**Commit:**

```
feat(post): update inline images for <post-slug>
```

**Body (opcional pero recomendado si hay contexto):**

```
- Replaced outdated images with higher resolution versions
- Optimized file sizes for faster loading
- Adjusted image paths and alt texts
```

**Alternativa más estricta (si no cambia funcionalidad, solo assets):**

```
chore(post): update inline images for <post-slug>
```

---

## 2) Actualización de contenido del post (texto)

**Commit:**

```
docs(post): update content for <post-slug>
```

**Body:**

```
- Improved wording and clarity
- Fixed typos and grammar issues
- Updated sections with new information
```

**Si el cambio es más significativo (reestructura):**

```
docs(post): revise and restructure content for <post-slug>
```

---

## 3) Actualización de imagen de portada (cover / featured image)

**Commit:**

```
feat(post): update cover image for <post-slug>
```

**Body:**

```
- Replaced cover image with new version
- Optimized dimensions and compression
- Updated metadata reference
```

**Alternativa más neutral:**

```
chore(post): update cover image for <post-slug>
```

---

## Recomendación técnica (importante)

- Usa siempre `<post-slug>` (ej: `how-to-use-n8n-agents`) para trazabilidad.
    
- Si trabajas con Astro/Markdown: separa bien cambios de `content` vs `assets`.
    
- Si hay impacto SEO (imágenes, contenido): añade nota en el body.
    
- Evita `update stuff` o mensajes genéricos — rompe el historial semántico.
    

---

Si quieres, puedo adaptarte esto a tu flujo exacto (Astro, Obsidian, CMS, estructura de carpetas, etc.) y dejarte un estándar listo para tu equipo.