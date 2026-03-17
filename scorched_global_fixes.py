import glob
import re
import os

html_files = glob.glob('e:/OXYBIO/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Purge <title> and <meta> tags ---
    # We want titles to look like: "Oxygen Bioinnovations | DETI@ACE TBI, Hosur"
    old_meta_desc_1 = "Real food built for absolute performance. We combine traditional millet fermentation with medicinal mushrooms for athletic regeneration, enhanced memory, and active professionals."
    new_meta_desc = "Oxygen Bioinnovations | R&D Lab currently active in DETI@ACE TBI, Hosur. Developing indigenous Indian biological models."
    # Wait, some pages might have customized meta descriptions. Let's just do a regex replace on all standard marketing ones.
    content = content.replace(old_meta_desc_1, new_meta_desc)
    content = re.sub(r'<title>.*?Oxygen Bioinnovations</title>', '<title>Oxygen Bioinnovations | DETI@ACE TBI</title>', content)

    # --- 2. Schema Org Description ---
    content = content.replace('"description": "Real food built for absolute performance. We combine traditional millet fermentation with medicinal mushrooms for athletic regeneration, enhanced memory, and active professionals."',
                              '"description": "Oxygen Bioinnovations | R&D Lab currently active in DETI@ACE TBI, Hosur."')

    # --- 3. Destroy Mega-Menu Marketing Logic ---
    content = content.replace('<h4>Who is Oxygen?</h4>', '<h4>Lab Priorities</h4>')
    content = content.replace('<p>Engineering India\'s first bio-fermented functional foods.</p>', '<p>Research targets and unvarnished realities.</p>')
    content = content.replace('<span class="link-desc">Why we started and what we built before launch.</span>', '<span class="link-desc">Frustrations and the realities of incubation.</span>')
    content = content.replace('<h4>The Science of Fermentation</h4>', '<h4>The Scientific Mechanisms</h4>')
    content = content.replace('<span class="link-desc">Understand the nutritional breakdown in urban India.</span>', '<span class="link-desc">The biological deficits mapping our targets.</span>')
    
    # "Ingredients Index" -> "Lab Materials"
    content = content.replace('Ingredients Index', 'Lab Materials')
    content = content.replace('Deep dive into every component of our formulations.', 'The raw extracts and compounds in our models.')
    
    # Footer "India's first..."
    footer_old = "Advanced functional foods for every ambitious Indian.<br><br>India's first bio-fermented nutrition system. Built on active millets, medicinal mushrooms, and real food science."
    footer_new = "R&D Lab incubating at DETI@ACE TBI.<br><br>Currently engineering experimental indigenous formulations using medicinal mushrooms and active millets. We do not have a launch product yet."
    footer_old_alt = "Advanced functional foods for every ambitious Indian.<br><br>India's first bio-fermented nutrition\n\n                    system. Built on active millets, medicinal mushrooms, and real food science."
    
    content = content.replace(footer_old, footer_new)
    content = content.replace(footer_old_alt, footer_new)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Global metadata, mega-menus, and footers rewritten as lab logs in {len(html_files)} files.")
