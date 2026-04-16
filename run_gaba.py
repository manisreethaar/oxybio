import re

# 1. science.html
with open('science.html', 'r', encoding='utf-8') as f:
    sh = f.read()

gaba_section = '''
<!-- NEW METHODOLOGY LAYERS -->
<section style="padding: 4rem 0; background: var(--bg); border-top: 1px solid var(--border);">
    <div class="container">
        <div style="max-width:800px; margin:0 auto;">
            <div style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-main); margin-bottom:1rem; letter-spacing:0.05em; border-bottom:1px solid var(--border); padding-bottom:0.5rem; display:inline-block;">R&amp;D FRAMEWORK</div>
            <h2 style="font-family:var(--font-serif); font-size:2.5rem; color:var(--text-main); margin-bottom:2rem; line-height:1.2;">The Phase 0 Validation Matrix.</h2>
            
            <div style="display:flex; flex-direction:column; gap:2rem;">
                
                <div style="border-left: 3px solid #0D8A74; padding-left:1.5rem;">
                    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                        <span style="background:#0D8A74; color:#fff; font-family:var(--font-mono); font-size:0.6rem; padding:0.25rem 0.5rem; border-radius:4px; font-weight:700; letter-spacing:0.1em;">PUBLISHED</span>
                        <h4 style="font-family:var(--font-serif); font-size:1.4rem; color:var(--text-main); margin:0;">Layer 01 / Fermented Base</h4>
                    </div>
                    <p style="font-size:0.95rem; color:var(--text-muted); line-height:1.6; margin:0;">Utilizing Ragi &amp; Karuppu Kavuni. Published literature confirms fermentation significantly reduces phytic acid, inherently increasing the bioavailability of indigenous minerals.</p>
                </div>

                <div style="border-left: 3px solid #eab308; padding-left:1.5rem;">
                    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                        <span style="background:#eab308; color:#fff; font-family:var(--font-mono); font-size:0.6rem; padding:0.25rem 0.5rem; border-radius:4px; font-weight:700; letter-spacing:0.1em;">PLAUSIBLE</span>
                        <h4 style="font-family:var(--font-serif); font-size:1.4rem; color:var(--text-main); margin:0;">Layer 02 / GABA Biosynthesis</h4>
                    </div>
                    <p style="font-size:0.95rem; color:var(--text-muted); line-height:1.6; margin:0;">Leveraging GAD-active *Lactobacillus plantarum*. We are actively validating the endogenous synthesis of Gamma-aminobutyric acid during the 48-hour fermentation cycle.</p>
                </div>

                <div style="border-left: 3px solid #f97316; padding-left:1.5rem;">
                    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                        <span style="background:#f97316; color:#fff; font-family:var(--font-mono); font-size:0.6rem; padding:0.25rem 0.5rem; border-radius:4px; font-weight:700; letter-spacing:0.1em;">PLANNED</span>
                        <h4 style="font-family:var(--font-serif); font-size:1.4rem; color:var(--text-main); margin:0;">Layer 03 / Species-Specific Extracts</h4>
                    </div>
                    <p style="font-size:0.95rem; color:var(--text-muted); line-height:1.6; margin:0;">Hot-water extraction of fruiting bodies (Lion's Mane, Cordyceps, Reishi). Investigating the synergistic suspension of beta-glucans and hericenones within the fermented matrix.</p>
                </div>
                
            </div>
        </div>
    </div>
</section>
'''

if "The Phase 0 Validation Matrix." not in sh:
    sh = sh.replace("</main>", gaba_section + "\n</main>")
    with open('science.html', 'w', encoding='utf-8') as f:
        f.write(sh)

print("Science fixed.")
