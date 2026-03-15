import os, re

html_files = [f for f in os.listdir(r'e:\OXYBIO') if f.endswith('.html') and f != 'index-single.html']
fixed = 0

TRANS_LINK = 'href="assets/css/transitions.css"'

for fname in sorted(html_files):
    fpath = os.path.join(r'e:\OXYBIO', fname)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    
    # Find and remove the existing transitions.css link tag (whatever form it is in)
    content_without = re.sub(r'[ \t]*<link[^>]+transitions\.css[^>]*>\n?', '', content)
    
    # Find the first styles.css link tag
    styles_match = re.search(r'(<link[^>]+styles\.css[^>]*>)', content_without)
    if styles_match:
        insert_pos = styles_match.start()
        trans_tag = '    <link rel="stylesheet" href="assets/css/transitions.css">\n'
        content_fixed = content_without[:insert_pos] + trans_tag + content_without[insert_pos:]
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content_fixed)
        fixed += 1
        print(f'Fixed: {fname}')
    else:
        print(f'No styles.css link found: {fname}')

print(f'\nTotal fixed: {fixed}')
