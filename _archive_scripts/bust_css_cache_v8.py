import glob

count = 0
for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'assets/css/styles.css?v=7\"' in content:
        content = content.replace('assets/css/styles.css?v=7\"', 'assets/css/styles.css?v=8\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    elif 'assets/css/styles.css?v=6\"' in content:
        content = content.replace('assets/css/styles.css?v=6\"', 'assets/css/styles.css?v=8\"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Total HTML files updated to v8 cache bust: {count}")
