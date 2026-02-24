import os, re

problem_path = r'e:\OXYBIO\problem.html'
with open(problem_path, 'r', encoding='utf-8') as f:
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
            <div class="badge" style="margin-bottom:var(--space-md);">Formulation Science</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">The Science<br><em>Behind Oxygen.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                Every formulation decision has a reason. Every reason has a reference. Every reference is available to you.
            </p>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     LAYER 1: THE MARKET PROBLEM
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border);">
    <div class="container reveal">
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;" class="mobile-stack">
            
            <div style="position:sticky; top:120px;" class="flow-left">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Layer 01</span>
                </div>
                <h2 class="headline" style="margin-top:var(--space-sm);">The Market Problem</h2>
                <h3 style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-main); margin-top:0.5rem;">India Has a Nutrition Crisis</h3>
                <p class="subtext editorial-col" style="margin-top:var(--space-sm); font-size:1.05rem; color:var(--text-muted);">
                    That nobody is talking about honestly. These are not estimates — these are ICMR, NFHS-5, and WHO measurements.
                </p>
            </div>

            <div class="bento-grid">
                <!-- Stats -->
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <div class="data-num" data-target="90" data-suffix="%">70-90%</div>
                    <div class="data-label">Vitamin D Deficient (Urban Indians)</div>
                    <p style="margin-top:var(--space-xs); font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">(Source: ICMR Task Force, 2022)</p>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <div class="data-num" data-target="47" data-suffix="%">47%</div>
                    <div class="data-label">B12 Deficient (Total population)</div>
                    <p style="margin-top:var(--space-xs); font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">(Source: J. Nutritional Science)</p>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <div class="data-num" data-target="53" data-suffix="%">53%</div>
                    <div class="data-label">Iron Deficient (Working women)</div>
                    <p style="margin-top:var(--space-xs); font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">(Source: NFHS-5)</p>
                </div>
                <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                    <div class="data-num" data-target="68" data-suffix="%">68%</div>
                    <div class="data-label">Multiple Deficiencies (Urban pros)</div>
                    <p style="margin-top:var(--space-xs); font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">(Source: Recent clinical data)</p>
                </div>

                <!-- Consequences -->
                <div class="bento-cell" style="grid-column: span 12; background:var(--text-main); color:var(--bg); padding:3rem 2rem;">
                    <h4 style="font-family:var(--font-mono); font-size:0.85rem; color:#A3A3A3; margin-bottom:1.5rem; letter-spacing:0.1em;">THE CONSEQUENCES</h4>
                    
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(250px, 1fr)); gap:2rem;">
                        <div>
                            <h5 style="font-family:var(--font-sans); font-size:1.125rem; font-weight:600; color:#fff; margin-bottom:0.5rem;">Cognitive Impact</h5>
                            <p style="font-size:0.9rem; color:#ccc; line-height:1.5; margin-bottom:0.5rem;">Iron deficiency reduces cognitive performance by 15-20% in working adults.</p>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#888;">Am J Clinical Nutrition</span>
                        </div>
                        <div>
                            <h5 style="font-family:var(--font-sans); font-size:1.125rem; font-weight:600; color:#fff; margin-bottom:0.5rem;">Economic Impact</h5>
                            <p style="font-size:0.9rem; color:#ccc; line-height:1.5; margin-bottom:0.5rem;">Nutritional deficiency costs India an estimated ₹4.5 lakh crore annually in lost productivity.</p>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#888;">World Bank India Report</span>
                        </div>
                        <div>
                            <h5 style="font-family:var(--font-sans); font-size:1.125rem; font-weight:600; color:#fff; margin-bottom:0.5rem;">Fatigue Burden</h5>
                            <p style="font-size:0.9rem; color:#ccc; line-height:1.5; margin-bottom:0.5rem;">Chronic fatigue affects 38% of urban working population — directly tied to micronutrient gaps.</p>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#888;">ASSOCHAM Survey</span>
                        </div>
                    </div>
                    
                    <div style="margin-top:2.5rem; padding-top:1.5rem; border-top:1px solid #333; text-align:center;">
                        <span style="font-family:var(--font-serif); font-size:1.5rem; font-style:italic; color:#fff;">"This is a public health crisis hiding in plain sight."</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     LAYER 2: THE BEHAVIORAL PROBLEM
════════════════════════════════════════════════════════ -->
<section class="structure-section">
    <div class="container reveal">
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;" class="mobile-stack">
            
            <div style="position:sticky; top:120px;" class="flow-left">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Layer 02</span>
                </div>
                <h2 class="headline" style="margin-top:var(--space-sm);">The Behavioral Problem</h2>
                <h3 style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-main); margin-top:0.5rem;">The Intention-Action Gap</h3>
                <p class="subtext editorial-col" style="margin-top:var(--space-sm); font-size:1.05rem; color:var(--text-muted);">
                    Urban Indians are more health-aware than any previous generation. They read about nutrition. They know what protein is. And yet deficiency rates are rising.
                </p>
            </div>

            <div class="bento-grid">
                <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                    <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">01</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.5rem; color:var(--text-main);">Time Scarcity</h4>
                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">The average working professional in Bangalore or Mumbai works 52 hours per week. Commutes consume another 2-3 hours daily. What remains is insufficient for meal planning, preparation, and consistent nutritional coverage.</p>
                    <p style="font-family:var(--font-serif); font-style:italic; color:var(--text-main); font-weight:500;">"This is not laziness. It is mathematics."</p>
                </div>

                <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                    <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">02</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.5rem; color:var(--text-main);">Trust Deficit</h4>
                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">CSE (Centre for Science and Environment) found that 68% of tested health food products failed to meet their own label claims. Maggi. Baby food controversies. Protein spiking scandals. The rational response is skepticism.</p>
                    <p style="font-family:var(--font-serif); font-style:italic; color:var(--text-main); font-weight:500;">"Why buy something you cannot trust?"</p>
                </div>

                <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                    <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">03</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.5rem; color:var(--text-main);">Relevance Gap</h4>
                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">Most nutrition science is conducted in Western populations. Indian bodies have different gut microbiome composition, dietary baselines (predominantly vegetarian), cooking methods, and specific deficiency profiles.</p>
                    <p style="font-family:var(--font-serif); font-style:italic; color:var(--text-main); font-weight:500;">"A Western product is not optimally designed for an Indian professional."</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     LAYER 3: THE SUPPLY PROBLEM
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border);">
    <div class="container reveal">
        <div class="section-label" style="margin-bottom:var(--space-md);">
            <div class="section-label-line"></div>
            <span class="section-label-text">Layer 03</span>
        </div>
        <h2 class="headline" style="margin-bottom:0.5rem;">The Supply Problem</h2>
        <h3 style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-muted); margin-bottom:var(--space-lg);">The Market Response Has Been Inadequate</h3>

        <div style="overflow-x:auto;">
            <table style="width:100%; text-align:left; border-collapse:collapse; font-size:0.95rem; min-width:800px; background:var(--bg);">
                <thead>
                    <tr style="border-bottom:2px solid var(--text-main); font-family:var(--font-mono); color:var(--text-muted);">
                        <th style="padding:1.5rem 1rem; width:25%;">CATEGORY</th>
                        <th style="padding:1.5rem 1rem; width:25%;">WHAT THEY OFFER</th>
                        <th style="padding:1.5rem 1rem; width:50%;">WHY IT FAILS THE INDIAN PROFESSIONAL</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom:1px solid var(--border);">
                        <td style="padding:1.5rem 1rem; font-weight:600;">Traditional Health Drinks<br><span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); font-weight:normal;">(Horlicks, Complan, Boost)</span></td>
                        <td style="padding:1.5rem 1rem; color:var(--text-main);">Strong distribution, nostalgic taste.</td>
                        <td style="padding:1.5rem 1rem; color:var(--text-muted);">Sugar: 16-18g/serving. Cheapest synthetic forms. Zero adaptogens. Formulations designed in the 1970s.</td>
                    </tr>
                    <tr style="border-bottom:1px solid var(--border);">
                        <td style="padding:1.5rem 1rem; font-weight:600;">Protein Supplements<br><span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); font-weight:normal;">(MuscleBlaze, ON India)</span></td>
                        <td style="padding:1.5rem 1rem; color:var(--text-main);">High protein density.</td>
                        <td style="padding:1.5rem 1rem; color:var(--text-muted);">Designed for narrow outcome (muscle mass). Ignores micronutrient deficiency. Relevant primarily for gym users.</td>
                    </tr>
                    <tr style="border-bottom:1px solid var(--border);">
                        <td style="padding:1.5rem 1rem; font-weight:600;">Imported Premium<br><span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); font-weight:normal;">(AG1, Huel, Ritual)</span></td>
                        <td style="padding:1.5rem 1rem; color:var(--text-main);">Genuine science, high-quality forms.</td>
                        <td style="padding:1.5rem 1rem; color:var(--text-muted);">Prohibitively costly for daily use (₹350-500/serving), no Indian indigenous ingredients, don't understand Indian usage patterns.</td>
                    </tr>
                    <tr>
                        <td style="padding:1.5rem 1rem; font-weight:600;">Nutraceutical Startups<br><span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); font-weight:normal;">(Emerging D2C brands)</span></td>
                        <td style="padding:1.5rem 1rem; color:var(--text-main);">Modern positioning, good design.</td>
                        <td style="padding:1.5rem 1rem; color:var(--text-muted);">Most are marketing companies, not science companies. Label claims without clinical evidence, heavily under-dosed actives.</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div style="margin-top:var(--space-lg); padding:2rem; border-left:4px solid var(--text-main); background:var(--bg);">
            <p style="font-size:1.125rem; line-height:1.6; color:var(--text-main);">
                The market has affordable products that are inadequate. Quality products that are inaccessible. Indian products that lack rigour. Rigorous products that lack Indian relevance. 
            </p>
            <p style="font-size:1.125rem; font-weight:600; font-family:var(--font-serif); margin-top:1rem;">
                Affordable. Quality. Indian. Rigorous. This intersection is currently empty. Oxygen is being built to occupy it.
            </p>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     HOW WE SOLVE IT (Formulation Science)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="border-top:1px solid var(--border);">
    <div class="container reveal">
        <div class="section-label" style="margin-bottom:var(--space-md);">
            <div class="section-label-line"></div>
            <span class="section-label-text">How We Solve It</span>
        </div>
        <h2 class="headline" style="margin-bottom:var(--space-lg);">Our Formulation Science</h2>

        <div class="bento-grid">
            <!-- Bioavailability -->
            <div class="bento-cell" style="grid-column: span 12; background:var(--text-main); color:var(--bg);">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:2rem;">
                    <div style="flex:1; min-width:300px;">
                        <h3 style="font-family:var(--font-serif); font-size:2rem; margin-bottom:1rem; color:#fff;">01 / The Bioavailability Problem</h3>
                        <p style="font-size:1.05rem; color:#ccc; line-height:1.6; margin-bottom:2rem;">Form matters more than dose. Generic supplements use cheap forms with massive drop-off rates.</p>
                        
                        <div style="background:#111; padding:1.5rem; border-radius:4px; border:1px solid #333;">
                            <h4 style="font-family:var(--font-mono); font-size:0.85rem; color:#888; margin-bottom:1rem; letter-spacing:0.05em;">MTHFR GENE VARIANTS</h4>
                            <p style="font-size:0.95rem; color:#ccc; line-height:1.5;">~40% of Indians carry an MTHFR variant causing them to poorly process synthetic folic acid. Oxygen bypasses this completely by using <strong>5-MTHF</strong> (the active form).</p>
                        </div>
                    </div>
                    
                    <div style="flex:1; min-width:300px;">
                        <table style="width:100%; font-size:0.9rem;">
                            <thead>
                                <tr style="font-family:var(--font-mono); color:#888; border-bottom:1px solid #333;">
                                    <th style="text-align:left; padding-bottom:0.5rem;">NUTRIENT</th>
                                    <th style="text-align:left; padding-bottom:0.5rem;">GENERIC (Standard)</th>
                                    <th style="text-align:right; padding-bottom:0.5rem; color:#fff;">OXYGEN (Active)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="border-bottom:1px solid #222;">
                                    <td style="padding:1rem 0; font-weight:600; color:#fff;">Iron</td>
                                    <td style="padding:1rem 0; color:#888;">FeSO4 <span style="font-family:var(--font-mono);">(8%)</span></td>
                                    <td style="padding:1rem 0; text-align:right; color:#fff;">Fe-Bisglycinate <span style="font-family:var(--font-mono); color:#4ade80;">(28%)</span></td>
                                </tr>
                                <tr style="border-bottom:1px solid #222;">
                                    <td style="padding:1rem 0; font-weight:600; color:#fff;">Zinc</td>
                                    <td style="padding:1rem 0; color:#888;">ZnO <span style="font-family:var(--font-mono);">(12%)</span></td>
                                    <td style="padding:1rem 0; text-align:right; color:#fff;">Zn-Bisglycinate <span style="font-family:var(--font-mono); color:#4ade80;">(41%)</span></td>
                                </tr>
                                <tr style="border-bottom:1px solid #222;">
                                    <td style="padding:1rem 0; font-weight:600; color:#fff;">Magnesium</td>
                                    <td style="padding:1rem 0; color:#888;">MgO <span style="font-family:var(--font-mono);">(4%)</span></td>
                                    <td style="padding:1rem 0; text-align:right; color:#fff;">Mg-Glycinate <span style="font-family:var(--font-mono); color:#4ade80;">(23%)</span></td>
                                </tr>
                                <tr style="border-bottom:1px solid #222;">
                                    <td style="padding:1rem 0; font-weight:600; color:#fff;">B12</td>
                                    <td style="padding:1rem 0; color:#888;">Cyanocobalamin <span style="font-family:var(--font-mono);">(15%)</span></td>
                                    <td style="padding:1rem 0; text-align:right; color:#fff;">Methylcobalamin <span style="font-family:var(--font-mono); color:#4ade80;">(55%)</span></td>
                                </tr>
                                <tr>
                                    <td style="padding:1rem 0; font-weight:600; color:#fff;">Folate</td>
                                    <td style="padding:1rem 0; color:#888;">Folic Acid <span style="font-family:var(--font-mono);">(20%)</span></td>
                                    <td style="padding:1rem 0; text-align:right; color:#fff;">5-MTHF <span style="font-family:var(--font-mono); color:#4ade80;">(70%)</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- The Millet System -->
            <div class="bento-cell" style="grid-column: span 6; background:var(--bg-alt);">
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:1rem; color:var(--text-main);">02 / The Millet System</h3>
                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:1.5rem;">Ragi has 344mg of Calcium per 100g (beating milk). But raw Ragi contains phytic acid which binds minerals, reducing absorption by 60-70%.</p>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-main);">
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg);">1. Source organic from Karnataka</div>
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg);">2. Sprout/Malt (48h, lowers phytic acid 60%)</div>
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg);">3. Gentle Drying</div>
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg);">4. Micro-Milling</div>
                </div>
                <p style="margin-top:1.5rem; font-weight:600; font-family:var(--font-serif);">Result: Highly bioavailable mineral matrix.</p>
            </div>

            <!-- Mushroom Science -->
            <div class="bento-cell" style="grid-column: span 6; background:var(--bg-alt);">
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:1rem; color:var(--text-main);">03 / The Mushroom Science</h3>
                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:1.5rem;">Most brands grow mycelium on grain, use a single extraction, provide no compound verification, and cannot guarantee active β-glucan.</p>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-main);">
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg); border-left:4px solid var(--text-main);">Fruiting body only</div>
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg); border-left:4px solid var(--text-main);">Dual extraction (Hot water + Ethanol)</div>
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg); border-left:4px solid var(--text-main);">Megazyme AOAC verified</div>
                    <div style="border:1px solid var(--border); padding:0.75rem; background:var(--bg); border-left:4px solid var(--text-main);">≥30% β-glucan guaranteed</div>
                </div>
            </div>

        </div>
        
        <div style="margin-top:var(--space-md); text-align:center;">
            <a href="ingredients.html" class="btn btn-primary">Explore Ingredients Index</a>
        </div>
    </div>
</section>

</main>
"""

with open(problem_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + FOOTER)

print("Updated problem.html with deep formulation science content.")
