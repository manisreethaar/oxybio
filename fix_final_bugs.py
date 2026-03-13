import traceback
import re

def fix_css_and_html():
    try:
        # --- 1. Fix CSS overflow issues ---
        with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
            css = f.read()
            
        # Target any remaining html or body overflow hidden rules
        css = re.sub(r'html\s*,\s*body\s*\{[^}]*overflow-x\s*:\s*hidden[^}]*\}', 
                     'html, body { overflow-x: clip !important; }', css)
                     
        # Also ensure body itself isn't overridden later
        css += '\n\n/* OVERRIDE FOR STICKY SCROLL */\nhtml, body {\n    overflow-x: clip !important;\n    overflow-y: auto !important;\n}\n\n.structure-section { overflow: clip !important; }'
        
        with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
        print("CSS overflow fixes applied.")

        # --- 2. Fix HTML Padding and Hero Margin ---
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # Greatly reduce padding
        old_padding = 'padding-top:clamp(100px, 14vh, 130px); padding-bottom:80px; background:var(--bg); border-bottom:1px solid var(--border); overflow:clip; position:relative;'
        new_padding = 'padding-top:clamp(40px, 8vh, 80px); padding-bottom:40px; background:var(--bg); border-bottom:1px solid var(--border); overflow:clip; position:relative;'
        
        if old_padding in idx:
            idx = idx.replace(old_padding, new_padding)
            print("Reduced top padding significantly.")
        else:
            print("Could not find the exact old padding string.")

        # Check if the solution cards section has any parent that might clip it
        # The apple-style scroll requires height on the cards so they have room to scroll over each other.
        # Ensure the slide has min-height and proper z-index.
        idx = idx.replace('class="apple-slide" id="slide-vitality"\n                        style="position:sticky; top:20px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10;"',
                          'class="apple-slide" id="slide-vitality"\n                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10; min-height: 80vh;"')
                          
        idx = idx.replace('class="apple-slide" id="slide-clarity"\n                        style="position:sticky; top:20px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);"',
                          'class="apple-slide" id="slide-clarity"\n                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;"')

        idx = idx.replace('class="apple-slide" id="slide-momentum"\n                        style="position:sticky; top:20px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);"',
                          'class="apple-slide" id="slide-momentum"\n                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;"')

        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)
        print("HTML modifications applied.")

    except Exception as e:
        traceback.print_exc()

fix_css_and_html()
