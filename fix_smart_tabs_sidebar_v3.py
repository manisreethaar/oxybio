import codecs
import re

with codecs.open('e:\\OXYBIO\\careers.html', 'r', 'utf-8') as f:
    html = f.read()

# Use regex with dotall and allowing variable spaces/newlines
bound_pattern = re.compile(r'(\s*<!-- Role Outline Card -->.+?)(?=<!-- [═]+?\r?\n\s+PREMIUM INTERNSHIP PORTAL)', re.DOTALL)
bound_match = bound_pattern.search(html)

if bound_match:
    section_html = bound_match.group(1)
    
    # Extract the necessary inner contents
    tab_overview_match = re.search(r'<div id="tab-overview" class="tab-content".*?>(.*?)</div>\s*<div id="tab-output"', section_html, re.DOTALL)
    tab_output_match = re.search(r'<div id="tab-output" class="tab-content".*?>(.*?)</div>\s*<div id="tab-profile"', section_html, re.DOTALL)
    tab_profile_match = re.search(r'<div id="tab-profile" class="tab-content".*?>(.*?)</div>\s*<div id="tab-offer"', section_html, re.DOTALL)
    
    # Offer match: careful with existing grid
    tab_offer_grid_match = re.search(r'<div id="tab-offer".*?(<div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem;" class="mobile-stack">.*?</div>\s*</div>)', section_html, re.DOTALL)

    if all([tab_overview_match, tab_output_match, tab_profile_match, tab_offer_grid_match]):
        
        NEW_ROLE_BLOCK = f'''        <!-- Role Outline Card -->
        <div style="background:var(--bg); border:1px solid var(--border); display:grid; grid-template-columns:350px 1fr; gap:0; border-radius:12px; overflow:hidden;" class="mobile-stack-card">
            
            <!-- ====== LEFT STICKY SIDEBAR (INNOVATION: VERTICAL TABS) ====== -->
            <div style="padding:4rem 3rem; border-right:1px solid var(--border); background:var(--bg-alt); position:relative;" class="left-sticky-col">
                <div style="position:sticky; top:120px; display:flex; flex-direction:column; min-height:calc(100vh - 160px); justify-content:space-between;">
                    
                    <div>
                        <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:2rem; text-transform:uppercase; letter-spacing:0.05em;">
                            <span style="color:var(--text-main); font-weight:700;">Full Time</span>
                            <span style="color:#ccc;">|</span>
                            <span>0-1 YR EXP</span>
                        </div>
                        <h3 class="display" style="font-size:clamp(2rem, 3vw, 2.75rem); line-height:1.1; letter-spacing:-0.02em; margin-bottom:1rem;">Research<br>Associate</h3>
                        <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-main); border:1px solid var(--text-main); border-radius:50px; display:inline-block; padding:0.4rem 0.8rem; margin-bottom:3rem;">Bio / Food Tech</div>
                        
                        <!-- Premium Interactive Left-Nav Tabs -->
                        <style>
                            .side-tab {{ display:block; width:100%; text-align:left; background:transparent; border:none; border-left:2px solid transparent; color:var(--text-muted); padding:1rem 1rem; font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; cursor:pointer; transition:all 0.3s ease; margin-bottom:0.5rem; outline:none; }}
                            .side-tab:hover {{ color:var(--text-main); background:rgba(0,0,0,0.02); }}
                            .side-tab.active {{ border-left:2px solid var(--text-main); color:var(--text-main); font-weight:600; background:rgba(0,0,0,0.03); }}
                            
                            /* Mobile fallback for tabs */
                            @media (max-width: 768px) {{
                                .side-tab-container {{ display:flex; overflow-x:auto; margin-bottom:0rem; padding-bottom:1rem; }}
                                .side-tab {{ border-left:none !important; border-bottom:2px solid transparent; padding:1rem; width:auto; flex-shrink:0; margin-bottom:0; flex:1; text-align:center; }}
                                .side-tab.active {{ border-bottom:2px solid var(--text-main); background:transparent; }}
                                .left-sticky-col > div {{ min-height: auto !important; position:relative !important; }}
                            }}
                            @keyframes tabFadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
                        </style>

                        <div class="side-tab-container" style="border-top:1px solid var(--border); padding-top:2rem; margin-top:2rem;">
                            <button onclick="openCareersTab(event, 'tab-overview')" class="side-tab tab-link active">01 / Overview</button>
                            <button onclick="openCareersTab(event, 'tab-output')" class="side-tab tab-link">02 / Validation</button>
                            <button onclick="openCareersTab(event, 'tab-profile')" class="side-tab tab-link">03 / The Profile</button>
                            <button onclick="openCareersTab(event, 'tab-offer')" class="side-tab tab-link">04 / The Offer</button>
                        </div>
                    </div>

                    <div style="margin-top:2.5rem; padding-top:2.5rem; border-top:1px solid var(--border);">
                        <a href="mailto:careers@oxygenbioinnovations.com?subject=Application%20for%20Research%20Associate" class="btn btn-primary" style="padding:1.2rem; width:100%; justify-content:center; border-radius:8px;">Apply via Email →</a>
                        <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); text-align:center; margin-top:1.5rem; margin-bottom:0;">careers@oxygenbioinnovations.com</p>
                    </div>
                </div>
            </div>
            
            <!-- ====== RIGHT DETAILS (CONTENT PANES) ====== -->
            <div style="padding:4rem;">
                <!-- Editorial Intro: Remains Static across tabs -->
                <div style="margin-bottom:4rem; padding-bottom:3rem; border-bottom:1px solid var(--border);">
                    <p style="font-size:1.5rem; line-height:1.6; color:var(--text-main); margin-bottom:2rem; font-weight:500; letter-spacing:-0.01em;">
                        We are seeking ambitious and research-driven individuals who aspire to build—not just join—a company.
                    </p>
                    <div style="padding:2rem; background:var(--bg-alt); border-left:4px solid var(--text-main); font-family:var(--font-serif); font-style:italic; font-size:1.25rem; color:var(--text-main);">
                        "This is not a routine laboratory role. It is a high-ownership position within a performance-driven startup ecosystem, where scientific rigor meets entrepreneurial execution."
                    </div>
                </div>

                <!-- Tab Contents Region (Replaces the long scroll) -->
                <div class="premium-tabs-container" style="position:relative; min-height:500px;">
                    
                    <div id="tab-overview" class="tab-content" style="display:block; animation:tabFadeIn 0.4s ease;">
                        <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:var(--text-main); text-transform:uppercase; margin-bottom:1.5rem;">01 / Overview</h4>
                        {tab_overview_match.group(1).strip()}
                    </div>
                    
                    <div id="tab-output" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:var(--text-main); text-transform:uppercase; margin-bottom:1.5rem;">02 / Validation Output</h4>
                        {tab_output_match.group(1).strip()}
                    </div>
                    
                    <div id="tab-profile" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:var(--text-main); text-transform:uppercase; margin-bottom:1.5rem;">03 / The Profile Requirements</h4>
                        {tab_profile_match.group(1).strip()}
                    </div>
                    
                    <div id="tab-offer" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:var(--text-main); text-transform:uppercase; margin-bottom:1.5rem;">04 / Value Proposition</h4>
                        {tab_offer_grid_match.group(1).strip()}
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
        </div>
    </div>
</section>
\n'''
        
        # Replace the matching section 
        new_html = html[:bound_match.start()] + NEW_ROLE_BLOCK + html[bound_match.end():]
        with codecs.open('e:\\OXYBIO\\careers.html', 'w', 'utf-8') as f:
            f.write(new_html)
        print("Successfully built Left Side ScrollSpy Navigation and fixed layout bugs.")
    else:
        print("Failed to extract inner tab content.")
else:
    print("Failed to find bound marker with regex.")
