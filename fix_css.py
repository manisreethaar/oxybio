import re
filepath = r"e:\OXYBIO\assets\css\styles.css"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the missing brace at 5720
# Looks like: .phase-detail-bar-fill { ... opacity: 0.4; } .phase-bar-blue { ...
# The lint says line 5720 missing }. Wait, in our earlier view:
# 5712: .phase-detail-bar-fill { ... 5718: } 5720: .phase-bar-blue {
# Actually, the lint at 5720 might just be a lingering error, let's look closer.
# Let's fix the known error around 236:
content = content.replace("transition: transform 0.3s;\n}\n\n.nav-item:hover>a svg {", ".nav-item:hover>a svg {")
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
