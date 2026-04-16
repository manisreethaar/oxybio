import re

filepath = r"E:\OXYBIO-WEBSITE\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Duel Comparison Section
content = re.sub(r'<!-- \S*?\n DUEL COMPARISON.*?</section>', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed Comparison Table")
