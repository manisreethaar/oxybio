import glob
import re

files = glob.glob('*.html')
files = [f for f in files if "backup_design" not in f and "artifacts" not in f and "node_modules" not in f]

# We don't touch the recently fully standardized science, problem, and ingredients pages that were completely verified, 
# except perhaps mapping their final clamp values if needed. Wait, those DO have clamp(). Let's map everything.

REPLACEMENTS = {
    # 1. Colors & Basic Hexes
    'color:#666': 'color:var(--text-muted)',
    'color: #666': 'color: var(--text-muted)',
    'color:#888': 'color:var(--text-muted)',
    'color: #888': 'color: var(--text-muted)',
    'color:#ccc': 'color:var(--text-muted)',
    'color: #ccc': 'color: var(--text-muted)',
    'color:#aaa': 'color:var(--text-muted)',
    'color:#a3a3a3': 'color:var(--accent-lime)',
    'color: #a3a3a3': 'color: var(--accent-lime)',
    'background:#fafafa': 'background:var(--bg-alt)',
    'background: #fafafa': 'background: var(--bg-alt)',
    'background:#f9f9f9': 'background:var(--bg-alt)',
    'background: #f9f9f9': 'background: var(--bg-alt)',
    
    # 2. Section Paddings
    'padding-top:clamp(90px, 12vh, 120px)': 'padding-top:var(--section-py)',
    'padding-top: clamp(90px, 12vh, 120px)': 'padding-top: var(--section-py)',
    'padding-top:clamp(100px, 12vh, 140px)': 'padding-top:var(--section-py)',
    'padding-top: clamp(100px, 12vh, 140px)': 'padding-top: var(--section-py)',
    'padding-top:clamp(80px,10vh,100px)': 'padding-top: calc(var(--section-py) * 0.8)', # The heroes
    
    'padding:100px 0': 'padding:var(--section-py) 0',
    'padding: 100px 0': 'padding: var(--section-py) 0',
    'padding:120px 0': 'padding:var(--section-py) 0',
    'padding: 120px 0': 'padding: var(--section-py) 0',
    'padding: 80px 0': 'padding: calc(var(--section-py) * 0.8) 0',
    'padding-bottom:100px': 'padding-bottom:var(--section-py)',
    'padding-bottom: 100px': 'padding-bottom: var(--section-py)',
    'padding: clamp(60px, 8vw, 100px) 0': 'padding: var(--section-py) 0',
    
    # 3. Typography cleanup
    'font-size: 1.25rem': 'font-size: var(--text-xl)',
    'font-size:1.25rem': 'font-size:var(--text-xl)',
    'font-size: 1.4rem': 'font-size: var(--text-2xl)',
    'font-size:1.4rem': 'font-size:var(--text-2xl)',
    'font-size: 0.85rem': 'font-size: var(--text-sm)',
    'font-size:0.85rem': 'font-size:var(--text-sm)',
    'font-size: 0.6rem': 'font-size: var(--text-xs)',
    'font-size:0.6rem': 'font-size:var(--text-xs)',
    'font-size: 0.65rem': 'font-size: var(--text-xs)',
    'font-size:0.65rem': 'font-size:var(--text-xs)',
    'font-size: 1rem': 'font-size: var(--text-base)',
    'font-size:1rem': 'font-size:var(--text-base)',
    
    # Advanced typography strings
    'font-size:clamp(1.1rem, 2vw, 1.35rem)': 'font-size:var(--text-lg)',
    'font-size: clamp(1.1rem, 2vw, 1.35rem)': 'font-size: var(--text-lg)',
    'font-size:clamp(3.5rem, 8vw, 8rem)': 'font-size:var(--text-6xl)',
    'font-size: clamp(3.5rem, 8vw, 8rem)': 'font-size: var(--text-6xl)',
    'font-size:clamp(2rem, 4vw, 3rem)': 'font-size:var(--text-3xl)',
    'font-size: clamp(2rem, 4vw, 3rem)': 'font-size: var(--text-3xl)',
}

def secure_replace():
    changes_made = 0
    for f in files:
        changed = False
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
        
        orig_html = html
        for target, replacement in REPLACEMENTS.items():
            html = html.replace(target, replacement)
        
        if html != orig_html:
            changed = True
            changes_made += 1
            with open(f, 'w', encoding='utf-8') as file:
                file.write(html)
            print(f"Updated: {f}")
            
    print(f"Total files updated: {changes_made}")

secure_replace()
