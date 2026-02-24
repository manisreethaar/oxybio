import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We want to replace hardcoded 4rem, 6rem, 8rem inline styles with the fluid variables so they shrink on mobile.
# --space-md = 2rem
# --space-lg = 4rem 
# --space-xl = 6rem (approx mapped from old 8rem context or just broadly)
# --space-2xl = 8rem/12rem

replacements = [
    # 4rem -> var(--space-lg)
    (r'margin-top:\s*4rem', 'margin-top:var(--space-lg)'),
    (r'margin-bottom:\s*4rem', 'margin-bottom:var(--space-lg)'),
    (r'padding-top:\s*4rem', 'padding-top:var(--space-lg)'),
    (r'padding-bottom:\s*4rem', 'padding-bottom:var(--space-lg)'),
    (r'gap:\s*4rem', 'gap:var(--space-lg)'),
    (r'padding:\s*4rem(?:;|(?=\s|"))', 'padding:var(--space-lg)'),
    (r'padding:\s*4rem\s+3rem', 'padding:var(--space-lg) 3rem'),
    
    # 6rem -> var(--space-xl)
    (r'margin-top:\s*6rem', 'margin-top:var(--space-xl)'),
    (r'margin-bottom:\s*6rem', 'margin-bottom:var(--space-xl)'),
    (r'padding-top:\s*6rem', 'padding-top:var(--space-xl)'),
    (r'padding-bottom:\s*6rem', 'padding-bottom:var(--space-xl)'),
    (r'gap:\s*6rem', 'gap:var(--space-xl)'),
    
    # 8rem -> var(--space-2xl)
    (r'margin-top:\s*8rem', 'margin-top:var(--space-2xl)'),
    (r'margin-bottom:\s*8rem', 'margin-bottom:var(--space-2xl)'),
    (r'padding-top:\s*8rem', 'padding-top:var(--space-2xl)'),
    (r'padding-bottom:\s*8rem', 'padding-bottom:var(--space-2xl)'),
    (r'gap:\s*8rem', 'gap:var(--space-2xl)'),
    
    # Also standardize some 3rem gaps to --space-lg or slightly custom if needed, let's leave 3rem alone if it exists as it scales okay by default.
]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    for old, new in replacements:
        # We use re.sub for safety in case of variable whitespace
        html = re.sub(old, new, html)

    # Note: index.html hero uses some specific layout grids that should probably shrink.
    # The fix is mostly targeting the inland grid padding.
    
    # Let's also enforce a cache bump to v24
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=24"', html)
    html = re.sub(r'href="assets/css/v2_premium\.css\?v=\d+"', 'href="assets/css/v2_premium.css?v=24"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Batch replaced static `rem` spacing values with fluid CSS variables across all templates.")
