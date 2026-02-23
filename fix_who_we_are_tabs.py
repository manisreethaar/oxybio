import re

with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# -------------------------------------------------------------
# 1. RENAME SIDEBAR TABS (01/02 -> 03/04)
# -------------------------------------------------------------
sidebar_old = """                                <div class="index-nav-item active-tab" data-target="chapter-03" onclick="switchTab('who', 'chapter-03')"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div class="tab-num" style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; transition:color 0.3s ease;">01</div>
                                    <div class="tab-title" style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-main); font-weight:600; line-height:var(--leading-tight); transition:color 0.3s ease;">The Founder</div>
                                </div>
                                <div class="index-nav-item" data-target="chapter-04" onclick="switchTab('who', 'chapter-04')"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div class="tab-num" style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; transition:color 0.3s ease;">02</div>
                                    <div class="tab-title" style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-muted); line-height:var(--leading-tight); font-weight:600; transition:color 0.3s ease;">Our Approach</div>
                                </div>"""

sidebar_new = """                                <div class="index-nav-item active-tab" data-target="chapter-03" onclick="switchTab('who', 'chapter-03')"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div class="tab-num" style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; transition:color 0.3s ease;">03</div>
                                    <div class="tab-title" style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-main); font-weight:600; line-height:var(--leading-tight); transition:color 0.3s ease;">The Founder</div>
                                </div>
                                <div class="index-nav-item" data-target="chapter-04" onclick="switchTab('who', 'chapter-04')"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div class="tab-num" style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; transition:color 0.3s ease;">04</div>
                                    <div class="tab-title" style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-muted); line-height:var(--leading-tight); font-weight:600; transition:color 0.3s ease;">Our Approach</div>
                                </div>"""
html = html.replace(sidebar_old, sidebar_new)


# -------------------------------------------------------------
# 2. RENAME CHAPTER CONTENT LABELS (Chapter 01/02 -> Chapter 03/04)
# -------------------------------------------------------------
label_founder_old = """                                <div
                                    style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); text-transform:uppercase;">
                                    Chapter 01</div>"""

label_founder_new = """                                <div
                                    style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); text-transform:uppercase;">
                                    Chapter 03</div>"""
html = html.replace(label_founder_old, label_founder_new)


label_approach_old = """                                <div
                                    style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); text-transform:uppercase;">
                                    Chapter 02</div>"""

label_approach_new = """                                <div
                                    style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); text-transform:uppercase;">
                                    Chapter 04</div>"""
html = html.replace(label_approach_old, label_approach_new)


# -------------------------------------------------------------
# 3. FIX THE OVERLAP BUG (Our Approach didn't have the tab-pane class)
# -------------------------------------------------------------
ch4_old = """                        <!-- ═══ CHAPTER 02: OUR APPROACH ═══ -->
                        <div id="chapter-04" class="chapter-section" style="padding-top:4rem; border-top:1px dashed var(--border);">"""

ch4_new = """                        <!-- ═══ CHAPTER 04: OUR APPROACH ═══ -->
                        <div id="chapter-04" class="chapter-section tab-pane" style="grid-area: 1 / 1; opacity: 0; visibility: hidden; transition: opacity 0.5s ease, visibility 0.5s ease; pointer-events: none;">"""
html = html.replace(ch4_old, ch4_new)


with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed 'Who We Are' tab overlap rendering and updated numbering to 03/04.")
