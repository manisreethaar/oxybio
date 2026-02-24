import os

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html', 'problem.html', 'ingredients.html']

for filename in files:
    filepath = os.path.join(r'e:\OXYBIO', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for Desktop & Mobile Mega Menus + Footers
    content = content.replace('href="science.html#problem"', 'href="problem.html"')
    content = content.replace('href="science.html#science"', 'href="ingredients.html"')
    
    # Also fix the "Our Science" link itself if it just goes to science.html, to keep things consistent,
    # but the user didn't ask to remove science.html. They just wanted these two pages.
    # The Mega Menu has: <a href="science.html">Our Science ...</a>
    # Let's keep that as is, so science.html is the landing page for science.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated navigation links to point to problem.html and ingredients.html")
