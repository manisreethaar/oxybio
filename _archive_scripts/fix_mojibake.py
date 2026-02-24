import re

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Mojave encoding errors introduced by old scripts
html = html.replace('ðŸŒ±', '🌱')
html = html.replace('â€¢', '•')
html = html.replace('âœ¦', '✦')
html = html.replace('âœ”', '✔')
html = html.replace('âœ—', '✖')
html = html.replace('Î²', 'β')
html = html.replace('TRAACSÂ®', 'TRAACS®')

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed Mojibake in index.html")
