import os, re

# ==========================================
# 1. APPEND CSS TO v2_premium.css
# ==========================================

css_append = """

/* 8. PREMIUM ANIMATED CARDS (Replacing Tables) */
.animated-card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.premium-anim-card {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2rem;
    position: relative;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    opacity: 0;
    transform: translateY(30px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
}

.premium-anim-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--text-main);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.premium-anim-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.06);
    border-color: rgba(10,10,10,0.1);
}

.premium-anim-card:hover::before {
    transform: scaleX(1);
}

/* Staggered reveal triggered by IntersectionObserver or delay */
.reveal .premium-anim-card, 
.premium-anim-card.revealed {
    animation: cardFloatUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.premium-anim-card:nth-child(1) { animation-delay: 0.1s; }
.premium-anim-card:nth-child(2) { animation-delay: 0.2s; }
.premium-anim-card:nth-child(3) { animation-delay: 0.3s; }
.premium-anim-card:nth-child(4) { animation-delay: 0.4s; }

@keyframes cardFloatUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.anim-card-tag {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.3rem 0.8rem;
    background: var(--bg-alt);
    border-radius: 100px;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
}

.anim-card-title {
    font-family: var(--font-serif);
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--text-main);
    line-height: 1.2;
}

.anim-card-text {
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--text-muted);
}

/* 9. VISUAL PROGRESS BAR COMPARISON (Nutrients) */
.visual-compare-list {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    width: 100%;
}

.compare-row {
    background: #1a1a1a;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 1.25rem 1.5rem;
    display: grid;
    grid-template-columns: 100px 1fr;
    gap: 1.5rem;
    align-items: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s ease, border-color 0.3s ease;
}

.compare-row:hover {
    transform: scale(1.02);
    border-color: #555;
}

.compare-nutrient {
    font-family: var(--font-serif);
    font-size: 1.1rem;
    font-weight: 700;
    color: #fff;
}

.compare-bars {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    width: 100%;
}

.bar-wrapper {
    display: flex;
    align-items: center;
    gap: 1rem;
    width: 100%;
}

.bar-label {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    color: #888;
    width: 80px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.bar-track {
    flex: 1;
    height: 6px;
    background: #222;
    border-radius: 100px;
    overflow: hidden;
    position: relative;
}

.bar-fill {
    height: 100%;
    border-radius: 100px;
    width: 0%; /* Animates in via JS or CSS */
    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal .bar-fill {
    /* When inside a reveal section, the width is set by an inline style var or class */
}

.bar-fill.generic { background: #555; }
.bar-fill.active { background: #4ade80; box-shadow: 0 0 10px rgba(74, 222, 128, 0.4); }

.bar-value {
    font-family: var(--font-mono);
    font-size: 0.8rem;
    font-weight: 700;
    width: 40px;
    text-align: right;
}

.bar-value.generic { color: #888; }
.bar-value.active { color: #4ade80; }

@media (max-width: 768px) {
    .compare-row {
        grid-template-columns: 1fr;
        gap: 1rem;
    }
    .compare-nutrient {
        border-bottom: 1px solid #333;
        padding-bottom: 0.5rem;
    }
}
"""

css_path = r'e:\OXYBIO\assets\css\v2_premium.css'
with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_append)
print("Appended CSS to v2_premium.css")


# ==========================================
# 2. REWRITE HTML IN problem.html
# ==========================================

html_path = r'e:\OXYBIO\problem.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Table 1 (Market Response)
new_cards_html = """
                <!-- PREMIUM ANIMATED MARKET CARDS -->
                <div class="animated-card-grid">
                    <div class="premium-anim-card">
                        <div class="anim-card-tag">Traditional Drinks</div>
                        <h4 class="anim-card-title">Horlicks & Bournvita</h4>
                        <div class="anim-card-text">
                            <strong>The Offer:</strong> Strong distribution, nostalgic taste.<br><br>
                            <strong>The Failure:</strong> Sugar: 16-18g/serving. Cheapest synthetic forms. Zero adaptogens. Formulations designed in the 1970s.
                        </div>
                    </div>
                    
                    <div class="premium-anim-card">
                        <div class="anim-card-tag">Protein Supplements</div>
                        <h4 class="anim-card-title">MuscleBlaze & ON India</h4>
                        <div class="anim-card-text">
                            <strong>The Offer:</strong> High protein density.<br><br>
                            <strong>The Failure:</strong> Designed for narrow outcome (muscle mass). Ignores micronutrient deficiency. Primarily targets gym users.
                        </div>
                    </div>
                    
                    <div class="premium-anim-card">
                        <div class="anim-card-tag">Imported Premium</div>
                        <h4 class="anim-card-title">AG1, Huel, Ritual</h4>
                        <div class="anim-card-text">
                            <strong>The Offer:</strong> Genuine science, high-quality forms.<br><br>
                            <strong>The Failure:</strong> Prohibitively costly for daily use (₹350-500/serving), no Indian indigenous ingredients, ignores Indian usage patterns.
                        </div>
                    </div>

                    <div class="premium-anim-card">
                        <div class="anim-card-tag">Recent Startups</div>
                        <h4 class="anim-card-title">Emerging D2C Brands</h4>
                        <div class="anim-card-text">
                            <strong>The Offer:</strong> Modern positioning, good design.<br><br>
                            <strong>The Failure:</strong> Marketing companies, not science companies. Label claims lack clinical evidence, heavily under-dosed actives.
                        </div>
                    </div>
                </div>
"""

# Find the whole div surrounding the first table layout to replace
table1_match = re.search(r'<div style="overflow-x:auto;">\s*<div class="table-responsive"[^>]*>\s*<table class="data-journal-table"[^>]*>.*?</table>\s*</div>', html, re.DOTALL)
if table1_match:
    html = html.replace(table1_match.group(0), new_cards_html)
    print("Replaced Table 1 (Market)")
else:
    print("WARNING: Table 1 not found via regex.")


# Replace Table 2 (Nutrients)
new_bars_html = """
                                <!-- PREMIUM VISUAL ABSORPTION PROGRESS BARS -->
                                <div class="visual-compare-list reveal">
                                    <div class="compare-row">
                                        <div class="compare-nutrient">Iron</div>
                                        <div class="compare-bars">
                                            <div class="bar-wrapper">
                                                <div class="bar-label">FeSO4 (Generic)</div>
                                                <div class="bar-track"><div class="bar-fill generic" style="width: 8%;"></div></div>
                                                <div class="bar-value generic">8%</div>
                                            </div>
                                            <div class="bar-wrapper">
                                                <div class="bar-label">Fe-Bisglycinate</div>
                                                <div class="bar-track"><div class="bar-fill active" style="width: 28%;"></div></div>
                                                <div class="bar-value active">28%</div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="compare-row">
                                        <div class="compare-nutrient">Zinc</div>
                                        <div class="compare-bars">
                                            <div class="bar-wrapper">
                                                <div class="bar-label">ZnO (Generic)</div>
                                                <div class="bar-track"><div class="bar-fill generic" style="width: 12%;"></div></div>
                                                <div class="bar-value generic">12%</div>
                                            </div>
                                            <div class="bar-wrapper">
                                                <div class="bar-label">Zn-Bisglycinate</div>
                                                <div class="bar-track"><div class="bar-fill active" style="width: 41%;"></div></div>
                                                <div class="bar-value active">41%</div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="compare-row">
                                        <div class="compare-nutrient">Magnesium</div>
                                        <div class="compare-bars">
                                            <div class="bar-wrapper">
                                                <div class="bar-label">MgO (Generic)</div>
                                                <div class="bar-track"><div class="bar-fill generic" style="width: 4%;"></div></div>
                                                <div class="bar-value generic">4%</div>
                                            </div>
                                            <div class="bar-wrapper">
                                                <div class="bar-label">Mg-Glycinate</div>
                                                <div class="bar-track"><div class="bar-fill active" style="width: 23%;"></div></div>
                                                <div class="bar-value active">23%</div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="compare-row">
                                        <div class="compare-nutrient">B12</div>
                                        <div class="compare-bars">
                                            <div class="bar-wrapper">
                                                <div class="bar-label">Cyanocobalamin</div>
                                                <div class="bar-track"><div class="bar-fill generic" style="width: 15%;"></div></div>
                                                <div class="bar-value generic">15%</div>
                                            </div>
                                            <div class="bar-wrapper">
                                                <div class="bar-label">Methylcobalamin</div>
                                                <div class="bar-track"><div class="bar-fill active" style="width: 55%;"></div></div>
                                                <div class="bar-value active">55%</div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="compare-row">
                                        <div class="compare-nutrient">Folate</div>
                                        <div class="compare-bars">
                                            <div class="bar-wrapper">
                                                <div class="bar-label">Folic Acid</div>
                                                <div class="bar-track"><div class="bar-fill generic" style="width: 20%;"></div></div>
                                                <div class="bar-value generic">20%</div>
                                            </div>
                                            <div class="bar-wrapper">
                                                <div class="bar-label">5-MTHF</div>
                                                <div class="bar-track"><div class="bar-fill active" style="width: 70%;"></div></div>
                                                <div class="bar-value active">70%</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
"""

table2_match = re.search(r'<div class="table-responsive"[^>]*>\s*<table class="data-journal-table"[^>]*>.*?</table>\s*</div>', html, re.DOTALL)
if table2_match:
    html = html.replace(table2_match.group(0), new_bars_html)
    print("Replaced Table 2 (Nutrients)")
else:
    print("WARNING: Table 2 not found via regex.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished updates.")
