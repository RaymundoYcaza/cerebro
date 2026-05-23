Estamos trabajando en /mnt/c/cerebro.

Antes de modificar archivos ejecuta:

python3 scripts/harness/harness.py context
python3 scripts/harness/harness.py status
python3 scripts/harness/harness.py scan-repo

Reglas:

- Trabaja por fases pequeñas.
- Usa scripts bash temporales en /tmp.
- No hagas refactor masivo.
- No hagas push/merge/rebase automático.
- Toda funcionalidad nueva debe actualizar documentación humana.
- Después de cambios ejecuta:
  python3 scripts/harness/harness.py check
  python3 scripts/harness/harness.py scan-repo

Lee y ejecuta la spec:

specs/backlog/20260523_phase-4d-transactions-rollback.md

Primero presenta:

- plan
- archivos a tocar
- riesgos

Luego implementa solamente esa spec.
