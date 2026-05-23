# File Modification Rules

## Filosofía

Las modificaciones deben hacerse preferentemente mediante scripts bash temporales:

```text
/tmp/nombre_del_cambio.sh
```

Luego se ejecutan con:

```bash
bash /tmp/nombre_del_cambio.sh
```

## Regla

No pegar comandos largos directamente en Fish.

## Protegido por defecto

- `.git`
- `vault/raymundo_ideaverse`

## Editable por defecto

- `scripts/cerebro_notes`
- `scripts/harness`
- documentación del repo
