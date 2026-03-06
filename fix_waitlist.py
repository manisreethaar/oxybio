import glob
import os

html_files = glob.glob(r'e:\OXYBIO\*.html')

for filepath in html_files:
    content = None
    for enc in ['utf-8', 'windows-1252', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
            
    if content:
        # replace "Join the Waitlist ?" or "Join the Waitlist AA+A'" with "Join the Waitlist →"
        content = content.replace('Join the Waitlist ?', 'Join the Waitlist →')
        content = content.replace('Join the Waitlist AA+A\'', 'Join the Waitlist →')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Waitlist arrows repaired.")
