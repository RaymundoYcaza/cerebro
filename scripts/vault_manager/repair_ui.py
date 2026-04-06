#!/usr/bin/env python3
"""
Interfaz gráfica para Vault Manager repair.

Combina search, filtro y confirmacion de cambios.
"""

import os
import sys
from pathlib import Path
from tkinter import Tk, Listbox, Entry, Button, Radiobutton, StringVar, Label, Toplevel, END
from typing import List, Dict, Tuple

from scripts.vault_manager.repair import detect_frontmatter, repair_action_apply  # mismo backend

VAULT_ROOT = Path("/mnt/disc-a00/Z01-DEVOPS/workspaces/personal/cerebro/vault/raymundo_ideaverse")
INBOX_DIR = VAULT_ROOT / "+"


class VaultManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vault Manager repair")

        # Filtro de entrada
        Label(root, text="Filtrar por nombre").pack()
        self.filter_entry = Entry(root)
        self.filter_entry.pack()

        # Listbox de archivos
        self.listbox = Listbox(root, width=80, height=20)
        self.listbox.pack()

        # Botones de acción
        self.apply_button = Button(root, text="Aplicar cambios", command=self.apply_selected)
        self.apply_button.pack()

        self.refresh_button = Button(root, text="Recargar", command=self.refresh_files)
        self.refresh_button.pack()

        # Variables de selección
        self.selected_file = None

        self.refresh_files()

    def refresh_files(self):
        self.listbox.delete(0, END)
        pattern = self.filter_entry.get()
        if pattern:
            pattern = "*" + pattern + "*"
        else:
            pattern = "*.md"

        matches = INBOX_DIR.glob(pattern)
        self.files = sorted(f for f in matches if f.is_file())
        for f in self.files:
            self.listbox.insert(END, f.name)

    def apply_selected(self):
        selection = self.listbox.curselection()
        if not selection:
            print("No file selected.")
            return
        idx = selection[0]
        file_path = self.files[idx]
        print(f"Reparando: {file_path}")
        repair_action_apply(file_path, dry_run=False)


if __name__ == "__main__":
    root = Tk()
    app = VaultManagerUI(root)
    root.mainloop()
