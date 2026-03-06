import glob
import re

html_files = glob.glob(r'e:\OXYBIO\*.html')

for filepath in html_files:
    # Read binary
    with open(filepath, 'rb') as f:
        content_bytes = f.read()

    # Decode using utf-8 with replacement for corrupted bytes
    content = content_bytes.decode('utf-8', errors='replace')
    
    # 1. Clean up garbled currency/dash symbols resulting from moji-bake
    # The corrupted characters often look like: \xed\xa0\xbd or similar depending on the read.
    # The 'errors="replace"' puts \ufffd (the '' replacement character) where bytes are invalid.
    
    # Let's just catch the context instead of the exact corrupted byte string since it varies.
    content = re.sub(r'[\ufffd\w,\.\'"\?\-]*18K\s*[\ufffd\w,\.\'"\?\-]*\s*25K/mo', '₹18K – 25K/mo', content)
    content = re.sub(r'[\ufffd\w,\.\'"\?\-]*4\.5 Lakh Crore', '₹4.5 Lakh Crore', content)
    content = re.sub(r'\([\ufffd\w,\.\'"\?\-]*350-500/serving\)', '(₹350-500/serving)', content)

    # Re-apply via Email arrow just in case
    content = re.sub(r'via Email \?', 'via Email →', content)
    content = re.sub(r'via Email .*<', 'via Email →<', content)

    # Re-apply footer alignment fix perfectly
    content = re.sub(
        r'<div class="footer-bottom"\s+style="([^"]+)"',
        lambda m: f'<div class="footer-bottom" style="{m.group(1)} grid-column: 1 / -1;"' 
                  if 'grid-column' not in m.group(1) else m.group(0),
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Cleaned up garbled strings and fixed alignment.')
