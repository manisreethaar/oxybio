import glob
import os

def update_linkedin():
    html_files = glob.glob(r'e:\\OXYBIO\\*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # LinkedIn URLs use hyphens instead of spaces for company names
        updated_content = content.replace(
            'https://linkedin.com/company/oxygenbioinnovations', 
            'https://www.linkedin.com/company/oxygen-bioinnovations'
        )
        
        if content != updated_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated LinkedIn link in {os.path.basename(file)}")

update_linkedin()
