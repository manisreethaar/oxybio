import codecs
import re

with codecs.open('e:\\OXYBIO\\about.html', 'r', 'utf-8') as f:
    html = f.read()

# The new highly-designed, clinical 'Our Approach' Grid
NEW_APPROACH = '''<!-- Premium numbered approach list -->
                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:2rem; margin-top:3rem;" class="mobile-stack">
                                
                                <!-- Card 01 -->
                                <div style="background:var(--bg); border:1px solid var(--border); padding:2.5rem; border-radius:12px; position:relative; overflow:hidden; transition:all 0.4s ease;" class="premium-card-hover">
                                    <div style="font-family:var(--font-mono); font-size:3.5rem; font-weight:700; color:var(--bg-alt); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;">01</div>
                                    <h4 style="font-family:var(--font-serif); font-size:1.4rem; margin-bottom:1rem; color:var(--text-main); position:relative; z-index:2; padding-right:3rem;">Science Before Marketing</h4>
                                    <div style="width:40px; height:2px; background:var(--text-main); margin-bottom:1.5rem;"></div>
                                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.65; position:relative; z-index:2; margin-bottom:0;">We designed the formulation before we designed the brand. We chose ingredients before we chose colors. This is backwards from how most nutrition companies work. We think it is the only sensible order.</p>
                                </div>
                                
                                <!-- Card 02 -->
                                <div style="background:var(--bg); border:1px solid var(--border); padding:2.5rem; border-radius:12px; position:relative; overflow:hidden; transition:all 0.4s ease;" class="premium-card-hover">
                                    <div style="font-family:var(--font-mono); font-size:3.5rem; font-weight:700; color:var(--bg-alt); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;">02</div>
                                    <h4 style="font-family:var(--font-serif); font-size:1.4rem; margin-bottom:1rem; color:var(--text-main); position:relative; z-index:2; padding-right:3rem;">India Is Not a Market Segment</h4>
                                    <div style="width:40px; height:2px; background:var(--text-main); margin-bottom:1.5rem;"></div>
                                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.65; position:relative; z-index:2; margin-bottom:0;">We did not take a Western formula and add Ashwagandha to make it Indian. We started from India. From what Indian bodies are deficient in. From what Indian ingredients can provide.</p>
                                </div>
                                
                                <!-- Card 03 -->
                                <div style="background:var(--bg); border:1px solid var(--border); padding:2.5rem; border-radius:12px; position:relative; overflow:hidden; transition:all 0.4s ease;" class="premium-card-hover">
                                    <div style="font-family:var(--font-mono); font-size:3.5rem; font-weight:700; color:var(--bg-alt); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;">03</div>
                                    <h4 style="font-family:var(--font-serif); font-size:1.4rem; margin-bottom:1rem; color:var(--text-main); position:relative; z-index:2; padding-right:3rem;">Transparency Is Not Optional</h4>
                                    <div style="width:40px; height:2px; background:var(--text-main); margin-bottom:1.5rem;"></div>
                                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.65; position:relative; z-index:2; margin-bottom:0;">We publish our lab reports. We name our ingredient suppliers. We cite the studies behind our claims. We tell you when a study is preliminary and when it is robust.</p>
                                </div>
                                
                                <!-- Card 04 -->
                                <div style="background:var(--bg); border:1px solid var(--border); padding:2.5rem; border-radius:12px; position:relative; overflow:hidden; transition:all 0.4s ease;" class="premium-card-hover">
                                    <div style="font-family:var(--font-mono); font-size:3.5rem; font-weight:700; color:var(--bg-alt); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;">04</div>
                                    <h4 style="font-family:var(--font-serif); font-size:1.4rem; margin-bottom:1rem; color:var(--text-main); position:relative; z-index:2; padding-right:3rem;">Dose Matters</h4>
                                    <div style="width:40px; height:2px; background:var(--text-main); margin-bottom:1.5rem;"></div>
                                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.65; position:relative; z-index:2; margin-bottom:0;">Ashwagandha at 50mg is not the same as Ashwagandha at 300mg. We formulate at clinically relevant doses &mdash; not at doses that merely allow us to list the ingredient on the label.</p>
                                </div>
                                
                                <!-- Card 05 -->
                                <div style="background:var(--bg); border:1px solid var(--border); padding:2.5rem; border-radius:12px; position:relative; overflow:hidden; transition:all 0.4s ease;" class="premium-card-hover">
                                    <div style="font-family:var(--font-mono); font-size:3.5rem; font-weight:700; color:var(--bg-alt); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;">05</div>
                                    <h4 style="font-family:var(--font-serif); font-size:1.4rem; margin-bottom:1rem; color:var(--text-main); position:relative; z-index:2; padding-right:3rem;">Bioavailability First</h4>
                                    <div style="width:40px; height:2px; background:var(--text-main); margin-bottom:1.5rem;"></div>
                                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.65; position:relative; z-index:2; margin-bottom:0;">A 100mg dose with 5% absorption delivers 5mg to your body. A 50mg dose with 35% absorption delivers 17.5mg. The nutrient that reaches your bloodstream is the only one that matters.</p>
                                </div>
                                
                                <!-- Card 06 -->
                                <div style="background:var(--bg); border:1px solid var(--border); padding:2.5rem; border-radius:12px; position:relative; overflow:hidden; transition:all 0.4s ease;" class="premium-card-hover">
                                    <div style="font-family:var(--font-mono); font-size:3.5rem; font-weight:700; color:var(--bg-alt); line-height:1; position:absolute; top:1.5rem; right:1.5rem; pointer-events:none;">06</div>
                                    <h4 style="font-family:var(--font-serif); font-size:1.4rem; margin-bottom:1rem; color:var(--text-main); position:relative; z-index:2; padding-right:3rem;">Clinical Evidence</h4>
                                    <div style="width:40px; height:2px; background:var(--text-main); margin-bottom:1.5rem;"></div>
                                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.65; position:relative; z-index:2; margin-bottom:0;">We designed our clinical study before we manufactured our first batch. Not because we are required to, but because no company should sell a health product without evidence that it works.</p>
                                </div>
                                
                            </div>'''

# Regex to safely target and replace the old list structure with the new grid
pattern = re.compile(
    r'<!-- Premium numbered approach list -->.*?<div style="display:flex; flex-direction:column;">.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

if pattern.search(html):
    new_html = pattern.sub(NEW_APPROACH + '\n                        </div>\n                    </div>', html, count=1)
    with codecs.open('e:\\OXYBIO\\about.html', 'w', 'utf-8') as f:
        f.write(new_html)
    print("about.html approach section upgraded to interactive grid.")
else:
    print("Failed to find approach section.")
