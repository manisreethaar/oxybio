import codecs
import re

with codecs.open('e:\\OXYBIO\\careers.html', 'r', 'utf-8') as f:
    html = f.read()

# We want to keep the Editorial Intro (lines 187-197), but target the 4 sections after it.
start_marker = '<!-- Role Overview -->'
end_marker = '<!-- \n\n        </div>\n\n    </div>\n</section>' # This is the end of the Right Details 

# Let's find the sections using precise regex to extract their inner HTML without removing anything
# Block 1: Role Overview
b1_pattern = re.compile(r'<!-- Role Overview -->\s*<div style=\"margin-bottom:4rem;\">\s*<h4.*?</h4>\s*(<p.*?</p>)\s*</div>', re.DOTALL)
b1_match = b1_pattern.search(html)

# Block 2: Key Responsibilities (The Output)
b2_pattern = re.compile(r'<!-- Key Responsibilities -->\s*<div style=\"margin-bottom:4rem;\">\s*<h4.*?</h4>\s*(<div style=\"display:grid.*?</div>\s*</div>)\s*</div>', re.DOTALL)
b2_match = b2_pattern.search(html)

# Block 3: Who We Are Looking For (The Profile)
b3_pattern = re.compile(r'<!-- Who We Are Looking For -->\s*<div style=\"margin-bottom:4rem;\">\s*<h4.*?</h4>\s*(<ul.*?</ul>)\s*</div>', re.DOTALL)
b3_match = b3_pattern.search(html)

# Block 4: What We Offer (The Offer)
b4_pattern = re.compile(r'<!-- What We Offer -->\s*(<div style=\"background:var\(--text-main\).*?</div>\s*</div>)\s*</div>\s*</div>\s*</div>\s*<!--', re.DOTALL)
b4_match = b4_pattern.search(html)

if b1_match and b2_match and b3_match and b4_match:
    content_overview = b1_match.group(1).strip()
    content_output = b2_match.group(1).strip()
    content_profile = b3_match.group(1).strip()
    
    # Target the inner grid of the offer block, stripping the dark background wrapper so it fits in the light tab
    b4_inner_pattern = re.compile(r'<div style=\"display:grid; grid-template-columns:1fr 1fr; gap:3rem;\" class=\"mobile-stack\">(.*?)</div>\s*</div>', re.DOTALL)
    b4_inner_match = b4_inner_pattern.search(b4_match.group(1))
    
    if b4_inner_match:
        content_offer_grid = b4_inner_match.group(1).strip()
        # Recolor the text from white/grey to the light theme defaults for the tab
        content_offer_grid = content_offer_grid.replace('color:#fff;', 'color:var(--text-main);')
        content_offer_grid = content_offer_grid.replace('color:#aaa;', 'color:var(--text-muted);')
        content_offer = f'<div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem;" class="mobile-stack">{content_offer_grid}</div>'
    else:
        # Fallback if inner not found
        content_offer = b4_match.group(1).strip()

    # The new Tab HTML structure
    TAB_UI = f'''
                <!-- Premium Interactive Tabs Container to Reduce Vertical length -->
                <style>
                @keyframes tabFadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
                .hide-scrollbar::-webkit-scrollbar {{ display: none; }}
                .tab-link:hover {{ color:var(--text-main) !important; }}
                </style>
                
                <div class="premium-tabs-container" style="display:flex; flex-direction:column; gap:2.5rem; margin-top:1rem;">
                    
                    <!-- Scrollable Horizontal Tab Controls -->
                    <div style="display:flex; overflow-x:auto; gap:2rem; padding-bottom:1rem; border-bottom:1px solid var(--border); scrollbar-width:none; -ms-overflow-style:none;" class="hide-scrollbar">
                        <button onclick="openCareersTab(event, 'tab-overview')" class="tab-link active" style="background:transparent; border:none; border-bottom:2px solid var(--text-main); color:var(--text-main); padding:0 0 0.5rem 0; font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; cursor:pointer; white-space:nowrap; transition:all 0.3s ease; position:relative; top:1px;">01 / Overview</button>
                        
                        <button onclick="openCareersTab(event, 'tab-output')" class="tab-link" style="background:transparent; border:none; border-bottom:2px solid transparent; color:var(--text-muted); padding:0 0 0.5rem 0; font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; cursor:pointer; white-space:nowrap; transition:all 0.3s ease; position:relative; top:1px;">02 / The Output</button>
                        
                        <button onclick="openCareersTab(event, 'tab-profile')" class="tab-link" style="background:transparent; border:none; border-bottom:2px solid transparent; color:var(--text-muted); padding:0 0 0.5rem 0; font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; cursor:pointer; white-space:nowrap; transition:all 0.3s ease; position:relative; top:1px;">03 / The Profile</button>
                        
                        <button onclick="openCareersTab(event, 'tab-offer')" class="tab-link" style="background:transparent; border:none; border-bottom:2px solid transparent; color:var(--text-muted); padding:0 0 0.5rem 0; font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; cursor:pointer; white-space:nowrap; transition:all 0.3s ease; position:relative; top:1px;">04 / The Offer</button>
                    </div>

                    <!-- Tab Contents (No content removed, just condensed) -->
                    <div id="tab-overview" class="tab-content" style="display:block; animation:tabFadeIn 0.4s ease;">
                        {content_overview}
                    </div>
                    
                    <div id="tab-output" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        {content_output}
                    </div>
                    
                    <div id="tab-profile" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        {content_profile}
                    </div>
                    
                    <div id="tab-offer" class="tab-content" style="display:none; animation:tabFadeIn 0.4s ease;">
                        {content_offer}
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
                        tablinks[i].style.borderBottom = "2px solid transparent";
                        tablinks[i].style.color = "var(--text-muted)";
                    }}
                    document.getElementById(tabName).style.display = "block";
                    evt.currentTarget.className += " active";
                    evt.currentTarget.style.borderBottom = "2px solid var(--text-main)";
                    evt.currentTarget.style.color = "var(--text-main)";
                }}
                </script>
'''

    # We now replace the entire block from <!-- Role Overview --> to the end of that section div
    replace_start = html.find('<!-- Role Overview -->')
    replace_end = b4_match.end() - 4 # stop before the <!-- Premium Internship Portal
    
    if replace_start != -1 and replace_end != -1:
        new_html = html[:replace_start] + TAB_UI + html[replace_end:]
        with codecs.open('e:\\OXYBIO\\careers.html', 'w', 'utf-8') as f:
            f.write(new_html)
        print("Successfully converted vertical sections to premium horizontal tabs.")
    else:
        print("Failed to replace block.")

else:
    print("Failed to match Regex for sections.")
    if not b1_match: print("- b1 failed")
    if not b2_match: print("- b2 failed")
    if not b3_match: print("- b3 failed")
    if not b4_match: print("- b4 failed")
