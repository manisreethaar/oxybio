import re

# ──────────────────────────────────────────────────────────
# 1. UPGRADE INGREDIENTS.HTML (Lab Formulary UI)
# ──────────────────────────────────────────────────────────
with open('e:\\OXYBIO\\ingredients.html', 'r', encoding='utf-8') as f:
    ing_html = f.read()

old_ing_start = ing_html.find('<!-- ═══════════════════════════════════════════════════════\n     INGREDIENTS LIST (Bento Architecture)')
old_ing_end = ing_html.find('<!-- ═══════════════════════════════════════════════════════\n     FOOTER NOTE (CoA)')

NEW_INGREDIENTS = '''<!-- ═══════════════════════════════════════════════════════
     PREMIUM INGREDIENT FORMULARY
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--text-main); color:var(--bg); border:none; padding-bottom:6rem; overflow:hidden; position:relative;">
    
    <!-- Abstract dark mode background glow -->
    <div style="position:absolute; top:10%; left:-10%; width:600px; height:600px; background:radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 70%); pointer-events:none;"></div>
    
    <div class="container" style="position:relative; z-index:2;">
        
        <!-- Category: Millet System -->
        <div id="millet" class="reveal" style="margin-bottom:6rem;">
            <div style="display:flex; align-items:center; gap:2rem; margin-bottom:3rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:1rem;">
                <div style="font-family:var(--font-mono); font-size:2rem; font-weight:700; color:var(--bg); opacity:0.2;">01</div>
                <div>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.5); margin-bottom:0.25rem;">The Foundation</div>
                    <h2 style="font-family:var(--font-serif); font-size:2.5rem; margin:0; color:#fff;">Millet Matrix</h2>
                </div>
            </div>
            
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(350px, 1fr)); gap:2rem;">
                <!-- Ragi -->
                <div style="background:#111; border:1px solid #333; border-radius:12px; padding:2.5rem; position:relative; overflow:hidden;" class="premium-card-hover">
                    <div style="position:absolute; top:0; right:0; padding:1.5rem; opacity:0.1;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><path d="M12 2L2 22h20L12 2z"></path></svg>
                    </div>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; color:#888; margin-bottom:1rem; border:1px solid #333; display:inline-block; padding:0.25rem 0.75rem; border-radius:20px;">BIOAVAILABLE CALCIUM</div>
                    <h3 style="font-family:var(--font-serif); font-size:2rem; color:#fff; margin-bottom:0.5rem;">Finger Millet (Ragi)</h3>
                    <p style="font-size:1.05rem; line-height:1.6; color:#aaa; margin-bottom:2rem;">Sprouted and micro-milled to reduce phytic acid by 60%, unlocking India's most calcium-dense forgotten grain without the anti-nutrients.</p>
                    
                    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #333; padding-top:1.5rem;">
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">STANDARDIZATION</span>
                            <span style="font-family:var(--font-mono); font-size:0.9rem; color:#ccc;">344mg Ca / 100g</span>
                        </div>
                        <div style="text-align:right;">
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">CLINICAL DOSE</span>
                            <span style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff;">8,000<span style="font-size:0.8rem; font-weight:400;">mg</span></span>
                        </div>
                    </div>
                </div>

                <!-- Bajra -->
                <div style="background:#111; border:1px solid #333; border-radius:12px; padding:2.5rem; position:relative; overflow:hidden;" class="premium-card-hover">
                    <div style="position:absolute; top:0; right:0; padding:1.5rem; opacity:0.1;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><circle cx="12" cy="12" r="10"></circle></svg>
                    </div>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; color:#888; margin-bottom:1rem; border:1px solid #333; display:inline-block; padding:0.25rem 0.75rem; border-radius:20px;">NATURAL IRON</div>
                    <h3 style="font-family:var(--font-serif); font-size:2rem; color:#fff; margin-bottom:0.5rem;">Pearl Millet (Bajra)</h3>
                    <p style="font-size:1.05rem; line-height:1.6; color:#aaa; margin-bottom:2rem;">The dense, resilient grain of Rajasthan. Rich in natural iron and slowly digestible starch, preventing insulin spikes while building foundational energy.</p>
                    
                    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #333; padding-top:1.5rem;">
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">STANDARDIZATION</span>
                            <span style="font-family:var(--font-mono); font-size:0.9rem; color:#ccc;">8mg Fe / 100g</span>
                        </div>
                        <div style="text-align:right;">
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">CLINICAL DOSE</span>
                            <span style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff;">4,000<span style="font-size:0.8rem; font-weight:400;">mg</span></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Category: Fungi Intelligence -->
        <div id="mushroom" class="reveal" style="margin-bottom:6rem;">
            <div style="display:flex; align-items:center; gap:2rem; margin-bottom:3rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:1rem;">
                <div style="font-family:var(--font-mono); font-size:2rem; font-weight:700; color:var(--bg); opacity:0.2;">02</div>
                <div>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.5); margin-bottom:0.25rem;">Nootropic & Immunity</div>
                    <h2 style="font-family:var(--font-serif); font-size:2.5rem; margin:0; color:#fff;">Fungi Intelligence</h2>
                </div>
            </div>
            
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(350px, 1fr)); gap:2rem;">
                <!-- Lion's Mane -->
                <div style="background:#111; border:1px solid #333; border-radius:12px; padding:2.5rem; position:relative; overflow:hidden;" class="premium-card-hover">
                    <div style="font-family:var(--font-mono); font-size:0.75rem; color:#888; margin-bottom:1rem; border:1px solid #333; display:inline-block; padding:0.25rem 0.75rem; border-radius:20px;">NEUROGENESIS (NGF)</div>
                    <h3 style="font-family:var(--font-serif); font-size:2rem; color:#fff; margin-bottom:0.5rem;">Lion's Mane Extract</h3>
                    <p style="font-size:1.05rem; line-height:1.6; color:#aaa; margin-bottom:2rem;">Dual-extracted (hot water + ethanol) fruiting body. Contains hericenones and erinacines proven to stimulate Nerve Growth Factor in the brain.</p>
                    
                    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #333; padding-top:1.5rem;">
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">STANDARDIZATION</span>
                            <span style="font-family:var(--font-mono); font-size:0.9rem; color:#ccc;">≥30% β-Glucans</span>
                        </div>
                        <div style="text-align:right;">
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">CLINICAL DOSE</span>
                            <span style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff;">1,000<span style="font-size:0.8rem; font-weight:400;">mg</span></span>
                        </div>
                    </div>
                </div>

                <!-- Cordyceps -->
                <div style="background:#111; border:1px solid #333; border-radius:12px; padding:2.5rem; position:relative; overflow:hidden;" class="premium-card-hover">
                    <div style="font-family:var(--font-mono); font-size:0.75rem; color:#888; margin-bottom:1rem; border:1px solid #333; display:inline-block; padding:0.25rem 0.75rem; border-radius:20px;">CELLULAR ATP</div>
                    <h3 style="font-family:var(--font-serif); font-size:2rem; color:#fff; margin-bottom:0.5rem;">Cordyceps Militaris</h3>
                    <p style="font-size:1.05rem; line-height:1.6; color:#aaa; margin-bottom:2rem;">The Olympic-grade mushroom. Enhances cellular oxygen utilization and ATP production, delaying fatigue by working at the mitochondrial level.</p>
                    
                    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #333; padding-top:1.5rem;">
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">STANDARDIZATION</span>
                            <span style="font-family:var(--font-mono); font-size:0.9rem; color:#ccc;">≥1% Cordycepin</span>
                        </div>
                        <div style="text-align:right;">
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">CLINICAL DOSE</span>
                            <span style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff;">500<span style="font-size:0.8rem; font-weight:400;">mg</span></span>
                        </div>
                    </div>
                </div>
                
                <!-- Reishi -->
                <div style="background:#111; border:1px solid #333; border-radius:12px; padding:2.5rem; position:relative; overflow:hidden;" class="premium-card-hover">
                    <div style="font-family:var(--font-mono); font-size:0.75rem; color:#888; margin-bottom:1rem; border:1px solid #333; display:inline-block; padding:0.25rem 0.75rem; border-radius:20px;">IMMUNE MODULATION</div>
                    <h3 style="font-family:var(--font-serif); font-size:2rem; color:#fff; margin-bottom:0.5rem;">Reishi (Ganoderma)</h3>
                    <p style="font-size:1.05rem; line-height:1.6; color:#aaa; margin-bottom:2rem;">The \\"Mushroom of Immortality\\". Heavy in triterpenes that modulate the immune system and promote deep, restorative calm without acting as a sedative.</p>
                    
                    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #333; padding-top:1.5rem;">
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">STANDARDIZATION</span>
                            <span style="font-family:var(--font-mono); font-size:0.9rem; color:#ccc;">≥2% Triterpenes</span>
                        </div>
                        <div style="text-align:right;">
                            <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block;">CLINICAL DOSE</span>
                            <span style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff;">400<span style="font-size:0.8rem; font-weight:400;">mg</span></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Category: Synthesis Stack -->
        <div id="adaptogens" class="reveal">
            <div style="display:flex; align-items:center; gap:2rem; margin-bottom:3rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:1rem;">
                <div style="font-family:var(--font-mono); font-size:2rem; font-weight:700; color:var(--bg); opacity:0.2;">03</div>
                <div>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.5); margin-bottom:0.25rem;">Stress & Resilience</div>
                    <h2 style="font-family:var(--font-serif); font-size:2.5rem; margin:0; color:#fff;">Adaptogen Protocol</h2>
                </div>
            </div>
            
            <div style="display:grid; grid-template-columns:1fr; gap:2rem;">
                <!-- KSM-66 -->
                <div style="background:linear-gradient(135deg, #111, #1a1a1a); border:1px solid #444; border-radius:12px; padding:3rem; display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:center;" class="mobile-stack">
                    <div>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; color:#888; margin-bottom:1rem; border:1px solid #333; display:inline-block; padding:0.25rem 0.75rem; border-radius:20px;">CLINICALLY PATENTED</div>
                        <h3 style="font-family:var(--font-serif); font-size:2.5rem; color:#fff; margin-bottom:1rem;">Ashwagandha KSM-66®</h3>
                        <p style="font-size:1.15rem; line-height:1.6; color:#aaa; margin-bottom:2.5rem;">The most extensively studied, highly concentrated root extract in the world. Validated in 24 double-blind clinical trials to lower cortisol, reduce stress, and improve sleep quality.</p>
                        
                        <div style="display:flex; gap:3rem; border-top:1px solid #333; padding-top:1.5rem;">
                            <div>
                                <span style="font-family:var(--font-mono); font-size:0.75rem; color:#666; display:block;">EXTRACTION</span>
                                <span style="font-family:var(--font-mono); font-size:1rem; color:#ccc;">Milk/Water (No Alcohol)</span>
                            </div>
                            <div>
                                <span style="font-family:var(--font-mono); font-size:0.75rem; color:#666; display:block;">WITHANOLIDES</span>
                                <span style="font-family:var(--font-mono); font-size:1rem; color:#ccc;">≥ 5%</span>
                            </div>
                            <div>
                                <span style="font-family:var(--font-mono); font-size:0.75rem; color:#666; display:block;">DOSE</span>
                                <span style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff;">600<span style="font-size:0.8rem; font-weight:400;">mg</span></span>
                            </div>
                        </div>
                    </div>
                    
                    <div style="border-left:1px dashed #444; padding-left:3rem;" class="mobile-no-border">
                        <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:#fff; margin-bottom:1rem;">Why not standard Ashwagandha?</h4>
                        <p style="font-size:0.95rem; line-height:1.6; color:#888; margin-bottom:1.5rem;">Generic ashwagandha often uses the leaves (cheaper) rather than just the roots. Leaves contain Withaferin A, which is cytotoxic in high amounts. KSM-66 ensures 100% root extraction for safety and maximal efficacy.</p>
                        <ul style="font-size:0.9rem; color:#aaa; padding-left:1.5rem; display:flex; flex-direction:column; gap:0.5rem; margin:0;">
                            <li>Reduces perceived stress by 27%</li>
                            <li>Lowers serum cortisol by 24%</li>
                            <li>Improves VO2 max in athletes</li>
                        </ul>
                    </div>
                </div>

                <!-- L-Theanine & Bacopa Group -->
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(350px, 1fr)); gap:2rem;">
                    <div style="background:#111; border:1px solid #333; border-radius:12px; padding:2rem;">
                        <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block; margin-bottom:1rem;">ALPHA BRAIN WAVES</span>
                        <h3 style="font-family:var(--font-serif); font-size:1.75rem; color:#fff; margin-bottom:0.5rem;">L-Theanine</h3>
                        <p style="font-size:0.95rem; line-height:1.6; color:#888; margin-bottom:1.5rem;">Pharmaceutical-grade (≥98% purity). When paired with caffeine, it eliminates the jittery spikes, providing smooth, relaxed alertness.</p>
                        <div style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff; border-top:1px dashed #333; padding-top:1rem;">200<span style="font-size:0.8rem; font-weight:400;">mg</span></div>
                    </div>
                    
                    <div style="background:#111; border:1px solid #333; border-radius:12px; padding:2rem;">
                        <span style="font-family:var(--font-mono); font-size:0.7rem; color:#666; display:block; margin-bottom:1rem;">MEMORY ENHANCEMENT</span>
                        <h3 style="font-family:var(--font-serif); font-size:1.75rem; color:#fff; margin-bottom:0.5rem;">Bacopa Monnieri</h3>
                        <p style="font-size:0.95rem; line-height:1.6; color:#888; margin-bottom:1.5rem;">The Ayurvedic memory herb. We use an extract standardized to ≥50% bacosides, proven to accelerate speed of visual information processing.</p>
                        <div style="font-family:var(--font-mono); font-size:1.25rem; font-weight:700; color:#fff; border-top:1px dashed #333; padding-top:1rem;">300<span style="font-size:0.8rem; font-weight:400;">mg</span></div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</section>
'''

if old_ing_start != -1 and old_ing_end != -1:
    ing_html = ing_html[:old_ing_start] + NEW_INGREDIENTS + ing_html[old_ing_end:]
    with open('e:\\OXYBIO\\ingredients.html', 'w', encoding='utf-8') as f:
        f.write(ing_html)
    print("ingredients.html upgraded to premium dark formulary.")
else:
    print("Could not find ingredients boundaries.")


# ──────────────────────────────────────────────────────────
# 2. UPGRADE PROBLEM.HTML (Aesthetic Data Interface)
# ──────────────────────────────────────────────────────────
with open('e:\\OXYBIO\\problem.html', 'r', encoding='utf-8') as f:
    prob_html = f.read()

old_prob_start = prob_html.find('<!-- ═══════════════════════════════════════════════════════\n     LAYER 1: THE MARKET PROBLEM')
old_prob_end = prob_html.find('<!-- ═══════════════════════════════════════════════════════\n     LAYER 2: THE BEHAVIORAL PROBLEM')

NEW_PROBLEM = '''<!-- ═══════════════════════════════════════════════════════
     LAYER 1: THE MARKET PROBLEM (Premium Interface)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:#0a0a0a; color:#fff; border-top:1px solid #333; padding-top:var(--space-2xl); padding-bottom:var(--space-2xl); overflow:hidden; position:relative;">
    
    <!-- Radar/Scan Grid Background -->
    <div style="position:absolute; top:0; left:0; right:0; bottom:0; background-image: linear-gradient(#1a1a1a 1px, transparent 1px), linear-gradient(90deg, #1a1a1a 1px, transparent 1px); background-size: 40px 40px; opacity: 0.3; pointer-events:none;"></div>

    <div class="container reveal" style="position:relative; z-index:2;">
        
        <div style="text-align:center; max-width:800px; margin:0 auto 5rem;">
            <div style="display:inline-flex; align-items:center; gap:0.5rem; background:rgba(220,38,38,0.1); border:1px solid rgba(220,38,38,0.3); color:#ef4444; padding:0.5rem 1rem; border-radius:50px; font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; margin-bottom:1.5rem;">
                <span style="width:6px; height:6px; background:#ef4444; border-radius:50%; box-shadow:0 0 8px #ef4444;"></span> CRITICAL DIAGNOSTIC
            </div>
            <h2 style="font-family:var(--font-serif); font-size:clamp(3rem, 6vw, 4.5rem); line-height:1; letter-spacing:-0.03em; margin-bottom:1.5rem;">India's Hidden Crisis.</h2>
            <p style="font-size:1.25rem; line-height:1.6; color:#a3a3a3;">These are not estimates. These are empirical measurements from the ICMR, WHO, and the National Family Health Survey. The urban Indian workforce is operating on empty.</p>
        </div>

        <!-- The Crisis Terminal -->
        <div style="border:1px solid #333; background:rgba(10,10,10,0.8); backdrop-filter:blur(10px); border-radius:12px; overflow:hidden; box-shadow:0 20px 40px rgba(0,0,0,0.5);">
            <!-- Terminal Header -->
            <div style="display:flex; justify-content:space-between; align-items:center; padding:1rem 1.5rem; border-bottom:1px solid #333; background:#111;">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:#666;">POPULATION_SCAN_V2.1</div>
                <div style="display:flex; gap:0.5rem;">
                    <span style="width:10px; height:10px; border-radius:50%; background:#333;"></span>
                    <span style="width:10px; height:10px; border-radius:50%; background:#333;"></span>
                    <span style="width:10px; height:10px; border-radius:50%; background:#dc2626; box-shadow:0 0 10px rgba(220,38,38,0.5);"></span>
                </div>
            </div>

            <!-- Terminal Data Grid -->
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); border-bottom:1px solid #333;">
                
                <div style="padding:3rem; border-right:1px solid #333; position:relative;" class="mobile-no-border">
                    <div style="position:absolute; top:2rem; right:2rem; font-family:var(--font-mono); color:#ef4444; opacity:0.3;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                    </div>
                    <div class="data-num" data-target="85" data-suffix="%" style="font-size:4.5rem; letter-spacing:-0.05em; line-height:1; font-family:var(--font-sans); font-weight:800; color:#ef4444; margin-bottom:0.5rem;">85%</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem; color:#fff;">Vitamin D Deficient</h4>
                    <p style="font-size:0.95rem; line-height:1.5; color:#888;">Urban professional baseline heavily compromised.</p>
                    <div style="margin-top:2rem; height:2px; background:#222; width:100%; position:relative;">
                        <div style="position:absolute; top:0; left:0; height:100%; background:#ef4444; width:85%;"></div>
                    </div>
                </div>

                <div style="padding:3rem; border-right:1px solid #333; position:relative;" class="mobile-no-border">
                    <div style="position:absolute; top:2rem; right:2rem; font-family:var(--font-mono); color:#ef4444; opacity:0.3;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg>
                    </div>
                    <div class="data-num" data-target="47" data-suffix="%" style="font-size:4.5rem; letter-spacing:-0.05em; line-height:1; font-family:var(--font-sans); font-weight:800; color:#ef4444; margin-bottom:0.5rem;">47%</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem; color:#fff;">B12 Depleted</h4>
                    <p style="font-size:0.95rem; line-height:1.5; color:#888;">Critical for neurological function. Epidemic in vegetarian diets.</p>
                    <div style="margin-top:2rem; height:2px; background:#222; width:100%; position:relative;">
                        <div style="position:absolute; top:0; left:0; height:100%; background:#ef4444; width:47%;"></div>
                    </div>
                </div>

                <div style="padding:3rem; position:relative;">
                    <div style="position:absolute; top:2rem; right:2rem; font-family:var(--font-mono); color:#ef4444; opacity:0.3;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>
                    </div>
                    <div class="data-num" data-target="53" data-suffix="%" style="font-size:4.5rem; letter-spacing:-0.05em; line-height:1; font-family:var(--font-sans); font-weight:800; color:#ef4444; margin-bottom:0.5rem;">53%</div>
                    <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem; color:#fff;">Iron Malnourished</h4>
                    <p style="font-size:0.95rem; line-height:1.5; color:#888;">Severe among working women. Drops cognitive output by 20%.</p>
                    <div style="margin-top:2rem; height:2px; background:#222; width:100%; position:relative;">
                        <div style="position:absolute; top:0; left:0; height:100%; background:#ef4444; width:53%;"></div>
                    </div>
                </div>
            </div>

            <!-- Terminal Footer / Impact -->
            <div style="padding:3rem; background:linear-gradient(to right, rgba(220,38,38,0.05), transparent);">
                <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:2rem;">
                    <div style="max-width:600px;">
                        <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:#ef4444; margin-bottom:1rem; text-transform:uppercase;">Extrapolated Economic Impact</h4>
                        <p style="font-size:1.25rem; line-height:1.6; color:#ccc; margin:0;">
                            This nutritional gap physically alters brain function, causing chronic fatigue and brain fog. It costs the Indian GDP an estimated <strong>₹4.5 Lakh Crore</strong> annually in lost productivity.
                        </p>
                    </div>
                    <div>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; color:#888; text-align:right;">
                            SOURCES VERIFIED<br>
                            ICMR, NFHS-5, WHO (2022)
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</section>
'''

if old_prob_start != -1 and old_prob_end != -1:
    prob_html = prob_html[:old_prob_start] + NEW_PROBLEM + prob_html[old_prob_end:]
    with open('e:\\OXYBIO\\problem.html', 'w', encoding='utf-8') as f:
        f.write(prob_html)
    print("problem.html upgraded to premium diagnostic terminal.")
else:
    print("Could not find problem boundaries.")

# Finally add a tiny CSS fix for the new premium card hover effect
css_inject = """
/* Premium Sub-page Enhancements */
.premium-card-hover {
    transition: transform 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}
.premium-card-hover:hover {
    transform: translateY(-5px);
    border-color: rgba(255, 255, 255, 0.3) !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}
.mobile-no-border { }
@media(max-width: 768px) {
    .mobile-no-border { border-right: none !important; border-bottom: 1px solid #333; }
}
"""

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'a', encoding='cp1252') as f:
    f.write(css_inject)
print("CSS updated for premium cards.")
