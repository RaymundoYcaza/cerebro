import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# --- RUTAS DE IDENTIDAD ---
# BASE_DIR es la carpeta "CerebroPortable"
BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta de la Bóveda de Obsidian (Prioridad 1: .env, Prioridad 2: Ruta hardcoded)
env_vault = os.getenv("VAULT_PATH")
if env_vault:
    VAULT_PATH = Path(env_vault)
else:
    VAULT_PATH = Path("X:\P01_RY-PERSONAL\cerebro\vault\raymundo_ideaverse")

# Localización de QMD (Basado en tu confirmación: qmd/dist/index.js)
QMD_INTERPRETER = "node"
QMD_JS_PATH = str(BASE_DIR / "qmd" / "dist" / "index.js")

# --- CONFIGURACIÓN DE QMD ---
DEFAULT_COLLECTIONS = ["dots", "sources"]

# --- LLM PARA RAZONAMIENTO ---
MODEL_REASONING = os.getenv("MODEL", "gemma3:4b")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

# --- RUTAS DE SALIDA ---
# Ahora usamos VAULT_PATH con seguridad
LOGS_GAPS_PATH = VAULT_PATH / "Atlas/Utilities/LogsGaps"
BORRADORES_PATH = VAULT_PATH / "Efforts/Borradores/Blog"

# Verificación de integridad al iniciar
if not os.path.exists(QMD_JS_PATH):
    print(f"⚠️ ERROR CRÍTICO: No se halló el archivo en {QMD_JS_PATH}")