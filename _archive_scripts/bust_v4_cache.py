import re

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all potential previous cache versions for V2 assets
html = html.replace('v2_premium.css?v=3', 'v2_premium.css?v=4')
html = html.replace('v2_premium.js?v=3', 'v2_premium.js?v=4')
html = html.replace('v2_canvas.js?v=3', 'v2_canvas.js?v=4')

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Busted V2 script caches to v=4 in index.html")
