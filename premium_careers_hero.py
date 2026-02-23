import codecs
import re

with codecs.open('e:\\OXYBIO\\careers.html', 'r', 'utf-8') as f:
    html = f.read()

# New Start-Up Focused Hero Section content
NEW_HERO_CONTENT = '''        <div class="flow-left reveal" style="max-width:1000px;">
            <div class="badge" style="margin-bottom:var(--space-lg); border-color:var(--text-main); color:var(--text-main); background:transparent;">Join Our Mission</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 8vw, 6.5rem); line-height:0.9; letter-spacing:-0.03em; margin-bottom:2rem;">
                A biotech startup.<br><em style="color:var(--text-muted); font-weight:400;">Challenging the status quo.</em>
            </h1>
            <p class="subtext editorial-col" style="font-size:clamp(1.25rem, 2vw, 1.5rem); line-height:1.6; color:var(--text-main); max-width:800px;">
                We are looking for high-agency builders, obsessive formulation scientists, and ambitious engineers to disrupt a stagnant industry. Fast-paced, science-first, and mission-driven. Help us build India's very first evidence-based precision nutrition system from the ground up at TBI, Adhiyamaan College of Engineering.
            </p>
        </div>'''

# Regex to safely replace just the flow-left div containing the hero text
pattern = re.compile(
    r'<div class=\"flow-left reveal\" style=\"max-width:1000px;\">.*?</div>',
    re.DOTALL
)

if pattern.search(html):
    new_html = pattern.sub(NEW_HERO_CONTENT, html, count=1)
    with codecs.open('e:\\OXYBIO\\careers.html', 'w', 'utf-8') as f:
        f.write(new_html)
    print("careers.html hero upgraded to Startup mode.")
else:
    print("Failed to find target div.")
