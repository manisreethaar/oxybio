import os
import re

CSS_FILE = r'e:\OXYBIO\assets\css\styles.css'
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Hide .desktop-nav on mobile
media_query_str = '@media (max-width: 1024px) {\n    .desktop-nav, .custom-nav-replaced { display: none !important; }\n'
if '.desktop-nav' not in css:
    css += '\n' + media_query_str + '}\n'
elif media_query_str not in css:
    css += '\n' + media_query_str + '}\n'

# 2. Fix animation-play-state: paused
css = css.replace('animation-play-state: paused;', '/* animation-play-state: paused; */')

# 3. Add Ashwagandha mobile grid fix for padding issues
padding_fix = """
@media (max-width: 768px) {
    .mobile-no-border {
        padding-left: 0 !important;
        margin-left: 0 !important;
        border-left: none !important;
        border-top: 1px dashed #444 !important;
        padding-top: 2rem !important;
        margin-top: 2rem !important;
    }
}
"""
if 'mobile-no-border {' not in css:
    css += padding_fix

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# 4. Ingredients HTML - Categories tab row
ING_FILE = r'e:\OXYBIO\ingredients.html'
with open(ING_FILE, 'r', encoding='utf-8') as f:
    ing = f.read()

good_cats = """<div class="side-tab-container" style="margin-bottom:var(--space-md);">
            <div class="side-tab" style="background:transparent!important; border:none!important; padding-left:0!important; color:var(--text-muted)!important; pointer-events:none;">CATEGORIES:</div>
            <a href="#millet" class="side-tab" style="text-decoration:none; color:var(--text-main);">Millet Base</a>
            <a href="#mushroom" class="side-tab" style="text-decoration:none; color:var(--text-main);">Mushroom Complex</a>
            <a href="#adaptogens" class="side-tab" style="text-decoration:none; color:var(--text-main);">Adaptogens</a>
            <a href="#cognitive" class="side-tab" style="text-decoration:none; color:var(--text-main);">Cognitive Stack</a>
            <a href="#performance" class="side-tab" style="text-decoration:none; color:var(--text-main);">Performance Stack</a>
        </div>"""

# Replace the specific block
ing = re.sub(r'<div style="font-family:var\(--font-mono\)[^>]+>\s*<span>CATEGORIES:</span>[\s\S]*?</div>', good_cats, ing)

with open(ING_FILE, 'w', encoding='utf-8') as f:
    f.write(ing)

# 5. Global Cache Bust
for f_name in os.listdir(r'e:\OXYBIO'):
    if f_name.endswith('.html'):
        path = os.path.join(r'e:\OXYBIO', f_name)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            content = re.sub(r'\?v=\d+"', '?v=28"', content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print("UX layout glitches resolved, CSS patched, cache to 28.")
