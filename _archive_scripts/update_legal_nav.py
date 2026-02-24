import os
import re

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html', 'problem.html', 'ingredients.html', 'blog.html', 'privacy.html', 'terms.html']

for filename in files:
    filepath = os.path.join(r'e:\\OXYBIO', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if Legal links are already in the navigation multiple times (safeguard)
    if content.count('href="privacy.html"') > 0:
        continue

    # We want to add Legal Links to the footer
    # Let's find: <div class="footer-bottom">
    # Replace it with:
    # <div class="footer-bottom" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
    #     <div>&copy; <span id="year"></span> Oxygen Bioinnovations. All rights reserved.</div>
    #     <div style="display: flex; gap: 1.5rem; font-size: 0.9rem;">
    #         <a href="privacy.html" style="color: var(--text-muted); text-decoration: none;">Privacy Policy</a>
    #         <a href="terms.html" style="color: var(--text-muted); text-decoration: none;">Terms & Conditions</a>
    #     </div>
    # </div>
    
    # Original HTML code:
    # <div class="footer-bottom">
    #    &copy; <span id="year"></span> Oxygen Bioinnovations. All rights reserved.
    # </div>
    
    replacement_footer = """<div class="footer-bottom" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <div>&copy; <span id="year"></span> Oxygen Bioinnovations. All rights reserved.</div>
                <div style="display: flex; gap: 1.5rem; font-size: 0.9rem;">
                    <a href="privacy.html" style="color: var(--text-muted); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text-muted)'">Privacy Policy</a>
                    <a href="terms.html" style="color: var(--text-muted); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text-muted)'">Terms & Conditions</a>
                </div>
            </div>"""

    # We need to use regex because the spaces/newlines might differ slightly.
    pattern = re.compile(r'<div class="footer-bottom">\s*&copy; <span id="year"></span> Oxygen Bioinnovations\. All rights reserved\.\s*</div>', re.DOTALL)
    content = pattern.sub(replacement_footer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated footer navigation links to include Privacy and Terms.")
