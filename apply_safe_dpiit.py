import os
import glob

def check_div_balance(html_content):
    return html_content.count('<div') - html_content.count('</div')

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    orig_div_balance = check_div_balance(html)
    
    # Apply replacements
    for old, new in replacements:
        if old in html:
            html = html.replace(old, new)
        else:
            print(f"Warning: Could not find '{old[:30]}...' in {filename}")

    new_div_balance = check_div_balance(html)
    if orig_div_balance != new_div_balance:
        print(f"ERROR: Div balance changed in {filename}! Old: {orig_div_balance}, New: {new_div_balance}")
        return False
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    return True

# 1. Global Navbars
global_replacements = [
    ("Vision &amp; Mission", "R&amp;D Platform Goals"),
    (">Vision & Mission<", ">R&D Platform Goals<"),
    ("Waitlist", "Follow the Build"),
    ("waitlist", "Follow the Build")
]

for file in glob.glob('*.html'):
    update_file(file, global_replacements)

# 2. index.html Replacements
index_replacements = [
    # Dual extract to hot-water
    ("Lion's Mane Dual-Extract (Hericenones & Erinacines)", "Lion's Mane Hot-Water Extract (Hericenones & Erinacines)"),
    ("Reishi Dual-Extract (Beta-Glucans standardised)", "Reishi Hot-Water Extract (Beta-Glucans standardised)"),
    ("Cordyceps militaris Dual-Extract (Cordycepin standardised)", "Cordyceps militaris Hot-Water Extract (Cordycepin)"),
    ("Lion's Mane mushroom dual-extract", "Lion's Mane mushroom hot-water extract"),
    # SKUs renaming - wait, 3530329 already had them named CLARITY, VITALITY, MOMENTUM. Let me skip SKU renaming to be safe, unless it wasn't done!
    # Wait, 3530329 is POST facace4. Let's check what 3530329 had!
    # facace4 ALREADY DID THE DPIIT COPY. Let's look at facace4!
    # Yes, facace4 had ALL the DPIIT copy but it BROKE layout.
    # WAIT! facace4 broke the layout. I just restored 3530329. But 3530329 IS AFTER facace4!
    # So 3530329 already HAS the broken layouts of facace4!!
    # If I just restored 3530329, I restored the BROKEN layouts!!
]
