import re
with open('problem.html', 'r', encoding='utf-8') as f:
    text = f.read()

def get_div_diff(html):
    return html.count('<div') - html.count('</div')

print('Overall diff:', get_div_diff(text))

layers = re.split(r'(<section\s+id="layer-\d+"[\s\S]*?</section>)', text, flags=re.IGNORECASE)
for i, layer in enumerate(layers):
    if '<section id="layer-' in layer.lower():
        print(f'Layer index {i} diff: ', get_div_diff(layer))
    else:
        print(f'Non-layer index {i} diff: ', get_div_diff(layer))
