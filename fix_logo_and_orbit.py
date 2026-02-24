"""
LOGO + ORBIT ANIMATION FIX
===========================
1. Logo: Change to exactly  O₂  |  Bioinnovations  
   - "O₂" in bold sans, clean chemical notation
   - "|" thin vertical bar separator  
   - "Bioinnovations" light weight, tracking
   
2. Orbit: Move wrapper higher (negative margin-top), 
   make the animation smoother and more visually interesting
"""

import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

# ────────────────────────────────────────────────────────────────
# 1. CSS: replace the old .nav-logo block
# ────────────────────────────────────────────────────────────────
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

NEW_LOGO_CSS = """
/* ═══════════════════════════════════════════════════════
   NAV LOGO  —  O₂ | Bioinnovations
   ═══════════════════════════════════════════════════════ */
.nav-logo {
    display: inline-flex;
    align-items: center;
    gap: 0;
    text-decoration: none !important;
    line-height: 1;
    letter-spacing: 0;
}
.nav-logo:hover { text-decoration: none !important; }

/* "O₂" — bold, chemical monogram */
.logo-o2 {
    font-family: var(--font-sans);
    font-weight: 800;
    font-size: 1.1rem;
    color: var(--text-main);
    letter-spacing: -0.02em;
    display: inline-flex;
    align-items: baseline;
    gap: 0;
}
.logo-o2 sub {
    font-size: 0.6em;
    font-weight: 700;
    vertical-align: sub;
    font-family: var(--font-mono);
    letter-spacing: 0;
    margin-left: 0.05em;
}

/* Thin vertical separator */
.logo-pipe {
    display: inline-block;
    width: 1px;
    height: 16px;
    background: currentColor;
    opacity: 0.25;
    margin: 0 0.55rem;
    vertical-align: middle;
    transition: opacity 0.25s;
}

/* "Bioinnovations" — light, tracked */
.logo-bio {
    font-family: var(--font-sans);
    font-weight: 400;
    font-size: 1.1rem;
    letter-spacing: 0.04em;
    color: var(--text-main);
    opacity: 0.65;
    transition: opacity 0.25s;
}

/* Hover: bio wakes up, pipe solidifies */
.nav-logo:hover .logo-bio  { opacity: 1; }
.nav-logo:hover .logo-pipe { opacity: 0.6; }

@media (max-width: 768px) {
    .logo-o2  { font-size: 0.95rem; }
    .logo-bio { font-size: 0.95rem; }
    .logo-pipe { height: 13px; margin: 0 0.4rem; }
}
"""

# Remove old .nav-logo block if present, then append fresh one
css = re.sub(
    r'/\* ═+\s*PREMIUM LOGO.*?(?=\n/\*|\Z)',
    '',
    css,
    flags=re.DOTALL
)
css = re.sub(
    r'/\* ═+\s*NAV LOGO.*?(?=\n/\*|\Z)',
    '',
    css,
    flags=re.DOTALL
)
css += NEW_LOGO_CSS

# ────────────────────────────────────────────────────────────────
# 2. CSS: move the orbit animation wrapper higher and improve rings
# ────────────────────────────────────────────────────────────────
# Move wrapper up by adding a negative margin-top so it sits at header level
css = css.replace(
    '.hero-animation-wrapper {\n    position: relative;\n    width: 320px;\n    height: 320px;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    margin: 0 auto;\n}',
    '.hero-animation-wrapper {\n    position: relative;\n    width: 340px;\n    height: 340px;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    margin: -60px auto 0;\n}'
)

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)
print('[CSS] Logo and orbit animation updated')

# ────────────────────────────────────────────────────────────────
# 3. HTML: replace all logo instances to new clean format
# ────────────────────────────────────────────────────────────────
NEW_LOGO_HTML = '<a href="index.html" class="nav-logo"><span class="logo-o2">O<sub>2</sub></span><span class="logo-pipe"></span><span class="logo-bio">Bioinnovations</span></a>'

all_pages = [f for f in os.listdir(ROOT) if f.endswith('.html')]
replaced = 0

for page in all_pages:
    path = os.path.join(ROOT, page)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html

    # Replace any existing .nav-logo anchor tag (multiline safe)
    html = re.sub(
        r'<a href="index\.html" class="nav-logo"[^>]*>[\s\S]*?</a>',
        NEW_LOGO_HTML,
        html
    )
    # Also catch old plain .logo fallback
    html = re.sub(
        r'<a href="index\.html" class="logo"[^>]*>[\s\S]*?</a>',
        NEW_LOGO_HTML,
        html
    )
    # Cache bust
    html = re.sub(r'\?v=\d+"', '?v=36"', html)

    if html != original:
        replaced += 1
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f'[HTML] Logo replaced in {replaced} pages, cache v36')
print('[DONE]')
