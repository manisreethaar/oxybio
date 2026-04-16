import re
import os

with open('E:\\OXYBIO-WEBSITE\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix "Dual-Extract" -> "Hot-Water Extract"
html = re.sub(r'Dual-Extract', 'Hot-Water Extract', html, flags=re.IGNORECASE)

# 2. Fix the "The Problem" section
# The old problem section has:
# <h2 class="display" style="font-family:var(--font-serif); font-size:3.5rem; line-height:1.1; margin-bottom:1.5rem;">The industry is built on bad biology.</h2>
# Let's replace the whole block carefully.
problem_start = html.find('The industry is built on bad biology.')
if problem_start != -1:
    old_h2_start = html.rfind('<h2', 0, problem_start)
    old_problem_end = html.find('<!-- -- Section: Solution ', problem_start)
    
    if old_h2_start != -1 and old_problem_end != -1:
        new_problem_html = '''<h2 class="display" style="font-family:var(--font-serif); font-size:3.5rem; line-height:1.1; margin-bottom:1.5rem;">The Functional Market Gap.</h2>
                        <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); margin-bottom:2.5rem; max-width:600px;">
                            We evaluated the current functional food landscape against DPIIT Phase 0 thresholds and identified three critical failure points in the Indian market.
                        </p>
                        <a href="problem.html" class="btn btn-outline" style="font-size:0.9rem; padding:0.75rem 1.75rem;">Explore the Data</a>
                    </div>
                    <div style="flex:1;">
                        <div style="display:flex; flex-direction:column; gap:2rem;">
                            <!-- Point 1 -->
                            <div class="reveal" style="padding-bottom:2rem; border-bottom:1px solid var(--border);">
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:var(--text-main); margin-bottom:0.75rem;">01 / THE SCIENCE GAP</div>
                                <h4 style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); margin-bottom:0.75rem;">Unvalidated Synthetic Formulations</h4>
                                <p style="font-size:0.95rem; color:var(--text-muted); line-height:1.6; margin:0;">
                                    Clinical trials consistently show that synthetic isolates suffer from poor cellular bioavailability. The industry ignores fermentation-driven metabolic pre-digestion.
                                </p>
                            </div>
                            <!-- Point 2 -->
                            <div class="reveal" style="padding-bottom:2rem; border-bottom:1px solid var(--border);">
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:var(--text-main); margin-bottom:0.75rem;">02 / THE EXTRACTION GAP</div>
                                <h4 style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); margin-bottom:0.75rem;">Mycelium on Grain Contamination</h4>
                                <p style="font-size:0.95rem; color:var(--text-muted); line-height:1.6; margin:0;">
                                    Current medicinal compounds often contain up to 70% starch because manufacturers do not utilize species-specific fruiting-body liquid extraction.
                                </p>
                            </div>
                            <!-- Point 3 -->
                            <div class="reveal">
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:var(--text-main); margin-bottom:0.75rem;">03 / THE PRICE GAP</div>
                                <h4 style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); margin-bottom:0.75rem;">Unaffordable Import Premiums</h4>
                                <p style="font-size:0.95rem; color:var(--text-muted); line-height:1.6; margin:0;">
                                    Scientifically backed functional health currently requires importing products at a 600% markup. There is no ₹65 indigenous equivalent.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>\n\n        '''
        
        html = html[:old_h2_start] + new_problem_html + html[old_problem_end:]

# 3. Check Trust Bar
# The old trust bar had things like "14x more cellular uptake ... 800mg baseline".
# Let's replace the whole marquee content.
trust_bar_pattern = r'(?s)<ul aria-hidden=\"true\" class=\"marquee__content\">.*?</ul>'
new_trust_bar = '''<ul aria-hidden="true" class="marquee__content">
                        <li><span>Phase 0 R&D — TBI Incubated</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>FSSAI Manufacturer Licensing Under Review</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>India's First Fermented Millet Platform</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>Hot-Water Extracts Only (No Ethanol)</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>100% Fruiting Body (No Mycelium on Grain)</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>DPIIT Recognition In Progress</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>Fermentation-Derived Bioavailability</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>Evidence-Based Nutrient Stacks</span></li>
                        <li><span class="dot"></span></li>
                        <li><span>Manufactured in TBI-ACE Facilities</span></li>
                    </ul>'''

html = re.sub(trust_bar_pattern, new_trust_bar, html, count=2)

with open('E:\\OXYBIO-WEBSITE\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")
