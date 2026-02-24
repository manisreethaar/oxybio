import glob

count = 0
for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'assets/css/styles.css?v=11\"' in content:
        content = content.replace('assets/css/styles.css?v=11\"', 'assets/css/styles.css?v=12\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    elif 'assets/css/styles.css?v=10\"' in content:
        content = content.replace('assets/css/styles.css?v=10\"', 'assets/css/styles.css?v=12\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Total HTML files updated to v12 cache bust: {count}")
