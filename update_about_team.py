import re

def update_about_file():
    with open('about.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # SECTION 1: Replace the Leadership top section
    # We want to replace from "<!-- ═══════════════════════════════════════════════════════" 
    # under SECTION 7 to the start of the grid "                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:3rem;" class="mobile-stack">"

    old_leader_start = '''        <!-- ═══════════════════════════════════════════════════════
             SECTION 7 — FOUNDER DEEP DIVE (Full credentials)
        ════════════════════════════════════════════════════════════ -->
        <section style="background:var(--bg-alt); padding:var(--space-xl) 0;">
            <div class="container reveal">

                <div style="max-width:800px; margin-bottom:var(--space-xl);">
                    <div class="section-label" style="margin-bottom:var(--space-md);">
                        <div class="section-label-line"></div>
                        <span class="section-label-text">The Full Record</span>
                    </div>
                    <h2 style="font-family:var(--font-serif); font-size:clamp(2rem, 4vw, 3rem); color:var(--text-main); margin-bottom:1rem;">Every credential. No gaps.</h2>
                    <p style="font-size:1.05rem; color:var(--text-muted); line-height:1.7;">We believe in transparency about who is building this. Here is the complete academic and professional record of the person running this lab.</p>
                </div>'''

    new_leader_top = '''        <!-- ═══════════════════════════════════════════════════════
             SECTION 7 — FOUNDING TEAM & CREDENTIALS
        ════════════════════════════════════════════════════════════ -->
        <section style="background:var(--bg-alt); padding:var(--space-xl) 0;">
            <div class="container reveal">

                <div style="max-width:800px; margin-bottom:var(--space-lg);">
                    <div class="section-label" style="margin-bottom:var(--space-md);">
                        <div class="section-label-line"></div>
                        <span class="section-label-text">Leadership</span>
                    </div>
                    <h2 style="font-family:var(--font-serif); font-size:clamp(2rem, 4vw, 3rem); color:var(--text-main); margin-bottom:1rem;">The Founding Team.</h2>
                    <p style="font-size:1.05rem; color:var(--text-muted); line-height:1.7;">Driven by a deep commitment to science and transparency.</p>
                </div>

                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:2rem; margin-bottom:4rem;">
                    
                    <!-- CEO Profile -->
                    <div class="premium-card-hover" style="background:var(--bg); border:1px solid var(--border); border-radius:12px; padding:2.5rem; text-align:center; position:relative; overflow:hidden;">
                        <div class="mentor-image-placeholder" style="width:120px; height:120px; border-radius:50%; margin:0 auto 1.5rem; border:2px dashed var(--border); background:var(--bg-alt); display:flex; align-items:center; justify-content:center;">
                            <span style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.1em; color:var(--text-muted);">IMAGE PENDING</span>
                        </div>
                        <h3 style="font-family:var(--font-serif); font-size:1.75rem; color:var(--text-main); margin-bottom:0.25rem;">Mani Sreethaar Selvaraj</h3>
                        <div style="font-family:var(--font-mono); font-size:0.8rem; color:#0D8A74; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:1.5rem; font-weight:700;">Founder &amp; CEO</div>
                        <p style="font-size:0.95rem; color:var(--text-muted); margin-bottom:2rem; line-height:1.6;">Biotechnologist (M.Tech Nanoscience, B.Tech Biotech) leading formulation R&amp;D with specialized expertise in microbial fermentation and bioprocess engineering.</p>
                        <a href="https://www.linkedin.com/in/manisreethaar-selvaraj-07242712a" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="padding:0.6rem 1.25rem; font-size:0.85rem; border-color:var(--text-main); color:var(--text-main); display:inline-flex; align-items:center; gap:0.5rem; justify-content:center;">
                            LinkedIn Profile &#x2197;
                        </a>
                    </div>

                    <!-- CTO Profile -->
                    <div class="premium-card-hover" style="background:var(--bg); border:1px solid var(--border); border-radius:12px; padding:2.5rem; text-align:center; position:relative; overflow:hidden;">
                        <div class="mentor-image-placeholder" style="width:120px; height:120px; border-radius:50%; margin:0 auto 1.5rem; border:2px dashed var(--border); background:var(--bg-alt); display:flex; align-items:center; justify-content:center;">
                            <span style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.1em; color:var(--text-muted);">IMAGE PENDING</span>
                        </div>
                        <h3 style="font-family:var(--font-serif); font-size:1.75rem; color:var(--text-main); margin-bottom:0.25rem;">C. Libinraj Christopher</h3>
                        <div style="font-family:var(--font-mono); font-size:0.8rem; color:#0D8A74; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:1.5rem; font-weight:700;">Chief Technology Officer</div>
                        <p style="font-size:0.95rem; color:var(--text-muted); margin-bottom:2rem; line-height:1.6;">Leading technical strategy, operational scale-up, and engineering development for Oxygen's product formulations and core laboratory capabilities.</p>
                        <a href="https://www.linkedin.com/in/libin-raj-christopher-61b4b0128/" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="padding:0.6rem 1.25rem; font-size:0.85rem; border-color:var(--text-main); color:var(--text-main); display:inline-flex; align-items:center; gap:0.5rem; justify-content:center;">
                            LinkedIn Profile &#x2197;
                        </a>
                    </div>

                </div>

                <div style="max-width:800px; margin-bottom:var(--space-md); padding-top:2rem; border-top:1px solid var(--border);">
                    <h2 style="font-family:var(--font-serif); font-size:1.75rem; color:var(--text-main); margin-bottom:1rem;">Core Record &amp; Competencies.</h2>
                    <p style="font-size:1rem; color:var(--text-muted); line-height:1.7;">A complete breakdown of our industrial and academic biotechnology track record. No black boxes.</p>
                </div>'''

    if old_leader_start in content:
        content = content.replace(old_leader_start, new_leader_top)
    else:
        print("ERROR: Could not find old_leader_start")


    # SECTION 2: Generate 11 Support Network Cards
    roles = [
        ("Industry Expert", "Industry", 3),
        ("Academic Expert", "Doctorate", 6),
        ("Academic Expert", "PhD Pursuing", 1),
        ("Academic Expert", "PhD Viva Completed", 1)
    ]
    
    mentors_html = ""
    delay = 0
    total_index = 1
    
    for role_badge, title_str, count in roles:
        for _ in range(count):
            card_html = f'''                    <!-- Mentor {total_index} -->
                    <div class="mentor-card mentor-reveal" data-delay="{delay}">
                        <div class="mentor-card-inner">
                            <div class="mentor-image-wrap">
                                <div class="mentor-image-placeholder">
                                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="rgba(13,138,116,0.6)" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
                                </div>
                                <div class="mentor-role-badge">{role_badge}</div>
                            </div>
                            <div class="mentor-info">
                                <h3 class="mentor-name">[Profile Pending]</h3>
                                <div class="mentor-title">{title_str}</div>
                                <div class="mentor-org">[Institution / Organisation]</div>
                                <div class="mentor-domain" style="margin-top:0.8rem;">
                                    <div style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.25rem 0.5rem; background:rgba(0,0,0,0.04); border-radius:4px; font-family:var(--font-mono); font-size:0.6rem; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; border:1px solid rgba(0,0,0,0.05);">
                                        <div style="width:4px; height:4px; background:#eab308; border-radius:50%;"></div> Confidential
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="mentor-card-glow"></div>
                    </div>
'''
            mentors_html += card_html
            total_index += 1
            delay += 50
            if delay > 250:
                delay = 0

    grid_start_idx = content.find('                <!-- Mentor Cards Grid -->')
    grid_end_idx = content.find('                <div class="mentor-reveal" style="margin-top:4rem;', grid_start_idx)
    
    if grid_start_idx != -1 and grid_end_idx != -1:
        # Reconstruct the grid
        new_grid_html = '''                <!-- Mentor Cards Grid -->
                <div id="mentor-grid" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%, 300px), 1fr)); gap:1.5rem;">

''' + mentors_html + '''
                </div>\n\n'''
        
        content = content[:grid_start_idx] + new_grid_html + content[grid_end_idx:]
    else:
        print("ERROR: Could not find mentor grid boundaries")


    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success updating about.html")

update_about_file()
