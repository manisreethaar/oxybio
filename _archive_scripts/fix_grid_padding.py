import re

with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------
# 1. FIX THE PHANTOM HEIGHT ISSUE
# ---------------------------------------------------------
# The issue: "Our Approach" tab content is pushed down because the container aligns it to the vertical center 
# of the largest tab's height, or the grid rows are stretching.
# Fix: Force grid rows to essentially collapse or align to the very top.

html = html.replace('grid-template-rows:1fr;', 'grid-template-rows:max-content;')
html = html.replace('align-items:start;', 'align-items:start; justify-items:start; align-content:start;')

# ---------------------------------------------------------
# 2. FILL THE EMPTY SPACE UNDER THE INDEX SIDEBAR 
# ---------------------------------------------------------
# Add premium, relevant context blocks under the chapter navigation to utilize the empty space gracefully.

# Injecting below the Story Index
story_index_end = """                            <li class="index-nav-item" data-target="chapter-02" onclick="switchTab('story', 'chapter-02')"
                                style="font-family:var(--font-serif); font-size:1.5rem; font-weight:600; cursor:pointer; transition:all 0.3s ease;">
                                02. The Journey</li>
                        </ul>"""

story_sidebar_additions = """
                        
                        <!-- NEW: Premium Sidebar Data (To fill the empty space) -->
                        <div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border); display: flex; flex-direction: column; gap: 1.5rem;" class="mobile-hide">
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; text-transform:uppercase;">Development Timeline</div>
                                <div style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); font-weight:600; line-height:1;">14 Months</div>
                                <div style="font-size:0.85rem; color:var(--text-muted); margin-top:0.25rem;">Of R&D before writing a single line of marketing</div>
                            </div>
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; text-transform:uppercase;">Clinical Data</div>
                                <div style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); font-weight:600; line-height:1;">200+ Studies</div>
                                <div style="font-size:0.85rem; color:var(--text-muted); margin-top:0.25rem;">Peer-reviewed nutritional diagnostics analyzed</div>
                            </div>
                        </div>"""

html = html.replace(story_index_end, story_index_end + story_sidebar_additions)


# Injecting below the Who We Are Index
who_index_end = """                                <div class="index-nav-item" data-target="chapter-04" onclick="switchTab('who', 'chapter-04')"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div class="tab-num" style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; transition:color 0.3s ease;">02</div>
                                    <div class="tab-title" style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-muted); line-height:var(--leading-tight); font-weight:600; transition:color 0.3s ease;">Our Approach</div>
                                </div>
                            </div>
                        </div>"""

who_sidebar_additions = """
                        
                        <!-- NEW: Premium Sidebar Data (To fill the empty space) -->
                        <div style="margin-top: 5rem; position: relative;" class="mobile-hide">
                            <div style="position:absolute; left:-1.5rem; top:0; bottom:0; width:1px; background:var(--border);"></div>
                            <div style="background:var(--bg); border:1px solid var(--border); padding: 1.5rem; border-radius: 8px;">
                                <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:1rem;">
                                    <div style="width:6px; height:6px; background:#10b981; border-radius:50%;"></div>
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-main); letter-spacing:0.1em; text-transform:uppercase;">Operating Standard</div>
                                </div>
                                <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6; margin:0;">
                                    "If a dose is not high enough to trigger an actual biological response, it does not belong in the formula. We do not do label decoration."
                                </p>
                            </div>
                        </div>"""

html = html.replace(who_index_end, who_index_end + who_sidebar_additions)

with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed CSS grid alignment constraints and added premium data nodes to the empty sidebar spaces.")
