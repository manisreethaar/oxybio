import os, re

careers_path = r'e:\OXYBIO\careers.html'
with open(careers_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_CONTENT = """
<main>

<!-- ═══════════════════════════════════════════════════════
     HERO SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="padding-top:140px; border-bottom:1px solid var(--border);">
    <div class="container">
        <div class="flow-left reveal" style="max-width:900px; margin-bottom:var(--space-md);">
            <div class="badge" style="margin-bottom:var(--space-md);">Join Our Mission</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">Build the Future of<br><em>Bio-Innovation.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                We are looking for passionate researchers and students to join our team at TBI, Adhiyamaan College of Engineering.
            </p>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     CURRENT OPENINGS (Split Layout)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt);">
    <div class="container reveal">
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;" class="mobile-stack">
            
            <div style="position:sticky; top:120px;" class="flow-left">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Open Roles</span>
                </div>
                <h2 class="headline" style="margin-top:var(--space-sm);">Current Openings</h2>
            </div>
            
            <div class="bento-grid">
                <!-- Role: Junior Research Associate -->
                <div class="bento-cell" style="grid-column: span 12; background:var(--bg);">
                    <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                        <span>Full Time</span> ·
                        <span>0-1 Year Exp</span> ·
                        <span>Hosur, Tamil Nadu</span>
                    </div>
                    
                    <h3 style="font-family:var(--font-serif); font-size:2rem; margin-bottom:1rem; color:var(--text-main);">Junior Research Associate / Research Associate<br><span style="font-size:1.25rem; font-family:var(--font-sans); font-weight:400; color:var(--text-muted);">(Bio/Food Technology)</span></h3>
                    
                    <p style="font-size:1.05rem; line-height:1.6; color:var(--text-main); margin-bottom:2rem; font-style:italic;">We are building a next-generation bio-innovation platform at the intersection of probiotic science, functional nutrition, and bio-based cosmetic technology.</p>
                    
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;" class="mobile-stack">
                        <!-- Left Column Details -->
                        <div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.75rem; color:var(--text-main);">Who we are seeking</h4>
                            <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:1.5rem;">Seeking ambitious and research-driven individuals who aspire to build—not just join—a company. This is not a routine laboratory role. It is a high-ownership position within a performance-driven startup ecosystem. You will contribute to the development, validation, and scale-up of products spanning R&D, regulatory alignment, and pilot production.</p>

                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.75rem; color:var(--text-main);">Who We Are Looking For</h4>
                            <ul style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); padding-left:1.25rem; margin-bottom:2rem;">
                                <li>B.Tech / B.Sc. / M.Sc. in Food Technology, Biotechnology, Cosmetic Science, or related.</li>
                                <li>Strong foundation in microbial fermentation, food process engineering, or emulsion chemistry.</li>
                                <li>Analytical thinker with strong documentation discipline and entrepreneurial mindset.</li>
                                <li>Self-driven, adaptable, aspiring to build long-term leadership roles.</li>
                            </ul>
                        </div>
                        
                        <!-- Right Column Details -->
                        <div>
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.75rem; color:var(--text-main);">Key Responsibilities</h4>
                            <ul style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); padding-left:1.25rem; margin-bottom:2rem;">
                                <li>Design and develop probiotic and functional food formulations grounded in fermentation science.</li>
                                <li>Develop and optimize bio-fermented cosmetic and skincare systems with stability and efficacy focus.</li>
                                <li>Execute laboratory-scale fermentation studies, formulation optimization, and analytical validation.</li>
                                <li>Conduct structured shelf-life, stability, and sensory evaluation studies.</li>
                                <li>Prepare and maintain SOPs, batch manufacturing records, and regulatory documentation.</li>
                                <li>Support pilot-scale trials, technology transfer, and scale-up processes.</li>
                                <li>Contribute to IP documentation, technical dossiers, and innovation pipeline development.</li>
                            </ul>
                            
                            <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.75rem; color:var(--text-main);">What We Offer</h4>
                            <ul style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); padding-left:1.25rem; margin-bottom:2rem;">
                                <li>Deep-Tech Innovation Exposure & Accelerated Career Growth.</li>
                                <li>End-to-End Product Development Experience.</li>
                                <li>Innovation & IP Participation with Founder-Level Mentorship.</li>
                                <li>Performance-Linked Incentives.</li>
                            </ul>
                            
                            <a href="mailto:careers@oxygenbioinnovations.com?subject=Application%20for%20Research%20Associate" class="btn btn-primary" style="width:100%; text-align:center;">Apply via Email</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     STUDENT INTERNSHIP PORTAL
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="border-top:1px solid var(--border);">
    <div class="container reveal">
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;" class="mobile-stack">
            
            <div style="position:sticky; top:120px;" class="flow-left">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">For Students</span>
                </div>
                <h2 class="headline" style="margin-top:var(--space-sm);">Internship Portal</h2>
                <p class="subtext editorial-col" style="margin-top:var(--space-sm); font-size:1.05rem; color:var(--text-muted);">
                    Open to Final Year B.Tech / B.Sc Students to work on live R&D projects alongside our founding team.
                </p>
                <div style="margin-top:var(--space-md); font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted);">
                    Contact via:<br>
                    <a href="mailto:careers@oxygenbioinnovations.com" style="color:var(--text-main); font-weight:600; text-decoration:none;">careers@oxygenbioinnovations.com</a>
                </div>
            </div>

            <!-- Internship Form Application structure -->
            <div class="bento-grid">
                <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                    <form style="display:flex; flex-direction:column; gap:1.5rem;" onsubmit="event.preventDefault(); alert('Application submitted successfully.');">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;" class="mobile-stack">
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Full Name *</label>
                                <input type="text" required style="padding:1rem; border:1px solid var(--border); background:var(--bg); border-radius:4px; font-family:var(--font-sans);">
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Year of Passing *</label>
                                <input type="text" required style="padding:1rem; border:1px solid var(--border); background:var(--bg); border-radius:4px; font-family:var(--font-sans);">
                            </div>
                        </div>
                        
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;" class="mobile-stack">
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">College / University *</label>
                                <input type="text" required style="padding:1rem; border:1px solid var(--border); background:var(--bg); border-radius:4px; font-family:var(--font-sans);">
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Degree & Branch *</label>
                                <input type="text" required style="padding:1rem; border:1px solid var(--border); background:var(--bg); border-radius:4px; font-family:var(--font-sans);">
                            </div>
                        </div>

                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Area of Interest *</label>
                            <select required style="padding:1rem; border:1px solid var(--border); background:var(--bg); border-radius:4px; font-family:var(--font-sans); appearance:none;">
                                <option value="" disabled selected>Select Area of Interest</option>
                                <option value="Research">Research/Fermentation</option>
                                <option value="Formulation">Product Formulation</option>
                                <option value="Marketing">Marketing & Design</option>
                            </select>
                        </div>
                        
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Message / Cover Letter *</label>
                            <textarea rows="5" required style="padding:1rem; border:1px solid var(--border); background:var(--bg); border-radius:4px; font-family:var(--font-sans);"></textarea>
                        </div>

                        <button type="submit" class="btn btn-outline" style="align-self:flex-start; margin-top:1rem;">Submit Application</button>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</section>

</main>
"""

with open(careers_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + FOOTER)

print("Updated careers.html with precise job descriptions and internship portal.")
