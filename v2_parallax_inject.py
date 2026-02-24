import re

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Isolate the main product image in the homepage hero and wrap it in the parallax mask
old_img = '<img src="assets/images/product-transparent.png" alt="Oxygen Bioinnovations Cognitive Formula"'
new_img = '<div class="v2-parallax-container" style="max-height:600px; display:flex; justify-content:center; align-items:center;">\n                            <img src="assets/images/product-transparent.png" alt="Oxygen Bioinnovations Cognitive Formula"'

if old_img in html:
    html = html.replace(old_img, new_img)
    # the image tag is self closing so we need to add the closing div after it
    # Find the end of the img tag
    img_end = html.find('>', html.find(new_img)) + 1
    html = html[:img_end] + '\n                        </div>' + html[img_end:]

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Injected Parallax Masks into index.html")
