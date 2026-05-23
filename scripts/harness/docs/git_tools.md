# Git Tools

`scripts/harness/git_tools.py` ofrece comandos Git seguros, locales y agnósticos de agente. No hace `push`, `merge` ni `rebase` automático.

## Status

```bash
python3 scripts/harness/git_tools.py status
```

Muestra:

- rama actual;
- estado limpio o sucio;
- archivos staged;
- archivos modificados;
- archivos untracked;
- operaciones en curso como merge, rebase o cherry-pick;
- último commit.

## Validate Branch

```bash
python3 scripts/harness/git_tools.py validate-branch
```

Valida la rama actual. Para validar una rama específica:

```bash
python3 scripts/harness/git_tools.py validate-branch --branch feat/20260523214730.123_core-obsidian-utils
```

Formato esperado:

```text
prefijo/YYYYMMDDhhmmss.xxx_slug
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

Ramas protegidas:

- `main`
- `master`
- `develop`
- `staging`
- `production`

## Create Branch

```bash
python3 scripts/harness/git_tools.py create-branch --type feat --name "core obsidian utils"
```

El comando genera un nombre seguro con timestamp y slug, lo muestra y pide confirmación antes de crear la rama.

## Diff Summary

```bash
python3 scripts/harness/git_tools.py diff-summary
```

Muestra archivos modificados, líneas añadidas/eliminadas, tipos de archivo y resumen técnico simple.

Para evitar Ollama:

```bash
python3 scripts/harness/git_tools.py diff-summary --no-ollama
```

Si Ollama está disponible, intenta producir un resumen breve y sugerir tipo de commit. Si falla, el comando sigue funcionando.

## Commit

```bash
python3 scripts/harness/git_tools.py commit
```

Flujo:

1. Valida que el repo sea Git.
2. Revisa que no haya merge, rebase o cherry-pick en curso.
3. Exige archivos staged.
4. Muestra resumen de diff.
5. Pide confirmación.
6. Intenta generar mensaje con Ollama.
7. Valida Conventional Commit.
8. Muestra el commit propuesto.
9. Pide confirmación final.
10. Ejecuta `git commit`.
11. Registra el cambio en memoria del harness y changelog.

El comando no hace `git add` automático.

## Conventional Commits

Formato:

```text
tipo(scope): resumen breve
```

Ejemplos:

```text
feat(harness): agrega flujo de specs
docs(git): documenta herramientas seguras
fix(reflective): corrige serialización de wikilinks
```

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

## Flujo sin créditos del modelo grande

Cuando no haya créditos o no convenga usar el modelo principal:

1. Usa `git_tools.py status` para entender el árbol.
2. Usa `git_tools.py diff-summary --no-ollama`.
3. Stagea manualmente los archivos.
4. Ejecuta `git_tools.py commit`.
5. Si Ollama local falla, escribe el Conventional Commit manualmente.

## Advertencias

- No usar estos comandos para saltarse revisión humana.
- No crear commits desde ramas protegidas.
- No commitear cambios de `vault/raymundo_ideaverse` salvo instrucción explícita.
- No hacer push, merge ni rebase automático.
