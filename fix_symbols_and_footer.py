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
            
    if not content:
        continue

    # 1. Fix footer alignment
    # We replace `<div class="footer-bottom" style="... ">` to include grid-column: 1 / -1;
    # Or just replace the style completely
    content = re.sub(
        r'<div class="footer-bottom"\s+style="([^"]+)"',
        lambda m: f'<div class="footer-bottom" style="{m.group(1)} grid-column: 1 / -1;"' 
                  if 'grid-column' not in m.group(1) else m.group(0),
        content
    )

    # 2. Fix stray '?' in careers and problem pages
    # Instead of exact string matches, we use regex to allow formatting/newlines
    content = re.sub(r'\?18K\s*[-–]\s*25K/mo', '₹18K – 25K/mo', content)
    content = re.sub(r'via Email \?', 'via Email →', content)
    content = re.sub(r'content:\s*\'\?\';', "content: '→';", content)
    
    # problem.html fixes
    content = re.sub(r'\?4\.5 Lakh\s*Crore', '₹4.5 Lakh Crore', content)
    content = re.sub(r'\(\?350-500/serving\)', '(₹350-500/serving)', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Alignment and regex symbol fixes applied successfully.")
