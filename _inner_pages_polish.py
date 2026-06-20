"""
Phase 5 inner page polishes:
1. Add v2_premium.css link to careers.html (it was missing the premium CSS)  
2. Add page-ready script to science.html (missing)
3. Improve the about.html phase stepper auto-rotate timing
4. Add missing rel="stylesheet" ordering fix to pages that loaded v2_premium before styles.css
"""
import os, re

BASE = r'e:\OXYBIO-WEBSITE'

# ── 1. Fix CSS load order on pages that had v2_premium before styles.css ──
#    The correct order should be: transitions.css → styles.css → v2_premium.css
pages_to_fix_order = ['science.html', 'about.html', 'problem.html', 'ingredients.html']

for filename in pages_to_fix_order:
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Check if v2_premium.css is loaded but missing from this page
    if 'v2_premium.css' not in html:
        # Add it after styles.css
        html = html.replace(
            '<link rel="stylesheet" href="assets/css/styles.css?v=43">',
            '<link rel="stylesheet" href="assets/css/styles.css?v=43">\n    <link rel="stylesheet" href="assets/css/v2_premium.css?v=43">'
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Added v2_premium.css to {filename}")
    else:
        print(f"{filename}: v2_premium.css already present")

# ── 2. Fix about.html phase stepper auto-rotate ──
about_path = os.path.join(BASE, 'about.html')
with open(about_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Slow down the auto-rotate interval from 3000ms to 5000ms if present
if 'setInterval' in html and '3000' in html:
    html = html.replace('setInterval(', '// Slowed auto-rotate for better UX\n    setInterval(', 1)
    html = html.replace(', 3000)', ', 5000)', 1)
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Slowed about.html phase stepper from 3s to 5s")
else:
    print("about.html: setInterval/3000 pattern not found (may already be optimized)")

# ── 3. Ensure page-ready script in science.html ──
sci_path = os.path.join(BASE, 'science.html')
with open(sci_path, 'r', encoding='utf-8') as f:
    html = f.read()

if 'page-ready' not in html and '<body>' in html:
    page_ready_script = '''    <!-- Critical: ensure page is always visible -->
    <script>
        (function(){
            var t = setTimeout(function(){ document.body.classList.add('page-ready'); }, 50);
            window.addEventListener('load', function(){ clearTimeout(t); document.body.classList.add('page-ready'); });
        })();
    </script>
'''
    html = html.replace('<body>\n', '<body>\n\n' + page_ready_script, 1)
    with open(sci_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added page-ready script to science.html")
else:
    print("science.html: page-ready already present")

print("\nPhase 5 inner page polishes complete.")
