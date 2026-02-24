import re

with open('e:\\OXYBIO\\science.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all potential previous cache versions for V2 CSS/JS locally one last time
html = html.replace('styles.css?v=13', 'styles.css?v=14')

with open('e:\\OXYBIO\\science.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Busted styles to v=14 in science.html")
