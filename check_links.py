import re
with open('problem.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<a[^>]+href="ingredients.html"[^>]*>', text):
    print(m.group())
