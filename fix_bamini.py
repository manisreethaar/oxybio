import base64
import re

with open(r'e:\\OXYBIO\\assets\\fonts\\Bamini_Tamil.ttf', 'rb') as f:
    b64_font = base64.b64encode(f.read()).decode('utf-8')

with open(r'e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the @font-face url with a base64 inline encoding
new_src = f"src: url('data:font/truetype;charset=utf-8;base64,{b64_font}') format('truetype');"
content = re.sub(r"src: url\('assets/fonts/Bamini_Tamil\.ttf'\) format\('truetype'\);", new_src, content)

# Fix the Tamil spelling encoding from czNth (உணவோ) to czNt (உணவே)
content = content.replace('czNth kUªJ.', 'czNt kUªJ.')

with open(r'e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Font injected and text updated successfully.')
