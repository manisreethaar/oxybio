import codecs
import re

with codecs.open('e:\\OXYBIO\\ingredients.html', 'r', 'utf-8') as f:
    html = f.read()

# Pattern to find the section block
# We look for the <section> tag containing "background:var(--text-main); color:var(--bg);"
# and we capture everything up to the next <section> tag which is the CoA section.
pattern = re.compile(
    r'(<section class=\"structure-section\" style=\"background:var\(--text-main\); color:var\(--bg\);.*?>.*?)(?=<!--.*?FOOTER NOTE \(CoA\))',
    re.DOTALL
)

match = pattern.search(html)

if match:
    section = match.group(1)
    
    # Perform Theme Swapping Regex/Replaces
    
    # 1. Main Background and text -> use light mode classes
    section = section.replace('background:var(--text-main); color:var(--bg); border:none;', 'background:var(--bg-alt); color:var(--text-main); border-top:1px solid var(--border); border-bottom:1px solid var(--border);')
    
    # 2. Abstract glow -> convert to grey glow
    section = section.replace('background:radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 70%);', 'background:radial-gradient(circle, rgba(0,0,0,0.03) 0%, transparent 70%);')
    
    # 3. Huge Category Numbers (01, 02, 03) -> make ghosted outline numbers
    section = section.replace('color:var(--bg); opacity:0.2;', 'color:var(--text-main); font-weight:900; opacity:0.04; font-size:3.5rem;')
    
    # 4. Category Subtitles -> use text-muted
    section = section.replace('color:rgba(255,255,255,0.5);', 'color:var(--text-muted);')
    
    # 5. Category Titles & Main Titles & Value amounts
    # Because there are many color:#fff; we replace them globally in this section
    section = section.replace('color:#fff;', 'color:var(--text-main);')
    
    # 6. Card Backgrounds and Borders -> change to pristine white cards with subtle shadows
    section = section.replace('background:#111; border:1px solid #333;', 'background:var(--bg); border:1px solid var(--border); box-shadow:0 10px 30px rgba(0,0,0,0.03);')
    # For KSM-66 block which is a gradient
    section = section.replace('background:linear-gradient(135deg, #111, #1a1a1a); border:1px solid #444;', 'background:var(--bg); border:1px solid var(--border); box-shadow:0 15px 40px rgba(0,0,0,0.04);')
    
    # 7. Card Tags Label -> transparent backgrounds with subtle borders
    section = section.replace('color:#888; margin-bottom:1rem; border:1px solid #333;', 'color:var(--text-muted); margin-bottom:1rem; border:1px solid var(--border); background:transparent;')
    
    # 8. Description Text -> mute the text
    section = section.replace('color:#aaa;', 'color:var(--text-muted);')
    
    # 9. Dividers -> use global border property
    section = section.replace('border-top:1px dashed #333;', 'border-top:1px dashed var(--border);')
    section = section.replace('border-top:1px solid #333;', 'border-top:1px solid var(--border);')
    section = section.replace('border-bottom:1px solid rgba(255,255,255,0.1);', 'border-bottom:1px solid var(--border);')
    section = section.replace('border-left:1px dashed #444;', 'border-left:1px solid var(--border);') # Made solid for cleaner clinical look
    
    # 10. Secondary Labels (STANDARDIZATION, EXTRACTION)
    section = section.replace('color:#666;', 'color:var(--text-muted);')
    
    # 11. Secondary Values (344mg Ca / 100g) -> make text-main for high contrast reading
    section = section.replace('color:#ccc;', 'color:var(--text-main); font-weight:500;')
    
    # 12. SVG Background icons -> faint dark accents
    section = section.replace('opacity:0.1;', 'opacity:0.03; color:var(--text-main);')
    
    # 13. KSM-66 specific text overrides
    section = section.replace('color:#888; margin-bottom:1.5rem;', 'color:var(--text-muted); margin-bottom:1.5rem;')
    
    # 14. Adjust the category headers specifically if they missed the general pass
    section = section.replace('color:rgba(255,255,255,0.5)', 'color:var(--text-muted)')
    
    # Replace in main HTML
    new_html = html[:match.start()] + section + html[match.end():]
    
    with codecs.open('e:\\OXYBIO\\ingredients.html', 'w', 'utf-8') as f:
        f.write(new_html)
    print("Ingredients formulary upgraded to pristine light theme.")
else:
    print("Failed to find section markers.")
