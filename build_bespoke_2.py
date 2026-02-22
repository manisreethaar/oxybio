import os, re

index_path = r'e:\OXYBIO\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_SCIENCE = """
<main>
    <section style="padding: clamp(8rem, 12vw, 12rem) 0 4rem; background:var(--bg);">
        <div class="container">
            <h1 style="font-size:clamp(3.5rem, 8vw, 6rem); font-family:var(--font-serif); line-height:1; letter-spacing:-0.03em;">The Lab<br><em>Journal.</em></h1>
            <p style="margin-top:2rem; font-size:1.25rem; color:var(--text-muted); max-width:600px;">
                We don't do proprietary blends. We don't hide behind marketing claims. This is the exact science, the exact extracts, and the exact clinical data behind RIZE.
            </p>
        </div>
    </section>

    <section style="background:var(--bg-alt); padding:4rem 0 8rem;">
        <div class="container">
            <!-- Lab Journal Grid Item 1 -->
            <div class="lab-grid">
                <div class="lab-sidebar">
                    <span class="lab-sidebar-num">EXP_001 / MINERALS</span>
                    <h2 style="font-size:2rem; font-family:var(--font-serif); margin-top:1rem;">Chelation &<br>Bioavailability</h2>
                </div>
                <div class="lab-content-block">
                    <p style="font-size:1.125rem; line-height:1.7; color:var(--text-main); margin-bottom:1.5rem;">
                        The human body is highly inefficient at absorbing inorganic minerals like ferrous sulfate (the standard iron used in 95% of Indian health drinks). Ferrous sulfate has an absorption rate of approximately 8% and commonly causes severe GI distress.
                    </p>
                    <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); margin-bottom:2rem;">
                        We utilize <strong>Iron Bisglycinate</strong>, a chelated amino acid complex. The mineral is bound to two glycine molecules, allowing it to bypass standard ionization in the stomach and absorb intact in the intestines.
                    </p>
                    
                    <div style="background:var(--bg); border:1px solid var(--border); padding:2rem; font-family:monospace;">
                        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border); padding-bottom:1rem; margin-bottom:1rem;">
                            <span>FERROUS SULFATE (STD)</span>
                            <span style="color:var(--text-muted);">8% ABS</span>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <strong>IRON BISGLYCINATE (RIZE)</strong>
                            <strong>58% ABS</strong>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Lab Journal Grid Item 2 -->
            <div class="lab-grid">
                <div class="lab-sidebar">
                    <span class="lab-sidebar-num">EXP_002 / ADAPTOGENS</span>
                    <h2 style="font-size:2rem; font-family:var(--font-serif); margin-top:1rem;">Standardized<br>Extraction</h2>
                </div>
                <div class="lab-content-block">
                    <p style="font-size:1.125rem; line-height:1.7; color:var(--text-main); margin-bottom:1.5rem;">
                        A "mushroom powder" label means nothing. Without standardizing the active compounds (beta-glucans and triterpenes), you are essentially eating expensive mushroom-flavored flour.
                    </p>
                    <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); margin-bottom:2rem;">
                        Our Lion's Mane is extracted via dual hot-water and ethanol protocol, standardized specifically to <strong>&gt;30% Beta-D-Glucans</strong>. This is the exact dosage and extraction methodology used in peer-reviewed clinical trials demonstrating Nerve Growth Factor (NGF) stimulation.
                    </p>
                </div>
            </div>
            
            <div style="text-align:center; padding-top:4rem;">
                <a href="#clinical-trial" class="btn btn-outline" style="border-radius:0;">View Full Clinical Protocol →</a>
            </div>
        </div>
    </section>
</main>
"""

MAIN_BLOG = """
<main>
    <section style="padding: clamp(8rem, 12vw, 12rem) 0 4rem; border-bottom:1px solid var(--border);">
        <div class="container">
            <h1 style="font-size:clamp(3.5rem, 8vw, 6rem); font-family:var(--font-serif); line-height:1; letter-spacing:-0.03em;">The Editorial.</h1>
            <p style="font-family:monospace; letter-spacing:0.1em; color:var(--text-muted); margin-top:2rem;">OXYGEN BIOINNOVATIONS / RESEARCH DEPT.</p>
        </div>
    </section>

    <!-- Featured Cover Story -->
    <section style="padding: 4rem 0;">
        <div class="container">
            <div style="display:grid; grid-template-columns:1fr; gap:2rem; border:1px solid var(--border); background:var(--bg-alt);">
                <div style="padding:clamp(2rem, 5vw, 4rem);">
                    <div style="font-family:monospace; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:1.5rem;">LATEST RESEARCH / VOL 04</div>
                    <h2 style="font-size:clamp(2rem, 4vw, 3.5rem); font-family:var(--font-serif); margin-bottom:1.5rem;">Why 40% of Indians cannot process standard Folic Acid.</h2>
                    <p style="font-size:1.125rem; line-height:1.6; color:var(--text-muted); max-width:700px; margin-bottom:3rem;">
                        The MTHFR gene mutation is arguably the most undiagnosed nutritional bottleneck in the subcontinent. If you have it, the synthetic folic acid in your prenatal supplement is biologically useless. Here is why we use 5-MTHF instead.
                    </p>
                    <a href="#article" class="btn btn-primary" style="border-radius:0; background:var(--text-main); color:var(--bg);">Read Cover Story</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Article Grid -->
    <section style="padding: 4rem 0 8rem; background:var(--bg);">
        <div class="container">
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:2rem;">
                
                <a href="#post" style="border:1px solid var(--border); padding:2rem; transition:background 0.3s; display:block;" onmouseover="this.style.background='var(--bg-alt)'" onmouseout="this.style.background='transparent'">
                    <div style="font-family:monospace; font-size:0.8rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:1rem;">FORMULATION / VOL 03</div>
                    <h3 style="font-size:1.5rem; font-family:var(--font-serif); margin-bottom:1rem;">The Death of the "Proprietary Blend"</h3>
                    <p style="color:var(--text-muted); font-size:0.95rem;">Why burying ingredient doses in a 'health matrix' is the oldest trick in the supplement playbook.</p>
                </a>
                
                <a href="#post" style="border:1px solid var(--border); padding:2rem; transition:background 0.3s; display:block;" onmouseover="this.style.background='var(--bg-alt)'" onmouseout="this.style.background='transparent'">
                    <div style="font-family:monospace; font-size:0.8rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:1rem;">LAB NOTES / VOL 02</div>
                    <h3 style="font-size:1.5rem; font-family:var(--font-serif); margin-bottom:1rem;">Why we rejected 14 suppliers for our Ashwagandha</h3>
                    <p style="color:var(--text-muted); font-size:0.95rem;">Not all roots are created equal. Tracing the supply chain of our KSM-66 extract.</p>
                </a>
                
                <a href="#post" style="border:1px solid var(--border); padding:2rem; transition:background 0.3s; display:block;" onmouseover="this.style.background='var(--bg-alt)'" onmouseout="this.style.background='transparent'">
                    <div style="font-family:monospace; font-size:0.8rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:1rem;">FOUNDATION / VOL 01</div>
                    <h3 style="font-size:1.5rem; font-family:var(--font-serif); margin-bottom:1rem;">Millets over Malt: The Bioavailability Scaffold</h3>
                    <p style="color:var(--text-muted); font-size:0.95rem;">Why Ragi and Jowar represent a superior delivery matrix compared to traditional malted barley.</p>
                </a>

            </div>
        </div>
    </section>
</main>
"""

pages = {
    'science.html': MAIN_SCIENCE,
    'blog.html': MAIN_BLOG
}

for name, main_html in pages.items():
    path = os.path.join(r'e:\OXYBIO', name)
    content = HEADER + main_html + '\n</main>\n' + FOOTER
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {name}")
