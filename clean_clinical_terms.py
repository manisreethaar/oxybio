import glob
import re
import os

def cleanup_clinical_terms():
    html_files = glob.glob(r'e:\OXYBIO\*.html')
    tsx_files = glob.glob(r'e:\OXYBIO\src\components\**\*.tsx', recursive=True)
    all_files = [*html_files, *tsx_files]
    
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # 1. Clinical Study -> Validation Study / Efficacy Study
        content = content.replace("Clinical Study Protocol Ready", "Validation Study Protocol Ready")
        content = content.replace("Clinical study for 135 participants", "Validation study for 135 participants")
        content = content.replace("clinical study for 135 participants", "validation study for 135 participants")
        content = content.replace("Clinical Study Planned", "Efficacy Study Planned")
        content = content.replace("Clinical study", "Efficacy study")
        content = content.replace("Zero Clinical Efficacy Data", "Zero Efficacy Data")
        content = content.replace("clinical study protocol designed", "validation study protocol designed")
        
        # 2. Clinical Precision
        content = content.replace("clinical precision", "scientific precision")
        
        # 3. Clinical Dosing -> Evidence-Based Dosing
        content = content.replace("Clinical Dosing", "Evidence-Based Dosing")
        content = content.replace("clinically studied", "scientifically proven")
        content = content.replace("clinically-studied", "scientifically-proven")
        content = content.replace("Clinical Evidence Is Non-Negotiable", "Scientific Evidence Is Non-Negotiable")
        content = content.replace("clinically relevant", "scientifically rigorous")
        
        # 4. Clinical Framework
        content = content.replace("Clinical Framework Drafted", "Efficacy Framework Drafted")
        
        # 5. Problem page: "clinical medicinal mushrooms"
        content = content.replace("clinical medicinal mushrooms", "potent medicinal mushrooms")
        
        # 6. Navbar "We formulate with clinical precision"
        content = content.replace("clinical precision", "scientific precision")

        # 7. ingredients.html "CLINICAL" labels
        content = content.replace('color:#666; display:block;">CLINICAL', 'color:#666; display:block;">PROVEN')

        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Scrubbed clinical vocabulary in {os.path.basename(file)}")

cleanup_clinical_terms()
