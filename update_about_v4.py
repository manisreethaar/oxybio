import re

def update_about_file():
    with open('about.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where the old list layout starts
    start_str = '                <!-- Premium List Layout for Support Network -->'
    start_idx = content.find(start_str)

    # We need to find the ending </section> tag for section 8. 
    # Since the previous code injected into section 8, we just need to search for '</section>' following start_idx
    end_idx = content.find('</section>', start_idx)

    if start_idx == -1 or end_idx == -1:
        print("ERROR: Could not find target boundaries in about.html")
        return

    premium_list_v2_html = '''                <!-- Premium List Layout for Support Network (v2) -->
                <style>
                    .support-banner-header {
                        font-family: var(--font-serif);
                        font-size: 1.75rem;
                        color: var(--text-main);
                        margin: 3rem 0 1.5rem 0;
                        padding-bottom: 0.5rem;
                        border-bottom: 1px solid var(--border);
                        display: flex;
                        align-items: center;
                        gap: 1rem;
                    }
                    .support-banner-header span.badge {
                        background:rgba(13,138,116,0.1); 
                        border:1px solid rgba(13,138,116,0.2); 
                        color:#0D8A74; 
                        padding:0.25rem 0.6rem; 
                        border-radius:4px; 
                        font-family:var(--font-mono); 
                        font-size:0.65rem; 
                        text-transform:uppercase; 
                        letter-spacing:0.1em;
                    }
                    .support-row {
                        display: grid;
                        grid-template-columns: 60px 2fr 3fr 120px;
                        gap: 1.5rem;
                        align-items: center;
                        padding: 1.25rem 1rem;
                        border-bottom: 1px solid var(--border);
                        transition: all 0.3s ease;
                        border-radius: 6px;
                    }
                    .support-row:hover {
                        background: rgba(13,138,116,0.03);
                        border-color: rgba(13,138,116,0.2);
                        transform: translateX(5px);
                    }
                    .support-avatar {
                        width: 48px;
                        height: 48px;
                        border-radius: 50%;
                        background: var(--bg);
                        border: 1px solid var(--border);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }
                    .support-avatar svg {
                        width: 20px;
                        height: 20px;
                        stroke: rgba(13,138,116,0.5);
                    }
                    @media (max-width: 768px) {
                        .support-row {
                            grid-template-columns: 48px 1fr;
                            gap: 1rem;
                            padding: 1.5rem;
                            background: var(--bg);
                            border: 1px solid var(--border);
                            margin-bottom: 1rem;
                            align-items: start;
                        }
                        .support-row > div:nth-child(3),
                        .support-row > div:nth-child(4) {
                            grid-column: 1 / -1;
                        }
                        .support-row:hover { transform: translateY(-3px); }
                    }
                </style>

                <div class="support-list-container" style="margin-top:2rem;">
                    
                    <!-- INDUSTRY BANNER -->
                    <div class="support-banner-header mentor-reveal">
                        Industry Advisory Board <span class="badge">03 Members</span>
                    </div>

                    <!-- Header Row (Hidden on mobile) -->
                    <div class="support-row mentor-reveal" style="border-bottom:2px solid var(--border); padding-bottom:1rem; margin-bottom:0.5rem; opacity:0.6;">
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Pic</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Name &amp; Nature of Support</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Designation &amp; Employment</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em; text-align:right;">Status</div>
                    </div>

'''
    
    # Generate 3 Industry Rows
    for _ in range(3):
        premium_list_v2_html += '''                    <!-- Industry Row -->
                    <div class="support-row mentor-reveal">
                        <div>
                            <div class="support-avatar"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg></div>
                        </div>
                        <div>
                            <div style="font-family:var(--font-serif); font-size:1.15rem; color:var(--text-main); font-weight:600; margin-bottom:0.25rem;">[Name Pending]</div>
                            <div style="font-size:0.85rem; color:#0D8A74;">[Nature of Support — e.g. Strategy / Scale-up]</div>
                        </div>
                        <div>
                            <div style="font-size:0.9rem; color:var(--text-main); font-weight:500;">[Current Designation]</div>
                            <div style="font-size:0.85rem; color:var(--text-muted);">[Institution / Organisation]</div>
                        </div>
                        <div style="text-align:right;">
                            <div style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.25rem 0.5rem; background:rgba(0,0,0,0.04); border-radius:4px; font-family:var(--font-mono); font-size:0.6rem; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; border:1px solid rgba(0,0,0,0.05);">
                                <div style="width:4px; height:4px; background:#eab308; border-radius:50%;"></div> Confidential
                            </div>
                        </div>
                    </div>
'''

    # ACADEMIC BANNER
    premium_list_v2_html += '''
                    <!-- ACADEMIC BANNER -->
                    <div class="support-banner-header mentor-reveal" style="margin-top:4rem;">
                        Academic &amp; Research Review <span class="badge" style="background:var(--bg); border-color:var(--border); color:var(--text-main);">08 Members</span>
                    </div>

                    <!-- Header Row (Hidden on mobile) -->
                    <div class="support-row mentor-reveal" style="border-bottom:2px solid var(--border); padding-bottom:1rem; margin-bottom:0.5rem; opacity:0.6;">
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Pic</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Name &amp; Nature of Support</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em;">Designation &amp; Employment</div>
                        <div style="font-family:var(--font-mono); font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em; text-align:right;">Status</div>
                    </div>
'''

    # Academic rows: 6 Doctorates, 1 PhD Pursuing, 1 PhD Viva Completed
    academic_types = ["Doctorate"] * 6 + ["PhD Pursuing"] * 1 + ["PhD Viva Completed"] * 1
    
    for degree in academic_types:
        name_prefix = "Dr. " if degree in ["Doctorate", "PhD Viva Completed"] else ""
        premium_list_v2_html += f'''                    <!-- Academic Row: {degree} -->
                    <div class="support-row mentor-reveal">
                        <div>
                            <div class="support-avatar"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg></div>
                        </div>
                        <div>
                            <div style="font-family:var(--font-serif); font-size:1.15rem; color:var(--text-main); font-weight:600; margin-bottom:0.25rem;">{name_prefix}[Name Pending]</div>
                            <div style="font-size:0.85rem; color:var(--text-main);">[Nature of Support — e.g. Scientific Validation]</div>
                        </div>
                        <div>
                            <div style="font-size:0.9rem; color:var(--text-main); font-weight:500;">{degree} <span style="font-weight:400; color:var(--text-muted);">&mdash; [Role]</span></div>
                            <div style="font-size:0.85rem; color:var(--text-muted);">[Institution / Organisation]</div>
                        </div>
                        <div style="text-align:right;">
                            <div style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.25rem 0.5rem; background:rgba(0,0,0,0.04); border-radius:4px; font-family:var(--font-mono); font-size:0.6rem; text-transform:uppercase; color:var(--text-muted); letter-spacing:0.05em; border:1px solid rgba(0,0,0,0.05);">
                                <div style="width:4px; height:4px; background:#eab308; border-radius:50%;"></div> Confidential
                            </div>
                        </div>
                    </div>
'''

    premium_list_v2_html += '''                </div>
            </div>
            
        '''
    
    # We reconstruct the file
    content = content[:start_idx] + premium_list_v2_html + content[end_idx:]

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updates applied successfully.")

if __name__ == '__main__':
    update_about_file()
