import os, re

problem_path = r'e:\OXYBIO\problem.html'
with open(problem_path, 'r', encoding='utf-8') as f:
    idx = f.read()

# ADD THE BLUEPRINT AND STRUCTURAL TYPOGRAPHY TO PROBLEM PAGE
# 1. Update Hero Section Typography
idx = idx.replace('font-size:clamp(3.5rem, 7vw, 6.5rem);', 'font-size:var(--text-6xl); line-height:var(--leading-none);')
idx = idx.replace('font-size:1.25rem;', 'font-size:var(--text-xl); line-height:var(--leading-relaxed);')

# 2. Update Stats with UI/UX Progress Bars and Scale
idx = idx.replace('<div class="data-num" data-target="90" data-suffix="%">70-90%</div>', 
                  '<div class="data-num" data-target="90" data-suffix="%" style="font-size:var(--text-6xl); line-height:var(--leading-none); color:#DC2626;">70-90%</div>')
idx = idx.replace('<div class="data-label">Vitamin D Deficient (Urban Indians)</div>',
                  '<div class="data-label" style="font-size:var(--text-base); font-weight:600; margin-top:0.5rem; line-height:var(--leading-snug);">Vitamin D Deficient (Urban Indians)</div>\n                    <div class="stat-bar-container" style="display:block; margin: 1rem 0;"><div class="stat-bar-fill" style="width: 85%; background:#DC2626;"></div></div>')

idx = idx.replace('<div class="data-num" data-target="47" data-suffix="%">47%</div>', 
                  '<div class="data-num" data-target="47" data-suffix="%" style="font-size:var(--text-6xl); line-height:var(--leading-none); color:#DC2626;">47%</div>')
idx = idx.replace('<div class="data-label">B12 Deficient (Total population)</div>',
                  '<div class="data-label" style="font-size:var(--text-base); font-weight:600; margin-top:0.5rem; line-height:var(--leading-snug);">B12 Deficient (Total population)</div>\n                    <div class="stat-bar-container" style="display:block; margin: 1rem 0;"><div class="stat-bar-fill" style="width: 47%; background:#DC2626;"></div></div>')

idx = idx.replace('<div class="data-num" data-target="53" data-suffix="%">53%</div>', 
                  '<div class="data-num" data-target="53" data-suffix="%" style="font-size:var(--text-6xl); line-height:var(--leading-none); color:#DC2626;">53%</div>')
idx = idx.replace('<div class="data-label">Iron Deficient (Working women)</div>',
                  '<div class="data-label" style="font-size:var(--text-base); font-weight:600; margin-top:0.5rem; line-height:var(--leading-snug);">Iron Deficient (Working women)</div>\n                    <div class="stat-bar-container" style="display:block; margin: 1rem 0;"><div class="stat-bar-fill" style="width: 53%; background:#DC2626;"></div></div>')

idx = idx.replace('<div class="data-num" data-target="68" data-suffix="%">68%</div>', 
                  '<div class="data-num" data-target="68" data-suffix="%" style="font-size:var(--text-6xl); line-height:var(--leading-none); color:#DC2626;">68%</div>')
idx = idx.replace('<div class="data-label">Multiple Deficiencies (Urban pros)</div>',
                  '<div class="data-label" style="font-size:var(--text-base); font-weight:600; margin-top:0.5rem; line-height:var(--leading-snug);">Multiple Deficiencies (Urban pros)</div>\n                    <div class="stat-bar-container" style="display:block; margin: 1rem 0;"><div class="stat-bar-fill" style="width: 68%; background:#DC2626;"></div></div>')

# 3. Apply the class data-journal-table to the Supply Problem table and remove inline styles that conflict
old_table = '<table style="width:100%; text-align:left; border-collapse:collapse; font-size:0.95rem; min-width:800px; background:var(--bg);">'
new_table = '<table class="data-journal-table" style="min-width:800px; background:var(--bg);">'
idx = idx.replace(old_table, new_table)
idx = re.sub(r'<tr style="border-bottom:2px solid var\(--text-main\); font-family:var\(--font-mono\); color:var\(--text-muted\);">', '<tr>', idx)
idx = re.sub(r'<th style="padding:1\.5rem 1rem; width:[0-9]+%;">', '<th>', idx)
idx = re.sub(r'<tr style="border-bottom:1px solid var\(--border\);">', '<tr>', idx)
idx = re.sub(r'<td style="padding:1\.5rem 1rem;([^"]*)">', r'<td style="\1">', idx)

old_bio_table = '<table style="width:100%; font-size:0.9rem;">'
new_bio_table = '<table class="data-journal-table" style="background:#111; color:#fff;">'
idx = idx.replace(old_bio_table, new_bio_table)

with open(problem_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("Updated problem.html with data visualization, blueprint aesthetics, and typography scale.")
