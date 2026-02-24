import re

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all potential previous cache versions for V2 assets
html = html.replace('v2_premium.css?v=2', 'v2_premium.css?v=3')
html = html.replace('v2_premium.css?v=1', 'v2_premium.css?v=3')

html = html.replace('v2_premium.js?v=2', 'v2_premium.js?v=3')
html = html.replace('v2_premium.js"', 'v2_premium.js?v=3"')

html = html.replace('v2_canvas.js?v=2', 'v2_canvas.js?v=3')
html = html.replace('v2_canvas.js"', 'v2_canvas.js?v=3"')

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Busted V2 script caches to v=3 in index.html")
