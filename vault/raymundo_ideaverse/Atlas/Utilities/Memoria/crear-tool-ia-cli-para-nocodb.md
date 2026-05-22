  
# Harness, SDD y Memoria Local para Framework NocoDB

## Resumen

Convertir el repositorio actual en una herramienta ordenada para gesti├│n de datos de negocio con NocoDB, IA asistida y consola. La base ser├í un framework liviano con harness de ejecuci├│n/evaluaci├│n, SDD, memoria local SQLite y documentaci├│n separada para usuario y desarrollador.

La implementaci├│n debe preservar el uso r├ípido desde consola, reducir dependencia de modelos grandes con contratos claros y preparar el proyecto para futuras funciones como dashboards,
an├ílisis de datos y automatizaci├│n de flujos.

## Cambios Clave

- Reestructurar el proyecto en m├│dulos: cliente NocoDB, configuraci├│n, flujos de negocio, LLM, memoria, CLI y utilidades de consola.
- Crear un harness ejecutable desde consola para correr escenarios controlados sin tocar datos reales por defecto.
- Adoptar SDD con carpeta specs/ para definir casos de uso, contratos de entrada/salida, criterios de aceptaci├│n y fixtures.
- Agregar memoria local SQLite como backend inicial, sin dependencia externa adicional.
- Mantener README.md como gu├¡a clara para usuario final.
- Crear docs/developer-guide.md o docs/developer/ para arquitectura, convenciones, testing, prompts, flujo SDD y operaci├│n con IA.
- Agregar pyproject.toml, pytest y convenciones m├¡nimas de calidad.

## Arquitectura Propuesta

- src/nocodb_toolkit/
- client.py: cliente NocoDB HTTP, errores y paginaci├│n.
- config.py: carga y validaci├│n de .env.
- llm.py: adaptador Ollama, fallback de modelos y contrato JSON.
- memory.py: SQLite local para runs, decisiones, snapshots y resultados.
- harness.py: ejecuci├│n de escenarios SDD con mocks, fixtures o modo live expl├¡cito.
- workflows/interactions.py: flujo CTS actual separado de la UI.
- cli.py: comandos consolidados para NocoDB, CTS, harness y memoria.

Memoria SQLite inicial:

- runs: ejecuciones de comandos/harness.
- decisions: decisiones t├⌐cnicas y de negocio relevantes.
- schema_snapshots: metadata de tablas NocoDB consultadas.
- llm_events: prompts, modelo usado, resultado, fallback y errores.
- artifacts: rutas o JSON de resultados generados.

SDD inicial:

- specs/cts_capture.md: flujo de captura CTS.
- specs/nocodb_client.md: contrato del cliente NocoDB.
- specs/harness.md: reglas de ejecuci├│n, fixtures y validaciones.
- specs/memory.md: contrato de memoria local.
- fixtures/: respuestas fake de NocoDB/Ollama para pruebas reproducibles.

## Convenciones

- Todo flujo nuevo debe tener spec antes de implementaci├│n.
- Toda llamada a NocoDB debe pasar por el cliente central.
- Todo uso de IA debe declarar modelo, prompt, formato esperado, fallback y validaci├│n.
- Por defecto, el harness corre en modo offline con fixtures.
- El modo live debe requerir flag expl├¡cito, por ejemplo --live.
- Los modelos peque├▒os solo deben operar sobre contratos cerrados, JSON schemas simples y ejemplos validados.
- Las credenciales quedan solo en .env; nunca en specs, fixtures ni memoria SQLite.
- Los comandos deben poder devolver salida humana y, cuando aplique, salida JSON para automatizaci├│n.

## Plan de Trabajo

1. Crear base de proyecto Python formal con pyproject.toml, estructura src/, tests/, specs/, docs/ y fixtures/.
2. Migrar sin cambiar comportamiento el cliente NocoDB y la CLI actual a m├│dulos importables.
3. Extraer el flujo CTS de interaction_crud.py en l├│gica testeable separada de prompts input().
4. Implementar memoria SQLite local con comandos m├¡nimos: init, log-run, list-runs, show-run, snapshot-schema.
5. Implementar harness offline con fixtures para validar cliente, payload CTS, parsing LLM, fallback heur├¡stico y renderizado de salida.
6. Agregar specs SDD iniciales para CTS, cliente NocoDB, memoria y harness.
7. Actualizar README.md como gu├¡a de uso de herramienta.
8. Crear gu├¡a de desarrollador con arquitectura, comandos, convenciones, flujo SDD, testing y estrategia de modelos.
9. Agregar pruebas unitarias y de harness para asegurar que modelos peque├▒os puedan trabajar sobre casos repetibles.
10. Preparar roadmap posterior para dashboards, an├ílisis de datos, generaci├│n de reportes y asistentes de consola.

## Test Plan

- Tests unitarios para normalizaci├│n de texto, fuzzy matching, parsing JSON de LLM, sanitizaci├│n de propuestas y construcci├│n de payload.
- Tests de cliente NocoDB con respuestas mockeadas.
- Tests de memoria SQLite usando base temporal.
- Tests de harness usando fixtures sin red.
- Test de CLI para comandos principales con salida JSON estable.
- Escenario live manual documentado para validar conexi├│n real con NocoDB y Ollama.

## Estrategia de Modelos

- Usar modelos potentes durante dise├▒o de specs, refactors grandes y nuevas capacidades anal├¡ticas.
- Guardar decisiones, ejemplos y salidas aceptadas en SQLite/specs para reducir razonamiento repetido.
- Usar modelos medianos/peque├▒os para tareas cerradas: generar payloads, clasificar interacciones, resumir registros, sugerir filtros y ejecutar specs existentes.
- Exigir salida JSON validada para cualquier tarea que impacte datos.
- Mantener fallback heur├¡stico local para operaciones cr├¡ticas de captura.

## Supuestos

- SQLite ser├í la memoria inicial por simplicidad, portabilidad y bajo costo operativo.
- Engram queda como opci├│n futura si aparece necesidad real de memoria sem├íntica o recuperaci├│n avanzada.
- NocoDB seguir├í siendo la fuente de verdad de datos de negocio.
- La herramienta debe priorizar consola e IA sobre UI web en la primera etapa.
- No se tocar├ín cambios locales existentes sin revisarlos antes, especialmente el cambio actual en interaction_crud.py.
