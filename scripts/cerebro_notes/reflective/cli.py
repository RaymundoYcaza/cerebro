from __future__ import annotations

import argparse
import sys
from pathlib import Path

from technical.config import load_config

from .pipeline import process_reflective_content


def read_input(args: argparse.Namespace) -> str:
    if args.stdin:
        return sys.stdin.read()

    if args.text:
        return args.text

    if args.input:
        return Path(args.input).read_text(encoding="utf-8")

    raise SystemExit("Debes usar --input, --stdin o --text.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Procesa un Spark en una sesión reflexiva guiada tipo LYT."
    )

    parser.add_argument("--config", default="config.yaml", help="Ruta a config.yaml.")
    parser.add_argument("--input", help="Archivo Markdown/texto a procesar.")
    parser.add_argument("--stdin", action="store_true", help="Leer contenido desde stdin.")
    parser.add_argument("--text", help="Texto directo a procesar.")
    parser.add_argument("--write", action="store_true", help="Escribir sesión reflexiva en output_dir.")
    parser.add_argument("--dry-run", action="store_true", help="Imprimir Markdown sin escribir archivo.")
    parser.add_argument("--think", action="store_true", help="Activar thinking en el modelo.")
    parser.add_argument("--nothink", action="store_true", help="Forzar thinking desactivado.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.think and args.nothink:
        raise SystemExit("Usa solo uno: --think o --nothink.")

    cfg = load_config(args.config)
    raw_content = read_input(args)

    think = None
    if args.think:
        think = True
    elif args.nothink:
        think = False

    result = process_reflective_content(
        raw_content,
        cfg,
        write=args.write,
        dry_run=args.dry_run,
        think=think,
    )

    if args.dry_run or not args.write:
        print(result.markdown)
        return

    print(f"OK: sesión reflexiva creada: {result.output_path}")
    print(f"Modelo usado: {result.model_used}")
    print(f"Tags: {', '.join(result.tags)}")


if __name__ == "__main__":
    main()
