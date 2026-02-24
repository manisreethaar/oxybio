import glob
import os

count = 0
for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'assets/css/styles.css?v=4\"' in content:
        content = content.replace('assets/css/styles.css?v=4\"', 'assets/css/styles.css?v=5\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    elif 'assets/css/styles.css?v=3\"' in content:
        content = content.replace('assets/css/styles.css?v=3\"', 'assets/css/styles.css?v=5\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Total HTML files updated to v5 cache bust: {count}")
