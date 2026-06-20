"""
Cache-bust all CSS/JS references: update v=42 to v=43 across all HTML files.
Also fix the homepage font loading (4 families -> 2 actually used).
"""
import os, re

BASE = r'e:\OXYBIO-WEBSITE'

html_files = [f for f in os.listdir(BASE) if f.endswith('.html') and not f.startswith('_')]

total_changes = 0

for filename in sorted(html_files):
    filepath = os.path.join(BASE, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # Update CSS/JS cache busters v=42 → v=43
    html = html.replace('styles.css?v=42', 'styles.css?v=43')
    html = html.replace('v2_premium.css?v=42', 'v2_premium.css?v=43')
    html = html.replace('main.js?v=42', 'main.js?v=43')

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        total_changes += 1
        print(f"Updated cache busters: {filename}")

print(f"\nTotal files updated: {total_changes}")

# ── Fix index.html font loading ──────────────────────────────────────────
index_path = os.path.join(BASE, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_font = '''    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@400;600;700;800;900&family=Quicksand:wght@500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap"
        rel="stylesheet">'''

new_font = '''    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@400;600;700;800;900&display=swap"
        rel="stylesheet">'''

if old_font in html:
    html = html.replace(old_font, new_font)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("\nFixed index.html font loading (removed unused Quicksand + Space Mono fonts)")
else:
    print("\nFont link not found exactly - no changes made to font loading")
