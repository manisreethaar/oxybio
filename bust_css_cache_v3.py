import glob
import os

count = 0
for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'assets/css/styles.css?v=2\"' in content:
        content = content.replace('assets/css/styles.css?v=2\"', 'assets/css/styles.css?v=3\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    elif 'assets/css/styles.css\"' in content:
        content = content.replace('assets/css/styles.css\"', 'assets/css/styles.css?v=3\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Total HTML files updated to v3 cache bust: {count}")
