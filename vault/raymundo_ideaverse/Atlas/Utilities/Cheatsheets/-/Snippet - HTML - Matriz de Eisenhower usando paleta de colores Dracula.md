---
up:
  - "[[Snippets]]"
related: 
created: 2025-05-23
---

 
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caja de Eisenhower - Dracula</title>
    <style>
        :root {
            --dracula-bg: #282a36;
            --dracula-current-line: #44475a;
            --dracula-foreground: #f8f8f2;
            --dracula-green: #50fa7b;
            --dracula-yellow: #f1fa8c;
            --dracula-orange: #ffb86c;
            --dracula-red: #ff5555;
            --dracula-purple: #bd93f9;
        }

        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: var(--dracula-bg);
            color: var(--dracula-foreground);
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .matrix-container {
            display: grid;
            grid-template-columns: auto 1fr 1fr;
            grid-template-rows: auto 1fr 1fr;
            gap: 10px;
            max-width: 1200px;
            width: 100%;
            aspect-ratio: 1.5;
        }

        .header {
            background-color: var(--dracula-purple);
            color: var(--dracula-bg);
            padding: 1rem;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.8rem;
            font-weight: bold;
        }

        .quadrant {
            padding: 2rem;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 1.4rem;
            transition: transform 0.3s ease;
        }

        .quadrant:hover {
            transform: scale(1.02);
        }

        .row-label {
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            background-color: var(--dracula-current-line);
            padding: 1.5rem;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            font-weight: bold;
        }

        .do { background-color: var(--dracula-green); color: var(--dracula-bg); }
        .plan { background-color: var(--dracula-yellow); color: var(--dracula-bg); }
        .delegate { background-color: var(--dracula-orange); color: var(--dracula-bg); }
        .eliminate { background-color: var(--dracula-red); color: var(--dracula-foreground); }

        .quadrant-title {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            font-weight: bold;
        }

        .quadrant-content {
            line-height: 1.5;
        }

        /* Posicionamiento grid */
        .header-urgente { grid-area: 1 / 2; }
        .header-no-urgente { grid-area: 1 / 3; }
        .row-importante { grid-area: 2 / 1; }
        .row-no-importante { grid-area: 3 / 1; }
        .do { grid-area: 2 / 2; }
        .plan { grid-area: 2 / 3; }
        .delegate { grid-area: 3 / 2; }
        .eliminate { grid-area: 3 / 3; }
    </style>
</head>
<body>
    <div class="matrix-container">
        <div class="header header-urgente">URGENTE</div>
        <div class="header header-no-urgente">NO URGENTE</div>
        
        <div class="row-label row-importante">IMPORTANTE</div>
        <div class="row-label row-no-importante">NO IMPORTANTE</div>

        <div class="quadrant do">
            <div class="quadrant-title">✅ HACER</div>
            <div class="quadrant-content">Tareas importantes<br>y urgentes</div>
        </div>
        
        <div class="quadrant plan">
            <div class="quadrant-title">📅 PLANIFICAR</div>
            <div class="quadrant-content">Tareas importantes<br>pero no urgentes</div>
        </div>
        
        <div class="quadrant delegate">
            <div class="quadrant-title">📤 DELEGAR</div>
            <div class="quadrant-content">Tareas urgentes<br>pero no importantes</div>
        </div>
        
        <div class="quadrant eliminate">
            <div class="quadrant-title">❌ NO HACER</div>
            <div class="quadrant-content">Tareas no urgentes<br>y no importantes</div>
        </div>
    </div>
</body>
</html>
```