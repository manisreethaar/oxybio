import os
import re

# 1. Bump hero clearance to an undeniable safe zone on mobile
# We will change clamp(120px, 15vh, 180px) --> clamp(160px, 20vh, 200px)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply hero clearance bump
    html = html.replace('clamp(120px, 15vh, 180px)', 'clamp(160px, 20vh, 200px)')
    
    # 2. Fix problem.html table overflow
    if filename == 'problem.html':
        # wrap the table
        if '<div class="table-responsive"' not in html:
            html = html.replace('<table class="data-journal-table"', '<div class="table-responsive" style="overflow-x: auto; width: 100%; -webkit-overflow-scrolling: touch;"><table class="data-journal-table" style="min-width:400px;"')
            html = html.replace('</table>\n                    </div>\n                </div>', '</table>\n                    </div></div>\n                </div>')
            # Alternatively, simpler regex:
    
    # Let's do a more robust replacement for the table in problem.html
    if filename == 'problem.html':
        # the table block is inside a div:
        # <div style="flex:1; min-width:300px;">
        #   <table class="data-journal-table" style="background:#111; color:#fff;">
        table_start = '<table class="data-journal-table"'
        # if not already wrapped
        if 'overflow-x: auto;' not in html.split(table_start)[0][-100:]:
            html = html.replace(table_start, '<div style="width:100%; overflow-x:auto; padding-bottom:1rem;"><table class="data-journal-table" style="min-width:400px; width:100%;"')
            html = html.replace('</table>', '</table></div>')
            
    # 3. Fix ingredients.html card paddings
    if filename == 'ingredients.html':
        # replace static padding:2.5rem; with fluid clamp
        html = re.sub(r'padding:\s*2\.5rem\s*;', 'padding: clamp(1.25rem, 5vw, 2.5rem);', html)
        html = re.sub(r'padding:\s*3rem\s*;', 'padding: clamp(1.5rem, 5vw, 3rem);', html)
        # Fix the word-break or hyphenation for the ingredient titles & descriptions
        html = html.replace('class="premium-card-hover"', 'class="premium-card-hover" style="word-break: break-word;"')

    # Bump cache
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=27"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied massive hero clearance bump, fixed table overflow, and injected fluid card paddings.")
