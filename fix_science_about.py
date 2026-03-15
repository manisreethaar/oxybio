"""
Content corrections for science.html and about.html:
1. science.html: unique page title
2. science.html: remove '(RIZE)' — fabricated product name not established anywhere
3. science.html: fix broken #evidence anchor — change to href="ingredients.html"
4. science.html: remove unused Space Mono font import
5. about.html: unique page title
6. about.html: remove Space Mono font import
"""
import re

# ============ SCIENCE.HTML ============
with open(r'e:\OXYBIO\science.html', encoding='utf-8') as f:
    science = f.read()

# Fix 1: Unique page title
science = science.replace(
    '<title>Oxygen Bioinnovations | Advanced Functional Foods. Powered by Fermentation.</title>',
    '<title>Our Science | Oxygen Bioinnovations</title>'
)

# Fix 2: Remove fabricated "(RIZE)" product name — it's just Iron Bisglycinate
science = science.replace('IRON BISGLYCINATE (RIZE)', 'IRON BISGLYCINATE')

# Fix 3: Fix broken #evidence anchor — point to ingredients page instead
science = science.replace(
    'href="#evidence"',
    'href="ingredients.html"'
)

# Fix 4: Remove Space Mono from font import
science = re.sub(r'&family=Space\+Mono[^&"]*', '', science)

with open(r'e:\OXYBIO\science.html', 'w', encoding='utf-8') as f:
    f.write(science)
print("Fixed science.html: title, removed (RIZE), fixed broken anchor, removed Space Mono")


# ============ ABOUT.HTML ============
with open(r'e:\OXYBIO\about.html', encoding='utf-8') as f:
    about = f.read()

# Fix 1: Unique page title
about = about.replace(
    '<title>Oxygen Bioinnovations | Advanced Functional Foods. Powered by Fermentation.</title>',
    '<title>About Us | Oxygen Bioinnovations</title>'
)

# Fix 2: Remove Space Mono from font import
about = re.sub(r'&family=Space\+Mono[^&"]*', '', about)

with open(r'e:\OXYBIO\about.html', 'w', encoding='utf-8') as f:
    f.write(about)
print("Fixed about.html: unique title, removed Space Mono font")


# ============ FIX REMAINING PAGES TOO ============
# Remove Space Mono and fix duplicate titles on all remaining pages
pages = {
    'problem.html': 'The Problem | Oxygen Bioinnovations',
    'careers.html': 'Careers | Oxygen Bioinnovations',
    'contact.html': 'Contact Us | Oxygen Bioinnovations',
    'ingredients.html': 'Ingredients Index | Oxygen Bioinnovations',
    'life.html': 'Life at Oxygen Bioinnovations',
    'faq.html': 'FAQ | Oxygen Bioinnovations',
}

OLD_TITLE = '<title>Oxygen Bioinnovations | Advanced Functional Foods. Powered by Fermentation.</title>'

for fname, new_title_text in pages.items():
    fpath = rf'e:\OXYBIO\{fname}'
    try:
        with open(fpath, encoding='utf-8') as f:
            content = f.read()
        changed = False
        if OLD_TITLE in content:
            content = content.replace(OLD_TITLE, f'<title>{new_title_text}</title>')
            changed = True
        content_new = re.sub(r'&family=Space\+Mono[^&"]*', '', content)
        if content_new != content:
            content = content_new
            changed = True
        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {fname}")
    except FileNotFoundError:
        print(f"Not found: {fname}")

print("\nAll content corrections applied.")
