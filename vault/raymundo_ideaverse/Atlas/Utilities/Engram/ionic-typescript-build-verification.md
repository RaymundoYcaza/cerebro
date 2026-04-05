---
type: engram
domain: typescript
status: refined
topic_key: ionic-typescript-build-verification
updated: 2026-04-03
---

## What: (Qué se hizo)

Se ejecutó una verificación de compilación TypeScript para validar que el código de **Ionic + TypeScript** compile correctamente, excluyendo archivos de pruebas `.spec.ts`, usando el siguiente comando:

```bash
npx tsc --noEmit --skipLibCheck 2>&1 | grep -v "\.spec\.ts"
```

Este comando:

- Ejecuta el compilador TypeScript
- No genera archivos (`--noEmit`)
- Omite verificación de librerías (`--skipLibCheck`)
- Redirige errores (`2>&1`)
- Filtra errores provenientes de archivos `.spec.ts`

---

## Why: (Racional técnico)

En proyectos Ionic/Angular:

- Los archivos `.spec.ts` suelen tener dependencias de testing no siempre configuradas
- Estos errores no afectan la compilación real de la aplicación
- Validar solo código productivo permite detectar errores reales sin ruido

Esto permite:

- Validación rápida de compilación
- Detección temprana de errores TypeScript
- Evitar falsos positivos provenientes de tests

---

## Where: (Nombre y ruta del archivo/proyecto)

Proyecto Ionic / Angular

Ejecutado desde:

```
Root del proyecto
```

Aplicable a:

- Proyectos Ionic
- Angular
- TypeScript monorepos
- CI/CD pipelines

---

## Learned: (Lección aprendida/Error evitado)

- `tsc --noEmit` es ideal para validación rápida sin build
- Filtrar `.spec.ts` evita ruido innecesario
- `--skipLibCheck` acelera considerablemente la verificación

Este comando es útil para:

- Pre-commit hooks
- CI pipelines
- Debug rápido antes de build

Comando recomendado para validación rápida de TypeScript en Ionic:

```bash
npx tsc --noEmit --skipLibCheck 2>&1 | grep -v "\.spec\.ts"
```

Patrón reutilizable para verificación silenciosa de compilación.
