import glob

html_files = glob.glob(r'e:\\OXYBIO\\*.html')

for filepath in html_files:
    content = None
    for enc in ['utf-8', 'windows-1252', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
            
    if not content: continue
    
    # EXACT string replacements for the stubborn remaining ? marks
    content = content.replace('?18K', '?18K')
    content = content.replace('?4.5 Lakh', '?4.5 Lakh')
    content = content.replace('(?350-500/serving)', '(?350-500/serving)')
    content = content.replace("content: '?';", "content: '?';")
    content = content.replace("via Email ?", "via Email ?")
    
    # Fix the footer flex alignment overriding text-align: center
    # Add 'justify-content: center;' to the inline style
    content = content.replace(
        'grid-column: 1 / -1;"', 
        'grid-column: 1 / -1; justify-content: center;"'
    )
    
    # Add one more cache bust for safety
    content = content.replace('logo-full.png?v=5', 'logo-full.png?v=6')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Symbols strictly replaced and flex alignment centered.")
