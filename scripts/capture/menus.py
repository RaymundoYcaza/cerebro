import shutil
import subprocess
import sys
from datetime import date


def _tty():
    try:
        return open("/dev/tty", "r+b", buffering=0)
    except OSError:
        return None


def gum_available() -> bool:
    return shutil.which("gum") is not None


def _gum(*args: str, input_text: str | None = None) -> tuple[int, str]:
    tty = _tty()
    try:
        result = subprocess.run(
            ["gum", *args],
            input=input_text.encode() if input_text is not None else None,
            stdin=None if input_text is not None else (tty or sys.stdin),
            stdout=subprocess.PIPE,
            stderr=tty or sys.stderr,
            text=False,
        )
        stdout = result.stdout.decode("utf-8", errors="replace").strip()
        return result.returncode, stdout
    except (OSError, KeyboardInterrupt):
        return 130, ""
    finally:
        if tty:
            tty.close()


def ask_text(prompt_text: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt_text}{suffix}: ").strip()
    return value if value else default


def choose_one(header: str, options: list[str], default: str | None = None) -> str:
    if gum_available():
        code, choice = _gum("choose", "--header", header, *options)
        if code in (1, 130):
            return ""
        return choice

    for i, option in enumerate(options, start=1):
        marker = " (por defecto)" if default and option == default else ""
        print(f"{i}. {option}{marker}")

    raw = input(f"Selecciona opción [{default or '1'}]: ").strip()
    if raw == "":
        return default or options[0]
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(options):
            return options[idx]
        return ""
    if raw in options:
        return raw
    return ""


def filter_one(options: list[str], placeholder: str, header: str | None = None) -> str:
    if not options:
        return ""

    if gum_available():
        args = ["filter", "--placeholder", placeholder]
        if header:
            args.extend(["--header", header])
        code, choice = _gum(*args, input_text="\n".join(options))
        if code in (1, 130):
            return ""
        return choice

    if header:
        print(header)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    raw = input("Selecciona ID: ").strip()
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(options):
            return options[idx]
    return ""


def confirm(message: str, default: bool = False) -> bool:
    if gum_available():
        code, _ = _gum("confirm", message)
        return code == 0

    fallback = "s" if default else "n"
    raw = ask_text(f"{message} (s/n)", fallback).lower()
    return raw in ("s", "si", "sí", "y", "yes")


def validate_iso_date(value: str, field_name: str) -> str:
    if not value:
        return ""
    try:
        date.fromisoformat(value)
        return value
    except ValueError:
        raise ValueError(f"{field_name} debe tener formato YYYY-MM-DD")


def ask_date(prompt_text: str, default: str = "", field_name: str = "fecha") -> str:
    value = ask_text(prompt_text, default)
    return validate_iso_date(value, field_name)


def pager(content: str, header: str | None = None) -> None:
    if gum_available():
        body = content if not header else f"{header}\n\n{content}"
        tty = _tty()
        try:
            subprocess.run(
                ["gum", "pager"],
                input=body.encode(),
                stdout=tty or sys.stdout,
                stderr=tty or sys.stderr,
                text=False,
            )
        except (OSError, KeyboardInterrupt):
            return
        finally:
            if tty:
                tty.close()
        return

    if header:
        print(header)
        print()
    print(content)
    input("\nPresiona Enter para continuar...")
