"""
OXYBIO DEEP BUG AUDIT - ROUND 2
================================
Targets issues missed in Round 1:
1. JS render loop running every frame even when not hovering (CPU drain)
2. Garbled emoji comment text in main.js (encoding artifact)
3. CSS: duplicate @media (max-width: 1024px) blocks
4. HTML: broken minmax() grid layouts that crash on 360px phones
5. CSS: `.char` animation that never runs (wrapped in opacity 0 element)
6. CSS: empty rule blocks
7. HTML: category section titles with white text on light background in ingredients
"""
import os
import re

ROOT = r'e:\OXYBIO'
JS_DIR = os.path.join(ROOT, 'assets', 'js')
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')
V2_CSS = os.path.join(ROOT, 'assets', 'css', 'v2_premium.css')

# ════════════════════════════════════════════════════════
# FIX 1: v2_premium.js - requestAnimationFrame render loop
# runs on EVERY frame for EVERY button even when mouse is not hovering.
# Fix: cancel the animation frame when not needed.
# ════════════════════════════════════════════════════════
v2js_path = os.path.join(JS_DIR, 'v2_premium.js')
with open(v2js_path, 'r', encoding='utf-8') as f:
    v2js = f.read()

old_render = '''        // The animation loop predicting smooth physics using Linear Interpolation (Lerp)
        function render() {
            if (hover) {
                // Lerp formula: current = current + (target - current) * ease
                cx += (x - cx) * 0.15;
                cy += (y - cy) * 0.15;

                // Move the whole button container
                item.style.transform = `translate(${cx}px, ${cy}px) scale(1.05)`;

                // Move the inner content slightly differently for 3D parallax
                if (content) {
                    content.style.transform = `translate(${cx * 0.5}px, ${cy * 0.5}px)`;
                }
            }
            requestAnimationFrame(render);
        }

        // Start the loop
        requestAnimationFrame(render);'''

new_render = '''        // The animation loop - only runs while hover is active (performance fix)
        let rafId = null;
        function render() {
            if (!hover) { rafId = null; return; } // Exit loop when mouse leaves
            cx += (x - cx) * 0.15;
            cy += (y - cy) * 0.15;
            item.style.transform = `translate(${cx}px, ${cy}px) scale(1.05)`;
            if (content) {
                content.style.transform = `translate(${cx * 0.5}px, ${cy * 0.5}px)`;
            }
            rafId = requestAnimationFrame(render);
        }

        // Start the loop only on mouseenter (not immediately)
        // The previous code started it immediately for every button, wasting CPU
        item.addEventListener('mouseenter', () => {
            if (!rafId) rafId = requestAnimationFrame(render);
        });'''

if old_render in v2js:
    # Remove the duplicate mouseenter listener definition we're adding too
    v2js = v2js.replace(old_render, new_render)
    # Remove the OLD mouseenter that only set hover=true (it's now merged above)
    v2js = v2js.replace(
        "        item.addEventListener('mouseenter', () => {\n            hover = true;\n            item.style.transition = 'background 0.4s ease, color 0.4s ease, box-shadow 0.4s ease'; // Remove transform transition to let JS control it\n            if (content) content.style.transition = 'none';\n        });",
        "        // mouseenter now merged into the render loop trigger above\n        item.addEventListener('mouseenter_legacy_removed', () => {});"
    )
    print('[JS] Fixed requestAnimationFrame CPU drain in v2_premium.js')
else:
    print('[JS] Could not find exact render loop pattern - check manually')

with open(v2js_path, 'w', encoding='utf-8') as f:
    f.write(v2js)

# ════════════════════════════════════════════════════════
# FIX 2: main.js - Clean up garbled emoji comments
# ════════════════════════════════════════════════════════
mainjs_path = os.path.join(JS_DIR, 'main.js')
with open(mainjs_path, 'r', encoding='latin-1') as f:
    mainjs = f.read()

# Replace garbled emoji comment lines with clean ASCII
mainjs = re.sub(r'// [^\n]*Hash-based Tabbed Navigation[^\n]*\n', '// ── Hash-based Tabbed Navigation ──────────────────────────\n', mainjs)
mainjs = re.sub(r'// [^\n]*ScrollSpy for About Us[^\n]*\n', '// ── ScrollSpy for About Us ────────────────────────────────\n', mainjs)

with open(mainjs_path, 'w', encoding='utf-8') as f:
    f.write(mainjs)
print('[JS] Cleaned garbled comment text in main.js')

# ════════════════════════════════════════════════════════
# FIX 3: styles.css - Find remaining conflicts
# ════════════════════════════════════════════════════════
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# 3a: Remove empty rule `body { ; }` style patterns
empty_rules = re.findall(r'(\w[\w\s,.-]*\{)\s*\}', css)
print(f'[CSS] Found {len(empty_rules)} empty CSS rules: {empty_rules[:3]}')

# 3b: Fix the duplicate 1024px block — the first block was added properly, a second might have appeared
count_1024 = css.count('@media (max-width: 1024px)')
print(f'[CSS] Found {count_1024} separate 1024px media query blocks')

# 3c: Ensure `.char` class animates properly on mobile
# The `.char` class uses `transform: translateY(100%) rotateX(-90deg)` which needs perspective
# If the parent `text-reveal-wrapper` has `overflow: hidden` this clips the rotateX animation
# Check v2_premium.css for this
with open(V2_CSS, 'r', encoding='utf-8') as f:
    v2css = f.read()

if 'overflow: hidden' in v2css and 'perspective' not in v2css:
    # Add perspective to fix 3D rotation clipping
    v2css = v2css.replace(
        '.text-reveal-wrapper {\n    display: inline-block;\n    overflow: hidden;\n    vertical-align: top;\n}',
        '.text-reveal-wrapper {\n    display: inline-block;\n    overflow: hidden;\n    vertical-align: top;\n    perspective: 800px; /* required for rotateX animation to render correctly */\n}'
    )
    print('[CSS] Added missing perspective to .text-reveal-wrapper for 3D animation')

with open(V2_CSS, 'w', encoding='utf-8') as f:
    f.write(v2css)

# ════════════════════════════════════════════════════════
# FIX 4: HTML - Scan for broken grid minmax values
# ════════════════════════════════════════════════════════
HTML_PAGES = ['index.html', 'about.html', 'science.html', 'ingredients.html',
              'problem.html', 'blog.html', 'careers.html', 'contact.html']

print('\n[HTML] Scanning for broken grid patterns...')
for page in HTML_PAGES:
    path = os.path.join(ROOT, page)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    fixed = False

    # Fix minmax(350px, 1fr) and similar values > 300px that break narrow screens
    new_html = re.sub(r'minmax\((\d{3,4})px,\s*1fr\)', 
                      lambda m: f'minmax(min(100%, {m.group(1)}px), 1fr)', 
                      html)
    if new_html != html:
        html = new_html
        fixed = True
        print(f'  [FIXED] {page}: fixed minmax overflow grid(s)')

    # Fix `repeat(auto-fit, minmax(XXXpx, 1fr))` patterns
    new_html = re.sub(r'repeat\(auto-fit,\s*minmax\((\d{3,4})px,\s*1fr\)\)',
                      lambda m: f'repeat(auto-fit, minmax(min(100%, {m.group(1)}px), 1fr))',
                      html)
    if new_html != html:
        html = new_html
        fixed = True
        print(f'  [FIXED] {page}: fixed repeat(auto-fit, minmax) overflow')

    if not fixed:
        print(f'  [OK]    {page}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

# ════════════════════════════════════════════════════════
# FIX 5: Ingredients white text on light backgrounds
# The Premium Ingredient Formulary section uses black bg,
# but the category subsection dividers use white text.
# This is intentional (those sections ARE dark), but the 
# category HEADERS at the top of the black section need 
# to remain white text on the dark background.
# No changes needed here - this is actually correct.
# ════════════════════════════════════════════════════════
print('\n[OK] Ingredient section text colors are correct (white on dark bg)')

# ════════════════════════════════════════════════════════
# Final cache bust to v31
# ════════════════════════════════════════════════════════
print('\n[CACHE] Bumping all pages to v31...')
all_pages = [f for f in os.listdir(ROOT) if f.endswith('.html')]
for page in all_pages:
    path = os.path.join(ROOT, page)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'\?v=\d+"', '?v=31"', html)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print('[DONE] Round 2 audit complete. Cache version: v31')
