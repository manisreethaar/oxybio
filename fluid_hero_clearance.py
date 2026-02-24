import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The universal scalable hero clearance
FLUID_HERO_PADDING = 'padding-top:clamp(120px, 15vh, 180px);'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # We previously forced padding-top:180px; in standardize_hero_spacing.py.
    # This proved too tall for mobile geometry, causing unpredictable native rendering.
    # We replace it with the fluid clamp.
    html = html.replace('padding-top:180px;', FLUID_HERO_PADDING)
    html = html.replace('padding-top:140px;', FLUID_HERO_PADDING)
    
    # Check for index.html edge case where it might have retained 140px if my previous script missed it.
    
    # 3. Bump cache
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=26"', html)
    html = re.sub(r'href="assets/css/v2_premium\.css\?v=\d+"', 'href="assets/css/v2_premium.css?v=26"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated Hero padding to clamp(120px, 15vh, 180px) on all pages.")
