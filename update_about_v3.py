import re

def update_about_file():
    with open('about.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Core Record & Competencies
    start_str = '''                <div style="max-width:800px; margin-bottom:var(--space-md); padding-top:2rem; border-top:1px solid var(--border);">
                    <h2 style="font-family:var(--font-serif); font-size:1.75rem; color:var(--text-main); margin-bottom:1rem;">Core Record &amp; Competencies.</h2>'''
                    
    end_str = '''                    </div>
                </div>''' # End of lab capabilities

    # Finding the exact block to delete
    start_idx = content.find(start_str)
    
    # We will just replace the whole text from start_idx up to the start of SECTION 8
    # with our new Team Photo Section
    
    section_8_start = '        <!-- ═══════════════════════════════════════════════════════\n             SECTION 8'
    end_idx = content.find(section_8_start)

    if start_idx != -1 and end_idx != -1:
        # New Core Lab Team Photo Section
        new_team_section = '''
                <!-- The Core Lab Team (Photo Section) -->
                <div class="reveal" style="margin-top:6rem; border-top:1px solid var(--border); padding-top:4rem;">
                    <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:2rem; flex-wrap:wrap; gap:1rem;">
                        <div>
                            <div class="section-label" style="margin-bottom:1rem;">
                                <div class="section-label-line"></div>
                                <span class="section-label-text">The Lab Core</span>
                            </div>
                            <h2 style="font-family:var(--font-serif); font-size:clamp(1.75rem, 3vw, 2.5rem); color:var(--text-main); margin-bottom:0.5rem;">Core Research Team.</h2>
                        </div>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#0D8A74; background:rgba(13,138,116,0.1); padding:0.5rem 1rem; border-radius:50px; border:1px solid rgba(13,138,116,0.2);">
                            ACTIVE IN DETI@ACE TBI
                        </div>
                    </div>
                    
                    <div style="position:relative; width:100%; border-radius:16px; overflow:hidden; border:1px solid var(--border); background:var(--bg-alt); min-height:450px; display:flex; align-items:center; justify-content:center;">
                        <!-- Placeholder for the actual image. Replace styles when actual image is added -->
                        <div style="position:absolute; inset:0; background:linear-gradient(45deg, rgba(13,138,116,0.05) 0%, rgba(0,0,0,0.02) 100%);"></div>
                        
                        <div style="text-align:center; z-index:2; padding:2rem;">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--text-muted)" stroke-width="1" style="margin:0 auto 1rem; opacity:0.5;"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
                            <div style="font-family:var(--font-mono); font-size:0.8rem; letter-spacing:0.2em; color:var(--text-muted); text-transform:uppercase;">Team Photo Placeholder</div>
                        </div>

                        <!-- Team Roster Glassmorphic Overlay -->
                        <div style="position:absolute; bottom:1.5rem; left:1.5rem; right:1.5rem; background:rgba(255,255,255,0.8); backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.5); padding:1.25rem 2rem; border-radius:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1.5rem;">
                            <div style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); font-weight:700;">
                                07 <span style="font-size:1rem; font-weight:400; color:var(--text-muted); font-family:var(--font-sans);">Members</span>
                            </div>
                            <div style="display:flex; gap:1.5rem; font-family:var(--font-mono); font-size:0.75rem; color:var(--text-main); text-transform:uppercase; letter-spacing:0.05em; flex-wrap:wrap;">
                                <div style="display:flex; align-items:center; gap:0.4rem;"><span style="width:6px; height:6px; border-radius:50%; background:#0D8A74;"></span> CEO</div>
                                <div style="display:flex; align-items:center; gap:0.4rem;"><span style="width:6px; height:6px; border-radius:50%; background:#0D8A74;"></span> CTO</div>
                                <div style="display:flex; align-items:center; gap:0.4rem;"><span style="width:6px; height:6px; border-radius:50%; background:#0D8A74;"></span> 01 Research Fellow</div>
                                <div style="display:flex; align-items:center; gap:0.4rem;"><span style="width:6px; height:6px; border-radius:50%; background:#0D8A74;"></span> 04 Research Interns</div>
                            </div>
                        </div>
                    </div>
                </div>

'''
        content = content[:start_idx] + new_team_section + content[end_idx:]

    # 3. Redesign Support Network structure 
    # Let's target the grid we placed earlier
    grid_start_idx = content.find('                <!-- Mentor Cards Grid -->')
    grid_end_idx = content.find('                <div class="mentor-reveal" style="margin-top:4rem;', grid_start_idx)

    if grid_start_idx != -1 and grid_end_idx != -1:
        
        premium_list_html = '''                <!-- Premium List Layout for Support Network -->
                <style>
                    .support-row {
                        display: grid;
                        grid-template-columns: 140px 1fr 1fr auto;
                        gap: 1.5rem;
                        align-items: center;
                        padding: 1.5rem 1rem;
                        border-bottom: 1px solid var(--border);
                        transition: all 0.3s ease;
                        border-radius: 6px;
                    }
                    .support-row:hover {
                        background: rgba(13,138,116,0.03);
                        border-color: rgba(13,138,116,0.2);
                        transform: translateX(5px);
                    }
                    .support-row-badge {
                        font-family: var(--font-mono);
                        font-size: 0.65rem;
                        padding: 0.3rem 0.6rem;
                        border-radius: 4px;
                        letter-spacing: 0.05em;
                        text-transform: uppercase;
                        display: inline-block;
                    }
                    .badge-industry { background: rgba(13,138,116,0.1); color: #0D8A74; border: 1px solid rgba(13,138,116,0.2); }
                    .badge-academic { background: var(--bg); border: 1px solid var(--border); color: var(--text-main); }
                    
                    @media (max-width: 768px) {
                        .support-row {
                            grid-template-columns: 1fr;
                            gap: 0.75rem;
                            padding: 1.5rem;
                            background: var(--bg);
                            border: 1px solid var(--border);
                            margin-bottom: 1rem;
                        }
                        .support-row:hover { transform: translateY(-3px); }
                    }
                </style>

                <div class="support-list-container" style="margin-top:2rem;">
                    
                    <!-- Header Row (Hidden on mobile) -->
                    <div class="support-row" style="border-bottom:2px solid var(--border); padding-bottom:1rem; margin-bottom:0.5rem; opacity:0.6;">
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Category</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Profile</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Credentials / Designation</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em; text-align:right;">Status</div>
                    </div>

'''
        # Industry Roles
        for _ in range(3):
            premium_list_html += '''                    <!-- Industry -->
                    <div class="support-row mentor-reveal">
                        <div><span class="support-row-badge badge-industry">Industry Expert</span></div>
                        <div style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-main); font-weight:600;">[Profile Pending]</div>
                        <div style="font-size:0.9rem; color:var(--text-muted);">[Institution / Organisation]</div>
                        <div style="text-align:right;">
                            <div style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.25rem 0.5rem; background:rgba(0,0,0,0.04); border-radius:4px; font-family:var(--font-mono); font-size:0.6rem; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; border:1px solid rgba(0,0,0,0.05);">
                                <div style="width:4px; height:4px; background:#eab308; border-radius:50%;"></div> Confidential
                            </div>
                        </div>
                    </div>
'''
        # Academic Doctorates
        for _ in range(6):
            premium_list_html += '''                    <!-- Academic -->
                    <div class="support-row mentor-reveal">
                        <div><span class="support-row-badge badge-academic">Academic</span></div>
                        <div style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-main); font-weight:600;">Dr. [Profile Pending]</div>
                        <div style="font-size:0.9rem; color:var(--text-muted);">Doctorate &mdash; [Institution]</div>
                        <div style="text-align:right;">
                            <div style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.25rem 0.5rem; background:rgba(0,0,0,0.04); border-radius:4px; font-family:var(--font-mono); font-size:0.6rem; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; border:1px solid rgba(0,0,0,0.05);">
                                <div style="width:4px; height:4px; background:#eab308; border-radius:50%;"></div> Confidential
                            </div>
                        </div>
                    </div>
'''
        # Academic Pursuing / Viva
        roles = [
            ("PhD Pursuing", "Research Scholar &mdash; [Institution]"),
            ("PhD Viva Completed", "Post-Doctoral &mdash; [Institution]")
        ]
        for role, desc in roles:
             premium_list_html += f'''                    <!-- Academic -->
                    <div class="support-row mentor-reveal">
                        <div><span class="support-row-badge badge-academic">{role}</span></div>
                        <div style="font-family:var(--font-serif); font-size:1.25rem; color:var(--text-main); font-weight:600;">[Profile Pending]</div>
                        <div style="font-size:0.9rem; color:var(--text-muted);">{desc}</div>
                        <div style="text-align:right;">
                            <div style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.25rem 0.5rem; background:rgba(0,0,0,0.04); border-radius:4px; font-family:var(--font-mono); font-size:0.6rem; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; border:1px solid rgba(0,0,0,0.05);">
                                <div style="width:4px; height:4px; background:#eab308; border-radius:50%;"></div> Confidential
                            </div>
                        </div>
                    </div>
'''      

        premium_list_html += '''                </div>\n'''
        
        content = content[:grid_start_idx] + premium_list_html + content[grid_end_idx:]

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updates applied successfully.")

if __name__ == '__main__':
    update_about_file()
