import sys, re

# ── 1. INDEX.HTML upgrades ─────────────────────────────────────────────────
with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1A. Comparison Table: remove jarring full-bleed black header bar,
#        replace with a lighter, integrated section header ──────────────────
OLD_TABLE_HEADER = '''                <!-- Full-bleed header bar -->
                <div style="background:var(--text-main); padding:3rem var(--container-pad, 2rem);">
                    <div class="container" style="display:grid; grid-template-columns:1fr auto; align-items:center; gap:2rem;">
                        <div>
                            <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.4); margin-bottom:1rem;">Transparency Report</div>
                            <h2 style="font-family:var(--font-serif); font-size:clamp(1.75rem,3.5vw,2.75rem); font-weight:900; color:#fff; line-height:1.1; letter-spacing:-0.03em;">Oxygen vs. the market.<br><em style="font-weight:400; color:rgba(255,255,255,0.55);">You deserve to see the difference.</em></h2>
                        </div>
                        <div style="text-align:right; display:flex; flex-direction:column; gap:0.5rem; align-items:flex-end;">
                            <div style="font-family:var(--font-mono); font-size:2.5rem; font-weight:900; color:#fff; line-height:1;">7</div>
                            <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; text-transform:uppercase; color:rgba(255,255,255,0.4);">Verified Standards</div>
                        </div>
                    </div>
                </div>'''

NEW_TABLE_HEADER = '''                <!-- Section header — integrated, no jarring black bar -->
                <div class="container" style="padding-top:4rem; padding-bottom:2.5rem;">
                    <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:2rem; flex-wrap:wrap; border-bottom:1px solid var(--border); padding-bottom:2rem;">
                        <div>
                            <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1rem;">Transparency Report</div>
                            <h2 style="font-family:var(--font-serif); font-size:clamp(1.75rem,3.5vw,2.75rem); font-weight:900; color:var(--text-main); line-height:1.1; letter-spacing:-0.03em;">Oxygen vs. the market.<br><em style="font-weight:400; color:var(--text-muted);">You deserve to see the difference.</em></h2>
                        </div>
                        <div style="text-align:right; display:flex; flex-direction:column; gap:0.25rem; align-items:flex-end; flex-shrink:0;">
                            <div style="font-family:var(--font-serif); font-size:3.5rem; font-weight:900; color:var(--text-main); line-height:1;">7</div>
                            <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted);">Verified Standards</div>
                        </div>
                    </div>
                </div>'''

if OLD_TABLE_HEADER in html:
    html = html.replace(OLD_TABLE_HEADER, NEW_TABLE_HEADER)
    sys.stderr.write("OK: comparison table header updated\n")
else:
    sys.stderr.write("WARN: comparison table header not found exactly\n")

# ── 1B. Comparison Table: remove the jarring black bottom padding div ──────
# The section wraps in padding:0 so there's a black remnant at bottom
# Change the outer section to have a proper bg and remove black bottom
html = html.replace(
    '<section style="padding:0; overflow:hidden; border-bottom:1px solid var(--border);">',
    '<section style="padding:0; overflow:hidden; border-bottom:1px solid var(--border); background:var(--bg);">'
)

# ── 1C. Comparison Table: make the Oxygen column highlight use a soft tint
#        instead of solid black for better visual harmony ───────────────────
# Column label header: keep black but soften
html = html.replace(
    '<div style="padding:1rem 1.5rem; border-right:1px solid var(--border); background:var(--text-main);">\n                            <span style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.6); font-weight:700;">✦ Oxygen Bioinnovations</span>',
    '<div style="padding:1rem 1.5rem; border-right:1px solid var(--border); background:#1a1a1a;">\n                            <span style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.75); font-weight:700;">✦ Oxygen Bioinnovations</span>'
)

# ── 1D. Solution section: replace old stacked card layout with premium
#        numbered editorial style with large product names & metadata ────────
OLD_SOLUTION_SECTION_START = '''<!-- Project Vitality -->
                        <div style="background:var(--bg); border-top:2px solid var(--text-main); padding-top:2rem; display:flex; flex-direction:column; gap:1.5rem;"
                            class="mobile-stack-card">'''

# Find the full solution cards block start and end
sol_start_marker = '<!-- Project Vitality -->'
sol_end_marker = '<!-- Project Momentum -->'

sol_start = html.find(sol_start_marker)
# Find end of Momentum card - it ends before the next section comment
# Find the closing divs after momentum
momentum_end = html.find('</div>\n\n                    </div>', html.find('<!-- Project Momentum -->'))
if momentum_end == -1:
    momentum_end = html.find('</div>\n\n                </div>\n            </section>', html.find('<!-- Project Momentum -->'))

# Find the enclosing container div closing
prod_wrapper_end = html.find('</div>\n\n                </div>\n            </section>', sol_start)
if prod_wrapper_end == -1:
    # backup search
    prod_wrapper_end = html.find('</div>\n            </section>', sol_start)

# Get the solution section wrapper to keep (up to first product)
prefix_end = html.find(sol_start_marker)

# Find what comes right after the cards (closing divs of solution section)
# The products are inside: <div style="display:flex; flex-direction:column; gap:3rem; margin-top:3rem;">
section_wrapper_open = '<div style="display:flex; flex-direction:column; gap:3rem; margin-top:3rem;">'
wrapper_pos = html.rfind(section_wrapper_open, 0, sol_start)
wrapper_close = html.find('</div>\n\n                </div>\n            </section>', sol_start)
if wrapper_close == -1:
    wrapper_close = html.find('        </section>', sol_start + 500)

# Simpler: find by exact block - replace from the flex wrapper to its closing
insertion_target = section_wrapper_open + '\n\n                        <!-- Project Vitality -->'
insert_replace_end = '</div>\n\n                </div>'

start_idx = html.find(insertion_target)

# Find end of momentum closing  
momentum_outer_close = html.find('                        </div>\n\n                    </div>', html.rfind('<!-- Project Momentum -->'))

# Check what we found
sys.stderr.write(f"sol_start={sol_start}, start_idx={start_idx}, wrapper_close={wrapper_close}\n")

PREMIUM_PRODUCTS = '''<div style="display:flex; flex-direction:column;">

                        <!-- VITALITY -->
                        <div style="padding:3rem 0; border-top:1px solid var(--border); display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:start;" class="mobile-stack-card">
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; display:flex; align-items:center; gap:0.75rem;"><span style="display:inline-block; width:20px; height:1px; background:var(--text-muted);"></span>01 / Pre-Clinical Optimization</div>
                                <h3 class="display" style="font-size:clamp(3.5rem,7vw,5.5rem); line-height:0.9; letter-spacing:-0.04em; margin:0 0 0.75rem;">VITALITY</h3>
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; border:1px solid var(--border); display:inline-block; padding:0.3rem 0.75rem;">Daily Deficiencies</div>
                                <p style="font-size:var(--text-base); line-height:1.7; color:var(--text-muted); margin-bottom:1.5rem;">For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.</p>
                                <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Covers 50% of your daily nutrient needs</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Sustained energy without sugar spikes</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Stress adaptation with KSM-66 Ashwagandha</li>
                                </ul>
                            </div>
                            <div style="background:var(--text-main); padding:2rem; color:#fff; position:relative; overflow:hidden;">
                                <div style="position:absolute; right:-1rem; bottom:-1rem; font-family:var(--font-serif); font-size:6rem; font-weight:900; color:rgba(255,255,255,0.05); line-height:1; pointer-events:none;">V</div>
                                <div style="position:relative;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.4); margin-bottom:1rem; text-transform:uppercase;">Formulation Stack</div>
                                    <p style="font-size:0.95rem; font-weight:600; line-height:1.65; color:#fff; margin:0;">Finger Millet, Ashwagandha KSM-66, Lion&rsquo;s Mane, Moringa, 22 Chelated Nutrients</p>
                                </div>
                            </div>
                        </div>

                        <!-- CLARITY -->
                        <div style="padding:3rem 0; border-top:1px solid var(--border); display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:start;" class="mobile-stack-card">
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; display:flex; align-items:center; gap:0.75rem;"><span style="display:inline-block; width:20px; height:1px; background:var(--text-muted);"></span>02 / Sensory Trials &amp; Taste Profiling</div>
                                <h3 class="display" style="font-size:clamp(3.5rem,7vw,5.5rem); line-height:0.9; letter-spacing:-0.04em; margin:0 0 0.75rem;">CLARITY</h3>
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; border:1px solid var(--border); display:inline-block; padding:0.3rem 0.75rem;">Cognitive Fatigue</div>
                                <p style="font-size:var(--text-base); line-height:1.7; color:var(--text-muted); margin-bottom:1.5rem;">The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3 pm crash.</p>
                                <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Clean focus without caffeine crash</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Memory and attention support (Lion&rsquo;s Mane)</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>L-Theanine:Caffeine ratio 2.5:1 (clinically studied)</li>
                                </ul>
                            </div>
                            <div style="background:var(--text-main); padding:2rem; color:#fff; position:relative; overflow:hidden;">
                                <div style="position:absolute; right:-1rem; bottom:-1rem; font-family:var(--font-serif); font-size:6rem; font-weight:900; color:rgba(255,255,255,0.05); line-height:1; pointer-events:none;">C</div>
                                <div style="position:relative;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.4); margin-bottom:1rem; text-transform:uppercase;">Formulation Stack</div>
                                    <p style="font-size:0.95rem; font-weight:600; line-height:1.65; color:#fff; margin:0;">Lion&rsquo;s Mane, Bacopa Monnieri, L-Theanine, Natural Caffeine, Active B Vitamins</p>
                                </div>
                            </div>
                        </div>

                        <!-- MOMENTUM -->
                        <div style="padding:3rem 0; border-top:1px solid var(--border); border-bottom:1px solid var(--border); display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:start;" class="mobile-stack-card">
                            <div>
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; display:flex; align-items:center; gap:0.75rem;"><span style="display:inline-block; width:20px; height:1px; background:var(--text-muted);"></span>03 / Formulation Finalized</div>
                                <h3 class="display" style="font-size:clamp(3.5rem,7vw,5.5rem); line-height:0.9; letter-spacing:-0.04em; margin:0 0 0.75rem;">MOMENTUM</h3>
                                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1.5rem; border:1px solid var(--border); display:inline-block; padding:0.3rem 0.75rem;">Cellular Recovery</div>
                                <p style="font-size:var(--text-base); line-height:1.7; color:var(--text-muted); margin-bottom:1.5rem;">An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.</p>
                                <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Faster muscle recovery (Kokum + Tart Cherry)</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>ATP production support (Cordyceps militaris)</li>
                                    <li style="display:flex; gap:0.75rem; align-items:flex-start; font-size:0.9rem; color:var(--text-main);"><span style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Strength and endurance (Creatine HCl + Citrulline)</li>
                                </ul>
                            </div>
                            <div style="background:var(--text-main); padding:2rem; color:#fff; position:relative; overflow:hidden;">
                                <div style="position:absolute; right:-1rem; bottom:-1rem; font-family:var(--font-serif); font-size:6rem; font-weight:900; color:rgba(255,255,255,0.05); line-height:1; pointer-events:none;">M</div>
                                <div style="position:relative;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.4); margin-bottom:1rem; text-transform:uppercase;">Formulation Stack</div>
                                    <p style="font-size:0.95rem; font-weight:600; line-height:1.65; color:#fff; margin:0;">Cordyceps, Creatine HCl, Kokum Extract, L-Citrulline, Electrolytes</p>
                                </div>
                            </div>
                        </div>'''

if start_idx != -1 and wrapper_close != -1:
    # Replace from the flex wrapper opening to the closing divs
    old_block = html[start_idx:wrapper_close]
    html = html[:start_idx] + PREMIUM_PRODUCTS + html[wrapper_close:]
    sys.stderr.write("OK: solution section upgraded\n")
else:
    sys.stderr.write(f"WARN: solution section not replaced. start_idx={start_idx}, wrapper_close={wrapper_close}\n")

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
sys.stderr.write("index.html saved\n")


# ── 2. CSS upgrades: O2 animation color & effect enhancements ─────────────
with open('e:\\OXYBIO\\assets\\css\\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

OLD_ATOM_CSS = '''.atom {
    position: absolute;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #4ade80, #0D8A74);
    box-shadow: 0 4px 12px rgba(13, 138, 116, 0.3), inset -4px -4px 8px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-mono);
    color: white;
    font-weight: 700;
    font-size: 1.25rem;
}'''

NEW_ATOM_CSS = '''.atom {
    position: absolute;
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #c8b49a, #7a6252);
    box-shadow: 0 6px 20px rgba(122, 98, 82, 0.4), inset -4px -4px 10px rgba(0,0,0,0.2), inset 2px 2px 6px rgba(255,255,255,0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-mono);
    color: white;
    font-weight: 700;
    font-size: 1.25rem;
    transition: box-shadow 0.3s;
}'''

OLD_MOLECULE_CSS = '''.molecule-result {
    position: absolute;
    width: 96px;
    height: 96px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #6EE7B7, #0D8A74);
    box-shadow: 0 0 40px rgba(13, 138, 116, 0.4), inset -6px -6px 16px rgba(0,0,0,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-sans);
    color: white;
    font-weight: 800;
    font-size: 2.5rem;
    letter-spacing: -1px;
    opacity: 0;
    transform: scale(0);
    animation: moleculePop 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}'''

NEW_MOLECULE_CSS = '''.molecule-result {
    position: absolute;
    width: 104px;
    height: 104px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 28%, #d4c0ae, #6b5244);
    box-shadow: 0 0 60px rgba(107, 82, 68, 0.35), 0 0 120px rgba(107, 82, 68, 0.12), inset -8px -8px 20px rgba(0,0,0,0.25), inset 3px 3px 10px rgba(255,255,255,0.18);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-sans);
    color: white;
    font-weight: 800;
    font-size: 2.5rem;
    letter-spacing: -1px;
    opacity: 0;
    transform: scale(0);
    animation: moleculePop 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    text-shadow: 0 1px 3px rgba(0,0,0,0.3);
}'''

OLD_ORBIT_CSS = '''.orbit-ring {
    position: absolute;
    border-radius: 50%;
    border: 1px dashed rgba(13, 138, 116, 0.2);
    animation: spin 15s linear infinite;
}
.orbit-ring-1 {
    width: 280px;
    height: 280px;
}
.orbit-ring-2 {
    width: 180px;
    height: 180px;
    border: 1px solid rgba(13, 138, 116, 0.1);
    animation: spin 10s linear infinite reverse;
}'''

NEW_ORBIT_CSS = '''.orbit-ring {
    position: absolute;
    border-radius: 50%;
    border: 1px dashed rgba(107, 82, 68, 0.25);
    animation: spin 15s linear infinite;
}
.orbit-ring-1 {
    width: 300px;
    height: 300px;
}
.orbit-ring-2 {
    width: 190px;
    height: 190px;
    border: 1px solid rgba(107, 82, 68, 0.15);
    animation: spin 10s linear infinite reverse;
}
.orbit-ring-3 {
    width: 240px;
    height: 240px;
    border: 1px dotted rgba(107, 82, 68, 0.08);
    animation: spin 25s linear infinite;
}'''

OLD_PULSE_CSS = '''.pulse-ring {
    position: absolute;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 2px solid #0D8A74;
    opacity: 0;
    animation: pulseExpand 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

@keyframes pulseExpand {
    0%, 43% { opacity: 0; transform: scale(0.8); }
    45% { opacity: 0.8; transform: scale(1.2); }
    55% { opacity: 0; transform: scale(2.5); }
    100% { opacity: 0; transform: scale(3); }
}'''

NEW_PULSE_CSS = '''.pulse-ring {
    position: absolute;
    width: 108px;
    height: 108px;
    border-radius: 50%;
    border: 1.5px solid rgba(107, 82, 68, 0.7);
    opacity: 0;
    animation: pulseExpand 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
.pulse-ring::after {
    content: '';
    position: absolute;
    inset: -12px;
    border-radius: 50%;
    border: 1px solid rgba(107, 82, 68, 0.3);
    animation: pulseExpand 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    animation-delay: 0.1s;
}

@keyframes pulseExpand {
    0%, 43% { opacity: 0; transform: scale(0.8); }
    45% { opacity: 0.9; transform: scale(1.15); }
    55% { opacity: 0; transform: scale(2.8); }
    100% { opacity: 0; transform: scale(3.2); }
}'''

OLD_MOLECULE_POP = '''@keyframes moleculePop {
    0%, 40% { opacity: 0; transform: scale(0); box-shadow: 0 0 0px rgba(13, 138, 116, 0); }
    45% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 60px rgba(13, 138, 116, 0.6); }
    50%, 80% { opacity: 1; transform: scale(1); box-shadow: 0 0 30px rgba(13, 138, 116, 0.3); }
    85%, 100% { opacity: 0; transform: scale(0); }
}'''

NEW_MOLECULE_POP = '''@keyframes moleculePop {
    0%, 40% { opacity: 0; transform: scale(0) rotate(-15deg); box-shadow: 0 0 0px rgba(107, 82, 68, 0); }
    44% { opacity: 0.8; transform: scale(1.25) rotate(5deg); box-shadow: 0 0 80px rgba(107, 82, 68, 0.5); }
    48%, 78% { opacity: 1; transform: scale(1) rotate(0deg); box-shadow: 0 0 40px rgba(107, 82, 68, 0.3), 0 0 80px rgba(107, 82, 68, 0.1); }
    83%, 100% { opacity: 0; transform: scale(0.2) rotate(10deg); }
}'''

replacements = [
    (OLD_ATOM_CSS, NEW_ATOM_CSS, "atom CSS"),
    (OLD_MOLECULE_CSS, NEW_MOLECULE_CSS, "molecule CSS"),
    (OLD_ORBIT_CSS, NEW_ORBIT_CSS, "orbit rings CSS"),
    (OLD_PULSE_CSS, NEW_PULSE_CSS, "pulse ring CSS"),
    (OLD_MOLECULE_POP, NEW_MOLECULE_POP, "moleculePop keyframes"),
]

for old, new, name in replacements:
    if old in css:
        css = css.replace(old, new)
        sys.stderr.write(f"OK: {name}\n")
    else:
        sys.stderr.write(f"WARN: {name} not found\n")

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
sys.stderr.write("styles.css saved\n")
sys.stderr.write("ALL DONE\n")
