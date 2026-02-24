import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

html_files = [f for f in os.listdir(ROOT) if f.endswith('.html')]

# 1. Gather all CSS classes defined in styles.css
css_classes = set()
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css_content = f.read()
    # Find all .classname
    matches = re.findall(r'\.([a-zA-Z0-9_-]+)[ \n\{:,>]', css_content)
    css_classes.update(matches)

# 2. Gather all classes and IDs used in HTML
used_classes = set()
used_ids = set()
inline_styles_count = 0
broken_links = []
local_files = set(html_files)
local_files.add('styles.css')
local_files.add('scripts.js')
# Add more generic checks if needed

for file in html_files:
    path = os.path.join(ROOT, file)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
        # Extract classes
        class_attrs = re.findall(r'class="([^"]+)"', html)
        for c_attr in class_attrs:
            used_classes.update(c_attr.split())
            
        # Extract IDs
        id_attrs = re.findall(r'id="([^"]+)"', html)
        used_ids.update(id_attrs)
        
        # Count inline styles
        inline_styles = re.findall(r'style="([^"]+)"', html)
        inline_styles_count += len(inline_styles)
        
        # Extract hrefs for internal links
        href_attrs = re.findall(r'href="([^"#]+)(?:#[^"]*)?"', html)
        for href in href_attrs:
            if not href.startswith('http') and not href.startswith('mailto') and not href.startswith('tel'):
                # Check if it's a local file that exists
                target = href.split('?')[0].lstrip('/')
                target_path = os.path.join(ROOT, target)
                if not os.path.exists(target_path):
                    broken_links.append((file, href))

# 3. Analyze CSS classes unused in HTML
unused_css = css_classes - used_classes
# Filter out pseudo-classes or animation frames that might get caught
unused_css = {c for c in unused_css if not c in ['active', 'hover', 'focus', 'before', 'after']}

print("="*50)
print("DEEP SITE AUDIT REPORT")
print("="*50)

print(f"Total HTML files analyzed: {len(html_files)}")
print(f"Total defined CSS classes in styles.css: {len(css_classes)}")
print(f"Total unique classes used in HTML: {len(used_classes)}")

# A simple heuristic to avoid dumping 500 unused classes - maybe just count and list a few.
# Many CSS classes might be dynamically added via JS or are standard resets.
print(f"\n[!] Potentially unused CSS classes in styles.css: {len(unused_css)}")
if len(unused_css) < 30:
    print(", ".join(unused_css))
else:
    print("Too many to list individually. Might include utility classes or JS-injected classes.")

print(f"\n[!] Total inline style attributes found: {inline_styles_count}")
print("Consider moving prominent inline styles to CSS utility classes for cleaner HTML.")

print(f"\n[!] Broken internal links: {len(broken_links)}")
for file, link in broken_links:
    print(f"  - In {file}: points to missing '{link}'")

# 4. Find unwanted/useless python script artifacts
py_files = [f for f in os.listdir(ROOT) if f.endswith('.py')]
print(f"\n[!] Temporary python scripts found in root: {len(py_files)}")
for p in py_files:
    print(f"  - {p} (Candidate for deletion)")

print("="*50)
