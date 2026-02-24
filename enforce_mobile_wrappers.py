import re
import os

with open('e:\\OXYBIO\\problem.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix table overflow by finding '<table class="data-journal-table"' and safely wrapping it
if '<div class="table-responsive"' not in html:
    html = re.sub(
        r'(<table[^>]*class=["\']data-journal-table["\'][^>]*>)',
        r'<div class="table-responsive" style="overflow-x: auto; width: 100%; -webkit-overflow-scrolling: touch;">\1\n',
        html
    )
    # We must also close the div after the </table>
    html = re.sub(
        r'(</table>)',
        r'\1\n</div>',
        html
    )

with open('e:\\OXYBIO\\problem.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('e:\\OXYBIO\\ingredients.html', 'r', encoding='utf-8') as f:
    ing = f.read()

# Make sure clamp padding was applied
if 'padding: clamp(' not in ing:
    print("re.sub for ingredients padding failed initially, retrying with flexible whitespace regex.")
    ing = re.sub(r'padding:\s*2\.5rem\s*;', 'padding:clamp(1.25rem, 5vw, 2.5rem);', ing)
    ing = re.sub(r'padding:\s*3rem\s*;', 'padding:clamp(1.5rem, 5vw, 3rem);', ing)

with open('e:\\OXYBIO\\ingredients.html', 'w', encoding='utf-8') as f:
    f.write(ing)
    
print("Table wrap and ingredients paddings applied.")
