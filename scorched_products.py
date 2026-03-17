import re

files = ['e:/OXYBIO/index.html', 'e:/OXYBIO/index-single.html']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Brands with EXP codes
    content = content.replace('VITALITY</h3>', 'EXP_02</h3>')
    content = content.replace('Daily Deficiencies</div>', 'Foundational Micronutrient Target</div>')
    
    content = content.replace('CLARITY</h3>', 'EXP_01</h3>')
    content = content.replace('Cognitive Fatigue</div>', 'Cognitive Rhythm Target</div>')
    
    content = content.replace('MOMENTUM</h3>', 'EXP_03</h3>')
    content = content.replace('Cellular Recovery</div>', 'Kinematic Recovery Target</div>')

    # Replace the huge background letters
    content = content.replace('pointer-events:none;">\n\n                                    V</div>', 'pointer-events:none;">\n\n                                    02</div>')
    content = content.replace('pointer-events:none;">\n\n                                    C</div>', 'pointer-events:none;">\n\n                                    01</div>')
    content = content.replace('pointer-events:none;">\n\n                                    M</div>', 'pointer-events:none;">\n\n                                    03</div>')
    
    # Also fix "Formulation Designed" if it survived due to spacing
    content = content.replace('/ Formulation Designed', '/ Active Research Target')
    content = content.replace('/ Formulation Targets', '/ Active Research Target')

    # Fix the description texts to be even colder
    content = content.replace('For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.', 'Hypothesis: Establish an everyday nutritional baseline addressing systemic dietary gaps in urban populations.')
    content = content.replace('The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3 pm crash.', 'Hypothesis: Stabilize cognitive rhythm without inducing standard caffeine fatigue or cortisol spikes.')
    content = content.replace('An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.', 'Hypothesis: Accelerate true muscle repair and ATP production without synthetic stimulation.')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Scorched earth executed on index product cards.")
