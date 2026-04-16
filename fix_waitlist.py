import glob
import re

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    orig = html
    
    # Fix "Join\n\n                    Waitlist" pattern (multi-line in about.html)
    html = re.sub(r'>Join[\s\n]+Waitlist<', '>Follow the Build<', html)
    # Fix single line "Join Waitlist" within any tag context
    html = html.replace('>Join Waitlist<', '>Follow the Build<')
    html = html.replace('"Join Waitlist"', '"Follow the Build"')
    html = html.replace("'Join Waitlist'", "'Follow the Build'")
    
    if html != orig:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed: {filename}")

print("Done.")
