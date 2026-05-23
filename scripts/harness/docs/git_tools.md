# Git Tools

Descripción:
Herramientas Git seguras para revisar estado, validar ramas, resumir diffs y crear commits con Ollama local o fallback manual.

`scripts/harness/git_tools.py` ofrece comandos Git seguros, locales y agnósticos de agente. No hace `push`, `merge` ni `rebase` automático.

## Comandos

Ver estado:

```bash
python3 scripts/harness/git_tools.py status
```

Validar rama:

```bash
python3 scripts/harness/git_tools.py validate-branch
```

Crear rama:

```bash
python3 scripts/harness/git_tools.py create-branch --type feat --name "nombre"
```

Resumir diff:

```bash
python3 scripts/harness/git_tools.py diff-summary
```

Crear commit:

```bash
python3 scripts/harness/git_tools.py commit
```

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
6. Intenta generar mensaje con Ollama usando texto plano, no JSON.
7. Si Ollama falla, muestra un error técnico resumido y permite fallback manual.
8. Valida Conventional Commit.
9. Muestra el commit propuesto.
10. Pide confirmación final.
11. Ejecuta `git commit`.
12. Registra el cambio en memoria del harness y changelog.

El comando no hace `git add` automático.

Modo debug:

```bash
python3 scripts/harness/git_tools.py commit --debug
```

Muestra `base_url`, modelo, endpoint (`/api/chat` o `/api/generate`), duración aproximada y si usó fallback.

El prompt pide solo este formato:

```text
tipo(scope): título breve

- punto 1
- punto 2
```

La respuesta puede venir como texto plano. Con `/api/chat` se lee `message.content`; con `/api/generate` se lee `response`.

El cliente HTTP usa `requests` si está disponible; si el intérprete de `python` no lo tiene instalado, usa `urllib` de la librería estándar.

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
5. Si Ollama local falla, el comando pide título y cuerpo opcional de forma manual.

## Advertencias

- No usar estos comandos para saltarse revisión humana.
- No crear commits desde ramas protegidas.
- No commitear cambios de `vault/raymundo_ideaverse` salvo instrucción explícita.
- No hacer push, merge ni rebase automático.


## Ejemplos

Revisar estado:

```bash
python3 scripts/harness/git_tools.py status
```

Crear rama:

```bash
python3 scripts/harness/git_tools.py create-branch --type feat --name "docs automation"
```

Commit con debug:

```bash
python3 scripts/harness/git_tools.py commit --debug
```

## Errores comunes

- `requests no está disponible`:
  - Causa: intérprete de Python sin dependencia opcional.
  - Solución: la herramienta usa `urllib` como fallback.

## Troubleshooting

- Ejecuta `diff-summary --no-ollama`.
- Verifica `ollama.base_url` en `scripts/harness/config.yaml`.
- Usa `commit --debug` para ver endpoint, modelo y duración.

## Relación con otras herramientas

- `harness.py log-change` registra cambios.
- `harness.py check` valida el repo antes de commitear.
