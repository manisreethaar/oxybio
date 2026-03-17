import re

file_path = 'e:/OXYBIO/about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Vision Header
content = content.replace('>Vision &amp; Mission</h2>', '>Our Lab Priorities</h2>')
content = content.replace('To build an innovation-driven biotechnology enterprise that prioritizes planetary health', 'To prove that indigenous Indian biology can be engineered into world-class nutrition.')

# Replace Mission Subheaders and texts
content = content.replace('>Building India\'s First Functional Food System.</h3>', '>1. Prove Indian Biology Works.</h3>')
content = content.replace('alongside human health — by transforming India\'s rich biological resources into globally', 'We are transforming India\'s rich but overlooked biological resources (like millets and adaptogenic mushrooms) into globally')
content = content.replace('competitive, evidence-backed products.', 'competitive, evidence-backed functional foods. We do not need to import our science.')

content = content.replace('>To make world-class nutrition accessible to every ambitious Indian.</h3>', '>2. Absolute Dose Transparency.</h3>')
content = content.replace('Oxygen exists to close the gap between what urban Indians need nutritionally and what the', 'If an ingredient is included, it must be included at the minimum clinical threshold required to trigger a biological response. Otherwise, it is excluded.')
content = content.replace('market currently offers them.', 'There is zero room for label decoration in our facility.')

content = content.replace('>Building products that compete globally, made right here.</h3>', '>3. No Synthetic Masks.</h3>')
content = content.replace('To develop and commercialize safe, natural, and sustainable', 'We refuse to use synthetic fillers, artificial sweeteners, or cheap mineral oxides (like ferrous sulfate).')
content = content.replace('products using bioprocessing, fermentation, and formulation technologies, ensuring', 'Every active ingredient must be bioavailable by design, achieved through bioprocessing, fermentation, and advanced chelation.')
content = content.replace('financial viability and market competitiveness.', '')

content = content.replace('>Advancing the edge of indigenous biotechnology science.</h3>', '>4. Radical Iteration.</h3>')
content = content.replace('To strengthen indigenous biotechnology innovation by', 'We publish our progress and our failures. We are actively formulating in the DETI@ACE - TBI lab.')
content = content.replace('advancing research in bioprocess engineering, microbial fermentation, and', 'When a batch fails sensory testing or extraction quotas, we tear it down and rebuild.')
content = content.replace('nanotechnology, supported through government grants and academic collaboration.', '')

content = content.replace('>Creating long-term ecological and social impact in India.</h3>', '>5. The "Unnave Marundhu" Ethos.</h3>')
content = content.replace('To create long-term environmental, social, and economic', 'Food is medicine. This isn\'t a marketing slogan; it is the fundamental biological reality we are engineering our products around.')
content = content.replace('impact by supporting circular bioeconomy practices, enabling skill development through', '')
content = content.replace('student mentorship and internships, and aligning with Make in India.', '')

content = content.replace('Planetary health and human health, together.', '')
content = content.replace('India\'s biology — globally competitive products.', '')
content = content.replace('Advanced biotech, responsible manufacturing.', '')

# Fix bullet sidebars
content = content.replace('01. Core Vision', '01. The Mandate')
content = content.replace('02. The Mission', '02. Priority One')
content = content.replace('03. Operations', '03. Priority Two')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("about.html corporate phrasing removed.")
