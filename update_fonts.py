import os, glob, re

root_dir = r'e:\OXYBIO'
html_files = glob.glob(os.path.join(root_dir, '*.html'))

# Old font URL
old_fonts = r'<link[^>]*href="https://fonts.googleapis.com/css2\?family=Playfair\+Display:ital,wght@0,700;0,800;0,900;1,700;1,800&family=Plus\+Jakarta\+Sans:wght@300;400;500;600;700&display=swap"[^>]*>'

# New font URLs (Outfit, Inter, Space Mono)
new_fonts = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@400;600;700;800;900&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace fonts
    updated = re.sub(old_fonts, new_fonts, content, flags=re.IGNORECASE)
    
    if updated != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated fonts in {os.path.basename(file)}")

print("Done linking new fonts.")
