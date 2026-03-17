import os
import re

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_text, new_text in replacements:
        content = content.replace(old_text, new_text)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = "e:/OXYBIO"

# 1. index-single.html
index_single_replacements = [
    ("A 50mg dose with 35% absorption", "A 50mg concentration with 35% absorption"),
    ("Every dose scientifically rigorous", "Every concentration scientifically rigorous")
]
replace_in_file(os.path.join(base_dir, "index-single.html"), index_single_replacements)

# 2. ingredients.html
ingredients_replacements = [
    (">DOSE<", ">CONCENTRATION<"),
    ("DOSE</span>", "CONCENTRATION</span>")
]
replace_in_file(os.path.join(base_dir, "ingredients.html"), ingredients_replacements)

# 3. science.html
science_replacements = [
    ("the exact dosage and", "the exact concentration and")
]
replace_in_file(os.path.join(base_dir, "science.html"), science_replacements)

# 4. life.html
def replace_regex_in_file(filepath, pattern, replacement):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(pattern, replacement, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Use regex to catch 'medical' regardless of spacing
replace_regex_in_file(os.path.join(base_dir, "life.html"), r'medical', r'health')

print("Final edge case compliance patch applied.")
