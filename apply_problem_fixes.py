import os
import re

file_path = 'e:/OXYBIO/problem.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# REWRITE LAYER 1 (Hidden Crisis)
layer1_replacement = """        <!-- -------------------------------------------------------
 LAYER 1: THE MARKET PROBLEM (Measured Science)
-------------------------------------------------------- -->
        <section id="layer-01" class="structure-section"
            style="background:var(--bg-alt); border-top:1px solid var(--border); padding-top:var(--space-2xl); padding-bottom:var(--space-2xl); overflow:hidden; position:relative;">

            <div class="container reveal" style="position:relative; z-index:2;">

                <div style="text-align:center; max-width:800px; margin:0 auto 4rem;">
                    <div
                        style="display:inline-flex; align-items:center; gap:0.5rem; background:rgba(13,138,116,0.1); border:1px solid rgba(13,138,116,0.3); color:#0D8A74; padding:0.5rem 1rem; border-radius:50px; font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; margin-bottom:1.5rem;">
                        <span
                            style="width:6px; height:6px; background:#0D8A74; border-radius:50%;"></span>
                        SCIENTIFIC CONTEXT
                    </div>
                    <h2
                        style="font-family:var(--font-serif); font-size:clamp(3rem, 6vw, 4.5rem); line-height:1; letter-spacing:-0.03em; margin-bottom:1.5rem; color:var(--text-main);">
                        The Nutritional Baseline.</h2>
                    <p style="font-size:1.25rem; line-height:1.6; color:var(--text-muted);">
                        "Unnave marundhu" (Food is medicine). We are researching the empirical nutritional gaps in modern diets. According to national health data (ICMR, NFHS), significant portions of the urban workforce operate with underlying deficiencies in bioavailable micronutrients.
                    </p>
                </div>

                <div style="border:1px solid var(--border); background:var(--bg); border-radius:12px; overflow:hidden;">
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 280px), 1fr));">
                        
                        <div style="padding:3rem; border-right:1px solid var(--border);" class="mobile-no-border">
                            <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.5rem; color:var(--text-main);">Vitamin D Baseline</h4>
                            <p style="font-size:1rem; line-height:1.6; color:var(--text-muted);">
                                With increased indoor work environments, a significant majority of urban professionals show suboptimal Vitamin D levels, impacting immune function and bone density over time.
                            </p>
                        </div>

                        <div style="padding:3rem; border-right:1px solid var(--border);" class="mobile-no-border">
                            <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.5rem; color:var(--text-main);">B12 in Vegetarian Diets</h4>
                            <p style="font-size:1rem; line-height:1.6; color:var(--text-muted);">
                                B12 is critical for neurological function. Plant-predominant regional diets often lack adequate, bioavailable sources of B12, requiring careful supplementation or fortification.
                            </p>
                        </div>

                        <div style="padding:3rem;">
                            <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.5rem; color:var(--text-main);">Iron Bioavailability</h4>
                            <p style="font-size:1rem; line-height:1.6; color:var(--text-muted);">
                                Even when iron is present in the diet, absorption remains a complex challenge. Poor iron bioavailability leads to diminished cognitive and physical stamina, particularly in working women.
                            </p>
                        </div>

                    </div>
                    <div style="padding:2rem 3rem; background:var(--bg-alt); border-top:1px solid var(--border);">
                        <p style="font-size:1.1rem; color:var(--text-muted); margin:0; font-family:var(--font-serif); font-style:italic;">
                            Our research focuses on bridging these gaps through bioavailable, fermented functional foods rather than synthetic pills.
                        </p>
                    </div>
                </div>
            </div>
        </section>"""

# Find LAYER 1 block and replace it
# Start marker: <!-- \n LAYER 1: THE MARKET PROBLEM (Premium Interface)\n-------------------------------------------------------- -->
# End marker is the start of Layer 2
layer1_pattern = re.compile(r'<!-- -------------------------------------------------------\n\n LAYER 1: THE MARKET PROBLEM \(Premium Interface\)\n\n-------------------------------------------------------- -->.*?<!-- -------------------------------------------------------\n\n LAYER 2: THE BEHAVIORAL PROBLEM\n\n-------------------------------------------------------- -->', re.DOTALL)
content = layer1_pattern.sub(layer1_replacement + "\n\n        <!-- -------------------------------------------------------\n\n LAYER 2: THE BEHAVIORAL PROBLEM\n\n-------------------------------------------------------- -->", content)

# REWRITE COMPETITORS

content = content.replace('<h4 class="anim-card-title">Horlicks & Bournvita</h4>', '<h4 class="anim-card-title">Traditional Malt Drinks</h4>')
content = content.replace('<h4 class="anim-card-title">MuscleBlaze & ON India</h4>', '<h4 class="anim-card-title">Standard Protein Supplements</h4>')
content = content.replace('<h4 class="anim-card-title">AG1, Huel, Ritual</h4>', '<h4 class="anim-card-title">Imported Premium Greens</h4>')
content = content.replace('<h4 class="anim-card-title">Emerging D2C Brands</h4>', '<h4 class="anim-card-title">Marketing-First D2C Brands</h4>')
content = content.replace('<strong>The Failure:</strong> Prohibitively costly for daily use (₹350-500/serving), no Indian indigenous ingredients, ignores Indian usage patterns.', '<strong>The Limit:</strong> Prohibitively costly for daily use, no Indian indigenous ingredients, ignores domestic usage patterns.')


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"problem.html processed.")
