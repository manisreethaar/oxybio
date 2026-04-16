"""
Safely audit each HTML page and report ONLY the hero/section top padding 
and color patterns actually used — so we know exactly what to fix.
Does NOT modify anything.
"""
import glob, re

files = ['index.html', 'about.html', 'science.html', 'problem.html', 
         'ingredients.html', 'careers.html', 'blog.html', 'contact.html', 
         'faq.html', 'life.html']

print("=" * 60)
print("HERO/SECTION PADDING AUDIT")
print("=" * 60)

for f in files:
    try:
        html = open(f, 'r', encoding='utf-8').read()
    except:
        print(f"\n{f}: CANNOT READ")
        continue
    
    print(f"\n--- {f} ---")
    
    # Find inline padding-top values on hero/first sections
    pad_matches = re.findall(
        r'(?:class="[^"]*hero[^"]*"[^>]*|id="[^"]*hero[^"]*"[^>]*|style="[^"]*padding-top[^"]*")[^>]*',
        html, re.IGNORECASE
    )
    for m in pad_matches[:3]:
        # extract just the padding
        pt = re.search(r'padding-top\s*:\s*([^;"\s]+)', m)
        if pt:
            print(f"  Hero pad-top: {pt.group(1)}")
    
    # Check what color is used for h1/h2 in inline styles
    color_patterns = re.findall(r'<h[12][^>]*style="[^"]*color\s*:\s*([^;"\s]+)', html)
    if color_patterns:
        print(f"  H1/H2 inline colors: {set(color_patterns[:5])}")
    
    # Check if uses hero-section class
    uses_hero_class = 'class="hero-section"' in html or "class='hero-section'" in html
    print(f"  Uses .hero-section class: {uses_hero_class}")
    
    # Check page-specific inline padding on first section after nav
    first_section = re.search(r'<section([^>]*)>', html[html.find('</header>'):html.find('</header>')+2000] if '</header>' in html else html[:2000])
    if first_section:
        style = re.search(r'style="([^"]*)"', first_section.group(1))
        if style:
            print(f"  First section style: {style.group(1)[:100]}")

print("\n" + "=" * 60)
