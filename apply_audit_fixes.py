import re
import glob

# =========================================================
# FIX 1 — ingredients.html: Duplicate style attr + content
# =========================================================
with open('ingredients.html', 'r', encoding='utf-8') as f:
    ing = f.read()

# Fix duplicate style attributes on all ingredient cards:
# Pattern: style="background:#111;...overflow:hidden;" class="premium-card-hover" style="word-break: break-word;"
# The second style attr is silently ignored — merge into first
ing = re.sub(
    r'(style="background:#111; border:1px solid #333; border-radius:12px; padding: clamp\(1\.25rem, 5vw, 2\.5rem\); position:relative; overflow:hidden;")\s*\n\s*class="premium-card-hover" style="word-break: break-word;"',
    r'style="background:#111; border:1px solid #333; border-radius:12px; padding: clamp(1.25rem, 5vw, 2.5rem); position:relative; overflow:hidden; word-break:break-word; overflow-wrap:break-word; min-width:0;"\n                            class="premium-card-hover"',
    ing
)

# Also handle variations with just a style on the same line
ing = ing.replace(
    'class="premium-card-hover" style="word-break: break-word;">',
    'class="premium-card-hover">'
)

# Fix Lion's Mane: "hot-water extraction (hot water + ethanol) of the fruiting body"
ing = ing.replace(
    'Currently testing hot-water extraction (hot water + ethanol) of the fruiting body.',
    'Currently testing hot-water extraction of the fruiting body (fruiting body hot-water protocol).'
)

# Fix Reishi: "triterpene standardization" → "beta-glucan standardization"
ing = ing.replace(
    'Testing triterpene standardization for immune system modulation. The hypothesis targets a restorative parasympathetic state without acting as a sedative.',
    'Investigating beta-glucan standardization for immunomodulatory activity. Published literature shows Ganoderma beta-glucans interact with macrophage and NK-cell pathways.'
)
# Fix Reishi standardization row: "≥2% Triterpenes" → "≥30% Beta-Glucan"
ing = ing.replace(
    '≥2%\r\n                                         Triterpenes',
    '≥30%\r\n                                         Beta-Glucan'
)
ing = ing.replace('≥2%\n                                         Triterpenes', '≥30%\n                                         Beta-Glucan')
# Handle any single-line variant
ing = ing.replace('≥2% Triterpenes', '≥30% Beta-Glucan')

with open('ingredients.html', 'w', encoding='utf-8') as f:
    f.write(ing)
print("ingredients.html fixed")

# =========================================================
# FIX 2 — careers.html: Nav CTA + mobile
# =========================================================
with open('careers.html', 'r', encoding='utf-8') as f:
    car = f.read()

# Fix "Follow Our R&D Journey" → "Follow the Build" in desktop nav btn
car = car.replace(
    '>Follow Our R&D Journey</a>',
    '>Follow the Build</a>'
)
# Also fix mobile menu CTA  
car = car.replace(
    '>Follow Our R\u0026D Journey</a>',
    '>Follow the Build</a>'
)

with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(car)
print("careers.html fixed")

# =========================================================
# FIX 3 — Global: overflow-x guard in CSS body rule
# =========================================================
with open('assets/css/styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Find the body rule and add overflow-x:hidden
old_body = 'body {\n    font-family: var(--font-sans);\n    background: var(--bg);\n    color: var(--text-main);\n}'
new_body = 'body {\n    font-family: var(--font-sans);\n    background: var(--bg);\n    color: var(--text-main);\n    overflow-x: hidden;\n}'
if new_body not in css:
    css = css.replace(old_body, new_body)

with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("styles.css: overflow-x:hidden added to body")

# =========================================================
# FIX 4 — Global: Fix remaining "Follow Our R&D Journey"
# =========================================================
for fname in glob.glob('*.html'):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    orig = html
    html = html.replace('>Follow Our R&D Journey</a>', '>Follow the Build</a>')
    html = html.replace('>Follow Our R\u0026D Journey</a>', '>Follow the Build</a>')
    if html != orig:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed nav CTA in: {fname}")

print("\nAll fixes complete.")
