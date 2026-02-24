import os, re

ingredients_path = r'e:\OXYBIO\ingredients.html'
with open(ingredients_path, 'r', encoding='utf-8') as f:
    idx = f.read()

# Update Hero Section Typography
idx = idx.replace('font-size:clamp(3.5rem, 7vw, 6.5rem);', 'font-size:var(--text-6xl); line-height:var(--leading-none);')
idx = idx.replace('font-size:1.25rem;', 'font-size:var(--text-xl); line-height:var(--leading-relaxed);')

# Update ingredient cards
idx = idx.replace('font-size:1.5rem;', 'font-size:var(--text-xl); line-height:var(--leading-tight);')
idx = idx.replace('font-size:0.95rem; line-height:1.6;', 'font-size:var(--text-base); line-height:var(--leading-relaxed);')

# Make the doses stand out uniquely
idx = idx.replace('font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;',
                  'font-family:var(--font-mono); font-size:var(--text-sm); padding-top:1rem; border-top:1px dashed var(--border); color:var(--accent-mid); font-weight:700;')

# Add the clinical-container class to the main bento grid sections
idx = idx.replace('<div class="bento-grid">', '<div class="bento-grid clinical-container" style="padding: 1.5rem; background: var(--bg-alt);">')

with open(ingredients_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("Updated ingredients.html with rigorous typography and clinical boundaries.")
