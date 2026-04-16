import re
import glob

# 1. Fix problem.html missing </div> tags
with open('problem.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We know the bug: <div class="container reveal"> or similar was opened but not closed right before </section>
# Let's count divs explicitly inside each section.
sections = re.split(r'(<section.*?>)', html)
new_html = sections[0]
for i in range(1, len(sections), 2):
    tag = sections[i]
    content = sections[i+1]
    
    s_part = content.split('</section>')[0]
    div_diff = s_part.count('<div') - s_part.count('</div')
    
    if div_diff > 0:
        # Inject closing tags right before </section>
        content = content.replace('</section>', '</div>\n' * div_diff + '</section>', 1)
        
    new_html += tag + content

with open('problem.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# 2. Fix about.html mismatched head/body
with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

# Check for duplicate <head> or similar issues
about_html = about_html.replace('</head>\n</head>', '</head>')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

# 3. Final Legacy Hex Purge (#111, #222, #333, #444)
files = glob.glob('*.html')
files = [f for f in files if 'backup' not in f and 'artifact' not in f]
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    orig = content
    # Some colors were borders, some backgrounds
    content = re.sub(r'#111\b|#222\b|#333\b|#444\b', 'var(--border)', content)
    
    if orig != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Purged dark hexes in {f}")

print("DOM Structural Repairs and Polish complete.")
