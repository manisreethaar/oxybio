import re

def create_grid_card(name, link, status, nature, degree, designation, institution):
    
    # Status styling
    if status == "Confirmed":
        status_styles = "background:rgba(13,138,116,0.1); color:#0D8A74; border:1px solid rgba(13,138,116,0.2);"
        dot_style = "background:#0D8A74;"
        status_text = "Confirmed"
    else:
        status_styles = "background:rgba(0,0,0,0.04); color:var(--text-muted); border:1px solid rgba(0,0,0,0.05);"
        dot_style = "background:#eab308;"
        status_text = "Confidential"

    # Degree / Sub-tag
    degree_html = f'<div style="font-family:var(--font-sans); font-size:0.8rem; color:var(--text-muted); margin-top:0.2rem;">{degree}</div>' if degree else ""

    # Link logic
    if link and link != "#":
        name_anchor = f'<a href="{link}" target="_blank" rel="noopener noreferrer" style="color:var(--text-main); text-decoration:none; transition:color 0.2s; display:inline-flex; align-items:center; gap:0.3rem;" onmouseover="this.style.color=\'#0D8A74\'" onmouseout="this.style.color=\'var(--text-main)\'">{name} <span style="font-family:var(--font-sans); font-size:1rem;">&#x2197;</span></a>'
    else:
        name_anchor = f'<span style="color:var(--text-main);">{name}</span>'

    html = f'''                    <!-- Mentor Grid Card -->
                    <div class="mentor-reveal" style="position:relative; background:var(--bg); border:1px solid var(--border); border-radius:12px; padding:2rem 1.5rem; display:flex; flex-direction:column; transition:all 0.3s ease;" onmouseover="this.style.borderColor='rgba(13,138,116,0.3)'; this.style.transform='translateY(-6px)';" onmouseout="this.style.borderColor='var(--border)'; this.style.transform='none';">
                        
                        <!-- Status Badge -->
                        <div style="position:absolute; top:1.25rem; right:1.25rem;">
                            <span style="font-family:var(--font-mono); font-size:0.55rem; text-transform:uppercase; letter-spacing:0.05em; padding:0.25rem 0.6rem; border-radius:4px; display:inline-flex; align-items:center; gap:0.4rem; {status_styles}">
                                <span style="width:4px; height:4px; border-radius:50%; {dot_style}"></span> {status_text}
                            </span>
                        </div>

                        <!-- Pic & Tag -->
                        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1.5rem;">
                            <div style="width:52px; height:52px; border-radius:50%; background:var(--bg-alt); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="rgba(13,138,116,0.5)" stroke-width="1.5" style="width:22px; height:22px;"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
                            </div>
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.6rem; color:#0D8A74; text-transform:uppercase; letter-spacing:0.05em;">{nature}</div>
                                {degree_html}
                            </div>
                        </div>

                        <!-- Name -->
                        <div style="margin-bottom:1.5rem;">
                            <h3 style="font-family:var(--font-serif); font-size:1.3rem; font-weight:600; color:var(--text-main); margin:0; line-height:1.2;">
                                {name_anchor}
                            </h3>
                        </div>

                        <!-- Designation & Org -->
                        <div style="margin-top:auto;">
                            <div style="font-size:0.9rem; font-weight:500; color:var(--text-main); margin-bottom:0.15rem;">{designation}</div>
                            <div style="font-size:0.8rem; color:var(--text-muted); line-height:1.4;">{institution}</div>
                        </div>
                    </div>\n'''
    return html

def update_about_file():
    with open('about.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We replace from <div class="support-list-container" style="margin-top:2rem;"> to the end of section 8
    start_str = '<div class="support-list-container" style="margin-top:2rem;">'
    start_idx = content.find(start_str)
    end_idx = content.find('</section>', start_idx)

    if start_idx == -1 or end_idx == -1:
        print("Could not find boundaries")
        return

    new_html = '''<div class="support-grid-container" style="margin-top:2rem;">

                    <!-- INDUSTRY BANNER -->
                    <div class="support-banner-header mentor-reveal">
                        Industry Advisory Board <span class="badge">03 Members</span>
                    </div>

                    <!-- 3 Column Grid -->
                    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%, 320px), 1fr)); gap:1.5rem; margin-bottom:3rem;">\n'''

    # Industry Mentors
    new_html += create_grid_card(
        name="Prabahar Jerik S",
        link="https://www.linkedin.com/in/prabahar-jerik-s-70430a162",
        status="Confirmed",
        nature="Scale-up Advisory",
        degree="",
        designation="Senior Scientist, MSAT",
        institution="Syngene International Limited"
    )
    new_html += create_grid_card(
        name="Yeslin Pushan M",
        link="https://www.linkedin.com/in/yeslin-pushan",
        status="Confirmed",
        nature="Scale-up Advisory",
        degree="",
        designation="Senior Scientist, MSAT",
        institution="Syngene International Limited"
    )
    new_html += create_grid_card(
        name="[Name Pending]",
        link="#",
        status="Confidential",
        nature="[Nature of Support]",
        degree="",
        designation="[Current Designation]",
        institution="[Institution / Organisation]"
    )

    new_html += '''                    </div>

                    <!-- ACADEMIC BANNER -->
                    <div class="support-banner-header mentor-reveal" style="margin-top:4rem;">
                        Academic &amp; Research Review <span class="badge" style="background:var(--bg); border-color:var(--border); color:var(--text-main);">08 Members</span>
                    </div>

                    <!-- 3 Column Grid -->
                    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%, 320px), 1fr)); gap:1.5rem; margin-bottom:3rem;">\n'''

    # Academic Mentors
    new_html += create_grid_card(
        name="Dr. S. Hari Lakshmi",
        link="https://www.linkedin.com/in/dr-hari-lakshmi-120a9b195/",
        status="Confirmed",
        nature="Scientific Validation",
        degree="Doctorate",
        designation="Assistant Professor",
        institution="Sri Shakthi Institute of Engineering and Technology, Coimbatore"
    )
    new_html += create_grid_card(
        name="R.C. Aashika",
        link="https://www.linkedin.com/in/aashikaravi24/",
        status="Confirmed",
        nature="Scientific Validation",
        degree="PhD Viva Completed",
        designation="Assistant Professor",
        institution="Jeppiaar Engineering College (Semmencheri, Chennai)"
    )
    new_html += create_grid_card(
        name="Gopi K",
        link="https://www.linkedin.com/in/gopi-karuppaiah-756411175/",
        status="Confirmed",
        nature="Scientific Validation",
        degree="PhD Pursuing",
        designation="Bioengineering Major",
        institution="Chung-Ang University, Seoul"
    )

    # Remaining 5 Confidential Doctorates
    for _ in range(5):
        new_html += create_grid_card(
            name="Dr. [Name Pending]",
            link="#",
            status="Confidential",
            nature="[Nature of Support]",
            degree="Doctorate",
            designation="[Role]",
            institution="[Institution / Organisation]"
        )

    new_html += '''                    </div>
                </div>
            </div>
            
        '''
    
    content = content[:start_idx] + new_html + content[end_idx:]

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success")

if __name__ == "__main__":
    update_about_file()
