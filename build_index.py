import os, re

index_path = r'e:\OXYBIO\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_CONTENT = """
<main>

<!-- ═══════════════════════════════════════════════════════
     HERO SECTION (Strict Asymmetrical Flow)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="padding-top:140px; border-bottom:none;">
    <div class="container">
        <div class="flow-left reveal" style="max-width:900px;">
            <div class="badge" style="margin-bottom:var(--space-md);">🌱 Currently in Development • TBI Incubated • Clinical Study Designed</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">Ancient Ingredients.<br>Modern Science.<br><em>No Compromise.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                India is building its first precision nutrition system. Built on Millet, Medicinal Mushrooms, and decades of scientific research. Designed for ambitious Indians who deserve better than what currently exists.
            </p>
            <div style="margin-top:var(--space-md); display:flex; gap:1rem; align-items:center; flex-wrap:wrap;">
                <a href="#join" class="btn btn-primary">Join Waitlist</a>
                <a href="problem.html" class="btn btn-outline">Read the Science</a>
            </div>
            <div style="margin-top:var(--space-md); font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); display:flex; gap:1.5rem; flex-wrap:wrap;">
                <span>✓ TBI Incubated Startup</span>
                <span>✓ FSSAI Licensing In Progress</span>
                <span>✓ 100% Indian Ingredients</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     MARQUEE SECTION (Technical)
════════════════════════════════════════════════════════ -->
<div class="marquee-section" style="border-top:1px solid var(--border); background:var(--bg-alt);">
    <div class="marquee-track" style="font-family:var(--font-mono); text-transform:uppercase; font-size:0.85rem;">
        <span class="marquee-item">TBI Incubated Startup <span class="marquee-dot"></span></span>
        <span class="marquee-item">Science-First Formulation <span class="marquee-dot"></span></span>
        <span class="marquee-item">FSSAI Licensing In Progress <span class="marquee-dot"></span></span>
        <span class="marquee-item">100% Indian Ingredients <span class="marquee-dot"></span></span>
        <span class="marquee-item">Third-Party Testing Planned <span class="marquee-dot"></span></span>
        <span class="marquee-item">Zero Artificial Ingredients <span class="marquee-dot"></span></span>
        <span class="marquee-item">Clinical Study Protocol Ready <span class="marquee-dot"></span></span>
        <span class="marquee-item">Peer-Reviewed Formulation <span class="marquee-dot"></span></span>
        <!-- Duplicate for infinite scroll -->
        <span class="marquee-item">TBI Incubated Startup <span class="marquee-dot"></span></span>
        <span class="marquee-item">Science-First Formulation <span class="marquee-dot"></span></span>
        <span class="marquee-item">FSSAI Licensing In Progress <span class="marquee-dot"></span></span>
        <span class="marquee-item">100% Indian Ingredients <span class="marquee-dot"></span></span>
        <span class="marquee-item">Third-Party Testing Planned <span class="marquee-dot"></span></span>
        <span class="marquee-item">Zero Artificial Ingredients <span class="marquee-dot"></span></span>
        <span class="marquee-item">Clinical Study Protocol Ready <span class="marquee-dot"></span></span>
        <span class="marquee-item">Peer-Reviewed Formulation <span class="marquee-dot"></span></span>
    </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     PROBLEM SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" id="problem">
    <div class="container">
        <div style="display:grid;grid-template-columns:1fr 2fr;gap:var(--space-lg);align-items:start;" class="mobile-stack">
            <div style="position:sticky;top:120px;" class="flow-left reveal">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">The Problem</span>
                </div>
                <h2 class="headline" style="margin-top:var(--space-sm);">You are probably nutritionally deficient.</h2>
                <p class="subtext editorial-col" style="margin-top:var(--space-sm);">Not because you are careless. Because modern Indian life makes proper nutrition almost impossible.</p>
                <div style="margin-top:var(--space-md);">
                    <a href="problem.html" class="btn btn-outline">Read the Clinical Data</a>
                </div>
            </div>

            <!-- Bento Structure for Problem Cards -->
            <div class="bento-grid reveal" style="margin-top:0;">
                
                <!-- KEY STATISTICS -->
                <div class="bento-cell" style="grid-column: span 6;">
                    <div class="data-num" data-target="73" data-suffix="%">73%</div>
                    <div class="data-label">Vitamin D Deficiency</div>
                    <p style="margin-top:var(--space-xs); font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">(Source: ICMR National Nutrition Survey)</p>
                </div>
                
                <div class="bento-cell" style="grid-column: span 6;">
                    <div class="data-num" data-target="50" data-suffix="%">50%</div>
                    <div class="data-label">Skip at least one meal/day</div>
                    <p style="margin-top:var(--space-xs); font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">(Source: ASSOCHAM Health Survey)</p>
                </div>

                <div class="bento-cell" style="grid-column: span 12;">
                    <div class="data-num" data-target="68" data-suffix="%">68%</div>
                    <div class="data-label">Indian health drinks fail their own label claims</div>
                    <p style="margin-top:var(--space-xs); font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">(Source: CSE Report 2023)</p>
                </div>

                <!-- PROBLEM DETAILS -->
                <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                    <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">01 / No time for real nutrition</h4>
                    <p style="color:var(--text-muted); line-height:1.6; font-size:0.95rem;">The average working professional has 22 minutes for lunch, often at their desk. Students skip meals before exams. Athletes eat whatever is convenient after training. The food system was not designed for how Indians actually live.</p>
                </div>

                <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                    <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">02 / Existing products deceive you</h4>
                    <p style="color:var(--text-muted); line-height:1.6; font-size:0.95rem;">Most Indian health drinks are primarily sugar with token doses of vitamins your body cannot absorb. Cheap synthetic forms, under-dosed actives, misleading labels. The same brand sells better formulas in foreign markets. You deserve to know this.</p>
                </div>

                <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                    <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">03 / Imported solutions do not fit India</h4>
                    <p style="color:var(--text-muted); line-height:1.6; font-size:0.95rem;">Products designed for Western nutritional deficiencies miss what Indian bodies need. They do not understand Ragi, Moringa, or Ashwagandha. They do not understand how Indians eat, work, or train. India needs an Indian solution.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     SOLUTION / PRODUCTS SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border);">
    <div class="container reveal">
        <div class="section-label">
            <div class="section-label-line"></div>
            <span class="section-label-text">The Solution</span>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:2rem; flex-wrap:wrap; margin-bottom:var(--space-md);">
            <div style="max-width:800px;">
                <h2 class="headline" style="margin-top:var(--space-sm);">So we built one. Meet Oxygen.</h2>
                <p class="subtext editorial-col" style="margin-top:var(--space-sm);">Three precision formulas. Each scientifically designed for a specific need. All built on the same uncompromising foundation: Indian ingredients, active nutrient forms, and doses that actually work.</p>
            </div>
        </div>

        <div class="bento-grid">
            <!-- Product 1 -->
            <div class="bento-cell product-card" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); border:1px solid var(--border); padding:0.25rem 0.5rem; display:inline-block; margin-bottom:1rem; border-radius:4px;">Pre-Clinical Optimization</div>
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem;">Project VITALITY</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Daily Deficiencies</p>
                <p style="font-size:0.95rem; line-height:1.5; color:var(--text-main); margin-bottom:1rem; font-style:italic;">For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.</p>
                <ul style="font-size:0.85rem; line-height:1.6; color:var(--text-muted); padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li>Covers 50% of your daily nutrient needs</li>
                    <li>Sustained energy without sugar spikes</li>
                    <li>Stress adaptation with KSM-66 Ashwagandha</li>
                </ul>
                <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                    <strong>INGREDIENTS:</strong> Finger Millet, Ashwagandha KSM-66, Lion's Mane, Moringa, 22 Chelated Nutrients
                </div>
            </div>

            <!-- Product 2 -->
            <div class="bento-cell product-card" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); border:1px solid var(--border); padding:0.25rem 0.5rem; display:inline-block; margin-bottom:1rem; border-radius:4px;">Sensory Trials & Taste Profiling</div>
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem;">Project CLARITY</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Cognitive Fatigue</p>
                <p style="font-size:0.95rem; line-height:1.5; color:var(--text-main); margin-bottom:1rem; font-style:italic;">The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3PM crash.</p>
                <ul style="font-size:0.85rem; line-height:1.6; color:var(--text-muted); padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li>Clean focus without caffeine crash</li>
                    <li>Memory and attention support (Lion's Mane)</li>
                    <li>L-Theanine:Caffeine ratio 2.5:1 (clinically studied)</li>
                </ul>
                <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                    <strong>INGREDIENTS:</strong> Lion's Mane, Bacopa Monnieri, L-Theanine, Natural Caffeine, Active B Vitamins
                </div>
            </div>

            <!-- Product 3 -->
            <div class="bento-cell product-card" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-main); border:1px solid var(--text-main); background:#e8e8e4; padding:0.25rem 0.5rem; display:inline-block; margin-bottom:1rem; border-radius:4px;">Formulation Finalized</div>
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem;">Project MOMENTUM</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Cellular Recovery</p>
                <p style="font-size:0.95rem; line-height:1.5; color:var(--text-main); margin-bottom:1rem; font-style:italic;">An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.</p>
                <ul style="font-size:0.85rem; line-height:1.6; color:var(--text-muted); padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li>Faster muscle recovery (Kokum + Tart Cherry)</li>
                    <li>ATP production support (Cordyceps militaris)</li>
                    <li>Strength and endurance (Creatine HCl + Citrulline)</li>
                </ul>
                <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                    <strong>INGREDIENTS:</strong> Cordyceps, Creatine HCl, Kokum Extract, L-Citrulline, Electrolytes
                </div>
            </div>

            <!-- Protein Bar -->
            <div class="bento-cell" style="grid-column: span 12; background:var(--text-main); color:var(--bg); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:3rem 2rem;">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:#888; margin-bottom:1rem; letter-spacing:0.1em; text-transform:uppercase;">Coming Soon</div>
                <h3 style="font-family:var(--font-serif); font-size:2.5rem; margin-bottom:1rem; color:#fff;">The Honest Protein Bar</h3>
                <p style="font-size:1.125rem; line-height:1.6; color:#ccc; max-width:600px; margin-bottom:1.5rem;">
                    Real dates, real cashews, real pumpkin seeds. 300mg KSM-66 Ashwagandha in every bar. No fake protein. No compound chocolate. Coming alongside our drink range.
                </p>
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:#888; border:1px solid #333; padding:0.5rem 1rem; border-radius:4px;">
                    DATES • CASHEWS • PUMPKIN SEEDS • KSM-66 ASHWAGANDHA • WHEY ISOLATE
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     SCIENCE & PILLARS SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section">
    <div class="container reveal">
        <div class="section-label">
            <div class="section-label-line"></div>
            <span class="section-label-text">The Science</span>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:2rem; flex-wrap:wrap; margin-bottom:var(--space-md);">
            <div style="max-width:800px;">
                <h2 class="headline" style="margin-top:var(--space-sm);">We show our work.</h2>
                <p class="subtext editorial-col" style="margin-top:var(--space-sm);">Every formulation decision has a peer-reviewed reason. Every ingredient has a verified source. Every claim is something we can prove.</p>
            </div>
            <a href="science.html" class="btn btn-outline" style="white-space:nowrap;">View Ingredients Index</a>
        </div>

        <div class="bento-grid">
            <div class="bento-cell" style="grid-column: span 12; display:grid; grid-template-columns:1fr 1fr 1fr; gap:var(--space-lg);" class="mobile-stack">
                <!-- Pillar 1 -->
                <div>
                    <div style="font-family:var(--font-mono); font-size:2rem; color:var(--text-muted); margin-bottom:1rem;">01</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1rem;">Active forms only</h4>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:1rem;">Most products use the cheapest permitted form. We use: Methylcobalamin, Pyridoxal-5-Phosphate, 5-MTHF Folate, Albion TRAACS® Chelated Minerals.</p>
                    <div class="data-num" style="font-size:1.25rem;">3-4x</div>
                    <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-top:0.25rem; text-transform:uppercase;">Better absorption vs generic.</p>
                    <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-main); margin-top:0.5rem; font-weight:700;">Cost diff: ₹2/serving</p>
                </div>

                <!-- Pillar 2 -->
                <div>
                    <div style="font-family:var(--font-mono); font-size:2rem; color:var(--text-muted); margin-bottom:1rem;">02</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1rem;">Verified, not assumed</h4>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:1rem;">Our Lion's Mane extract is verified using the Megazyme AOAC method — the gold standard verification method. Not marketing weight. Verified active compound content.</p>
                    <div class="data-num" style="font-size:1.25rem;">>30%</div>
                    <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-top:0.25rem; text-transform:uppercase;">β-glucan guaranteed.</p>
                </div>

                <!-- Pillar 3 -->
                <div>
                    <div style="font-family:var(--font-mono); font-size:2rem; color:var(--text-muted); margin-bottom:1rem;">03</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1rem;">Proving it, not claiming it</h4>
                    <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:1rem;">We have designed a clinical study for 135 participants across 8 weeks — before we launch commercially. Primary outcomes: Biomarkers + cognitive tests.</p>
                    <div class="data-num" style="font-size:1.25rem;">135</div>
                    <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-top:0.25rem; text-transform:uppercase;">clinical study participants.</p>
                    <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-main); margin-top:0.5rem; font-weight:700;">Results will be published regardless of outcome.</p>
                </div>
            </div>

            <!-- Comparison Table Component -->
            <div class="bento-cell" style="grid-column: span 12; overflow-x:auto;">
                <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1.5rem;">What We Do vs. What Most Brands Do</h4>
                <table style="width:100%; text-align:left; border-collapse:collapse; font-size:0.95rem; min-width:600px;">
                    <thead>
                        <tr style="border-bottom:1px solid var(--text-main); font-family:var(--font-mono); color:var(--text-muted);">
                            <th style="padding:1rem 0; width:30%;">METRIC</th>
                            <th style="padding:1rem 0; width:35%; color:var(--text-main);">OXYGEN BIOINNOVATIONS</th>
                            <th style="padding:1rem 0; width:35%;">THE INDUSTRY STANDARD</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom:1px solid var(--border);">
                            <td style="padding:1rem 0; font-weight:600;">Vitamin Forms</td>
                            <td style="padding:1rem 0; font-weight:600; color:var(--text-main);">Active (bioavailable) Forms</td>
                            <td style="padding:1rem 0; color:var(--text-muted);">Cheapest Synthetic Forms</td>
                        </tr>
                        <tr style="border-bottom:1px solid var(--border);">
                            <td style="padding:1rem 0; font-weight:600;">Vitamin B12</td>
                            <td style="padding:1rem 0; font-weight:600; color:var(--text-main);">Methylcobalamin</td>
                            <td style="padding:1rem 0; color:var(--text-muted);">Cyanocobalamin</td>
                        </tr>
                        <tr style="border-bottom:1px solid var(--border);">
                            <td style="padding:1rem 0; font-weight:600;">Minerals</td>
                            <td style="padding:1rem 0; font-weight:600; color:var(--text-main);">Chelated (TRAACS®) Amino Acid</td>
                            <td style="padding:1rem 0; color:var(--text-muted);">Oxide / Sulfate Forms</td>
                        </tr>
                        <tr style="border-bottom:1px solid var(--border);">
                            <td style="padding:1rem 0; font-weight:600;">Mineral Absorption</td>
                            <td style="padding:1rem 0; font-weight:600; color:var(--text-main);">~28% (Oxygen)</td>
                            <td style="padding:1rem 0; color:var(--text-muted);">~8% (Standard)</td>
                        </tr>
                        <tr style="border-bottom:1px solid var(--border);">
                            <td style="padding:1rem 0; font-weight:600;">Mushroom Extracts</td>
                            <td style="padding:1rem 0; font-weight:600; color:var(--text-main);">Verified β-glucan %</td>
                            <td style="padding:1rem 0; color:var(--text-muted);">Unverified weight labels</td>
                        </tr>
                        <tr style="border-bottom:1px solid var(--border);">
                            <td style="padding:1rem 0; font-weight:600;">Efficacy Data</td>
                            <td style="padding:1rem 0; font-weight:600; color:var(--text-main);">Pre-Launch Clinical Study</td>
                            <td style="padding:1rem 0; color:var(--text-muted);">Zero Clinical Efficacy Data</td>
                        </tr>
                        <tr>
                            <td style="padding:1rem 0; font-weight:600;">Lab Reports</td>
                            <td style="padding:1rem 0; font-weight:600; color:var(--text-main);">Public CoA for every batch</td>
                            <td style="padding:1rem 0; color:var(--text-muted);">No Transparency</td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     CTA SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" id="join" style="background:var(--text-main); color:var(--bg); border:none;">
    <div class="container" style="text-align:center; padding:var(--space-xl) 0;">
        <h2 class="display" style="color:var(--bg); font-size:clamp(3rem, 6vw, 5rem);">Stop guessing with<br>your <em>health.</em></h2>
        <p class="subtext" style="color:#A3A3A3; margin:var(--space-md) auto; max-width:600px;">
            Join the waitlist to receive access to our clinical study results, formulation deep-dives, and founding member pricing.
        </p>
        <form style="display:flex; flex-direction:column; gap:1rem; max-width:400px; margin:0 auto;" onsubmit="event.preventDefault(); alert('Waitlist strictly joined. Check console log for integration.');">
            <input type="email" placeholder="Enter your email address" required style="width:100%; padding:1rem; border:1px solid #333; background:transparent; color:#fff; font-family:var(--font-sans); font-size:1rem; border-radius:4px; outline:none;">
            <select required style="width:100%; padding:1rem; border:1px solid #333; background:transparent; color:#fff; font-family:var(--font-sans); font-size:1rem; border-radius:4px; outline:none; appearance:none;">
                <option value="" disabled selected>Primary Health Goal</option>
                <option value="energy">Daily Energy & Focus</option>
                <option value="deficiency">Correcting Deficiencies (Vitamin D, B12)</option>
                <option value="recovery">Athletic Recovery</option>
                <option value="longevity">General Longevity</option>
            </select>
            <button type="submit" class="btn" style="background:var(--bg); color:var(--text-main); width:100%; justify-content:center; padding:1.25rem;">Join the Waitlist</button>
        </form>
    </div>
</section>

</main>
"""

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + FOOTER)

print("Updated index.html with provided content in Bento Grid format.")
