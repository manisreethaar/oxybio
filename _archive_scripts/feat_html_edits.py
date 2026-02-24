import re
import os

html_path = r'e:\OXYBIO\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove redundancy in hero
redundant_pattern = re.compile(
    r'<div style="margin-top:var\(--space-md\); font-family:var\(--font-mono\); font-size:0\.85rem; color:var\(--text-muted\); display:flex; gap:1\.5rem; flex-wrap:wrap;">\s*<span>✓ TBI Incubated Startup</span>\s*<span>✓ FSSAI Licensing In Progress</span>\s*<span>✓ 100% Indian Ingredients</span>\s*</div>',
    re.MULTILINE
)
html = redundant_pattern.sub('', html)

# 2. Make Marquee an individual card
marquee_old = r'<div class="marquee-section" style="border-top:1px solid var(--border); background:var(--bg-alt);">'
marquee_new = r'<div class="container pb-12"><div class="marquee-section" style="border:1px solid var(--border); background:var(--bg-alt); border-radius:12px; padding:1.5rem 0; box-shadow:var(--shadow-md);">'
html = html.replace(marquee_old, marquee_new)

# Close the new container div for marquee
track_end_old = r'    </div>\n</div>'
track_end_new = r'    </div>\n</div>\n</div>'
html = html.replace(track_end_old, track_end_new)


# 3. Enhance Text Colors and Aligment in Product Cards
# Project Vitality
vitality_old = """<h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project VITALITY</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Daily Deficiencies</p>
                <p style="font-size:var(--text-base); line-height:var(--leading-normal); color:var(--text-main); margin-bottom:1rem; font-style:italic;">For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.</p>
                <ul style="font-size:var(--text-sm); line-height:var(--leading-relaxed); color:var(--text-muted); padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li>Covers 50% of your daily nutrient needs</li>
                    <li>Sustained energy without sugar spikes</li>
                    <li>Stress adaptation with KSM-66 Ashwagandha</li>
                </ul>
                <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                    <strong>INGREDIENTS:</strong> Finger Millet, Ashwagandha KSM-66, Lion's Mane, Moringa, 22 Chelated Nutrients
                </div>"""

vitality_new = """<h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project VITALITY</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-main); font-weight:600; margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Daily Deficiencies</p>
                <p style="font-size:var(--text-base); line-height:var(--leading-normal); color:var(--text-main); margin-bottom:1rem; font-weight:500;">For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.</p>
                <ul style="font-size:var(--text-sm); line-height:var(--leading-relaxed); color:var(--text-main); font-weight:500; padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li style="margin-bottom:0.5rem;">Covers 50% of your daily nutrient needs</li>
                    <li style="margin-bottom:0.5rem;">Sustained energy without sugar spikes</li>
                    <li style="margin-bottom:0.5rem;">Stress adaptation with KSM-66 Ashwagandha</li>
                </ul>
                <div style="font-family:var(--font-mono); display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem; padding:1rem; background:var(--bg-alt); border-radius:8px; color:var(--text-main);">
                    <strong>INGREDIENTS:</strong>
                    <span>Finger Millet, Ashwagandha KSM-66, Lion's Mane, Moringa, 22 Chelated Nutrients</span>
                </div>"""
html = html.replace(vitality_old, vitality_new)

# Project Clarity
clarity_old = """<h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project CLARITY</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Cognitive Fatigue</p>
                <p style="font-size:var(--text-base); line-height:var(--leading-normal); color:var(--text-main); margin-bottom:1rem; font-style:italic;">The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3PM crash.</p>
                <ul style="font-size:var(--text-sm); line-height:var(--leading-relaxed); color:var(--text-muted); padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li>Clean focus without caffeine crash</li>
                    <li>Memory and attention support (Lion's Mane)</li>
                    <li>L-Theanine:Caffeine ratio 2.5:1 (clinically studied)</li>
                </ul>
                <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                    <strong>INGREDIENTS:</strong> Lion's Mane, Bacopa Monnieri, L-Theanine, Natural Caffeine, Active B Vitamins
                </div>"""

clarity_new = """<h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project CLARITY</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-main); font-weight:600; margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Cognitive Fatigue</p>
                <p style="font-size:var(--text-base); line-height:var(--leading-normal); color:var(--text-main); margin-bottom:1rem; font-weight:500;">The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3PM crash.</p>
                <ul style="font-size:var(--text-sm); line-height:var(--leading-relaxed); color:var(--text-main); font-weight:500; padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li style="margin-bottom:0.5rem;">Clean focus without caffeine crash</li>
                    <li style="margin-bottom:0.5rem;">Memory and attention support (Lion's Mane)</li>
                    <li style="margin-bottom:0.5rem;">L-Theanine:Caffeine ratio 2.5:1 (clinically studied)</li>
                </ul>
                <div style="font-family:var(--font-mono); display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem; padding:1rem; background:var(--bg-alt); border-radius:8px; color:var(--text-main);">
                    <strong>INGREDIENTS:</strong>
                    <span>Lion's Mane, Bacopa Monnieri, L-Theanine, Natural Caffeine, Active B Vitamins</span>
                </div>"""
html = html.replace(clarity_old, clarity_new)

# Project Momentum
momentum_old = """<h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project MOMENTUM</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Cellular Recovery</p>
                <p style="font-size:var(--text-base); line-height:var(--leading-normal); color:var(--text-main); margin-bottom:1rem; font-style:italic;">An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.</p>
                <ul style="font-size:var(--text-sm); line-height:var(--leading-relaxed); color:var(--text-muted); padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li>Faster muscle recovery (Kokum + Tart Cherry)</li>
                    <li>ATP production support (Cordyceps militaris)</li>
                    <li>Strength and endurance (Creatine HCl + Citrulline)</li>
                </ul>
                <div style="font-family:var(--font-mono); font-size:0.75rem; padding-top:1rem; border-top:1px solid var(--border); color:#888;">
                    <strong>INGREDIENTS:</strong> Cordyceps, Creatine HCl, Kokum Extract, L-Citrulline, Electrolytes
                </div>"""

momentum_new = """<h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project MOMENTUM</h3>
                <p style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-main); font-weight:600; margin-bottom:1rem; letter-spacing:0.05em; text-transform:uppercase;">Cellular Recovery</p>
                <p style="font-size:var(--text-base); line-height:var(--leading-normal); color:var(--text-main); margin-bottom:1rem; font-weight:500;">An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.</p>
                <ul style="font-size:var(--text-sm); line-height:var(--leading-relaxed); color:var(--text-main); font-weight:500; padding-left:1.25rem; margin-bottom:1.5rem;">
                    <li style="margin-bottom:0.5rem;">Faster muscle recovery (Kokum + Tart Cherry)</li>
                    <li style="margin-bottom:0.5rem;">ATP production support (Cordyceps militaris)</li>
                    <li style="margin-bottom:0.5rem;">Strength and endurance (Creatine HCl + Citrulline)</li>
                </ul>
                <div style="font-family:var(--font-mono); display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem; padding:1rem; background:var(--bg-alt); border-radius:8px; color:var(--text-main);">
                    <strong>INGREDIENTS:</strong>
                    <span>Cordyceps, Creatine HCl, Kokum Extract, L-Citrulline, Electrolytes</span>
                </div>"""
html = html.replace(momentum_old, momentum_new)

# 4. Table adjustments
html = html.replace('<div class="bento-cell" style="grid-column: span 12; overflow-x:auto;">', '<div class="bento-cell" style="grid-column: span 12;">')
html = html.replace('<table style="width:100%; text-align:left; border-collapse:collapse; font-size:0.95rem; min-width:600px;">', '<table style="width:100%; text-align:left; border-collapse:collapse; font-size:0.95rem;">')
html = html.replace('~28% (Oxygen)', '~28% (Oxygen Bioinnovations)')


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Updated {html_path}")


# 5. Fix Mega Menu styles in styles.css
css_path = r'e:\OXYBIO\assets\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the mega menu CSS with a dark variant
import re
megamenu_pattern = re.compile(r'\.mega-menu \{.*?\n\}', re.DOTALL)
new_megamenu_css = """.mega-menu {
    position: absolute;
    top: calc(100% + 1.5rem);
    left: 50%;
    transform: translateX(-50%) translateY(10px) scale(0.98);
    background: rgba(10, 10, 12, 0.95);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 1.5rem;
    min-width: 320px;
    display: flex;
    gap: 1.5rem;
    box-shadow: 0 30px 60px rgba(0,0,0,0.4), 0 0 0 1px rgba(255,255,255,0.05) inset;
    opacity: 0;
    visibility: hidden;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    pointer-events: none;
    color: var(--text-main);
}
.nav-item:hover .mega-menu {
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) translateY(0) scale(1);
    pointer-events: auto;
}
.mega-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.08) 100%);
    padding: 1.25rem;
    border-radius: 12px;
    min-width: 140px;
    border: 1px solid rgba(255,255,255,0.05);
    color: var(--text-main);
}
.mega-links {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.mega-links a {
    position: relative;
    padding-left: 0 !important;
    transition: transform 0.2s ease, color 0.2s ease;
    color: var(--text-muted);
    font-weight: 500;
}
.mega-links a:hover {
    transform: translateX(4px);
    color: #fff;
}
.mega-links a::after {
    content: "→";
    position: absolute;
    right: -20px;
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.2s ease;
}
.mega-links a:hover::after {
    opacity: 1;
    transform: translateX(0);
}
"""

# Apply regex substitution for the main block, and let's manually replace mega-card and mega-links a if they exist
css = megamenu_pattern.sub(new_megamenu_css, css)

# Clean up any leftover duplicate mega-card or mega-links a that I appended earlier
remove_old_mega = re.compile(r'\.mega-card \{.*?\}\n\.mega-links a \{.*?\}\n\.mega-links a:hover \{.*?\}\n\.mega-links a::after \{.*?\}\n\.mega-links a:hover::after \{.*?\}\n', re.DOTALL)
css = remove_old_mega.sub("", css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print(f"Updated {css_path}")
