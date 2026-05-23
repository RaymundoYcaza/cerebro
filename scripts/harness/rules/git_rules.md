# Git Safety Rules

Estas reglas aplican a `scripts/harness/git_tools.py` y a cualquier agente que opere Git dentro de este repositorio.

## Reglas de seguridad

- No hacer `push` automático.
- No hacer `merge` automático.
- No hacer `rebase` automático.
- No crear commits sin confirmación explícita.
- No agregar archivos al index automáticamente durante `commit`.
- No operar sobre `vault/raymundo_ideaverse` salvo instrucción explícita del usuario.
- Si hay merge, rebase o cherry-pick en curso, detener el flujo de commit.

## Ramas protegidas

Estas ramas no deben usarse para trabajo directo:

- `main`
- `master`
- `develop`
- `staging`
- `production`

## Convención de ramas

Formato:

```text
prefijo/YYYYMMDDhhmmss.xxx_slug
```

Ejemplo:

```text
feat/20260523214730.123_core-obsidian-utils
```

Prefijos permitidos:

- `feat`
- `fix`
- `refactor`
- `docs`
- `test`
- `chore`
- `ci`
- `perf`
- `style`
- `build`
- `hotfix`
- `experiment`

El slug debe usar minúsculas, números y guiones.

## Convención de commits

Formato:

```text
tipo(scope): resumen breve
```

El cuerpo es opcional y puede estar en español.

Tipos permitidos:

- `feat`
- `fix`
- `refactor`
- `docs`
- `test`
- `chore`
- `ci`
- `perf`
- `style`
- `build`
- `revert`

## Flujo recomendado

1. Revisar estado:

```bash
python3 scripts/harness/git_tools.py status
```

2. Crear rama segura:

```bash
python3 scripts/harness/git_tools.py create-branch --type feat --name "nombre del cambio"
```

3. Revisar resumen:

```bash
python3 scripts/harness/git_tools.py diff-summary
```

4. Stagear archivos manualmente.

5. Crear commit seguro:

```bash
python3 scripts/harness/git_tools.py commit
```
