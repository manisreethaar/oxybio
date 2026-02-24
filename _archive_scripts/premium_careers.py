import re

with open('e:\\OXYBIO\\careers.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Redesign Hero Section ──
old_hero_start = html.find('<!-- ═══════════════════════════════════════════════════════\n     HERO SECTION')
old_hero_end = html.find('<!-- ═══════════════════════════════════════════════════════\n     CURRENT OPENINGS')

NEW_HERO = '''<!-- ═══════════════════════════════════════════════════════
     PREMIUM HERO SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="padding-top:160px; padding-bottom:100px; background:var(--bg); border-bottom:1px solid var(--border); position:relative; overflow:hidden;">
    <div class="container" style="position:relative; z-index:2;">
        <div class="flow-left reveal" style="max-width:1000px;">
            <div class="badge" style="margin-bottom:var(--space-lg); border-color:var(--text-main); color:var(--text-main); background:transparent;">Join the Lab</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 8vw, 6.5rem); line-height:0.9; letter-spacing:-0.03em; margin-bottom:2rem;">
                Not a company.<br><em style="color:var(--text-muted); font-weight:400;">A research collective.</em>
            </h1>
            <p class="subtext editorial-col" style="font-size:clamp(1.25rem, 2vw, 1.5rem); line-height:1.6; color:var(--text-main); max-width:800px;">
                We are looking for obsessive formulation scientists, fermentation engineers, and clinical researchers to build India's first evidence-based precision nutrition system at TBI, Adhiyamaan College of Engineering.
            </p>
        </div>
    </div>
    
    <!-- Abstract background element -->
    <div style="position:absolute; right:-10%; top:20%; width:600px; height:600px; border-radius:50%; border:1px dashed var(--border); opacity:0.5; pointer-events:none; z-index:1;"></div>
    <div style="position:absolute; right:5%; top:40%; width:300px; height:300px; border-radius:50%; border:1px solid var(--border); opacity:0.3; pointer-events:none; z-index:1;"></div>
</section>
'''

if old_hero_start != -1 and old_hero_end != -1:
    html = html[:old_hero_start] + NEW_HERO + html[old_hero_end:]
    print("Hero updated.")


# ── 2. Redesign Openings Section ──
# Refresh content to find new boundaries
old_openings_start = html.find('<!-- ═══════════════════════════════════════════════════════\n     CURRENT OPENINGS')
old_openings_end = html.find('<!-- ═══════════════════════════════════════════════════════\n     STUDENT INTERNSHIP PORTAL')

NEW_OPENINGS = '''<!-- ═══════════════════════════════════════════════════════
     PREMIUM CURRENT OPENINGS
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt); padding:var(--space-2xl) 0;">
    <div class="container reveal">
        
        <div style="display:flex; justify-content:space-between; align-items:flex-end; border-bottom:1px solid var(--border); padding-bottom:2rem; margin-bottom:4rem;">
            <div>
                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1rem;">Open Positions</div>
                <h2 style="font-family:var(--font-serif); font-size:clamp(2rem,4vw,3rem); font-weight:900; color:var(--text-main); line-height:1.1; letter-spacing:-0.02em;">Roles at the bench.</h2>
            </div>
            <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); text-align:right;">
                Location: <span style="color:var(--text-main); font-weight:600;">Hosur, Tamil Nadu</span><br>
                Mode: <span style="color:var(--text-main); font-weight:600;">On-site (TBI Lab)</span>
            </div>
        </div>

        <!-- Role Outline Card -->
        <div style="background:var(--bg); border:1px solid var(--border); display:grid; grid-template-columns:1fr 2fr; gap:0;" class="mobile-stack-card">
            
            <!-- Left Header -->
            <div style="padding:3rem; border-right:1px solid var(--border); display:flex; flex-direction:column; justify-content:space-between;">
                <div>
                    <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:2rem; text-transform:uppercase; letter-spacing:0.05em;">
                        <span style="color:var(--text-main); font-weight:700;">Full Time</span> ·
                        <span>0-1 YR EXP</span>
                    </div>
                    <h3 class="display" style="font-size:clamp(2.5rem, 4vw, 3rem); line-height:1; letter-spacing:-0.02em; margin-bottom:1rem;">Research Associate</h3>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted); border:1px solid var(--border); display:inline-block; padding:0.4rem 0.8rem; margin-bottom:2rem;">Bio / Food Tech</div>
                </div>
                
                <div>
                    <a href="mailto:careers@oxygenbioinnovations.com?subject=Application%20for%20Research%20Associate" class="btn btn-primary" style="padding:1rem 2rem; width:100%; justify-content:center;">Apply via Email →</a>
                </div>
            </div>
            
            <!-- Right Details -->
            <div style="padding:3rem;">
                <p style="font-size:1.2rem; line-height:1.6; color:var(--text-main); margin-bottom:3rem; padding-bottom:2rem; border-bottom:1px solid var(--border); font-style:italic;">
                    "We are building a next-generation bio-innovation platform at the intersection of probiotic science, functional nutrition, and bio-based cosmetic technology."
                </p>
                
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem;" class="mobile-stack">
                    <div>
                        <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1.5rem; color:var(--text-main);">The Profile</h4>
                        <ul style="font-size:1.05rem; line-height:1.75; color:var(--text-muted); padding-left:1.25rem; margin-bottom:0; display:flex; flex-direction:column; gap:0.75rem;">
                            <li><strong style="color:var(--text-main); font-weight:500;">Degree:</strong> B.Tech / B.Sc. / M.Sc. in Food Technology, Biotechnology, Cosmetic Science, or related.</li>
                            <li><strong style="color:var(--text-main); font-weight:500;">Core Skills:</strong> Strong foundation in microbial fermentation, food process engineering, or emulsion chemistry.</li>
                            <li><strong style="color:var(--text-main); font-weight:500;">Mindset:</strong> Analytical thinker with strong documentation discipline and entrepreneurial ownership.</li>
                        </ul>
                    </div>
                    
                    <div>
                        <h4 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1.5rem; color:var(--text-main);">The Output</h4>
                        <ul style="font-size:1.05rem; line-height:1.75; color:var(--text-muted); padding-left:1.25rem; margin-bottom:0; display:flex; flex-direction:column; gap:0.75rem;">
                            <li>Design and develop probiotic and functional food formulations grounded in fermentation science.</li>
                            <li>Execute laboratory-scale fermentation studies, formulation optimization, and analytical validation.</li>
                            <li>Conduct structured shelf-life, stability, and sensory evaluation studies.</li>
                            <li>Prepare and maintain SOPs, batch records, and regulatory documentation.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

    </div>
</section>
'''

if old_openings_start != -1 and old_openings_end != -1:
    html = html[:old_openings_start] + NEW_OPENINGS + html[old_openings_end:]
    print("Openings updated.")


# ── 3. Redesign Internship Section ──
old_intern_start = html.find('<!-- ═══════════════════════════════════════════════════════\n     STUDENT INTERNSHIP PORTAL')
old_intern_end = html.find('<!-- Site Footer -->')

if old_intern_end == -1: # check alternative
    old_intern_end = html.find('<!-- Mobile Sticky CTA -->')

NEW_INTERNSHIP = '''<!-- ═══════════════════════════════════════════════════════
     PREMIUM INTERNSHIP PORTAL
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--text-main); color:var(--bg); border-top:1px solid var(--border); padding:var(--space-2xl) 0;">
    <div class="container reveal">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center;" class="mobile-stack">
            
            <!-- Pitch col -->
            <div class="flow-left">
                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.4); margin-bottom:1rem;">Incubator Program</div>
                <h2 style="font-family:var(--font-serif); font-size:clamp(2.5rem, 5vw, 4rem); font-weight:900; color:#fff; line-height:1.1; letter-spacing:-0.02em; margin-bottom:1.5rem;">Student<br><em style="font-weight:400; color:rgba(255,255,255,0.6);">Internships.</em></h2>
                
                <p style="font-size:1.15rem; line-height:1.7; color:rgba(255,255,255,0.7); margin-bottom:2rem; max-width:500px;">
                    Open to final year B.Tech / B.Sc students. You will not be making coffee. You will be assigned to live R&D projects alongside our founding team, working with raw materials and conducting literature reviews that directly impact our formulation pipeline.
                </p>
                
                <div style="padding-top:2rem; border-top:1px solid rgba(255,255,255,0.1); width:100%; max-width:400px;">
                    <span style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:rgba(255,255,255,0.4); display:block; margin-bottom:0.5rem;">Or email your CV to:</span>
                    <a href="mailto:careers@oxygenbioinnovations.com" style="color:#fff; font-size:1.1rem; text-decoration:none; font-weight:600; border-bottom:1px solid #fff; padding-bottom:2px;">careers@oxygenbioinnovations.com</a>
                </div>
            </div>

            <!-- Form col -->
            <div style="background:var(--bg); padding:3rem; border-radius:12px; position:relative;">
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; color:var(--text-main); margin-bottom:2rem;">Apply for Intake</h3>
                
                <form onsubmit="event.preventDefault(); alert('Application submitted successfully.');" style="display:flex; flex-direction:column; gap:1.5rem;">
                    
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;" class="mobile-stack">
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Full Name *</label>
                            <input type="text" required style="padding:1rem; border:1px solid #e5e5e5; background:#fafafa; border-radius:4px; font-family:var(--font-sans); outline:none;">
                        </div>
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Year of Passing *</label>
                            <input type="text" required style="padding:1rem; border:1px solid #e5e5e5; background:#fafafa; border-radius:4px; font-family:var(--font-sans); outline:none;">
                        </div>
                    </div>
                    
                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">College / University *</label>
                        <input type="text" required style="padding:1rem; border:1px solid #e5e5e5; background:#fafafa; border-radius:4px; font-family:var(--font-sans); outline:none;">
                    </div>

                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Major / Degree Specialization *</label>
                        <input type="text" required placeholder="e.g. B.Tech Biotechnology" style="padding:1rem; border:1px solid #e5e5e5; background:#fafafa; border-radius:4px; font-family:var(--font-sans); outline:none;">
                    </div>
                    
                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Why Oxygen Bioinnovations? (Brief) *</label>
                        <textarea required rows="4" style="padding:1rem; border:1px solid #e5e5e5; background:#fafafa; border-radius:4px; font-family:var(--font-sans); resize:vertical; outline:none;"></textarea>
                    </div>

                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Portfolio / LinkedIn / Resume Link</label>
                        <input type="url" placeholder="https://" style="padding:1rem; border:1px solid #e5e5e5; background:#fafafa; border-radius:4px; font-family:var(--font-sans); outline:none;">
                    </div>

                    <button type="submit" class="btn btn-primary" style="margin-top:1rem; padding:1.25rem; font-size:1.1rem; justify-content:center;">Submit Application</button>
                    
                </form>
            </div>
            
        </div>
    </div>
</section>

</main>
    
'''

# Find exactly where to end
if old_intern_end != -1:
    footer_start = html.find('<!-- Site Footer -->', old_intern_start)
    if footer_start != -1:
        html = html[:old_intern_start] + NEW_INTERNSHIP + html[footer_start:]
        print("Internship updated.")

with open('e:\\OXYBIO\\careers.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("careers.html saved.")
