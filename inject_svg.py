import os
import glob

svg_code = '''<svg viewBox="0 0 120 150" style="height:1.15em; width:auto; margin-top:-0.15em; margin-right:1px;" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <mask id="b-cutout">
            <rect width="120" height="150" fill="white" />
            <path d="M 5 105 A 35 35 0 0 0 50 145" stroke="black" stroke-width="8" stroke-linecap="round" fill="none" />
        </mask>
    </defs>
    <path mask="url(#b-cutout)" d="M 25 10 L 60 10 C 80 10, 95 20, 95 40 C 95 55, 80 65, 65 65 C 55 65, 50 60, 50 55 C 50 50, 55 48, 60 48 C 70 48, 70 30, 55 30 C 40 30, 35 45, 45 60 C 55 75, 65 75, 80 75 C 110 75, 120 110, 95 130 C 85 140, 65 140, 45 140 L 25 140 A 10 10 0 0 1 15 130 L 15 20 A 10 10 0 0 1 25 10 Z" />
</svg>ioinnovations'''

html_files = glob.glob('e:/OXYBIO/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace normal Bioinnovations text with SVG
    content = content.replace('<span class="logo-bio">Bioinnovations</span>', f'<span class="logo-bio" style="display:inline-flex; align-items:center;">{svg_code}</span>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully replaced custom B in HTML files.")
