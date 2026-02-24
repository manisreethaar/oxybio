import glob

count = 0
for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'assets/css/styles.css?v=9\"' in content:
        content = content.replace('assets/css/styles.css?v=9\"', 'assets/css/styles.css?v=10\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    elif 'assets/css/styles.css?v=8\"' in content:
        content = content.replace('assets/css/styles.css?v=8\"', 'assets/css/styles.css?v=10\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Total HTML files updated to v10 cache bust: {count}")
