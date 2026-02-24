import re

# Update v2 variables in index.html specifically
with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('v2_premium.css?v=1', 'v2_premium.css?v=2')
html = html.replace('v2_premium.js', 'v2_premium.js?v=2')
html = html.replace('v2_canvas.js', 'v2_canvas.js?v=2')

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Busted V2 script caches to v=2 in index.html")
