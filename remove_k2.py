import re

filepath = r"E:\OXYBIO-WEBSITE\ingredients.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove remaining D3+K2
content = re.sub(r'<!-- Category: Synthesis Stack -->.*?</div>\s*</div>\s*</div>\s*</div>', '<!-- Category: Synthesis Stack -->\n</div>\n</div>', content, flags=re.DOTALL)

# And if there are any lingering empty divs
content = re.sub(r'<!-- Vitamin D3 \+ K2 -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed D3+K2 from ingredients")
