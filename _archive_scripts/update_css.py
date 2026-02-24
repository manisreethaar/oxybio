import os
import re

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html']
for filename in files:
    filepath = os.path.join(r'e:\OXYBIO', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if <link rel="stylesheet" href="assets/css/styles.css"> is already there
    if 'href="assets/css/styles.css"' not in content:
        new_content, count = re.subn(r'<style>.*?</style>', '<link rel="stylesheet" href="assets/css/styles.css">', content, flags=re.DOTALL)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
        else:
            print(f'No <style> block found in {filename}')
    else:
        print(f'{filename} already has external CSS linked.')
