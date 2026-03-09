import glob
import re

html_files = glob.glob(r'e:\OXYBIO\*.html')
tsx_files = glob.glob(r'e:\OXYBIO\src\components\**\*.tsx', recursive=True)
all_files = [*html_files, *tsx_files]

for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Text replacements to force 'DETI@ACE - TBI' everywhere
    replacements = [
        ('TBI - DETI@ACE', 'DETI@ACE - TBI'),
        ('TBI, DETI @ ACE', 'DETI@ACE - TBI'),
        ('Technology Business Incubator (TBI), Adhiyamaan', 'DETI@ACE - TBI, Adhiyamaan'),
        ('Technology Business Incubator (TBI) at Adhiyamaan', 'DETI@ACE - TBI at Adhiyamaan'),
        ('Technology Business Incubator, Adhiyamaan', 'DETI@ACE - TBI, Adhiyamaan'),
        ('Technology Business Incubator at Adhiyamaan', 'DETI@ACE - TBI at Adhiyamaan'),
        ('TBI-ACE, Hosur', 'DETI@ACE - TBI, Hosur'),
        ('TBI-ACE', 'DETI@ACE - TBI'),
        ('TBI, Adhiyamaan', 'DETI@ACE - TBI, Adhiyamaan'),
    ]
    
    for old_str, new_str in replacements:
        content = content.replace(old_str, new_str)
        
    # Edge case cleanup if something became DETI@ACE - DETI@ACE etc
    content = content.replace('DETI@ACE - DETI@ACE', 'DETI@ACE - TBI')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Location strings updated to DETI@ACE - TBI.")
