import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update cache versions
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=23"', html)
    html = re.sub(r'href="assets/css/v2_premium\.css\?v=\d+"', 'href="assets/css/v2_premium.css?v=23"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Globally updated CSS cache versions to v23.")
