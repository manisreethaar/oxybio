import glob, re

# Fix 1: Update all schema.org logo URLs from logo-dark.png to logo-full.png
# Fix 2: Check and update any meta descriptions with "No compromise"

html_files = glob.glob('e:/OXYBIO/*.html')
fixed_logo = 0
fixed_meta = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix schema logo
    content = content.replace(
        '"logo": "https://oxygenbioinnovations.com/assets/images/logo-dark.png"',
        '"logo": "https://oxygenbioinnovations.com/assets/images/logo-full.png"'
    )
    
    # Fix any meta descriptions with "No compromise"
    content = re.sub(
        r'(content="[^"]*?)No compromise\.?\s*([^"]*")',
        r'\1\2',
        content
    )
    # Clean up double spaces left behind
    content = re.sub(r'  +', ' ', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")

print("Done.")
