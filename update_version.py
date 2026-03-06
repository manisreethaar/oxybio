import glob
import os

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
            
    if content:
        content = content.replace('logo-full.png?v=3', 'logo-full.png?v=4')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated logo version to ?v=4.")
