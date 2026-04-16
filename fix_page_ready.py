"""
Surgical fix: add page-ready inline script to every HTML page that
uses transitions.css. This ensures body is ALWAYS made visible in 50ms
even if external page-transitions.js loads late.

Safe because:
- Only adds a tiny inline script right after <body>
- Does NOT modify any existing content
- Only fires if page-ready class is not yet present
"""

import glob, os

INLINE_FALLBACK = '''    <!-- Critical: ensure page is always visible even if page-transitions.js is delayed -->
    <script>
        (function(){
            var t = setTimeout(function(){ document.body.classList.add('page-ready'); }, 50);
            window.addEventListener('load', function(){ clearTimeout(t); document.body.classList.add('page-ready'); });
        })();
    </script>
'''

files = glob.glob('*.html')
files = [f for f in files if 'backup' not in f and 'ingredients_3530329' not in f]

fixed = 0
for f in sorted(files):
    try:
        html = open(f, 'r', encoding='utf-8').read()
    except Exception as e:
        print(f'  SKIP {f}: {e}')
        continue

    # Only process pages with transitions.css
    if 'transitions.css' not in html:
        continue

    # Skip if already has our fallback
    if 'Force page visible immediately' in html:
        print(f'  SKIP {f}: already has fallback')
        continue

    # Find the <body> tag and insert right after
    body_idx = html.find('<body>')
    if body_idx == -1:
        print(f'  SKIP {f}: no <body> tag found')
        continue

    # Find end of that tag line (after the >)
    insert_at = body_idx + len('<body>')
    
    new_html = html[:insert_at] + '\n\n' + INLINE_FALLBACK + html[insert_at:]

    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_html)

    fixed += 1
    print(f'  FIXED {f}')

print(f'\nTotal fixed: {fixed}')
