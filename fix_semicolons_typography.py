import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. Regex to fix missing semicolons:
# We want to find `var(--space-[a-z0-9]+)` followed by whitespace and a CSS property `[a-z-]+:`, or closing brace, etc
# If there is no semicolon between them, insert one.
# For example: `padding:var(--space-lg) display:flex;` -> `padding:var(--space-lg); display:flex;`
# Regex: (var\(--space-(?:xs|sm|md|lg|xl|2xl)\))\s+([a-zA-Z-]+:) -> Replace with \1; \2
pattern = re.compile(r'(var\(--space-(?:xs|sm|md|lg|xl|2xl)\))\s+([a-zA-Z-]+:)')

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply semicolon fix
    html = pattern.sub(r'\1; \2', html)
    
    # 2. Add padding-top to mobile overrides to definitively fix the header overlap
    # We will just inject a mobile-specific container margin to all hero flow-left wrappers.
    # No, better to just increase the padding-top inline if it's strictly the problem, but wait...
    # Unify Hero Font Size explicitly:
    # All `<h1 class="display" ...>...</h1>` should use `--text-6xl`.
    # Let's replace font-size:clamp(....) or font-size:... with font-size:var(--text-6xl)
    
    # For H1 displays:
    html = re.sub(
        r'(<h1 class="display"[^>]*style="[^"]*)font-size:[^;]+;',
        r'\1font-size:var(--text-6xl);',
        html
    )

    # 3. Bump cache
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=25"', html)
    html = re.sub(r'href="assets/css/v2_premium\.css\?v=\d+"', 'href="assets/css/v2_premium.css?v=25"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed CSS semicolons and unified H1 typography.")
