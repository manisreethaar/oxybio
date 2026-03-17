import os
import glob
import re

html_files = glob.glob('e:/OXYBIO/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Leftover waitlist
    content = re.sub(r'Join the\s*Waitlist\s*→', 'Follow Our R&D Journey →', content)
    content = re.sub(r'Join the\s*Waitlist', 'Follow Our R&D Journey', content)
    content = re.sub(r'>\s*Waitlist\s*</a>', '>R&D Updates</a>', content)
    content = content.replace("Waitlist growing", "Community growing")
    
    # In index.html line 1609: "Join the waitlist to receive access..."
    content = content.replace('Join the waitlist', 'Join our community')
    content = content.replace("alert('Waitlist strictly joined.", "alert('Successfully joined.")
    
    # 2. Science "proven" fixes
    content = content.replace('scientifically-proven', 'evidence-backed')
    content = content.replace('proven to stimulate Nerve Growth Factor', 'shown in studies to stimulate Nerve Growth Factor')
    content = content.replace('proven to', 'demonstrated to')
    content = content.replace('>PROVEN', '>SUPPORTED')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} files. Removed waitlist and proven claims.")
