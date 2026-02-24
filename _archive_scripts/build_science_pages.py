import os
import re

# Read template structure from index.html
with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header (up to <main>) and footer (from </main> to end)
header_match = re.search(r'(.*?<main>)', html, re.DOTALL)
footer_match = re.search(r'(</main>.*)', html, re.DOTALL)

if not header_match or not footer_match:
    print("Error extracting header/footer")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

# -- THE PROBLEM PAGE CONTENT --
problem_content = """
        <!-- Problem Hero Section -->
        <section class="hero" id="problem-hero" style="min-height: 50vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="hero-glow"></div>
            <div class="container hero-content" style="text-align: center;">
                <div class="badge reveal" style="transition-delay: 0ms; margin: 0 auto 1.5rem;">Formulation Science</div>
                <h1 class="reveal" style="transition-delay: 150ms;">
                    The Science Behind <span style="color: var(--accent);">Oxygen.</span>
                </h1>
                <p class="subtitle reveal" style="transition-delay: 300ms;" style="max-width: 650px; margin-left: auto; margin-right: auto;">
                    Every formulation decision has a reason. Every reason has a reference. Every reference is available to you.
                </p>
            </div>
        </section>

        <!-- LAYER 1: Market Problem -->
        <section id="layer-1" style="background: var(--bg); padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container">
                <div class="section-header reveal">
                    <div class="badge badge-accent" style="margin-bottom: 1rem;">Layer 1</div>
                    <h2>The Market Problem <span style="color: var(--text-muted); font-size: 1.5rem; display:block; margin-top:0.5rem;">(India Has a Nutrition Crisis)</span></h2>
                    <p style="font-size: 1.125rem; margin-top: 1rem;">That nobody is talking about honestly. These are not estimates — these are ICMR, NFHS-5, and WHO measurements.</p>
                </div>

                <div class="stat-grid" style="margin-top: 3rem; margin-bottom: 3rem;">
                    <article class="stat-card reveal">
                        <div style="font-size: 3.5rem; font-weight: 800; color: var(--accent); line-height: 1;">70-90%</div>
                        <div class="stat-label" style="margin-top:0.5rem;">Vitamin D Deficient (Urban)</div>
                        <div class="stat-source">Source: ICMR Task Force, 2022</div>
                    </article>
                    <article class="stat-card reveal" style="transition-delay: 100ms;">
                        <div style="font-size: 3.5rem; font-weight: 800; color: var(--accent); line-height: 1;">47%</div>
                        <div class="stat-label" style="margin-top:0.5rem;">B12 Deficient (Total pop)</div>
                        <div class="stat-source">Source: J. Nutritional Science</div>
                    </article>
                    <article class="stat-card reveal" style="transition-delay: 200ms;">
                        <div style="font-size: 3.5rem; font-weight: 800; color: var(--accent); line-height: 1;">53%</div>
                        <div class="stat-label" style="margin-top:0.5rem;">Iron Deficient (Working women)</div>
                        <div class="stat-source">Source: NFHS-5</div>
                    </article>
                </div>

                <div class="cards-grid reveal" style="margin-top: 3rem;">
                    <div class="feature-card" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h4 style="color: var(--accent); margin-bottom: 0.5rem;">Cognitive Impact</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Iron deficiency reduces cognitive performance by 15-20% in working adults. <br><em style="font-size: 0.85rem;">(Source: Am J Clinical Nutrition)</em></p>
                    </div>
                    <div class="feature-card" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h4 style="color: var(--accent); margin-bottom: 0.5rem;">Economic Impact</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Nutritional deficiency costs India an estimated ₹4.5 lakh crore annually in lost productivity. <br><em style="font-size: 0.85rem;">(Source: World Bank India Report)</em></p>
                    </div>
                    <div class="feature-card" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h4 style="color: var(--accent); margin-bottom: 0.5rem;">Fatigue Burden</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Chronic fatigue affects 38% of urban working population — directly tied to micronutrient gaps. <br><em style="font-size: 0.85rem;">(Source: ASSOCHAM Survey)</em></p>
                    </div>
                    <div class="feature-card" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h4 style="color: var(--accent); margin-bottom: 0.5rem;">Student Impact</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Micronutrient deficiency linked to 21% reduction in academic performance. <br><em style="font-size: 0.85rem;">(Source: Nutrition Reviews Journal)</em></p>
                    </div>
                </div>

                <div class="reveal" style="text-align: center; margin-top: 3rem; padding: 2rem; background: var(--text-main); color: #fff; border-radius: 12px;">
                    <h3 style="margin: 0;">"This is a public health crisis hiding in plain sight."</h3>
                </div>
            </div>
        </section>

        <!-- LAYER 2: Behavioral Problem -->
        <section id="layer-2" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container">
                <div class="section-header reveal">
                    <div class="badge badge-accent" style="margin-bottom: 1rem;">Layer 2</div>
                    <h2>The Behavioral Problem <span style="color: var(--text-muted); font-size: 1.5rem; display:block; margin-top:0.5rem;">(The Intention-Action Gap)</span></h2>
                    <p style="font-size: 1.125rem; margin-top: 1rem; max-width: 800px;">Urban Indians are more health-aware than any previous generation. They read about nutrition. They follow wellness accounts. They know what protein is. And yet deficiency rates are rising.</p>
                </div>

                <div class="cards-grid" style="margin-top: 3rem;">
                    <article class="problem-card reveal">
                        <div class="card-icon" style="background: var(--bg); color: var(--accent); font-weight: 800; font-size: 1.5rem; display:flex; align-items:center; justify-content:center;">01</div>
                        <h3>Time Scarcity</h3>
                        <p>The average working professional in Bangalore or Mumbai works 52 hours per week. Commutes consume another 2-3 hours daily. What remains is insufficient for meal planning, preparation, and consistent nutritional coverage.</p>
                        <p style="font-style: italic; color: var(--accent); margin-top: 1rem;">"This is not laziness. It is mathematics."</p>
                    </article>

                    <article class="problem-card reveal" style="transition-delay: 150ms;">
                        <div class="card-icon" style="background: var(--bg); color: var(--accent); font-weight: 800; font-size: 1.5rem; display:flex; align-items:center; justify-content:center;">02</div>
                        <h3>Trust Deficit</h3>
                        <p>CSE (Centre for Science and Environment) found that 68% of tested health food products failed to meet their own label claims. Maggi. Baby food controversies. Protein spiking scandals. The rational response is skepticism.</p>
                        <p style="font-style: italic; color: var(--accent); margin-top: 1rem;">"Why buy something you cannot trust?"</p>
                    </article>

                    <article class="problem-card reveal" style="transition-delay: 300ms;">
                        <div class="card-icon" style="background: var(--bg); color: var(--accent); font-weight: 800; font-size: 1.5rem; display:flex; align-items:center; justify-content:center;">03</div>
                        <h3>Relevance Gap</h3>
                        <p>Most nutrition science is conducted in Western populations. Indian bodies have different gut microbiome composition, dietary baselines (predominantly vegetarian), cooking methods, and specific deficiency profiles.</p>
                        <p style="font-style: italic; color: var(--accent); margin-top: 1rem;">"A Western product is not optimally designed for an Indian professional."</p>
                    </article>
                </div>
            </div>
        </section>

        <!-- LAYER 3: Supply Problem -->
        <section id="layer-3" style="background: var(--bg); padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container">
                <div class="section-header reveal">
                    <div class="badge badge-accent" style="margin-bottom: 1rem;">Layer 3</div>
                    <h2>The Supply Problem <span style="color: var(--text-muted); font-size: 1.5rem; display:block; margin-top:0.5rem;">(The Market Response Has Been Inadequate)</span></h2>
                </div>

                <div class="roles-grid" style="display: grid; gap: 1.5rem; margin-top: 3rem;">
                    <div class="role-card reveal" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h3 style="margin-bottom: 0.5rem; color: var(--text-main);">Traditional Health Drinks <span style="font-size: 0.9rem; color: var(--text-muted); font-weight: normal;">(Horlicks, Complan, Bournvita, Boost)</span></h3>
                        <div style="display: flex; gap: 2rem; margin-top: 1rem;">
                            <div style="flex: 1;"><strong style="color: #10B981;">Offers:</strong> Strong distribution.</div>
                            <div style="flex: 2;"><strong style="color: #E11D48;">Fails because:</strong> Sugar: 16-18g/serving. Cheapest synthetic forms. Zero adaptogens. Designed in 1970s.</div>
                        </div>
                    </div>
                    
                    <div class="role-card reveal" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h3 style="margin-bottom: 0.5rem; color: var(--text-main);">Protein Supplements <span style="font-size: 0.9rem; color: var(--text-muted); font-weight: normal;">(MuscleBlaze, ON India)</span></h3>
                        <div style="display: flex; gap: 2rem; margin-top: 1rem;">
                            <div style="flex: 1;"><strong style="color: #10B981;">Offers:</strong> High protein.</div>
                            <div style="flex: 2;"><strong style="color: #E11D48;">Fails because:</strong> Designed for narrow outcome (muscle mass). Ignores micronutrient deficiency. Relevant for gym users only.</div>
                        </div>
                    </div>

                    <div class="role-card reveal" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h3 style="margin-bottom: 0.5rem; color: var(--text-main);">Imported Premium Products <span style="font-size: 0.9rem; color: var(--text-muted); font-weight: normal;">(AG1, Huel, Ritual)</span></h3>
                        <div style="display: flex; gap: 2rem; margin-top: 1rem;">
                            <div style="flex: 1;"><strong style="color: #10B981;">Offers:</strong> Genuine science.</div>
                            <div style="flex: 2;"><strong style="color: #E11D48;">Fails because:</strong> Prohibitively costly for daily use (₹350-500/serving), no Indian ingredients, don't understand Indian patterns.</div>
                        </div>
                    </div>

                    <div class="role-card reveal" style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                        <h3 style="margin-bottom: 0.5rem; color: var(--text-main);">Nutraceutical Startups <span style="font-size: 0.9rem; color: var(--text-muted); font-weight: normal;">(Emerging Indian brands)</span></h3>
                        <div style="display: flex; gap: 2rem; margin-top: 1rem;">
                            <div style="flex: 1;"><strong style="color: #10B981;">Offers:</strong> Modern positioning.</div>
                            <div style="flex: 2;"><strong style="color: #E11D48;">Fails because:</strong> Most are marketing companies, not science companies. Label claims without evidence, low doses.</div>
                        </div>
                    </div>
                </div>

                <div class="reveal" style="margin-top: 4rem; padding: 2.5rem; background: var(--card-bg); border-radius: 12px; border: 1px solid var(--accent); border-left: 6px solid var(--accent);">
                    <p style="font-size: 1.1rem; line-height: 1.6; margin: 0; color: var(--text-main);">
                        The market has affordable products that are inadequate. Quality products that are inaccessible. Indian products that lack rigour. Rigorous products that lack Indian relevance. <br><br>
                        <strong>Affordable. Quality. Indian. Rigorous.</strong> This intersection is currently empty. Oxygen is being built to occupy it.
                    </p>
                </div>
            </div>
        </section>

        <!-- Formulations Science -->
        <section id="formulation-science" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container">
                <div class="section-header reveal" style="text-align: center; margin-bottom: 4rem;">
                    <h2>HOW WE SOLVE IT: <span style="color: var(--accent);">Our Formulation Science</span></h2>
                </div>

                <!-- Section 1 -->
                <div class="reveal" style="margin-bottom: 4rem;">
                    <h3 style="font-size: 1.5rem; margin-bottom: 1.5rem; display:flex; align-items:center; gap:0.5rem;"><div class="badge badge-accent">1</div> The Bioavailability Problem (Form matters more than dose)</h3>
                    <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 2rem;"><strong>Claim vs Reality:</strong> Generic supplements use Ferrous Oxide (5% absorption). We use Ferrous Bisglycinate (Albion TRAACS®) (25-35%).</p>
                    
                    <div class="c-table-wrap">
                        <table class="c-table">
                            <thead>
                                <tr>
                                    <th>Nutrient</th>
                                    <th>Oxygen Formulations</th>
                                    <th>Most Brands</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Iron</strong></td>
                                    <td class="us">✔ Fe-Bisglycinate (Ours 28%)</td>
                                    <td class="them">FeSO4 (Generic 8%)</td>
                                </tr>
                                <tr>
                                    <td><strong>Zinc</strong></td>
                                    <td class="us">✔ Zn-Bisglycinate (Ours 41%)</td>
                                    <td class="them">ZnO (Generic 12%)</td>
                                </tr>
                                <tr>
                                    <td><strong>Magnesium</strong></td>
                                    <td class="us">✔ Mg-Glycinate (Ours 23%)</td>
                                    <td class="them">MgO (Generic 4%)</td>
                                </tr>
                                <tr>
                                    <td><strong>Vitamin B12</strong></td>
                                    <td class="us">✔ Methylcobalamin (Ours 55%)</td>
                                    <td class="them">Cyanocobalamin (Generic 15%)</td>
                                </tr>
                                <tr>
                                    <td><strong>Folate</strong></td>
                                    <td class="us">✔ 5-MTHF (Ours 70%)</td>
                                    <td class="them">Folic Acid (Generic 20%)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div style="background: rgba(13, 148, 136, 0.1); padding: 1.5rem; border-radius: 8px; margin-top: 2rem; border-left: 4px solid var(--accent);">
                        <strong>MTHFR variants:</strong> ~40% of Indians carry an MTHFR variant causing them to poorly process synthetic folic acid. Oxygen bypasses this by using 5-MTHF.
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem; margin-bottom: 4rem;">
                    <!-- Section 2 -->
                    <div class="reveal">
                        <h3 style="font-size: 1.5rem; margin-bottom: 1.5rem; display:flex; align-items:center; gap:0.5rem;"><div class="badge badge-accent">2</div> The Millet System</h3>
                        <div style="background: var(--bg); padding: 2rem; border-radius: 12px; height: 100%;">
                            <p><strong>Ragi (Finger Millet):</strong> 344mg Calcium per 100g (beats milk).</p>
                            <p style="color: #E11D48; margin-top: 1rem;"><strong>Problem:</strong> Raw Ragi has phytic acid which binds minerals reducing absorption by 60-70%.</p>
                            <p style="color: var(--accent); margin-top: 1rem;"><strong>Our Process:</strong></p>
                            <ul style="padding-left: 1.2rem; color: var(--text-muted); line-height: 1.8;">
                                <li>Sourcing organic from Karnataka.</li>
                                <li>Sprouting/Malting (48hrs, reduces phytic acid by 60%).</li>
                                <li>Gentle Drying.</li>
                                <li>Micro-Milling.</li>
                            </ul>
                            <p style="margin-top: 1rem; font-weight: 600;">Result: Highly bioavailable mineral matrix.</p>
                        </div>
                    </div>

                    <!-- Section 3 -->
                    <div class="reveal">
                        <h3 style="font-size: 1.5rem; margin-bottom: 1.5rem; display:flex; align-items:center; gap:0.5rem;"><div class="badge badge-accent">3</div> The Mushroom Science</h3>
                        <div style="background: var(--bg); padding: 2rem; border-radius: 12px; height: 100%;">
                            <p style="color: #E11D48;"><strong>Most brands:</strong></p>
                            <p style="color: var(--text-muted); margin-bottom: 1.5rem;">Mycelium grown on grain, no compound verification, single extraction, no β-glucan guarantee.</p>
                            
                            <p style="color: var(--accent);"><strong>Our approach:</strong></p>
                            <ul style="padding-left: 1.2rem; color: var(--text-main); font-weight: 500; line-height: 1.8;">
                                <li>Fruiting body only</li>
                                <li>Dual extraction (Hot water + Ethanol)</li>
                                <li>Megazyme AOAC verified</li>
                                <li>≥30% β-glucan guaranteed</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Section 4 -->
                <div class="reveal" style="background: var(--text-main); color: #fff; padding: 3rem; border-radius: 12px;">
                    <h3 style="font-size: 1.5rem; margin-bottom: 1.5rem; display:flex; align-items:center; gap:0.5rem;"><div class="badge" style="background: #333; color: #fff; border:none;">4</div> References</h3>
                    <p style="color: #ccc; margin-bottom: 1.5rem;">A full bibliography of clinical references and DOIs supporting our formulation matrix.</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                        <span class="badge" style="background: rgba(255,255,255,0.1); border:none; color: #fff;">Millet Research</span>
                        <span class="badge" style="background: rgba(255,255,255,0.1); border:none; color: #fff;">Mushroom Research</span>
                        <span class="badge" style="background: rgba(255,255,255,0.1); border:none; color: #fff;">Ashwagandha Research</span>
                        <span class="badge" style="background: rgba(255,255,255,0.1); border:none; color: #fff;">Cognitive Ingredients</span>
                        <span class="badge" style="background: rgba(255,255,255,0.1); border:none; color: #fff;">Bioavailability Research</span>
                    </div>
                </div>
            </div>
        </section>
"""

# -- INGREDIENTS INDEX PAGE CONTENT --
ingredients_content = """
        <!-- Ingredients Hero Section -->
        <section class="hero" id="ingredients-hero" style="min-height: 50vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="hero-glow"></div>
            <div class="container hero-content" style="text-align: center;">
                <div class="badge reveal" style="transition-delay: 0ms; margin: 0 auto 1.5rem;">Full Transparency</div>
                <h1 class="reveal" style="transition-delay: 150ms;">
                    Every ingredient.<br>
                    <span style="color: var(--accent);">Every reason.</span>
                </h1>
                <p class="subtitle reveal" style="transition-delay: 300ms;" style="max-width: 650px; margin-left: auto; margin-right: auto;">
                    Nothing in Oxygen is there by accident. Nothing is there for label appeal. Everything has peer-reviewed evidence for its inclusion.
                </p>
            </div>
        </section>

        <!-- Category Overview -->
        <section id="categories" style="background: var(--bg); padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container">
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem;">
                    <a href="#millet-base" class="btn btn-outline" style="min-height: 40px; border-radius: 30px;">Millet Base</a>
                    <a href="#mushroom-complex" class="btn btn-outline" style="min-height: 40px; border-radius: 30px;">Mushroom Complex</a>
                    <a href="#adaptogens" class="btn btn-outline" style="min-height: 40px; border-radius: 30px;">Adaptogens</a>
                    <a href="#cognitive-stack" class="btn btn-outline" style="min-height: 40px; border-radius: 30px;">Cognitive Stack</a>
                    <a href="#performance-stack" class="btn btn-outline" style="min-height: 40px; border-radius: 30px;">Performance Stack</a>
                </div>
            </div>
        </section>

        <!-- Ingredients Detail Section -->
        <section id="ingredients-detail" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container">
                
                <!-- Category 1: Millet Base -->
                <div id="millet-base" class="reveal" style="margin-bottom: 5rem;">
                    <h2 style="border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem;">Millet Base</h2>
                    <div style="display: grid; gap: 1.5rem;">
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Finger Millet (Ragi)</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"India's most nutritious forgotten grain"</p>
                            <p>Sprouted & micro-milled flour. Standardized to 344mg calcium/100g.</p>
                            <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">8g (CORE)</span></p>
                        </div>
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Pearl Millet (Bajra)</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The iron-rich ancient grain of Rajasthan"</p>
                            <p>Whole grain micro-milled flour. Standardized to 8mg iron/100g.</p>
                            <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">4g (CORE)</span></p>
                        </div>
                    </div>
                </div>

                <!-- Category 2: Mushroom Complex -->
                <div id="mushroom-complex" class="reveal" style="margin-bottom: 5rem;">
                    <h2 style="border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem;">Mushroom Complex</h2>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Lion's Mane</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The neurotrophic mushroom"</p>
                            <p>Hot-water + ethanol dual extract (fruiting body). Standardized ≥30% β-glucan, ≥1% hericenones. Stimulates NGF.</p>
                        </div>
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Cordyceps</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The ATP production mushroom"</p>
                            <p>Hot-water extract (fruiting body). Standardized ≥1% cordycepin. Enhances cellular ATP production.</p>
                        </div>
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Reishi</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The immune modulation mushroom"</p>
                            <p>Dual extract (fruiting body). Standardized ≥30% polysaccharides, ≥2% triterpenes.</p>
                        </div>
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Chaga</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The antioxidant powerhouse"</p>
                            <p>Hot-water extract. Standardized ≥30% polysaccharides.</p>
                        </div>
                    </div>
                </div>

                <!-- Category 3: Adaptogens -->
                <div id="adaptogens" class="reveal" style="margin-bottom: 5rem;">
                    <h2 style="border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem;">Adaptogens</h2>
                    <div style="display: grid; gap: 1.5rem;">
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Ashwagandha KSM-66®</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The stress adaptation root"</p>
                            <p>Full-spectrum root extract. Standardized ≥5% withanolides.</p>
                            <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">600mg</span></p>
                        </div>
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Moringa</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The nutrient-dense Indian superfood"</p>
                            <p>Shade-dried leaf powder. Standardized min 2% total flavonoids.</p>
                            <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">500mg</span></p>
                        </div>
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Bacopa Monnieri</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"The Ayurvedic memory herb"</p>
                            <p>Standardized extract ≥50% bacosides.</p>
                            <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">300mg</span></p>
                        </div>
                    </div>
                </div>

                <!-- Category 4: Cognitive & Performance Stack -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 3rem; margin-bottom: 5rem;">
                    <div id="cognitive-stack" class="reveal">
                        <h2 style="border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem;">Cognitive Stack</h2>
                        <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem;">L-Theanine</h3>
                            <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"Calm focus without sedation"</p>
                            <p>Pharmaceutical-grade L-Theanine ≥98% purity. Provides relaxed alertness when paired with caffeine.</p>
                            <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">200mg</span></p>
                        </div>
                    </div>

                    <div id="performance-stack" class="reveal">
                        <h2 style="border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem;">Performance Stack</h2>
                        <div style="display: grid; gap: 1.5rem;">
                            <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                                <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Creatine HCl</h3>
                                <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"Strength and power, bioavailable form"</p>
                                <p>38x more soluble than monohydrate, no loading phase. ≥99% purity.</p>
                                <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">2g</span></p>
                            </div>
                            <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                                <h3 style="color: var(--accent); margin-bottom: 0.5rem;">L-Citrulline</h3>
                                <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"Blood flow and endurance amplifier"</p>
                                <p>Free-form L-Citrulline for nitric oxide production. ≥99% purity.</p>
                                <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">3g</span></p>
                            </div>
                            <div style="background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                                <h3 style="color: var(--accent); margin-bottom: 0.5rem;">Kokum Extract</h3>
                                <p style="font-style: italic; color: var(--text-muted); margin-bottom: 1rem;">"India's recovery fruit"</p>
                                <p>Standardized fruit extract ≥10% garcinol potent anti-inflammatory.</p>
                                <p style="margin-top: 0.5rem; font-weight: 600;">Dose: <span style="font-weight: normal;">500mg</span></p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Footer Note -->
                <div class="reveal" style="background: var(--bg); padding: 3rem; border-radius: 12px; text-align: center; border-top: 4px solid var(--accent);">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); margin-bottom: 1rem;"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="9" x2="15" y2="15"></line><line x1="15" y1="9" x2="9" y2="15"></line></svg>
                    <h3 style="margin-bottom: 1rem;">Full Certificate of Analysis for every batch</h3>
                    <p style="color: var(--text-muted); max-width: 700px; margin: 0 auto; line-height: 1.6;">
                        When we launch, every batch will have a publicly available CoA with third-party verified test results. Scan the QR code on any product to see the exact test report for your batch.
                    </p>
                </div>

            </div>
        </section>
"""

with open(r'e:\OXYBIO\problem.html', 'w', encoding='utf-8') as f:
    f.write(header_html + f'<main>\n{problem_content}\n</main>\n' + footer_html)

with open(r'e:\OXYBIO\ingredients.html', 'w', encoding='utf-8') as f:
    f.write(header_html + f'<main>\n{ingredients_content}\n</main>\n' + footer_html)

print("Generated problem.html and ingredients.html")
