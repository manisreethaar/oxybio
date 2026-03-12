import glob
import re
import os

def fix_corrupted_characters():
    html_files = glob.glob(r'e:\\OXYBIO\\*.html')
    
    # Arrow SVG icon
    arrow_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left:4px; margin-bottom:-2px;"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>'
    
    # Checkmark SVG icon
    check_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0D8A74" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>'

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Replace 'SocialMedia ?' with 'SocialMedia arrow_svg'
        content = re.sub(r'(LinkedIn|Twitter|Instagram)\s*\?', r'\\1 ' + arrow_svg, content)
        
        # Replace 'Send an Inquiry ?'
        content = re.sub(r'Send an Inquiry\s*\?', 'Send an Inquiry ' + arrow_svg, content)
        
        # Replace 'Message sent successfully. ?'
        content = re.sub(r'\?\s*Message sent successfully', check_svg + ' Message sent successfully', content)
        
        # Replace 'Download Document ?' if any
        content = re.sub(r'Download\s*\?', 'Download ' + arrow_svg, content)

        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed literal question marks in {os.path.basename(file)}")

fix_corrupted_characters()
