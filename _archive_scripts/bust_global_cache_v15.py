import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Target and standardize the styles cache busting to v=15 across the board
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=15"', html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print('Busted Global CSS Styles file Cache to v=15')
