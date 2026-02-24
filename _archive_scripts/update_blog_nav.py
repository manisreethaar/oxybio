import os
import re

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html', 'problem.html', 'ingredients.html', 'blog.html']

for filename in files:
    filepath = os.path.join(r'e:\\OXYBIO', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if Blog is already in the navigation multiple times (safeguard)
    if content.count('href="blog.html"') > 0:
        continue

    # 1. Desktop Nav Replacement
    content = content.replace(
        '<a href="careers.html">Careers</a>',
        '<a href="blog.html">Blog</a>\n                <a href="careers.html">Careers</a>',
        1 # Only replace the first occurrence (which is the desktop nav)
    )

    # 2. Mobile Nav Replacement
    content = content.replace(
        '<a href="careers.html" class="menu-link" style="margin-top:1rem;">Careers</a>',
        '<a href="blog.html" class="menu-link" style="margin-top:1rem;">Blog</a>\n        <a href="careers.html" class="menu-link">Careers</a>'
    )

    # 3. Footer Links Replacement
    # In footer, it looks like:
    # <div class="footer-links">
    #     <a href="about.html">About Us</a>
    #     <a href="problem.html">The Problem</a>
    #     <a href="index.html#products">Formulas</a>
    #     <a href="science.html">Science</a>
    #     <a href="contact.html">Contact</a>
    # </div>
    # We will insert standard Blog and Careers link before Contact in the footer links.
    footer_pattern = r'(<div class="footer-links">.*?)(\s*<a href="contact.html">Contact</a>)'
    content = re.sub(
        footer_pattern, 
        r'\1\n                <a href="blog.html">Blog</a>\n                <a href="careers.html">Careers</a>\2',
        content, 
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navigation updated successfully.")
