import re

with open('problem.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I am going to find the precise start of the hero section and the start of layer-01
hero_start = html.find('<section class="hero-section"')
layer_01_start = html.find('<section id="layer-01"')

if hero_start != -1 and layer_01_start != -1:
    print("Found boundaries.")
    old_hero = html[hero_start:layer_01_start]
else:
    print("Error finding boundaries.")

# Look at layer 1 content preview
print(html[layer_01_start:layer_01_start+500])

