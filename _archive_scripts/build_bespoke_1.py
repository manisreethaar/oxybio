import os, re

index_path = r'e:\OXYBIO\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_ABOUT = """
<main>
    <section class="bespoke-split">
        <div class="bespoke-split-sticky">
            <h1 style="font-size:clamp(3rem, 6vw, 5rem); line-height:1.1; margin-bottom:2rem; font-family:var(--font-serif); font-weight:800;">We were tired of being lied to by labels.</h1>
            <p style="font-size:1.25rem; color:var(--text-muted); max-width:480px;">So we built a brand that operates with absolute transparency.</p>
        </div>
        
        <div class="bespoke-split-content">
            <div style="max-width: 600px; margin:0 auto;">
                <div style="font-family:monospace; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:2rem;">01 / THE MANIFESTO</div>
                
                <h2 style="font-size:2.5rem; font-family:var(--font-serif); margin-bottom:2rem;">The nutrition industry is broken by design.</h2>
                <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); margin-bottom:1.5rem;">
                    If you open the back of any mainstream Indian health drink, you'll see a long list of vitamins and minerals. What they don't tell you is that they are using the absolute cheapest chemical forms available.
                </p>
                <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); margin-bottom:3rem;">
                    Ferrous sulfate instead of iron bisglycinate. Cyanocobalamin instead of methylcobalamin. Zinc oxide instead of zinc glycinate. These ingredients look good on a label, but your body can barely absorb them.
                </p>

                <div style="padding:-left:2rem; border-left:4px solid var(--text-main); margin:3rem 0;">
                    <p style="font-size:1.5rem; font-family:var(--font-serif); font-style:italic;">"We aren't building a marketing company. We are building a science company that happens to sell a product."</p>
                </div>

                <div style="font-family:monospace; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:2rem; margin-top:5rem;">02 / THE SOLUTION</div>
                
                <h2 style="font-size:2.5rem; font-family:var(--font-serif); margin-bottom:2rem;">Complete Transparency.</h2>
                <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); margin-bottom:1.5rem;">
                    Oxygen Bioinnovations was born out of the Technology Business Incubator (TBI) at Adhiyamaan College of Engineering in Hosur. We are technologists, formulators, and obsessionaries. 
                </p>
                <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); margin-bottom:3rem;">
                    We publish our clinical study designs before we run them. We use millet and mushroom extraction protocols that prioritize bioavailability, not just cheap mass scaling. 
                </p>
                
                <a href="science.html" class="btn btn-outline" style="border-radius:0;">Read the Science →</a>
            </div>
        </div>
    </section>
</main>
"""

MAIN_CAREERS = """
<main>
    <section class="typo-hero">
        <div class="container">
            <h1>We are looking for<br><em>obsessives.</em></h1>
            <p>We don't do regular hours. We don't do "good enough." We are building India's most important nutrition company, and we need people who treat their work as a craft.</p>
        </div>
    </section>

    <section style="padding: 8rem 0;">
        <div class="container">
            <div style="display:grid; grid-template-columns:1fr 2fr; gap:4rem;">
                <div>
                    <h2 style="font-size:2rem; font-family:var(--font-serif);">Open Missions</h2>
                    <p style="color:var(--text-muted); margin-top:1rem;">We don't have jobs. We have missions that need to be accomplished.</p>
                </div>
                
                <div style="border-top:1px solid var(--border);">
                    <div style="padding: 2rem 0; border-bottom:1px solid var(--border); display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <h3 style="font-size:1.5rem;">Lead Food Formulator</h3>
                            <p style="color:var(--text-muted); margin-top:0.5rem; font-family:monospace;">HOSUR (IN-LAB) / FULL-TIME</p>
                        </div>
                        <a href="#apply" class="btn btn-outline" style="border-radius:0;">Apply</a>
                    </div>
                    <div style="padding: 2rem 0; border-bottom:1px solid var(--border); display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <h3 style="font-size:1.5rem;">Clinical Research Coordinator</h3>
                            <p style="color:var(--text-muted); margin-top:0.5rem; font-family:monospace;">HOSUR / HYBRID</p>
                        </div>
                        <a href="#apply" class="btn btn-outline" style="border-radius:0;">Apply</a>
                    </div>
                    <div style="padding: 2rem 0; border-bottom:1px solid var(--border); display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <h3 style="font-size:1.5rem;">Head of Brand & Editorial</h3>
                            <p style="color:var(--text-muted); margin-top:0.5rem; font-family:monospace;">REMOTE (INDIA)</p>
                        </div>
                        <a href="#apply" class="btn btn-outline" style="border-radius:0;">Apply</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>
"""

pages = {
    'about.html': MAIN_ABOUT,
    'careers.html': MAIN_CAREERS
}

for name, main_html in pages.items():
    path = os.path.join(r'e:\OXYBIO', name)
    content = HEADER + main_html + '\n</main>\n' + FOOTER
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {name}")
