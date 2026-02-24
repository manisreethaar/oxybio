import codecs
import re

with codecs.open('e:\\OXYBIO\\careers.html', 'r', 'utf-8') as f:
    html = f.read()

# We need to completely rewrite the `mobile-stack-card` grid to fix the layout and move tabs
# to the left side.

# Let's extract everything inside the grid
start_marker = '        <!-- Role Outline Card -->\n        <div style="background:var(--bg); border:1px solid var(--border); display:grid; grid-template-columns:350px 1fr; gap:0; border-radius:12px; overflow:hidden;" class="mobile-stack-card">'
end_marker = '<!-- \n\n        </div>\n\n    </div>\n</section>' # This broke last time because of missing divs... wait, look at the view_file.

# In the current file, line 315 is `<!-- `
# Let's just use regex to grab the Left Sticky Header, the Editorial Intro, and the 4 Tab Contents.

left_header_match = re.search(r'<!-- Left Sticky Header -->(.*?)<!-- Right Details \(Extensive\) -->', html, re.DOTALL)
editorial_match = re.search(r'<!-- Editorial Intro -->(.*?)<!-- Premium Interactive Tabs Container to Reduce Vertical length -->', html, re.DOTALL)

tab_overview_match = re.search(r'<div id="tab-overview" class="tab-content".*?>(.*?)</div>\s*<div id="tab-output"', html, re.DOTALL)
tab_output_match = re.search(r'<div id="tab-output" class="tab-content".*?>(.*?)</div>\s*<div id="tab-profile"', html, re.DOTALL)
tab_profile_match = re.search(r'<div id="tab-profile" class="tab-content".*?>(.*?)</div>\s*<div id="tab-offer"', html, re.DOTALL)
tab_offer_match = re.search(r'<div id="tab-offer" class="tab-content".*?>(.*?)<!--', html, re.DOTALL)

if all([left_header_match, editorial_match, tab_overview_match, tab_output_match, tab_profile_match]):
    
    # We will reconstruct the exact structure from the Role Outline Card to the Premium Internship Portal
    # Ensuring all divs are closed.

    # We augment the left header to include the tab buttons
    sticky_header_content = '''
            <!-- Left Sticky Header -->
            <div style="padding:4rem 3rem; border-right:1px solid var(--border); background:var(--bg-alt); position:relative;" class="left-sticky-col">
                <div style="position:sticky; top:120px; display:flex; flex-direction:column; height:calc(100vh - 160px); justify-content:space-between;">
                    
                    <div>
                        <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:2rem; text-transform:uppercase; letter-spacing:0.05em;">
                            <span style="color:var(--text-main); font-weight:700;">Full Time</span>
                            <span style="color:#ccc;">|</span>
                            <span>0-1 YR EXP</span>
                        </div>
                        <h3 class="display" style="font-size:clamp(2rem, 3vw, 2.75rem); line-height:1.1; letter-spacing:-0.02em; margin-bottom:1rem;">Research<br>Associate</h3>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-main); border:1px solid var(--text-main); border-radius:50px; display:inline-block; padding:0.4rem 0.8rem; margin-bottom:3rem;">Bio / Food Tech</div>
                        
                        <!-- NEW: Vertical Tab Navigation Menu -->
                        <style>
                            .side-tab {{ display:block; width:100%; text-align:left; background:transparent; border:none; border-left:2px solid transparent; color:var(--text-muted); padding:1rem 1rem; font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; cursor:pointer; transition:all 0.3s ease; margin-bottom:0.5rem; }}
                            .side-tab:hover {{ color:var(--text-main); background:rgba(0,0,0,0.02); }}
                            .side-tab.active {{ border-left:2px solid var(--text-main); color:var(--text-main); font-weight:600; background:rgba(0,0,0,0.03); }}
                            
                            /* Mobile adjustment: If on small screen, make side tabs horizontal again temporarily but better formatted */
                            @media (max-width: 768px) {{
                                .side-tab-container {{ display:flex; overflow-x:auto; margin-bottom:2rem; }}
                                .side-tab {{ border-left:none; border-bottom:2px solid transparent; padding:0.5rem; width:auto; flex-shrink:0; margin-bottom:0; margin-right:1rem; }}
                                .side-tab.active {{ border-left:none; border-bottom:2px solid var(--text-main); }}
                                .left-sticky-col > div {{ height: auto !important; position:relative !important; }}
                            }}
                        </style>

                        <div class="side-tab-container" style="border-top:1px solid var(--border); padding-top:2rem; margin-top:2rem;">
                            <button onclick="openCareersTab(event, 'tab-overview')" class="side-tab tab-link active">01 / Overview</button>
                            <button onclick="openCareersTab(event, 'tab-output')" class="side-tab tab-link">02 / The Output</button>
                            <button onclick="openCareersTab(event, 'tab-profile')" class="side-tab tab-link">03 / The Profile</button>
                            <button onclick="openCareersTab(event, 'tab-offer')" class="side-tab tab-link">04 / The Offer</button>
                        </div>
                    </div>

                    <div style="margin-top:2rem;">
                        <a href="mailto:careers@oxygenbioinnovations.com?subject=Application%20for%20Research%20Associate" class="btn btn-primary" style="padding:1.2rem; width:100%; justify-content:center; border-radius:8px;">Apply via Email →</a>
                        <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); text-align:center; margin-top:1.5rem;">careers@oxygenbioinnovations.com</p>
                    </div>

                </div>
            </div>
'''

    right_content = f'''
            <!-- Right Details (Extensive) -->
            <div style="padding:4rem;">
                
                <!-- Editorial Intro -->
                <div style="margin-bottom:4rem; padding-bottom:3rem; border-bottom:1px solid var(--border);">
                    <p style="font-size:1.5rem; line-height:1.6; color:var(--text-main); margin-bottom:2rem; font-weight:500; letter-spacing:-0.01em;">
                        We are seeking ambitious and research-driven individuals who aspire to build—not just join—a company.
                    </p>
                    <p style="font-size:1.15rem; line-height:1.7; color:var(--text-muted); margin-bottom:2rem;">
                        This opportunity is ideal for candidates who are passionate about deep-tech innovation and are prepared to grow as the organization scales from laboratory research to full-scale commercialization.
                    </p>
                    <div style="padding:2rem; background:var(--bg-alt); border-left:4px solid var(--text-main); font-family:var(--font-serif); font-style:italic; font-size:1.25rem; color:var(--text-main);">
                        "This is not a routine laboratory role. It is a high-ownership position within a performance-driven startup ecosystem, where scientific rigor meets entrepreneurial execution."
                    </div>
                </div>

                <!-- Tab Contents Region -->
                <div class="premium-tabs-container" style="position:relative; min-height:600px;">
                    
                    <style>@keyframes tabFadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}</style>

                    <div id="tab-overview" class="tab-content" style="display:block; animation:tabFadeIn 0.4s ease;">
                        {tab_overview_match.group(1).strip()}
                    </div>
                    
                    <div id="tab-output" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        {tab_output_match.group(1).strip()}
                    </div>
                    
                    <div id="tab-profile" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        {tab_profile_match.group(1).strip()}
                    </div>
                    
                    <div id="tab-offer" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        <!-- The Offer Content Extracted manually to fix broken closure -->
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem;" class="mobile-stack">
                            <div>
                                <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:var(--text-main); margin-bottom:0.75rem;">Deep-Tech Exposure</h5>
                                <p style="font-size:1rem; color:var(--text-muted); line-height:1.6;">Work on high-impact R&D projects with real commercialization pathways.</p>
                            </div>
                            <div>
                                <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:var(--text-main); margin-bottom:0.75rem;">Accelerated Career Growth</h5>
                                <p style="font-size:1rem; color:var(--text-muted); line-height:1.6;">Performance-based responsibility expansion with leadership opportunities.</p>
                            </div>
                            <div>
                                <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:var(--text-main); margin-bottom:0.75rem;">End-to-End Experience</h5>
                                <p style="font-size:1rem; color:var(--text-muted); line-height:1.6;">From lab-scale concept to regulatory approval and market launch.</p>
                            </div>
                            <div>
                                <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:var(--text-main); margin-bottom:0.75rem;">Innovation & IP Participation</h5>
                                <p style="font-size:1rem; color:var(--text-muted); line-height:1.6;">Exposure to patent drafting, technology validation, and commercialization.</p>
                            </div>
                            <div>
                                <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:var(--text-main); margin-bottom:0.75rem;">Founder-Level Mentorship</h5>
                                <p style="font-size:1rem; color:var(--text-muted); line-height:1.6;">Direct collaboration with leadership in a high-visibility growth environment.</p>
                            </div>
                            <div>
                                <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:var(--text-main); margin-bottom:0.75rem;">Incentive Aligned</h5>
                                <p style="font-size:1rem; color:var(--text-muted); line-height:1.6;">Competitive compensation structured with capability, contribution, and milestones.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                function openCareersTab(evt, tabName) {{
                    var i, tabcontent, tablinks;
                    tabcontent = document.getElementsByClassName("tab-content");
                    for (i = 0; i < tabcontent.length; i++) {{
                        tabcontent[i].style.display = "none";
                    }}
                    tablinks = document.getElementsByClassName("tab-link");
                    for (i = 0; i < tablinks.length; i++) {{
                        tablinks[i].className = tablinks[i].className.replace(" active", "");
                    }}
                    document.getElementById(tabName).style.display = "block";
                    evt.currentTarget.className += " active";
                }}
                </script>

            </div>
        </div> <!-- CLOSING ROLE OUTLINE CARD -->
    </div> <!-- CLOSING CONTAINER -->
</section> <!-- CLOSING SECTION -->
'''
    
    # We replace from Role Outline Card to Premium Internship Portal safely
    replace_start = html.find('        <!-- Role Outline Card -->')
    replace_end = html.find('<!-- ═══════════════════════════════════════════════════════\n     PREMIUM INTERNSHIP PORTAL')

    if replace_start != -1 and replace_end != -1:
        new_html = html[:replace_start] + '        <!-- Role Outline Card -->\n        <div style="background:var(--bg); border:1px solid var(--border); display:grid; grid-template-columns:350px 1fr; gap:0; border-radius:12px; overflow:hidden;" class="mobile-stack-card">\n' + sticky_header_content + right_content + html[replace_end:]
        with codecs.open('e:\\OXYBIO\\careers.html', 'w', 'utf-8') as f:
            f.write(new_html)
        print("Successfully rebuilt Role Card with Left Sidebar Navigation.")
    else:
        print("Failed to find replacement indices.")

else:
    print("Match failed. Debug:")
    print("Left Header:", left_header_match is not None)
    print("Editorial:", editorial_match is not None)
    print("Overview:", tab_overview_match is not None)
    print("Output:", tab_output_match is not None)
    print("Profile:", tab_profile_match is not None)
    print("Offer:", tab_offer_match is not None)
