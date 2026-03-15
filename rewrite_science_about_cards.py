"""
Rewrite static cards in science.html and about.html to use the new animated premium designs.
"""
import re

# ==========================================
# 1. REWRITE ABOUT.HTML (The 6 Static Cards)
# ==========================================
about_path = r'e:\OXYBIO\about.html'
with open(about_path, 'r', encoding='utf-8') as f:
    about = f.read()

# Replace the entire grid of 6 cards with the new animated-card-grid and premium-anim-card
new_about_cards = """
                            <!-- Premium Animated Approach List -->
                            <div class="animated-card-grid reveal">

                                <!-- Card 01 -->
                                <div class="premium-anim-card">
                                    <div style="font-family:var(--font-mono); font-size:4rem; font-weight:800; color:rgba(13, 138, 116, 0.08); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;" class="bg-num">01</div>
                                    <h4 class="anim-card-title" style="padding-right:3rem; position:relative; z-index:2;">Science Before Marketing</h4>
                                    <div class="anim-card-text" style="position:relative; z-index:2;">
                                        We designed the formulation before we designed the brand. We chose ingredients
                                        before we chose colors. This is backwards from how most nutrition companies
                                        work. We think it is the only sensible order.
                                    </div>
                                </div>

                                <!-- Card 02 -->
                                <div class="premium-anim-card">
                                    <div style="font-family:var(--font-mono); font-size:4rem; font-weight:800; color:rgba(13, 138, 116, 0.08); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;" class="bg-num">02</div>
                                    <h4 class="anim-card-title" style="padding-right:3rem; position:relative; z-index:2;">India Is Not a Market Segment</h4>
                                    <div class="anim-card-text" style="position:relative; z-index:2;">
                                        We did not take a Western formula and add Ashwagandha to make it Indian. We
                                        started from India. From what Indian bodies are deficient in. From what Indian
                                        ingredients can provide.
                                    </div>
                                </div>

                                <!-- Card 03 -->
                                <div class="premium-anim-card">
                                    <div style="font-family:var(--font-mono); font-size:4rem; font-weight:800; color:rgba(13, 138, 116, 0.08); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;" class="bg-num">03</div>
                                    <h4 class="anim-card-title" style="padding-right:3rem; position:relative; z-index:2;">Transparency Is Not Optional</h4>
                                    <div class="anim-card-text" style="position:relative; z-index:2;">
                                        We publish our lab reports. We name our ingredient suppliers. We cite the
                                        studies behind our claims. We tell you when a study is preliminary and when it
                                        is robust.
                                    </div>
                                </div>

                                <!-- Card 04 -->
                                <div class="premium-anim-card">
                                    <div style="font-family:var(--font-mono); font-size:4rem; font-weight:800; color:rgba(13, 138, 116, 0.08); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;" class="bg-num">04</div>
                                    <h4 class="anim-card-title" style="padding-right:3rem; position:relative; z-index:2;">Dose Matters</h4>
                                    <div class="anim-card-text" style="position:relative; z-index:2;">
                                        Ashwagandha at 50mg is not the same as Ashwagandha at 300mg. We formulate at
                                        scientifically rigorous doses &mdash; not at doses that merely allow us to list the
                                        ingredient on the label.
                                    </div>
                                </div>

                                <!-- Card 05 -->
                                <div class="premium-anim-card">
                                    <div style="font-family:var(--font-mono); font-size:4rem; font-weight:800; color:rgba(13, 138, 116, 0.08); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;" class="bg-num">05</div>
                                    <h4 class="anim-card-title" style="padding-right:3rem; position:relative; z-index:2;">Bioavailability First</h4>
                                    <div class="anim-card-text" style="position:relative; z-index:2;">
                                        A 100mg dose with 5% absorption delivers 5mg to your body. A 50mg dose with 35%
                                        absorption delivers 17.5mg. The nutrient that reaches your bloodstream is the
                                        only one that matters.
                                    </div>
                                </div>

                                <!-- Card 06 -->
                                <div class="premium-anim-card">
                                    <div style="font-family:var(--font-mono); font-size:4rem; font-weight:800; color:rgba(13, 138, 116, 0.08); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;" class="bg-num">06</div>
                                    <h4 class="anim-card-title" style="padding-right:3rem; position:relative; z-index:2;">Clinical Evidence</h4>
                                    <div class="anim-card-text" style="position:relative; z-index:2;">
                                        We committed to designing our clinical validation study before manufacturing any
                                        product — not because regulations require it, but because no company should sell
                                        a health product without a pre-committed plan to prove it works.
                                    </div>
                                </div>

                            </div>
"""

# Extract the block to replace
about_block_match = re.search(r'<!-- Premium numbered approach list -->.*?<div style="display:grid[^>]*>.*?<!-- Card 06 -->.*?</div>\s*</div>', about, re.DOTALL)
if about_block_match:
    about = about.replace(about_block_match.group(0), new_about_cards)
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(about)
    print("Replaced 6 cards in about.html")
else:
    print("WARNING: Could not find the 6 cards grid in about.html")


# ==========================================
# 2. REWRITE SCIENCE.HTML (The Inline Iron Box)
# ==========================================
science_path = r'e:\OXYBIO\science.html'
with open(science_path, 'r', encoding='utf-8') as f:
    science = f.read()

new_science_iron = """
                        <div class="visual-compare-list reveal" style="margin-top: 2rem;">
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
                                        <div class="bar-track"><div class="bar-fill active" style="width: 58%;"></div></div>
                                        <div class="bar-value active" style="width:50px;">58%</div>
                                    </div>
                                </div>
                            </div>
                        </div>
"""

science_block_match = re.search(r'<div[^>]*style="background:var\(--bg\); border:1px solid var\(--border\); padding:2rem; font-family:monospace;"[^>]*>.*?FERROUS SULFATE.*?</div>\s*</div>', science, re.DOTALL)
if science_block_match:
    science = science.replace(science_block_match.group(0), new_science_iron)
    with open(science_path, 'w', encoding='utf-8') as f:
        f.write(science)
    print("Replaced inline iron box in science.html")
else:
    print("WARNING: Could not find the inline iron box in science.html")

