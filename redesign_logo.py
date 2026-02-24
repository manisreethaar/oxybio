"""
REDESIGN THE NAVIGATION LOGO TEXT
=================================
Goal: Make "Oxygen Bioinnovations" outstanding and unique.

Design concept: "Scientific Split Typography"
- "O₂" rendered as a chemical formula monogram (tight, bold, uppercase)
- "XYGEN" completes the word in tracked uppercase 
- A thin vertical divider line
- "bioinnovations" in lowercase serif italic — editorial contrast

This creates a split between the hard science (O₂XYGEN) and the 
organic/living side (bioinnovations) — perfectly expressing the brand.
"""
import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

# ─── 1. Add premium logo CSS ─────────────────────────────────
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

logo_css = """
/* ═══════════════════════════════════════════════════════
   PREMIUM LOGO TYPOGRAPHY
   ═══════════════════════════════════════════════════════ */
.nav-logo {
    display: inline-flex;
    align-items: center;
    gap: 0;
    text-decoration: none !important;
    line-height: 1;
}

.nav-logo:hover {
    text-decoration: none !important;
}

/* "O" with subscript "2" — chemical formula style */
.logo-monogram {
    font-family: var(--font-serif);
    font-weight: 900;
    font-size: 1.4rem;
    color: var(--text-main);
    letter-spacing: -0.03em;
    line-height: 1;
}

.logo-monogram sub {
    font-size: 0.6em;
    font-weight: 700;
    vertical-align: baseline;
    position: relative;
    bottom: -0.15em;
    margin-left: -0.05em;
    font-family: var(--font-mono);
}

/* "XYGEN" completing the word — tracked uppercase */
.logo-word {
    font-family: var(--font-serif);
    font-weight: 900;
    font-size: 1.4rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-main);
    line-height: 1;
}

/* Thin vertical divider */
.logo-divider {
    width: 1px;
    height: 18px;
    background: var(--border);
    margin: 0 0.6rem;
    opacity: 0.6;
}

/* "bioinnovations" — lowercase serif italic, editorial contrast */
.logo-sub {
    font-family: var(--font-serif);
    font-weight: 400;
    font-style: italic;
    font-size: 0.85rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
    line-height: 1;
    text-transform: lowercase;
}

/* Hover: the muted part wakes up */
.nav-logo:hover .logo-sub {
    color: var(--text-main);
    transition: color 0.3s ease;
}

.nav-logo:hover .logo-divider {
    opacity: 1;
    background: var(--text-main);
    transition: opacity 0.3s ease, background 0.3s ease;
}

/* Mobile adjustments */
@media (max-width: 768px) {
    .logo-word, .logo-monogram {
        font-size: 1.15rem;
    }
    .logo-sub {
        font-size: 0.72rem;
    }
    .logo-divider {
        height: 14px;
        margin: 0 0.4rem;
    }
}
"""

if '.nav-logo' not in css:
    css += logo_css
    print('[CSS] Added premium logo typography styles')
else:
    print('[CSS] Logo styles already exist, skipping')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# ─── 2. Replace the plain text logo in ALL HTML pages ─────────
OLD_LOGO = '<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen\n                Bioinnovations</a>'
OLD_LOGO_ALT = '<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen Bioinnovations</a>'

NEW_LOGO = '''<a href="index.html" class="nav-logo">
                <span class="logo-monogram">O<sub>2</sub></span><span class="logo-word">XYGEN</span>
                <span class="logo-divider"></span>
                <span class="logo-sub">bioinnovations</span>
            </a>'''

all_pages = [f for f in os.listdir(ROOT) if f.endswith('.html')]
replaced = 0

for page in all_pages:
    path = os.path.join(ROOT, page)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # Try multiple patterns since formatting may vary
    # Pattern 1: multiline with indentation
    html = re.sub(
        r'<a href="index\.html" class="logo"[^>]*>[\s]*Oxygen[\s]*Bioinnovations[\s]*</a>',
        NEW_LOGO,
        html
    )
    
    if html != original:
        replaced += 1
    
    # Cache bust
    html = re.sub(r'\?v=\d+"', '?v=35"', html)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f'[HTML] Replaced logo in {replaced} pages, cache bumped to v35')

# ─── 3. Also replace the mobile menu logo if it exists ────────
for page in all_pages:
    path = os.path.join(ROOT, page)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check for mobile menu header logo
    if 'mobile-menu-header' in html and 'class="logo"' in html:
        html = re.sub(
            r'<a href="index\.html" class="logo"[^>]*>[^<]*</a>',
            NEW_LOGO.replace('\n                ', '\n                    '),
            html
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print('[DONE] Premium logo deployed across all pages!')
