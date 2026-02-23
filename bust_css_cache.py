import glob
import os

count = 0
for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to force the browser to load the new CSS
    if 'assets/css/styles.css\"' in content:
        content = content.replace('assets/css/styles.css\"', 'assets/css/styles.css?v=2\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Busted CSS cache injected to {file_path}")
        count += 1

print(f"Total HTML files updated: {count}")
