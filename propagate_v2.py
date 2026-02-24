import os
import re

# Define exact replacements
js_deps = """
    <script src="assets/js/v2_scroll.js"></script>
    <script src="assets/js/v2_canvas.js"></script>
    <script src="assets/js/v2_premium.js"></script>
"""

css_deps = '<link rel="stylesheet" href="assets/css/v2_premium.css?v=5">'

# Process all html except index and careers (which we just handled)
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('index.html', 'careers.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject CSS if not present
    if 'v2_premium.css' not in html:
        # We find the styles.css link and insert the v2 premium link right after it
        if 'styles.css?v=' in html:
            # simple replace ensuring we get the latest cache
            html = re.sub(r'href="(assets/css/styles\.css\?v=\d+)">', r'href="\1">\n    ' + css_deps, html)
        else:
             html = html.replace('</head>', f'    {css_deps}\n</head>')

    # 2. Inject JS if not present
    if 'v2_premium.js' not in html:
        html = html.replace('<script src="assets/js/main.js"></script>', '<script src="assets/js/main.js"></script>' + js_deps)

    # 3. Apply magnetic classes to buttons, but avoid double applying
    if 'magnetic-btn' not in html:
        html = html.replace('class="btn btn-primary"', 'class="btn btn-primary magnetic-btn"')
        html = html.replace('class="btn btn-outline"', 'class="btn btn-outline magnetic-btn"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Propagated V2 dependencies (Canvas, Scroll, Film Grain, Magnetic Math) to: {html_files}")
