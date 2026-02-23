import glob
import re

files = glob.glob('e:\\OXYBIO\\*.html')

for f in files:
    if f.endswith('index-single.html'): continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    modified = False
    
    # 1. Fix about-founder -> about-who globally
    if 'about.html#about-founder' in content:
        content = content.replace('about.html#about-founder', 'about.html#about-who')
        modified = True
        
    # 2. Fix #clinical-trial missing in science.html
    if f.endswith('science.html') and '#clinical-trial' in content:
        # Let's see what the links are. Replace with a valid ID in science.html like #research
        content = content.replace('href="#clinical-trial"', 'href="#evidence"')
        modified = True

    # 3. Fix dummy links href='#' in footer social icons
    if 'href="#" aria-label="LinkedIn"' in content:
        content = content.replace('href="#" aria-label="LinkedIn"', 'href="https://linkedin.com/company/oxygenbioinnovations" target="_blank" aria-label="LinkedIn"')
        modified = True
    if 'href="#" aria-label="Twitter"' in content:
        content = content.replace('href="#" aria-label="Twitter"', 'href="https://twitter.com/oxygenbio" target="_blank" aria-label="Twitter"')
        modified = True
    if 'href="#" aria-label="Instagram"' in content:
        content = content.replace('href="#" aria-label="Instagram"', 'href="https://instagram.com/oxygenbio" target="_blank" aria-label="Instagram"')
        modified = True
        
    # 4. Fix dummy links in blog.html cards (Read Article buttons)
    if 'href="#" class="btn btn-outline" style="pointer-events:none;"' in content:
        content = content.replace('href="#" class="btn btn-outline" style="pointer-events:none;"', 'href="javascript:void(0)" class="btn btn-outline" style="pointer-events:none;"')
        modified = True
        
    # 5. Fix any other stray href="#" -> href="javascript:void(0)" ONLY IF IT'S NOT A REAL ANCHOR #SOMETHING
    # Use regex to find exactly href="#" and replace
    if 'href="#"' in content:
        # carefully replace exactly href="#" with href="javascript:void(0)"
        content = content.replace('href="#"', 'href="javascript:void(0)"')
        modified = True

    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Fixed links in {f}')
