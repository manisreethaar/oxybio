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

# 1. problem.html
problem_replacements = [
    ("High-dose inorganic", "High-concentration inorganic"),
    ("high dose is useless", "high concentration is useless"),
    ("High-dose synthetic", "High-concentration synthetic"),
    ("matters more than dose", "matters more than input amount")
]
replace_in_file(os.path.join(base_dir, "problem.html"), problem_replacements)

# 2. life.html
life_replacements = [
    ("not comparable to lar", "not comparable to leg") # targeting "large pharma or FMCG" -> "legacy FMCG"
]
replace_in_file(os.path.join(base_dir, "life.html"), life_replacements)

# Regex substitute for pharma in life.html
def replace_regex_in_file(filepath, pattern, replacement):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(pattern, replacement, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
replace_regex_in_file(os.path.join(base_dir, "life.html"), r"large pharma or FMCG company", r"legacy FMCG conglomerate")

print("Final mop-up applied.")
