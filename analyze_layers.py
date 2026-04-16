import re
with open('problem.html', 'r', encoding='utf-8') as f:
    text = f.read()

layers = re.split(r'(<section\s+id="layer-\d+"[\s\S]*?</section>)', text, flags=re.IGNORECASE)
print(layers[3][:100])
print(layers[5][:100])
