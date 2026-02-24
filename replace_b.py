import os
import re

html_files = [f for f in os.listdir('e:/OXYBIO') if f.endswith('.html')]

# The premium wave 'B' SVG
new_svg = '''<svg viewBox="0 0 100 140" class="logo-b-svg" style="height: 1.15em; width: auto; vertical-align: -16%; margin-top: -2px; margin-right: 0px; display: inline-block;" xmlns="http://www.w3.org/2000/svg">
<defs>
<clipPath id="custom-b-wave">
  <path d="M 25 0 C 55 0, 85 0, 85 30 C 85 50, 70 58, 55 60 C 85 62, 100 85, 95 115 C 90 140, 55 140, 25 140 C 10 140, 0 130, 0 115 L 0 25 C 0 10, 10 0, 25 0 Z M 40 28 C 25 28, 25 52, 40 52 C 55 52, 55 28, 40 28 Z" fill-rule="evenodd"/>
</clipPath>
</defs>
<g clip-path="url(#custom-b-wave)">
  <rect x="-10" y="-10" width="120" height="160" fill="#061B40"/>
  <path d="M -10 100 Q 30 70, 110 120 L 110 150 L -10 150 Z" fill="#1465AD"/>
  <path d="M -10 65 Q 40 45, 110 90 L 110 150 L -10 150 Z" fill="#1F8EC8"/>
  <path d="M -10 30 Q 50 10, 110 60 L 110 150 L -10 150 Z" fill="#2EBAED"/>
  <path d="M -10 -10 Q 60 -10, 110 30 L 110 0 L -10 0 Z" fill="#42D3FF"/>
</g>
</svg>'''

new_logo_html = f'<span class="logo-bio">{new_svg}ioinnovations</span>'

# Fix HTML files
for h in html_files:
    filepath = os.path.join('e:/OXYBIO', h)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace existing SVG or word
    content = re.sub(r'<span class="logo-bio">.*?ioinnovations</span>', new_logo_html, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# Fix React Navbar
navbar_path = r"e:\OXYBIO\src\components\layout\Navbar.tsx"
with open(navbar_path, 'r', encoding='utf-8') as file:
    nav_content = file.read()

# Replace the Quicksand B with the SVG
react_svg = '''<svg viewBox="0 0 100 140" className="inline-block" style={{ height: '1.2em', width: 'auto', verticalAlign: '-16%', marginTop: '-2px', marginRight: '0px' }} xmlns="http://www.w3.org/2000/svg">
<defs>
<clipPath id="custom-b-wave">
  <path d="M 25 0 C 55 0, 85 0, 85 30 C 85 50, 70 58, 55 60 C 85 62, 100 85, 95 115 C 90 140, 55 140, 25 140 C 10 140, 0 130, 0 115 L 0 25 C 0 10, 10 0, 25 0 Z M 40 28 C 25 28, 25 52, 40 52 C 55 52, 55 28, 40 28 Z" fillRule="evenodd"/>
</clipPath>
</defs>
<g clipPath="url(#custom-b-wave)">
  <rect x="-10" y="-10" width="120" height="160" fill="#0A1E4A"/>
  <path d="M -10 100 Q 30 70, 110 120 L 110 150 L -10 150 Z" fill="#1465AD"/>
  <path d="M -10 65 Q 40 45, 110 90 L 110 150 L -10 150 Z" fill="#1F8EC8"/>
  <path d="M -10 30 Q 50 10, 110 60 L 110 150 L -10 150 Z" fill="#2EBAED"/>
  <path d="M -10 -10 Q 60 -10, 110 30 L 110 0 L -10 0 Z" fill="#42D3FF"/>
</g>
</svg>'''

nav_content = re.sub(r'<span class="font-\[\'Quicksand\'\][^>]*>Bioinnovations</span>', 
                     f'<span className="font-[\'Quicksand\'] tracking-normal font-bold ml-1.5 opacity-90 pb-0.5 flex items-center">{react_svg}ioinnovations</span>', 
                     nav_content)

with open(navbar_path, 'w', encoding='utf-8') as file:
    file.write(nav_content)

print("Replacement complete.")
