import os, re

ingredients_path = r'e:\OXYBIO\ingredients.html'
with open(ingredients_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_CONTENT = """
<main>

<!-- ═══════════════════════════════════════════════════════
     HERO SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="padding-top:140px; border-bottom:none;">
    <div class="container">
        <div class="flow-left reveal" style="max-width:900px; margin-bottom:var(--space-xl);">
            <div class="badge" style="margin-bottom:var(--space-md);">Full Transparency</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">Every ingredient.<br><em>Every reason.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                Nothing in Oxygen is there by accident. Nothing is there for label appeal. Everything has peer-reviewed evidence for its inclusion.
            </p>
        </div>
        
        <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:var(--space-md);">
            <span>CATEGORIES:</span>
            <a href="#millet" style="color:var(--text-main); text-decoration:none;">Millet Base</a> ·
            <a href="#mushroom" style="color:var(--text-main); text-decoration:none;">Mushroom Complex</a> ·
            <a href="#adaptogens" style="color:var(--text-main); text-decoration:none;">Adaptogens</a> ·
            <a href="#cognitive" style="color:var(--text-main); text-decoration:none;">Cognitive Stack</a> ·
            <a href="#performance" style="color:var(--text-main); text-decoration:none;">Performance Stack</a>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     INGREDIENTS LIST (Bento Architecture)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border);">
    <div class="container">
        
        <!-- Category: Millet Base -->
        <div id="millet" class="reveal" style="margin-bottom:var(--space-xl);">
            <div class="section-label" style="margin-bottom:var(--space-md);">
                <div class="section-label-line"></div>
                <span class="section-label-text">The Foundation</span>
            </div>
            <h2 class="headline" style="margin-bottom:var(--space-md);">Millet Base</h2>
            
            <div class="bento-grid">
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Finger Millet (Ragi)</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">India's most nutritious forgotten grain</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Sprouted & micro-milled flour. Standardized to 344mg calcium/100g.</p>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                        DOSE: 8g
                    </div>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Pearl Millet (Bajra)</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The iron-rich ancient grain of Rajasthan</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Whole grain micro-milled flour. Standardized to 8mg iron/100g.</p>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                        DOSE: 4g
                    </div>
                </div>
            </div>
        </div>

        <!-- Category: Mushroom Complex -->
        <div id="mushroom" class="reveal" style="margin-bottom:var(--space-xl);">
            <div class="section-label" style="margin-bottom:var(--space-md);">
                <div class="section-label-line"></div>
                <span class="section-label-text">Fungi Intelligence</span>
            </div>
            <h2 class="headline" style="margin-bottom:var(--space-md);">Mushroom Complex</h2>
            
            <div class="bento-grid">
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Lion's Mane</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The neurotrophic mushroom</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Hot-water + ethanol dual extract (fruiting body). Standardized ≥30% β-glucan, ≥1% hericenones. Stimulates NGF.</p>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Cordyceps</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The ATP production mushroom</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Hot-water extract (fruiting body). Standardized ≥1% cordycepin. Enhances cellular ATP production.</p>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Reishi</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The immune modulation mushroom</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Dual extract (fruiting body). Standardized ≥30% polysaccharides, ≥2% triterpenes.</p>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Chaga</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The antioxidant powerhouse</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Hot-water extract. Standardized ≥30% polysaccharides.</p>
                </div>
            </div>
        </div>

        <!-- Category: Adaptogens -->
        <div id="adaptogens" class="reveal" style="margin-bottom:var(--space-xl);">
            <div class="section-label" style="margin-bottom:var(--space-md);">
                <div class="section-label-line"></div>
                <span class="section-label-text">Botanical Resilience</span>
            </div>
            <h2 class="headline" style="margin-bottom:var(--space-md);">Adaptogens</h2>
            
            <div class="bento-grid">
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Ashwagandha KSM-66®</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The stress adaptation root</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Full-spectrum root extract. Standardized ≥5% withanolides.</p>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                        DOSE: 600mg
                    </div>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Moringa</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The nutrient-dense Indian superfood</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Shade-dried leaf powder. Standardized min 2% total flavonoids.</p>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                        DOSE: 500mg
                    </div>
                </div>
                <div class="bento-cell" style="grid-column: span 12; background:var(--bg);">
                    <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Bacopa Monnieri</h3>
                    <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">The Ayurvedic memory herb</p>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Standardized extract ≥50% bacosides.</p>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                        DOSE: 300mg
                    </div>
                </div>
            </div>
        </div>

        <!-- Category: Cognitive & Performance Stack -->
        <div class="reveal" style="display:grid; grid-template-columns:1fr 1fr; gap:var(--space-lg);" class="mobile-stack">
            <!-- Cognitive Stack -->
            <div id="cognitive">
                <div class="section-label" style="margin-bottom:var(--space-md);">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Focus & Mental Clarity</span>
                </div>
                <h2 class="headline" style="margin-bottom:var(--space-md);">Cognitive Stack</h2>
                
                <div class="bento-grid">
                    <div class="bento-cell" style="grid-column: span 12; background:var(--bg);">
                        <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">L-Theanine</h3>
                        <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Calm focus without sedation</p>
                        <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Pharmaceutical-grade L-Theanine ≥98% purity. Provides relaxed alertness when paired with caffeine.</p>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                            DOSE: 200mg
                        </div>
                    </div>
                </div>
            </div>

            <!-- Performance Stack -->
            <div id="performance">
                <div class="section-label" style="margin-bottom:var(--space-md);">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Cellular Repair</span>
                </div>
                <h2 class="headline" style="margin-bottom:var(--space-md);">Performance Stack</h2>
                
                <div class="bento-grid">
                    <div class="bento-cell" style="grid-column: span 12; background:var(--bg);">
                        <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">Creatine HCl</h3>
                        <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Strength and power, bioavailable form</p>
                        <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">38x more soluble than monohydrate, no loading phase. ≥99% purity.</p>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                            DOSE: 2g
                        </div>
                    </div>
                    <div class="bento-cell" style="grid-column: span 12; background:var(--bg);">
                        <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.25rem;">L-Citrulline</h3>
                        <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Blood flow and endurance amplifier</p>
                        <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Free-form L-Citrulline for nitric oxide production. ≥99% purity.</p>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                            DOSE: 3g
                        </div>
                    </div>
                    <div class="bento-cell" style="grid-column: span 12; background:var(--bg);">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;" class="mobile-stack">
                            <div>
                                <h3 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.25rem;">Kokum Extract</h3>
                                <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem; letter-spacing:0.05em; text-transform:uppercase;">India's recovery fruit</p>
                                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Standardized fruit extract ≥10% garcinol potent anti-inflammatory.</p>
                                <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                                    DOSE: 500mg
                                </div>
                            </div>
                            <div>
                                <h3 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.25rem;">Chelated Electrolyte Complex</h3>
                                <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem; letter-spacing:0.05em; text-transform:uppercase;">Hydration with absorption</p>
                                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-main); margin-bottom:1rem;">Albion TRAACS® Sodium, Potassium, Magnesium bisglycinate. Highly bioavailable.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     FOOTER NOTE (CoA)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--text-main); color:var(--bg); border:none;">
    <div class="container" style="text-align:center; padding:var(--space-md) 0;">
        <h4 style="font-family:var(--font-mono); font-size:0.85rem; color:#A3A3A3; margin-bottom:1rem; letter-spacing:0.1em;">THE OXYGEN GUARANTEE</h4>
        <h2 style="font-family:var(--font-serif); font-size:2rem; margin-bottom:1rem; color:#fff;">Full Certificate of Analysis for every batch.</h2>
        <p style="font-size:1.125rem; line-height:1.6; color:#ccc; max-width:600px; margin:0 auto;">
            When we launch, every batch will have a publicly available CoA with third-party verified test results. Scan the QR code on any product to see the exact test report for your batch.
        </p>
    </div>
</section>

</main>
"""

with open(ingredients_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + FOOTER)

print("Updated ingredients.html with the new transparent index.")
