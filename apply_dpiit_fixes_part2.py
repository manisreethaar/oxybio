import os
import re

BASE_DIR = r"E:\OXYBIO-WEBSITE"

def modify_file(filename, replacements):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for target, replacement in replacements:
        if callable(target):
            content = target(content)
        else:
            content = re.sub(target, replacement, content, flags=re.DOTALL)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")


# 1. ingredients.html
def trim_ingredients(content):
    # Remove Category: Baseline Protocol (id="baseline")
    content = re.sub(r'<!-- Category: Baseline Protocol — B12 \+ D3\+K2 -->.*?<div id="baseline" class="reveal".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    # Remove Adaptogens (id="adaptogens")
    content = re.sub(r'<div id="adaptogens" class="reveal">.*?<!-- L-Theanine & Bacopa Group — Cognitive Stack -->', '<!-- L-Theanine & Bacopa Group — Cognitive Stack -->', content, flags=re.DOTALL)
    # Remove Cognitive Stack (id="cognitive")
    content = re.sub(r'<!-- L-Theanine & Bacopa Group — Cognitive Stack -->\s*<div id="cognitive".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    # Remove Side Navigation Links for Baseline and Cognitive
    content = re.sub(r'<a href="#baseline".*?</a>', '', content, flags=re.DOTALL)
    content = re.sub(r'<a href="#cognitive".*?</a>', '', content, flags=re.DOTALL)
    content = re.sub(r'<a href="#adaptogens".*?</a>', '', content, flags=re.DOTALL)
    # Remove ethanol
    content = re.sub(r'\(hot water \+ ethanol\)', '(hot water)', content, flags=re.DOTALL)
    return content

ingredients_replacements = [
    (trim_ingredients, '')
]
modify_file('ingredients.html', ingredients_replacements)

# 2. about.html
about_replacements = [
    # Remove nano-encapsulation
    (r'and nano-encapsulation', ''),
    # CGPA Removal
    (r'(?i)cgpa[\s:]*[\d\.]+', ''),
    # Phase 3 to Phase 0 Lab Validation
    # In my previous grep it was already partially updated, but just in case:
    (r'Phase 3 — Prototype Development', r'Phase 0 — Lab Validation'),
    (r'Phase 3', r'Phase 0')
]
modify_file('about.html', about_replacements)

# 3. science.html
science_replacements = [
    (r'\(hot water \+ ethanol\)', '(hot water)'),
    (r'and ethanol method', 'method'),
    (r'<div[^>]*>Vitamin K2 \(MK-7\) & Calcium Distribution</div>.*?</div>', ''),
]
modify_file('science.html', science_replacements)

# 4. problem.html
problem_replacements = [
    (r'\(Hot water \+ Ethanol\)', '(Hot water)'),
]
modify_file('problem.html', problem_replacements)

