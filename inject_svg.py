import glob, re

# Clean monochrome SVG B using currentColor so it inherits whatever color the parent text has
SVG_B = '''<svg viewBox="0 0 100 140" class="logo-b-svg" style="height:1.15em;width:auto;vertical-align:-16%;display:inline-block;margin-right:0;" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" d="M 25 0 C 55 0, 85 0, 85 30 C 85 50, 70 58, 55 60 C 85 62, 100 85, 95 115 C 90 140, 55 140, 25 140 C 10 140, 0 130, 0 115 L 0 25 C 0 10, 10 0, 25 0 Z M 40 28 C 25 28, 25 52, 40 52 C 55 52, 55 28, 40 28 Z"/>
</svg>ioinnovations'''

html_files = glob.glob('e:/OXYBIO/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the whole logo-bio span contents (between the tags) with clean version
    content = re.sub(
        r'<span class="logo-bio"[^>]*>.*?</span>',
        f'<span class="logo-bio" style="display:inline-flex;align-items:center;">{SVG_B}</span>',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed {len(html_files)} HTML files.")
