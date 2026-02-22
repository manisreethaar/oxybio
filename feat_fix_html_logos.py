import os
html_files = [r'e:\OXYBIO\index-single.html', r'e:\OXYBIO\problem.html', r'e:\OXYBIO\science.html', r'e:\OXYBIO\about.html', r'e:\OXYBIO\blog.html', r'e:\OXYBIO\careers.html', r'e:\OXYBIO\contact.html', r'e:\OXYBIO\privacy.html', r'e:\OXYBIO\terms.html']
for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(r'<a href="index.html" class="logo">OXYGEN<span>.</span></a>', r'<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen Bioinnovations<span>.</span></a>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
print("Updated HTML files.")
