import glob
import re
import os

def cleanup_lingering_terms():
    html_files = glob.glob(r'e:\OXYBIO\*.html')
    tsx_files = glob.glob(r'e:\OXYBIO\src\components\**\*.tsx', recursive=True)
    all_files = [*html_files, *tsx_files]
    
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # 1. "precision nutrition system"
        content = content.replace(
            "precision nutrition system",
            "functional food system"
        )
        content = content.replace(
            "Precision Nutrition System",
            "Functional Food System"
        )
        
        # 2. "precision nutrition"
        content = content.replace(
            "precision nutrition",
            "functional nutrition"
        )
        content = content.replace(
            "Precision Nutrition",
            "Functional Nutrition"
        )
        
        # 3. "precision nutrition enterprise"
        content = content.replace(
            "precision nutrition enterprise",
            "functional food enterprise"
        )
        
        # 4. In Blog-origin and other files referring to "supplements" favorably (we can keep it when attacking them)
        # However, for the user's origin story where he says "I wanted to build a precision nutrition brand" -> it's now "functional food brand"
        
        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Cleaned legacy terminology in {os.path.basename(file)}")

cleanup_lingering_terms()
