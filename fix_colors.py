import re

files = ['science.html', 'ingredients.html', 'problem.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Backgrounds
    html = html.replace('background: #050f0d', 'background: var(--bg)')
    html = html.replace('background:#050f0d', 'background: var(--bg)')
    
    # 2. Text colors
    html = html.replace('color: #fff', 'color: var(--text-main)')
    html = html.replace('color:#fff', 'color: var(--text-main)')
    
    html = html.replace('color: rgba(255,255,255,0.55)', 'color: var(--text-muted)')
    html = html.replace('color: rgba(255,255,255,0.4)', 'color: var(--text-muted)')
    html = html.replace('color: rgba(255,255,255,0.3)', 'color: var(--text-muted)')
    html = html.replace('color: rgba(255,255,255,0.35)', 'color: var(--text-muted)')
    html = html.replace('color: rgba(255,255,255,0.25)', 'color: var(--text-muted)')
    html = html.replace('color: rgba(255,255,255,0.2)', 'color: var(--text-muted)')
    html = html.replace('color: rgba(255,255,255,0.15)', 'color: var(--text-muted)')
    
    # 3. Borders / Background overlays
    html = html.replace('border: 1px solid rgba(255,255,255,0.06)', 'border: 1px solid var(--border)')
    html = html.replace('border-bottom: 1px solid rgba(255,255,255,0.06)', 'border-bottom: 1px solid var(--border)')
    html = html.replace('border-left: 1px solid rgba(255,255,255,0.06)', 'border-left: 1px solid var(--border)')
    
    html = html.replace('background: rgba(255,255,255,0.06)', 'background: var(--bg-alt)')
    html = html.replace('background: rgba(255,255,255,0.03)', 'background: var(--bg)')
    html = html.replace('background: rgba(255,255,255,0.015)', 'background: var(--bg-tint)')
    
    # 4. Specific dark mode artifacts
    html = html.replace('background: rgba(13,138,116,0.08)', 'background: rgba(13,138,116,0.04)') # make green softer on light mode
    
    html = html.replace('rgba(255, 255, 255, 0.08)', 'var(--border)')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Color updates applied to bring pages into global light palette.")

