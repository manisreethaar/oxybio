import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_text, new_text in replacements:
        content = content.replace(old_text, new_text)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = "e:/OXYBIO"

# 1. faq.html replacements
faq_replacements = [
    ("We treat our products as ongoing scientific projects", "We approach our products as ongoing scientific projects"),
    ("it is very hard to prevent it.", "it is very hard to avoid it."),
    ("pharma or FMCG company.", "legacy FMCG conglomerate.")
]
replace_in_file(os.path.join(base_dir, "faq.html"), faq_replacements)

# 2. ingredients.html replacements
ingredients_replacements = [
    ("THE OXYGEN GUARANTEE", "THE OXYGEN BENCHMARK"),
    ("Targeting natural iron isolates to prevent", "Targeting natural iron isolates to address")
]
replace_in_file(os.path.join(base_dir, "ingredients.html"), ingredients_replacements)

# 3. problem.html replacements
problem_replacements = [
    ("cannot guarantee active", "cannot verify active"),
    ("exact dosage and sourcing protocol", "exact concentration and sourcing protocol"),
    ("implementing exact dosage floors", "implementing exact concentration floors")
]
replace_in_file(os.path.join(base_dir, "problem.html"), problem_replacements)

# 4. life.html replacements
life_replacements = [
    ("extensive medical, and family", "extensive health, and family"),
    ("pharma or FMCG company.", "legacy FMCG conglomerate.")
]
replace_in_file(os.path.join(base_dir, "life.html"), life_replacements)

# 5. about.html replacements
about_replacements = [
    ("Every dose set at scientifically rigorous thresholds", "Every concentration set at scientifically rigorous thresholds"),
    ("Absolute Dose Transparency", "Absolute Concentration Transparency"),
    ("If a dose is not high enough", "If a nutrient concentration is not high enough"),
    ("Clinical Aesthetic", "Scientific Aesthetic"),
    ("8-week clinical testing", "8-week physiological testing"),
    ("minimum clinical threshold", "minimum physiological threshold")
]
replace_in_file(os.path.join(base_dir, "about.html"), about_replacements)

# 6. index-single.html and others with 'dose' 
index_single_replacements = [
    ("Dose Matters As Much As Ingredient", "Concentration Matters As Much As Ingredient"),
    ("A 100mg dose with 5% absorption delivers", "A 100mg input with 5% absorption delivers")
]
replace_in_file(os.path.join(base_dir, "index-single.html"), index_single_replacements)

# 7. science.html replacements
science_replacements = [
    ("exact dosage and extraction method", "exact concentration and extraction method")
]
replace_in_file(os.path.join(base_dir, "science.html"), science_replacements)

print("Food regulatory deep compliance scrub complete.")
