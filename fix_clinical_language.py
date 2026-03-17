import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_text, new_text in replacements:
        content = content.replace(old_text, new_text)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = "e:/OXYBIO"
index_path = os.path.join(base_dir, "index.html")
about_path = os.path.join(base_dir, "about.html")
problem_path = os.path.join(base_dir, "problem.html")
ingredients_path = os.path.join(base_dir, "ingredients.html")

# 1. index.html replacements
index_replacements = [
    # Solution 1 (EXP_01)
    ("exact 2.5:1 clinical ratios", "optimal 2.5:1 nutritional ratios"),
    
    # Problem section
    ("clinically established", "scientifically established"),
    
    # Solution intro
    ("clinically transparent dosing", "scientifically rigorous nutrient")
]
replace_in_file(index_path, index_replacements)

# 2. about.html replacements
about_replacements = [
    # Principles Text
    ("clinical methodologies", "nutritional methodologies"),
    ("Pharmacological Thresholds", "Nutritional Thresholds"),
    ("clinical outcome", "physiological outcome"),
    ("registered clinical efficacy trials", "structured physiological efficacy testing"),
    ("clinical endpoint", "physiological endpoint")
]
replace_in_file(about_path, about_replacements)

# 3. problem.html replacements
problem_replacements = [
    ("clinical efficacy", "physiological efficacy"),
    ("clinical outcomes", "physiological outcomes"),
    ("Pharmacological dosing", "Targeted nutrient dosing"),
    ("pharmacological", "biochemical")
]
replace_in_file(problem_path, problem_replacements)

# 4. ingredients.html replacements
ingredients_replacements = [
    ("clinical trials", "physiological testing"),
    ("clinical efficacy", "functional efficacy"),
    ("pharmacological", "biochemical")
]
replace_in_file(ingredients_path, ingredients_replacements)

print("Food regulatory compliance language patch complete.")
