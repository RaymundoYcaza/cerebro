import subprocess
import json
import os
import re
from scripts.core_config import QMD_INTERPRETER, QMD_JS_PATH, BASE_DIR

def qmd_search(query, collections=None, limit=7, intent=None):
    if not QMD_JS_PATH or not os.path.exists(QMD_JS_PATH):
        return []

    # Definimos la caché y la raíz de QMD
    cache_path = str(BASE_DIR / "qmd" / ".cache")
    qmd_root = str(BASE_DIR / "qmd")
    
    env = os.environ.copy()
    env["XDG_CACHE_HOME"] = cache_path
    
    # Comando: node qmd/dist/index.js query "docker" --json -C 7
    cmd = [QMD_INTERPRETER, QMD_JS_PATH, "query", query, "--json", "-C", str(limit)]
    
    if collections:
        for c in collections:
            cmd.extend(["-c", c])

    try:
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            env=env,
            cwd=qmd_root, # Ejecutar desde la raíz de qmd ayuda a resolver módulos
            shell=True    # Necesario en Windows para resolver 'node'
        )

        if not result.stdout.strip():
            if result.stderr:
                print(f"\n[DEBUG QMD]: {result.stderr}")
            return []

        # Limpiar salida y buscar el JSON (lista o objeto)
        json_match = re.search(r'[\[\{].*', result.stdout, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        
        return []
        
    except Exception as e:
        print(f"\n[ERROR BRIDGE]: {str(e)}")
        return []