import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

# ─── FIX 1: Careers pull quote font too large on mobile ─────────
# The pull quote has `font-size: 1.5rem` which is large.
# Fix via CSS media query so desktop is unchanged.
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

careers_mobile_fix = """
/* Careers page: tighten the pull quote on mobile */
@media (max-width: 768px) {
    .careers-pull-quote {
        font-size: 1.1rem !important;
        line-height: 1.5 !important;
    }
}
"""
if 'careers-pull-quote' not in css:
    css += careers_mobile_fix
    print('[CSS] Added careers pull quote mobile override')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# ─── Also add class to the careers paragraph directly ────────────
careers_path = os.path.join(ROOT, 'careers.html')
with open(careers_path, 'r', encoding='utf-8') as f:
    careers = f.read()

# Add class to the pull quote paragraph
careers = careers.replace(
    'style="font-size:1.5rem; line-height:1.6; color:var(--text-main); margin-bottom:2rem; font-weight:500; letter-spacing:-0.01em;"',
    'class="careers-pull-quote" style="font-size:1.5rem; line-height:1.6; color:var(--text-main); margin-bottom:2rem; font-weight:500; letter-spacing:-0.01em;"'
)

# Cache bust
careers = re.sub(r'\?v=\d+"', '?v=33"', careers)
with open(careers_path, 'w', encoding='utf-8') as f:
    f.write(careers)
print('[HTML] Careers: pull quote class added + cache v33')

# ─── FIX 2: Ingredients category headers invisible (white on light bg) ─
# These headers sit between dark ingredient cards but on the
# LIGHT var(--bg-alt) outer section background.
# They need to be dark text, not white.
ing_path = os.path.join(ROOT, 'ingredients.html')
with open(ing_path, 'r', encoding='utf-8') as f:
    ing = f.read()

# The category header rows have this pattern — fix all 5 category h2s
# Pattern: h2 style with color:#fff that contains the category name
ing = re.sub(
    r'(<h2 style="font-family:var\(--font-serif\); font-size:2\.5rem; margin:0; )color:#fff;(")',
    r'\1color:var(--text-main);\2',
    ing
)

# Also fix the subtitle labels above each h2 (color:rgba(255,255,255,0.5))
ing = re.sub(
    r'color:rgba\(255,255,255,0\.5\);',
    'color:var(--text-muted);',
    ing
)

# Fix the large faded number (01, 02, 03) using color:var(--bg) that becomes invisible on light bg
# Change to var(--text-main) with low opacity instead
ing = re.sub(
    r'color:var\(--bg\); opacity:0\.2;',
    'color:var(--text-main); opacity:0.1;',
    ing
)

# Fix the separator border that uses rgba white (invisible on light bg)
ing = re.sub(
    r'border-bottom:1px solid rgba\(255,255,255,0\.1\);',
    'border-bottom:1px solid var(--border);',
    ing
)

# Cache bust
ing = re.sub(r'\?v=\d+"', '?v=33"', ing)
with open(ing_path, 'w', encoding='utf-8') as f:
    f.write(ing)
print('[HTML] Ingredients: category header colors fixed to dark text')

# ─── Cache bust remaining pages ──────────────────────────────────
for page in os.listdir(ROOT):
    if page.endswith('.html') and page not in ('careers.html', 'ingredients.html'):
        path = os.path.join(ROOT, page)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'\?v=\d+"', '?v=33"', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print('[DONE] All fixes applied. Cache v33.')
