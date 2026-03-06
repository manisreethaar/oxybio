import glob
import os
import re

html_files = glob.glob(r'e:\OXYBIO\*.html')

for filepath in html_files:
    content = None
    for enc in ['utf-8', 'windows-1252', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
            
    if content is None:
        continue

    # Update logo in header nav (find <a href="index.html" class="nav-logo">...</a>)
    # Replaces the old single image with flex container holding image + text
    header_pattern = re.compile(r'<a href="index\.html" class="nav-logo">\s*<img src="assets/images/logo-full\.png\?v=3" alt="Oxygen\s*Bioinnovations"\s*style="height:36px; width:auto; display:block;">\s*</a>')
    
    header_replacement = '''<a href="index.html" class="nav-logo" style="display:flex; align-items:center; gap:10px; text-decoration:none;">
                <img src="assets/images/logo-full.png?v=3" alt="Oxygen Bioinnovations Logo" style="height:36px; width:auto; display:block;">
                <span style="font-family: var(--font-heading, ''Inter'', sans-serif); font-weight: 800; font-size: 1.25rem; color: var(--text-main, #0B192C); letter-spacing: -0.02em;">Oxygen <span style="color:#0D8A74;">Bioinnovations</span></span>
            </a>'''
            
    content = header_pattern.sub(header_replacement, content)
    
    # Update logo in footer
    footer_pattern = re.compile(r'<a href="index\.html" style="display:inline-block; margin-bottom:1rem;">\s*<img\s*src="assets/images/logo-full\.png\?v=3" alt="Oxygen Bioinnovations"\s*style="height:36px; width:auto; display:block;">\s*</a>')
    
    footer_replacement = '''<a href="index.html" style="display:flex; align-items:center; gap:10px; margin-bottom:1.5rem; text-decoration:none;">
                    <img src="assets/images/logo-full.png?v=3" alt="Oxygen Bioinnovations Logo" style="height:36px; width:auto; display:block;">
                    <span style="font-family: var(--font-heading, ''Inter'', sans-serif); font-weight: 800; font-size: 1.25rem; color: var(--text-main, #0B192C); letter-spacing: -0.02em;">Oxygen <span style="color:#0D8A74;">Bioinnovations</span></span>
                </a>'''
                
    content = footer_pattern.sub(footer_replacement, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML logo texts updated.")
