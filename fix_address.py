import glob
import re

html_files = glob.glob(r'e:\OXYBIO\*.html')
tsx_files = glob.glob(r'e:\OXYBIO\src\components\**\*.tsx', recursive=True)

all_files = html_files + tsx_files

for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Update TBI Incubated -> Incubated in TBI - DETI@ACE
    content = content.replace('TBI Incubated Startup', 'Incubated in TBI - DETI@ACE')
    content = content.replace('TBI Incubated', 'Incubated in TBI - DETI@ACE')
    # Fix potential double replacement if 'Incubated in TBI - DETI@ACE Startup' happened
    content = content.replace('Incubated in TBI - DETI@ACE Startup', 'Incubated in TBI - DETI@ACE')

    # 2. Update address
    # Variant 1: HTML files
    addr_pattern_1 = r'Cabin - D, Technology Business Incubator,<br>\s*Adhiyamaan College of Engineering Campus,<br>\s*Hosur, Tamil Nadu'
    content = re.sub(
        addr_pattern_1, 
        r'Cabin D, TBI, DETI @ ACE,<br>\n                                Adhiyamaan College of Engineering Campus,<br>\n                                Hosur, Tamil Nadu', 
        content
    )
    
    # Variant 2: React files (Footer.tsx)
    addr_pattern_2 = r'Cabin D, Technology Business Incubator,<br />\s*Adhiyamaan College of Engineering Campus'
    content = re.sub(
        addr_pattern_2, 
        r'Cabin D, TBI, DETI @ ACE,<br />\n                                    Adhiyamaan College of Engineering Campus', 
        content
    )
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Text replacements completed.")
