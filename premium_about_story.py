import codecs
import re

with codecs.open('e:\\OXYBIO\\about.html', 'r', 'utf-8') as f:
    html = f.read()

# Define the replacement block
NEW_STORY = '''<section class="structure-section" id="about-story" style="background:#0a0a0a; color:#fff; border-bottom:1px solid #333; padding-bottom:var(--space-2xl); position:relative; overflow:hidden;">
    
    <!-- Abstract dark mode background glow -->
    <div style="position:absolute; top:0; left:50%; transform:translateX(-50%); width:1000px; height:1000px; background:radial-gradient(circle, rgba(255,255,255,0.02) 0%, transparent 60%); pointer-events:none;"></div>
    
    <div class="container" style="position:relative; z-index:2; padding-top:140px;">

        <!-- Hero -->
        <div class="flow-left reveal" style="max-width:900px; margin-bottom:6rem;">
            <div class="badge" style="margin-bottom:var(--space-md); border-color:#333; color:#ccc; background:transparent;">Origin Protocol</div>
            <h1 class="display" style="font-size:clamp(4rem, 8vw, 6rem); line-height:0.95; letter-spacing:-0.03em;">Built from<br><em style="color:#aaa; font-weight:400;">frustration.</em></h1>
            <p class="editorial-col" style="margin-top:2.5rem; font-size:1.25rem; line-height:1.6; color:#a3a3a3;">
                This is not a corporate origin story. This is the honest account of a problem we couldn't ignore, a gap nobody was filling, and a decision to build something better.
            </p>
        </div>

        <!-- Story Chapters: layout override -->
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;" class="mobile-stack reveal">

            <!-- Sidebar Index -->
            <div style="position:sticky; top:120px;" class="editorial-col">
                <div style="font-family:var(--font-mono); font-size:var(--text-xs); letter-spacing:0.1em; color:#666; margin-bottom:2rem; text-transform:uppercase;">THE ARCHIVES</div>
                <ul style="list-style:none; padding:0; margin:0; border-left:1px solid #333; padding-left:1.5rem; display:flex; flex-direction:column; gap:1.5rem;">
                    <li class="index-nav-item" data-target="chapter-01" style="font-family:var(--font-serif); font-size:1.5rem; color:#fff; font-weight:600; cursor:pointer; transition:color 0.3s ease;">
                        01. The Hook</li>
                    <li class="index-nav-item" data-target="chapter-02" style="font-family:var(--font-serif); font-size:1.5rem; color:#666; cursor:pointer; transition:color 0.3s ease;">
                        02. The Journey</li>
                </ul>
            </div>

            <!-- Chapters Content (Dark Premium) -->
            <div>
                <!-- Chapter 01: The Hook (Diagnostic Aesthetic) -->
                <div id="chapter-01" class="chapter-section" style="margin-bottom:6rem;">
                    <div style="display:inline-flex; align-items:center; gap:0.5rem; font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#888; margin-bottom:1.5rem; border:1px solid #333; padding:0.4rem 0.8rem; border-radius:50px;">
                        <span style="width:6px; height:6px; background:#ef4444; border-radius:50%;"></span> CHAPTER 01
                    </div>
                    <h3 class="headline" style="font-size:3rem; line-height:var(--leading-tight); margin-bottom:1.5rem; color:#fff;">The Hook</h3>
                    
                    <div class="editorial-col" style="font-size:1.15rem; line-height:1.7; color:#a3a3a3;">
                        <p style="margin-bottom:2rem;">We spent six months trying to find a daily nutrition product we would actually recommend to someone we cared about. We could not find one. Either the science was inadequate, or the ingredients were compromised, or the price was inaccessible, or it was designed for a Western diet and simply repacked for India.</p>
                        
                        <!-- Premium Research Result Block -->
                        <div style="background:#111; border:1px solid #333; border-radius:12px; padding:3rem; margin:3rem 0; position:relative; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.5);">
                            <div style="position:absolute; top:2rem; right:2rem; color:#333;">
                                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                            </div>
                            <h4 style="font-family:var(--font-sans); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; color:#ef4444; margin-bottom:1rem;">Diagnostic Result //</h4>
                            <p style="font-family:var(--font-serif); font-size:1.5rem; line-height:1.6; color:#fff; margin-bottom:0;">
                                We analyzed blood reports from urban Indians across multiple cities. The pattern was consistent and alarming. Seven out of ten showed at least one significant deficiency. Most were health-conscious people who had no idea they were deficient.
                            </p>
                        </div>
                        
                        <p style="color:#fff; font-size:1.35rem; font-family:var(--font-serif); font-style:italic; border-left:2px solid #fff; padding-left:1.5rem;">
                            The food system was failing people who were trying to do the right thing.<br>
                            "We decided the only option was to build it ourselves."
                        </p>
                    </div>
                </div>

                <!-- Chapter 02: The Journey (Illuminated Timeline) -->
                <div id="chapter-02" class="chapter-section" style="padding-top:6rem; border-top:1px dashed #333;">
                    <div style="display:inline-flex; align-items:center; gap:0.5rem; font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#888; margin-bottom:1.5rem; border:1px solid #333; padding:0.4rem 0.8rem; border-radius:50px;">
                        <span style="width:6px; height:6px; background:#10b981; border-radius:50%;"></span> CHAPTER 02
                    </div>
                    <h3 class="headline" style="font-size:3rem; line-height:var(--leading-tight); margin-bottom:1.5rem; color:#fff;">The Journey So Far</h3>
                    <p style="font-size:1.15rem; line-height:1.7; color:#a3a3a3; margin-bottom:4rem; max-width:600px;">
                        What we have built before we built anything physical. Most companies build first and think about science second. We spent months thinking about the science before building anything.
                    </p>

                    <!-- Glowing Timeline -->
                    <div style="display:flex; flex-direction:column; gap:0; position:relative;">
                        <!-- Continuous vertical line -->
                        <div style="position:absolute; left:24px; top:0; bottom:0; width:1px; background:linear-gradient(to bottom, #333 0%, #333 80%, transparent 100%);"></div>
                        
                        <!-- Timeline Nodes -->
                        <!-- Node 1 -->
                        <div style="position:relative; padding-left:5rem; padding-bottom:3rem; transition:transform 0.3s ease;">
                            <div style="position:absolute; left:18px; top:4px; width:13px; height:13px; background:#10b981; border-radius:50%; box-shadow:0 0 15px rgba(16, 185, 129, 0.4); z-index:2; border:2px solid #0a0a0a;"></div>
                            <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#10b981; margin-bottom:0.5rem;">COMPLETED PHASE</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem; color:#fff;">6+ months of nutritional deficiency research</h4>
                            <p style="font-size:1.05rem; line-height:1.6; color:#888;">Analyzed ICMR, NFHS-5, WHO India data. Mapped exact deficiency profiles by demographic and lifestyle. Built the evidence base for product necessity.</p>
                        </div>

                        <!-- Node 2 -->
                        <div style="position:relative; padding-left:5rem; padding-bottom:3rem; transition:transform 0.3s ease;">
                            <div style="position:absolute; left:18px; top:4px; width:13px; height:13px; background:#10b981; border-radius:50%; box-shadow:0 0 15px rgba(16, 185, 129, 0.4); z-index:2; border:2px solid #0a0a0a;"></div>
                            <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#10b981; margin-bottom:0.5rem;">COMPLETED PHASE</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem; color:#fff;">Complete formulation design</h4>
                            <p style="font-size:1.05rem; line-height:1.6; color:#888;">Reviewed 200+ peer-reviewed studies. Designed complete formulas for 3 drinks + 1 bar. Every ingredient evidence-based. Every dose clinically relevant.</p>
                        </div>

                        <!-- Node 3 -->
                        <div style="position:relative; padding-left:5rem; padding-bottom:3rem; transition:transform 0.3s ease;">
                            <div style="position:absolute; left:18px; top:4px; width:13px; height:13px; background:var(--accent-mid); border-radius:50%; box-shadow:0 0 15px rgba(255, 255, 255, 0.3); z-index:2; border:2px solid #0a0a0a;"></div>
                            <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#ccc; margin-bottom:0.5rem;">IN PROGRESS</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem; color:#fff;">Regulatory pathway fully mapped</h4>
                            <p style="font-size:1.05rem; line-height:1.6; color:#888;">FSSAI compliance audited per ingredient. Clinical study protocol designed. Ethics committee application in process. Label compliance framework completed.</p>
                        </div>

                        <!-- Node 4 -->
                        <div style="position:relative; padding-left:5rem; padding-bottom:3rem; transition:transform 0.3s ease;">
                            <div style="position:absolute; left:18px; top:4px; width:13px; height:13px; background:#3b82f6; border-radius:50%; box-shadow:0 0 15px rgba(59, 130, 246, 0.4); z-index:2; border:2px solid #0a0a0a;"></div>
                            <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#3b82f6; margin-bottom:0.5rem;">ACTIVE STAGE</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem; color:#fff;">TBI Incubation secured</h4>
                            <p style="font-size:1.05rem; line-height:1.6; color:#888;">Accepted by Technology Business Incubator at ACE, Hosur. Prototype development currently underway. Sensory testing beginning soon.</p>
                        </div>

                        <!-- Node 5 -->
                        <div style="position:relative; padding-left:5rem; padding-bottom:0;">
                            <div style="position:absolute; left:18px; top:4px; width:13px; height:13px; background:var(--bg); border-radius:50%; z-index:2; border:2px solid #555;"></div>
                            <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#666; margin-bottom:0.5rem;">GROWING</div>
                            <h4 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:0.5rem; color:#fff;">Waitlist growth</h4>
                            <p style="font-size:1.05rem; line-height:1.6; color:#888;">Before a single product exists — validation that the demand is real. Real people who believe something better should exist.</p>
                        </div>

                    </div>
                </div>
            </div>
            
        </div>
    </div>
</section>
'''

# Use regex to find the `about-story` section and replace it up until the next section
pattern = re.compile(r'<section class=\"structure-section\" id=\"about-story\".*?(?=<!-- ═══════════════════════════════════════════════════════\s*SECTION 2)', re.DOTALL)

if pattern.search(html):
    new_html = pattern.sub(NEW_STORY, html, count=1)
    with codecs.open('e:\\OXYBIO\\about.html', 'w', 'utf-8') as f:
        f.write(new_html)
    print("about.html story section upgraded successfully.")
else:
    print("Failed to find insertion pattern.")
