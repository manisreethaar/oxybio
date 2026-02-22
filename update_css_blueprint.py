import os, re

css_path = r'e:\OXYBIO\assets\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

blueprint_css = """
/* ── UI/UX Premium Enhancements (Blueprint / Clinical Data) ──────────────── */
body {
    /* Subtle dot grid for the lab/clinical feel */
    background-image: radial-gradient(var(--border) 1px, transparent 1px);
    background-size: 24px 24px;
    background-color: var(--bg);
}

.clinical-container {
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    background: var(--bg);
}

.bento-cell {
    position: relative;
}

/* Coordinate markers for Bento Cells */
.bento-cell::before {
    content: '+' ;
    position: absolute;
    top: -4px;
    left: -4px;
    color: var(--text-muted);
    font-family: var(--font-mono);
    font-size: 10px;
    pointer-events: none;
}
.bento-cell::after {
    content: '+' ;
    position: absolute;
    bottom: -4px;
    right: -4px;
    color: var(--text-muted);
    font-family: var(--font-mono);
    font-size: 10px;
    pointer-events: none;
}

/* Data Journal Tables */
.data-journal-table {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--font-mono);
    font-size: var(--text-sm);
}

.data-journal-table th {
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    border-bottom: 2px solid var(--text-main);
    padding: 1.5rem 1rem;
    text-align: left;
}

.data-journal-table td {
    border-bottom: 1px solid var(--border);
    padding: 1.5rem 1rem;
    color: var(--text-main);
}

.data-journal-table tbody tr:hover {
    background: var(--bg-alt);
}
"""

if "clinical-container" not in css:
    css += '\n' + blueprint_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated styles.css with blueprint background and clinical styling.")
else:
    print("styles.css already has the blueprint specs.")

