import os
import re

css_path = r'e:\OXYBIO\assets\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    'section.structure-section[style*="padding-top"] { \n        padding-top: 5rem !important; \n        padding-bottom: 4rem !important; \n    }',
    'section.structure-section[style*="padding-top"] { \n        /* REMOVED: padding-top: 5rem !important; (Was clipping badges) */ \n        padding-bottom: 4rem !important; \n    }'
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

ing_path = r'e:\OXYBIO\ingredients.html'
with open(ing_path, 'r', encoding='utf-8') as f:
    ing = f.read()

# Fix light mode text colors in categories
ing = re.sub(r'border-bottom:1px solid rgba\(255,255,255,0\.1\);', 'border-bottom:1px solid var(--border);', ing)
ing = re.sub(r'color:var\(--bg\);\s*opacity:0\.2;', 'color:var(--text-main); opacity:0.1;', ing)
ing = re.sub(r'color:rgba\(255,255,255,0\.5\);', 'color:var(--text-muted);', ing)
ing = re.sub(r'color:#fff;(.*?>Millet Matrix|.*?>Fungi Intelligence|.*?>Adaptogen Protocol|.*?>Cognitive Stack|.*?>Performance Stack)', lambda m: 'color:var(--text-main);' + m.group(1), ing)

# Make sure grid minmax doesn't cause overflow on tiny phones
ing = ing.replace('minmax(350px, 1fr)', 'minmax(min(100%, 300px), 1fr)')
ing = ing.replace('minmax(320px, 1fr)', 'minmax(min(100%, 300px), 1fr)')

# Cache bust
for f_name in os.listdir(r'e:\OXYBIO'):
    if f_name.endswith('.html'):
        path = os.path.join(r'e:\OXYBIO', f_name)
        with open(path, 'r', encoding='utf-8') as f_h:
            content = f_h.read()
            content = re.sub(r'\?v=\d+"', '?v=29"', content)
        with open(path, 'w', encoding='utf-8') as f_h:
            f_h.write(content)

print("Applied padding unlock and text color refactoring.")
