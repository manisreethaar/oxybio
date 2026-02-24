import os, re

about_path = r'e:\OXYBIO\about.html'
with open(about_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_CONTENT = """
<main>

<!-- ═══════════════════════════════════════════════════════
     VISION & MISSION (Part 1)
════════════════════════════════════════════════════════ -->
<section class="structure-section" id="about-vision" style="padding-top:140px; border-bottom:none;">
    <div class="container">
        
        <!-- Hero -->
        <div class="flow-left reveal" style="max-width:900px; margin-bottom:var(--space-xl);">
            <div class="badge" style="margin-bottom:var(--space-md);">Our Vision & Mission</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">Why Oxygen<br><em>exists.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                This is not a corporate origin story. This is the honest account of a problem we couldn't ignore, a gap nobody was filling, and a decision to build something better.
            </p>
        </div>

        <!-- The Vision -->
        <div class="bento-grid reveal" style="margin-bottom:var(--space-xl);">
            <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                <div class="section-label" style="margin-bottom:var(--space-md);">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">The Vision</span>
                </div>
                <h2 style="font-family:var(--font-serif); font-size:2.5rem; margin-bottom:1rem; max-width:800px;">
                    Building India's First Precision Nutrition System.
                </h2>
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); display:flex; gap:1.5rem; flex-wrap:wrap; margin-bottom:2rem;">
                    <span>SUSTAINABLE</span>
                    <span>INDIGENOUS</span>
                    <span>CIRCULAR</span>
                </div>
                
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:2rem;">
                    <div>
                        <h4 style="font-family:var(--font-sans); font-weight:600; margin-bottom:0.5rem;">Sustainable Enterprise</h4>
                        <p style="color:var(--text-muted); font-size:0.95rem; line-height:1.6;">To build an innovation-driven biotechnology enterprise that prioritizes planetary health alongside human health.</p>
                    </div>
                    <div>
                        <h4 style="font-family:var(--font-sans); font-weight:600; margin-bottom:0.5rem;">Indigenous Resources</h4>
                        <p style="color:var(--text-muted); font-size:0.95rem; line-height:1.6;">To transform India's rich biological resources into globally competitive biocosmetic and food products.</p>
                    </div>
                    <div>
                        <h4 style="font-family:var(--font-sans); font-weight:600; margin-bottom:0.5rem;">Circular Bioeconomy</h4>
                        <p style="color:var(--text-muted); font-size:0.95rem; line-height:1.6;">To operate strictly through advanced biotechnology, circular bioeconomy principles, and responsible manufacturing.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- The Mission -->
        <div class="reveal" style="display:grid; grid-template-columns:1fr 1fr; gap:var(--space-lg);" class="mobile-stack">
            <div class="flow-left" style="position:sticky; top:120px;">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">The Mission</span>
                </div>
                <h2 class="headline" style="margin-top:var(--space-sm);">To make world-class nutrition accessible to every ambitious Indian.</h2>
                <p class="subtext" style="color:var(--text-muted); font-style:italic; margin-top:var(--space-sm);">By combining India's ancient ingredient wisdom with modern nutritional science — and refusing to compromise on either.</p>
            </div>
            
            <div class="editorial-col" style="font-size:1.125rem; line-height:1.7; color:var(--text-muted);">
                <p style="margin-bottom:1rem;">Oxygen exists to close the gap between what urban Indians need nutritionally and what the market currently offers them.</p>
                <p style="margin-bottom:1rem;">We believe Indian ingredients are world-class. We believe Indian consumers deserve products formulated to global scientific standards. We believe honesty about what is in a product is not a marketing strategy — it is a minimum standard that the industry has failed to meet.</p>
                <p style="margin-bottom:2rem; color:var(--text-main); font-weight:500;">Our mission is to build the products that prove all three beliefs simultaneously.</p>
                
                <h4 style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); margin-bottom:1rem;">The 3 Pillars</h4>
                <div style="border-left:2px solid var(--border); padding-left:1.5rem;">
                    <p style="margin-bottom:1.5rem;"><strong>1. Product & Commercial:</strong> To develop and commercialize safe, natural, and sustainable biocosmetic and food products using innovative bioprocessing, fermentation, and formulation technologies, ensuring financial viability and market competitiveness.</p>
                    <p style="margin-bottom:1.5rem;"><strong>2. Research & Innovation:</strong> To strengthen indigenous biotechnology innovation by advancing research in bioprocess engineering, microbial fermentation, and nanotechnology, supported through government grants, academic collaboration, and applied research programs.</p>
                    <p><strong>3. Impact & Ecosystem:</strong> To create long-term environmental, social, and economic impact by supporting circular bioeconomy practices, enabling skill development through student mentorship and internships, generating employment, and aligning operations with national initiatives such as Make in India and sustainability-driven growth.</p>
                </div>
            </div>
        </div>

    </div>
</section>


<!-- ═══════════════════════════════════════════════════════
     FOUNDER & TEAM (Part 2)
════════════════════════════════════════════════════════ -->
<section class="structure-section" id="about-founder" style="background:var(--bg-alt); border-top:1px solid var(--border);">
    <div class="container">
        
        <!-- Hero -->
        <div class="flow-left reveal" style="max-width:900px; margin-bottom:var(--space-xl);">
            <div class="badge" style="margin-bottom:var(--space-md); border-color:var(--text-main);">The People Behind Oxygen</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">Built by<br><em>scientists.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                We aren't nutritionists who became entrepreneurs. We are people who were frustrated by what existed and decided to fix it properly.
            </p>
        </div>

        <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;" class="mobile-stack reveal">
            <!-- Sidebar Navigation / Chapters -->
            <div style="position:sticky; top:120px;" class="editorial-col">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:2rem;">INDEX</div>
                <ul style="list-style:none; padding:0; margin:0; border-left:1px solid var(--border); padding-left:1.5rem; display:flex; flex-direction:column; gap:1.5rem;">
                    <li style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-main);">01. The Hook</li>
                    <li style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-muted);">02. The Founder</li>
                    <li style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-muted);">03. Our Approach</li>
                    <li style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-muted);">04. The Journey</li>
                </ul>
            </div>

            <!-- Main Content Chapters -->
            <div>
                <!-- Chapter 01 -->
                <div style="margin-bottom:var(--space-xl);">
                    <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">CHAPTER 01</div>
                    <h3 class="headline" style="font-size:2rem; margin-bottom:1.5rem;">The Hook</h3>
                    <div class="editorial-col" style="font-size:1.125rem; line-height:1.7; color:var(--text-muted);">
                        <p style="margin-bottom:1rem;">We spent six months trying to find a daily nutrition product we would actually recommend to someone we cared about. We could not find one. Either the science was inadequate, or the ingredients were compromised, or the price was inaccessible, or it was designed for a Western diet and simply repacked for India.</p>
                        <div style="background:var(--bg); border:1px solid var(--border); padding:2rem; margin:2rem 0;">
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-main); margin-bottom:0.5rem;">Research Result</h4>
                            <p style="font-size:0.95rem; margin-bottom:0;">We analyzed blood reports from urban Indians across multiple cities. The pattern was consistent and alarming. Seven out of ten showed at least one significant deficiency. Most were health-conscious people. Most were not eating badly by any measure. Most had no idea they were deficient.</p>
                        </div>
                        <p style="color:var(--text-main); font-weight:500; font-style:italic;">The food system was failing people who were trying to do the right thing. "We decided the only option was to build it ourselves."</p>
                    </div>
                </div>

                <!-- Chapter 02 -->
                <div style="margin-bottom:var(--space-xl); padding-top:var(--space-xl); border-top:1px dashed var(--border);">
                    <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">CHAPTER 02</div>
                    <h3 class="headline" style="font-size:2rem; margin-bottom:1.5rem;">The Founder</h3>
                    <div class="editorial-col" style="font-size:1.125rem; line-height:1.7; color:var(--text-muted);">
                        <p style="color:var(--text-main); font-weight:600; font-family:var(--font-serif); font-size:1.5rem; margin-bottom:0.5rem;">Chief Science Officer</p>
                        <p style="margin-bottom:1.5rem;">A pharmaceutical scientist who turned fermentation into food — with the precision of a lab and the soul of a craft.</p>
                        
                        <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-main); padding:1rem; border:1px solid var(--border); margin-bottom:2rem; background:var(--bg);">
                            Operating at the intersection of:<br>
                            🔬 Pharmaceutical Bioprocessing × 🧬 Nanoscience × 🌾 Fermented Food
                        </div>

                        <ul style="padding-left:1.5rem; margin-bottom:2rem;">
                            <li style="margin-bottom:0.5rem;">Incubated at TBI — Technology Business Incubator, ACE Hosur</li>
                            <li>Personally analyzed 200+ peer-reviewed studies for this project</li>
                        </ul>

                        <blockquote style="font-family:var(--font-serif); font-size:1.5rem; line-height:1.4; color:var(--bg); background:var(--text-main); padding:2rem; margin:2rem 0; font-style:italic;">
                            "I am building Oxygen because I am genuinely angry at what the market currently offers people who are trying to take their health seriously. I have seen the research. I know what good nutrition science looks like. And I know that the gap between what is possible and what is being sold is not technical — it is a choice. We are choosing differently."
                        </blockquote>

                        <p style="font-size:0.95rem;"><strong>Responsible for:</strong> Formulation Design, Ingredient Sourcing, Clinical Study Protocol, Science Communication</p>
                    </div>
                </div>

                <!-- Chapter 03 -->
                <div style="margin-bottom:var(--space-xl); padding-top:var(--space-xl); border-top:1px dashed var(--border);">
                    <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">CHAPTER 03</div>
                    <h3 class="headline" style="font-size:2rem; margin-bottom:1.5rem;">Our Approach</h3>
                    
                    <div class="bento-grid" style="grid-template-columns:1fr 1fr;">
                        <div class="bento-cell" style="background:var(--bg);">
                            <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">01</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Science Before Marketing</h4>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.5;">We designed the formulation before we designed the brand. We chose ingredients before we chose colors. We cited our evidence before we wrote our copy. This is backwards from how most nutrition companies work. We think it is the only sensible order.</p>
                        </div>
                        <div class="bento-cell" style="background:var(--bg);">
                            <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">02</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">India Is Not a Market Segment</h4>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.5;">We did not take a Western formula and add Ashwagandha to make it Indian. We started from India. From what Indian bodies are deficient in. From what Indian ingredients can provide. From what Indian lifestyles demand.</p>
                        </div>
                        <div class="bento-cell" style="background:var(--bg);">
                            <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">03</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Transparency Is Not Optional</h4>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.5;">We will publish our lab reports. We will name our ingredient suppliers. We will cite the studies behind our claims. We will tell you when a study is preliminary and when it is robust.</p>
                        </div>
                        <div class="bento-cell" style="background:var(--bg);">
                            <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">04</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Dose Matters</h4>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.5;">Ashwagandha at 50mg is not the same as Ashwagandha at 300mg. Lion's Mane at 100mg is not what the research studied. We formulate at clinically relevant doses — not at doses that allow us to put the ingredient on the label.</p>
                        </div>
                        <div class="bento-cell" style="background:var(--bg);">
                            <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">05</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Bioavailability First</h4>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.5;">A 100mg dose with 5% absorption delivers 5mg to your body. A 50mg dose with 35% absorption delivers 17.5mg. The nutrient that reaches your bloodstream is the only nutrient that matters.</p>
                        </div>
                        <div class="bento-cell" style="background:var(--bg);">
                            <div style="font-family:var(--font-mono); font-size:1.5rem; color:var(--text-muted); margin-bottom:0.5rem;">06</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Clinical Evidence</h4>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.5;">We designed our clinical study before we manufactured our first batch. Not because we are required to, but because we believe no company should sell a health product without evidence that it works.</p>
                        </div>
                    </div>
                </div>

                <!-- Chapter 04 -->
                <div style="padding-top:var(--space-xl); border-top:1px dashed var(--border);">
                    <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">CHAPTER 04</div>
                    <h3 class="headline" style="font-size:2rem; margin-bottom:1.5rem;">The Journey So Far</h3>
                    <p style="font-size:1.125rem; color:var(--text-muted); margin-bottom:2rem; max-width:600px;">What we have built before we built anything physical. Most companies build first and think about science second. We spent months thinking about the science before building anything.</p>

                    <div style="display:flex; flex-direction:column; gap:1.5rem;">
                        <div style="border-left:2px solid var(--text-main); padding-left:1.5rem;">
                            <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-main); margin-bottom:0.5rem;">COMPLETED</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">6+ months of nutritional deficiency research</h4>
                            <p style="font-size:0.95rem; color:var(--text-muted);">Analyzed ICMR, NFHS-5, WHO India data. Mapped exact deficiency profiles by demographic and lifestyle. Built the evidence base for product necessity.</p>
                        </div>
                        <div style="border-left:2px solid var(--text-main); padding-left:1.5rem;">
                            <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-main); margin-bottom:0.5rem;">COMPLETED</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Complete formulation design</h4>
                            <p style="font-size:0.95rem; color:var(--text-muted);">Reviewed 200+ peer-reviewed studies. Designed complete formulas for 3 drinks + 1 bar. Every ingredient evidence-based. Every dose clinically relevant.</p>
                        </div>
                        <div style="border-left:2px solid var(--border); padding-left:1.5rem;">
                            <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem;">IN PROGRESS</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Regulatory pathway fully mapped</h4>
                            <p style="font-size:0.95rem; color:var(--text-muted);">FSSAI compliance audited per ingredient. Clinical study protocol designed. Ethics committee application in process. Label compliance framework completed.</p>
                        </div>
                        <div style="border-left:2px solid var(--border); padding-left:1.5rem;">
                            <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem;">ACTIVE</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">TBI Incubation secured</h4>
                            <p style="font-size:0.95rem; color:var(--text-muted);">Accepted by Technology Business Incubator at ACE, Hosur. Prototype development currently underway. Sensory testing beginning soon.</p>
                        </div>
                        <div style="border-left:2px solid var(--border); padding-left:1.5rem;">
                            <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem;">GROWING</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Waitlist growing</h4>
                            <p style="font-size:0.95rem; color:var(--text-muted);">Before a single product exists — validation that the demand is real. Real people who believe something better should exist.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</section>

</main>
"""

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + FOOTER)

print("Updated about.html with comprehensive Vision, Mission, and Founder content.")
