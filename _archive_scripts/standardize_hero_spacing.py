import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We want all interior pages to use a standardized hero spacing to avoid the "jumping" effect between pages
# We will define a standard padding-top. About 180px looks premium and clears the mobile header well.
STANDARD_HERO_PADDING = 'padding-top:180px;'

for filename in html_files:
    if filename == 'index.html':
        continue # index has a unique fullscreen video hero, usually handled differently. Let's check it later if needed.
        
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace various padding-top values on the first section
    # Many use style="padding-top:140px;..." or style="padding-top:clamp(140px, 15vh, 180px);..."
    
    # Regex to find the first instance of padding-top inside a style tag on a section
    # Let's be more specific. We want to target the first structure-section's padding.
    
    html = re.sub(r'style="padding-top:140px;', f'style="{STANDARD_HERO_PADDING}', html)
    html = re.sub(r'style="padding-top:200px;', f'style="{STANDARD_HERO_PADDING}', html)
    html = re.sub(r'style="padding-top:clamp\(140px,\s*15vh,\s*180px\);', f'style="{STANDARD_HERO_PADDING}', html)
    html = re.sub(r'style="padding-top:160px;', f'style="{STANDARD_HERO_PADDING}', html)
    
    # Ensure cache bust
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=19"', html)
    html = re.sub(r'href="assets/css/v2_premium\.css\?v=\d+"', 'href="assets/css/v2_premium.css?v=19"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print('Standardized Global Hero Spacing to 180px.')
