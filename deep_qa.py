import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')
JS_FILE = os.path.join(ROOT, 'assets', 'js', 'scripts.js')

print("="*50)
print("DEEP QA & CODE CLEANLINESS ANALYSIS")
print("="*50)

# 1. Analyze CSS for Empty Blocks and Duplicates
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

empty_blocks = re.findall(r'([^{]+)\{\s*\}', css)
if empty_blocks:
    print(f"[CSS] Found {len(empty_blocks)} empty CSS blocks (useless code).")
else:
    print("[CSS] No empty CSS blocks found.")

# Let's find duplicated properties in blocks
blocks = re.findall(r'([^{]+)\{([^}]+)\}', css)
duplicate_props = 0
for sel, rules in blocks:
    props = re.findall(r'([\w-]+)\s*:', rules)
    if len(props) != len(set(props)):
        duplicate_props += 1

print(f"[CSS] Found {duplicate_props} CSS blocks with duplicate properties.")

# 2. Analyze HTML for Empty Tags and Inline Styles
html_files = [f for f in os.listdir(ROOT) if f.endswith('.html')]
empty_divs = 0
console_logs = 0

for file in html_files:
    path = os.path.join(ROOT, file)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Empty tags like <div></div> or <span></span> (ignoring self-closing)
    empties = re.findall(r'<([a-z]+)[^>]*>\s*</\1>', html)
    # Filter out valid empties like <div class="spacer"></div>
    # Actually, let's just count purely empty <div></div>
    pure_empties = re.findall(r'<div>\s*</div>', html)
    empty_divs += len(pure_empties)

    # Inline scripts console.logs
    logs = re.findall(r'console\.log\(', html)
    if logs:
        console_logs += len(logs)
        print(f"[HTML] Found {len(logs)} console.log statements in {file}")

print(f"[HTML] Found {empty_divs} completely empty <div></div> tags across all pages.")

# 3. JS Analysis
if os.path.exists(JS_FILE):
    with open(JS_FILE, 'r', encoding='utf-8') as f:
        js = f.read()
    logs = re.findall(r'console\.log\(', js)
    if logs:
        console_logs += len(logs)
        print(f"[JS] Found {len(logs)} console.log statements in scripts.js")

print(f"[JS] Total console.log statements to clean: {console_logs}")

# 4. Find CSS classes truly unused
css_classes = set(re.findall(r'\.([a-zA-Z0-9_-]+)[ \n\{:,>]', css))
used_in_html = set()
used_in_js = set()

for file in html_files:
    with open(os.path.join(ROOT, file), 'r', encoding='utf-8') as f:
        html = f.read()
        for c in re.findall(r'class="([^"]+)"', html):
            used_in_html.update(c.split())
        for c in re.findall(r"classList\.(?:add|remove|toggle|contains)\(['\"]([^'\"]+)['\"]\)", html):
            used_in_js.add(c)

if os.path.exists(JS_FILE):
    for c in re.findall(r"classList\.(?:add|remove|toggle|contains)\(['\"]([^'\"]+)['\"]\)", js):
        used_in_js.add(c)
    # Also find jQuery or querySelector('.class')
    for c in re.findall(r"querySelector(?:All)?\(['\"]\.([^'\"]+)['\"]\)", js):
        used_in_js.add(c.split('.')[0]) # Simplified

true_unused = css_classes - used_in_html - used_in_js
# Exclude pseudo, generic
true_unused = {c for c in true_unused if not c in ['active', 'hover', 'focus', 'before', 'after', 'visible']}

print(f"\n[CSS] Found {len(true_unused)} truly dead CSS classes (not in HTML, not in JS classList).")
print("="*50)
