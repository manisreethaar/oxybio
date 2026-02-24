import codecs
import re

with codecs.open('e:\\OXYBIO\\index.html', 'r', 'utf-8') as f:
    html = f.read()

# Define the new HTML
new_html = """
            <!-- CSS STICKY STACKED CARDS -->
            <section id="solution-cards" style="background:var(--bg-alt); padding-top: 2rem; padding-bottom: 4rem; position: relative;">
                <div class="container" style="display: flex; flex-direction: column; gap: 0;">
                    
                    <!-- VITALITY -->
                    <div class="apple-slide" id="slide-vitality" style="position:sticky; top:20px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10;">
                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:4rem; align-items:center;" class="mobile-stack-card">
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; display:flex; align-items:center; gap:0.75rem;"><span style="display:inline-block; width:20px; height:1px; background:var(--text-muted);"></span>01 / Pre-Clinical Optimization</div>
                                <h3 class="display" style="font-size:clamp(3.5rem,7vw,5.5rem); line-height:0.9; letter-spacing:-0.04em; margin:0 0 0.75rem;">VITALITY</h3>
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; border:1px solid var(--border); display:inline-block; padding:0.3rem 0.75rem;">Daily Deficiencies</div>
                                <p style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.</p>
                                <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Covers 50% of your daily nutrient needs</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Sustained energy without sugar spikes</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Stress adaptation with KSM-66 Ashwagandha</li>
                                </ul>
                            </div>
                            <div style="background:var(--text-main); padding:2rem; color:#fff; position:relative; overflow:hidden;">
                                <div style="position:absolute; right:-1rem; bottom:-1rem; font-family:var(--font-serif); font-size:6rem; font-weight:900; color:rgba(255,255,255,0.05); line-height:1; pointer-events:none;">V</div>
                                <div style="position:relative;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.4); margin-bottom:1rem; text-transform:uppercase;">Formulation Stack</div>
                                    <p style="font-size:0.95rem; font-weight:600; line-height:1.65; color:#fff; margin:0;">Finger Millet, Ashwagandha KSM-66, Lion's Mane, Moringa, 22 Chelated Nutrients</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- CLARITY -->
                    <div class="apple-slide" id="slide-clarity" style="position:sticky; top:20px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);">
                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:4rem; align-items:center;" class="mobile-stack-card">
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; display:flex; align-items:center; gap:0.75rem;"><span style="display:inline-block; width:20px; height:1px; background:var(--text-muted);"></span>02 / Sensory Trials &amp; Taste Profiling</div>
                                <h3 class="display" style="font-size:clamp(3.5rem,7vw,5.5rem); line-height:0.9; letter-spacing:-0.04em; margin:0 0 0.75rem;">CLARITY</h3>
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; border:1px solid var(--border); display:inline-block; padding:0.3rem 0.75rem;">Cognitive Fatigue</div>
                                <p style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3 pm crash.</p>
                                <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Clean focus without caffeine crash</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Memory and attention support (Lion's Mane)</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>L-Theanine:Caffeine ratio 2.5:1 (clinically studied)</li>
                                </ul>
                            </div>
                            <div style="background:var(--text-main); padding:2rem; color:#fff; position:relative; overflow:hidden;">
                                <div style="position:absolute; right:-1rem; bottom:-1rem; font-family:var(--font-serif); font-size:6rem; font-weight:900; color:rgba(255,255,255,0.05); line-height:1; pointer-events:none;">C</div>
                                <div style="position:relative;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.4); margin-bottom:1rem; text-transform:uppercase;">Formulation Stack</div>
                                    <p style="font-size:0.95rem; font-weight:600; line-height:1.65; color:#fff; margin:0;">Lion's Mane, Bacopa Monnieri, L-Theanine, Natural Caffeine, Active B Vitamins</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- MOMENTUM -->
                    <div class="apple-slide" id="slide-momentum" style="position:sticky; top:20px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);">
                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:4rem; align-items:center;" class="mobile-stack-card">
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; display:flex; align-items:center; gap:0.75rem;"><span style="display:inline-block; width:20px; height:1px; background:var(--text-muted);"></span>03 / Formulation Finalized</div>
                                <h3 class="display" style="font-size:clamp(3.5rem,7vw,5.5rem); line-height:0.9; letter-spacing:-0.04em; margin:0 0 0.75rem;">MOMENTUM</h3>
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; border:1px solid var(--border); display:inline-block; padding:0.3rem 0.75rem;">Cellular Recovery</div>
                                <p style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.</p>
                                <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Faster muscle recovery (Kokum + Tart Cherry)</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>ATP production support (Cordyceps militaris)</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Strength and endurance (Creatine HCl + Citrulline)</li>
                                </ul>
                            </div>
                            <div style="background:var(--text-main); padding:2rem; color:#fff; position:relative; overflow:hidden;">
                                <div style="position:absolute; right:-1rem; bottom:-1rem; font-family:var(--font-serif); font-size:6rem; font-weight:900; color:rgba(255,255,255,0.05); line-height:1; pointer-events:none;">M</div>
                                <div style="position:relative;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.4); margin-bottom:1rem; text-transform:uppercase;">Formulation Stack</div>
                                    <p style="font-size:0.95rem; font-weight:600; line-height:1.65; color:#fff; margin:0;">Cordyceps, Creatine HCl, Kokum Extract, L-Citrulline, Electrolytes</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

# Extract the old wrapper block and JS using regex
import re
pattern = re.compile(r'<!-- Added via python to fix spacing -->.+?</script>', re.DOTALL)
html = pattern.sub(new_html, html)

with codecs.open('e:\\OXYBIO\\index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Replaced JS nested scroll with pure CSS sticky layer cards.")
