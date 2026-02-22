import os

files_to_update = [
    r'e:\OXYBIO\assets\css\styles.css',
    r'e:\OXYBIO\index.html'
]

replacements = {
    # CSS variable hexes
    "16A34A": "0A0A0A",
    "1A7A3C": "0A0A0A",
    "84CC16": "A3A3A3",
    "D1FAE5": "E8E8E4",
    
    # RGBA greens
    "rgba(22, 163, 74,": "rgba(10, 10, 10,",
    "rgba(132, 204, 22,": "rgba(163, 163, 163,",
    "rgba(26, 122, 60,": "rgba(10, 10, 10,",
    
    # specific index.html inline styles
    "rgba(22,163,74,0.12)": "rgba(10,10,10,0.06)",
    "rgba(163,230,53,0.12)": "rgba(163,163,163,0.15)",
    
    # Outline button
    "btn-outline-green": "btn-outline"
}

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")
