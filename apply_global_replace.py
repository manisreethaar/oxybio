import os
import glob

html_files = glob.glob('e:/OXYBIO/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Waitlist CTA
    content = content.replace('Join Waitlist', 'Follow Our R&D Journey')
    content = content.replace('href="index.html#join"', 'href="index.html#updates"')
    content = content.replace('href="#join"', 'href="#updates"')

    # 2. Unlocking bioavailability -> Researching bioavailability
    content = content.replace('Unlocking millet bioavailability and mushroom fortification', 'Researching millet bioavailability and mushroom fortification')
    content = content.replace('Efficacy Study Planned (Pre-Launch)', 'In Active Research & Development')
    content = content.replace('Efficacy Study Planned', 'Research & Development Phase')
    
    # Write back
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} files.")
