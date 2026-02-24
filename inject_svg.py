import glob, re

# The SVG is in assets/images/logo-b.svg — use it as an <img> tag
# For CSS color inheritance we use a filter trick or just keep it black (it's monochrome anyway)
LOGO_B_TAG = '<img src="assets/images/logo-b.svg" class="logo-b-img" style="height:1.1em;width:auto;display:inline-block;vertical-align:-17%;margin-right:0;" alt="B">'

html_files = glob.glob('e:/OXYBIO/*.html')
for filepath in html_files:
    if 'test_b' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace whole logo-bio span  
    content = re.sub(
        r'<span class="logo-bio"[^>]*>.*?</span>',
        f'<span class="logo-bio" style="display:inline-flex;align-items:center;">{LOGO_B_TAG}ioinnovations</span>',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files.")
