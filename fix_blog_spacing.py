import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# We need to remove `.subtext` from the global justify rule because short hero blurbs look terrible justified.
old_rule = """    p, .subtext, .editorial-col, .editorial-col p {
        text-align: justify !important;
        text-justify: inter-word !important;
        hyphens: auto !important;
        -webkit-hyphens: auto !important;
        -ms-hyphens: auto !important;
        margin-bottom: 1.75rem !important; /* Increase vertical breathing room */
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }"""

new_rule = """    p, .editorial-col, .editorial-col p {
        text-align: justify !important;
        text-justify: inter-word !important;
        hyphens: auto !important;
        -webkit-hyphens: auto !important;
        -ms-hyphens: auto !important;
        margin-bottom: 1.75rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    
    /* Exception for short hero text — never justify short blurbs or titles */
    .subtext, .page-hero-badge {
        text-align: left !important; /* or natural alignment */
        text-justify: auto !important;
        hyphens: none !important;
        letter-spacing: normal !important;
    }"""

if old_rule in css:
    css = css.replace(old_rule, new_rule)
    print("Fixed CSS rule for justification.")
else:
    print("Could not find the exact old rule string! Check styles.css manually.")

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bust HTML
for file in os.listdir(ROOT):
    if file.endswith('.html'):
        path = os.path.join(ROOT, file)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'\?v=\d+"', '?v=34"', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
print("Updated HTML cache to v34.")
