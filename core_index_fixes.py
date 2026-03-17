import re

files = ['e:/OXYBIO/index.html', 'e:/OXYBIO/index-single.html']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change section label
    content = content.replace('<span class="section-label-text">The Solution / Products</span>', '<span class="section-label-text">Our Formulation Targets</span>')
    content = content.replace('<h2 class="display" style="font-size:clamp(3rem, 6vw, 4.5rem); line-height:1; letter-spacing:-0.03em; margin-bottom:1.5rem;">Three functional food formulation targets under research</h2>', '<h2 class="display" style="font-size:clamp(3rem, 6vw, 4.5rem); line-height:1; letter-spacing:-0.03em; margin-bottom:1.5rem;">Targets currently in research</h2>')
    
    # Change "Formulation Designed" tag
    content = content.replace('<div class="status-badge" style="background:rgba(13,138,116,0.1); color:#0D8A74; padding:0.4rem 1rem; border-radius:50px; font-size:0.8rem; font-weight:600; display:inline-block; margin-bottom:1rem;">Formulation Designed</div>', '<div class="status-badge" style="background:rgba(13,138,116,0.1); color:#0D8A74; padding:0.4rem 1rem; border-radius:50px; font-size:0.8rem; font-weight:600; display:inline-block; margin-bottom:1rem;">Research Target</div>')

    # Change Vitality bullets
    content = content.replace('Covers 50% of your daily nutrient needs', 'Targeting 50% baseline coverage of daily micronutrient gaps')
    content = content.replace('Formulated with highly bioavailable Iron Bisglycinate', 'Testing Iron Bisglycinate vs standard sulfates for higher absorption')
    content = content.replace('Fermented millets optimize digestion & gut health', 'Researching fermented millets for optimal gut transit times')

    # Change Clarity bullets
    content = content.replace('Clean focus without caffeine crash', 'Mapping cognitive endurance without standard caffeine spikes')
    content = content.replace('Uses precise L-Theanine:Caffeine ratio (evidence-backed)', 'Experimenting with exact L-Theanine:Caffeine clinical ratios')
    content = content.replace('Lion\'s Mane extract naturally stimulates Nerve Growth Factor', 'Sourcing Lion\'s Mane standardized to stimulate Nerve Growth Factor')

    # Change Momentum bullets
    content = content.replace('Faster muscle recovery', 'Testing recovery metrics post-workout')
    content = content.replace('Cordyceps extract improves ATP production & stamina', 'Evaluating Cordyceps standardization for ATP improvement')
    content = content.replace('Ashwagandha KSM-66 actively lowers post-stress cortisol', 'Incorporating KSM-66 protocols for cortisol modulation')


    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("index and index-single product cards rebuilt into 'targets in research'.")
