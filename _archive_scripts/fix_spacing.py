import codecs

with codecs.open('e:\\OXYBIO\\index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Fix the top spacing gap in the Solution Section caused by Apple Scroll replacing static grids
html = html.replace('<div class="container" style="padding-top:12vh; flex-shrink:0; position:relative; z-index:10;">',
                    '<div class="container" style="padding-top:8vh; flex-shrink:0; position:relative; z-index:10;">')


# 2. Fix the huge white space gap under the Problem section copy
old_problem_grid = '<div style="display:grid;grid-template-columns:1fr 2fr;gap:var(--space-lg);align-items:start;"'
new_problem_grid = '<div style="display:grid;grid-template-columns:1fr 2fr;gap:var(--space-2xl);align-items:center;"'
html = html.replace(old_problem_grid, new_problem_grid)

old_problem_left = '<div style="position:sticky;top:120px;" class="flow-left reveal">'
new_problem_left = '<div class="flow-left reveal">'
html = html.replace(old_problem_left, new_problem_left)

with codecs.open('e:\\OXYBIO\\index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Spacing fixed!")
