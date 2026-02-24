import re
import os

html_path = r'e:\OXYBIO\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update logo OXYGEN. to Oxygen Bioinnovations.
logo_old = r'<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen Bioinnovations<span>.</span></a>'
logo_new = r'<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen Bioinnovations<span>.</span></a>'
html = html.replace(logo_old, logo_new)


# 2. Overhaul the "The Solution" Section (Project Cards)
# We will replace the bento-grid setup with a sleek, vertical, full-width "editorial block" layout that looks incredible on mobile.
original_solution_block = r"""        <div class="bento-grid">
            <!-- Product 1 -->
            <div class="bento-cell product-card" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); border:1px solid var(--border); padding:0.25rem 0.5rem; display:inline-block; margin-bottom:1rem; border-radius:4px;">Pre-Clinical Optimization</div>
                <h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project VITALITY</h3>
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
                </div>
            </div>

            <!-- Product 2 -->
            <div class="bento-cell product-card" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); border:1px solid var(--border); padding:0.25rem 0.5rem; display:inline-block; margin-bottom:1rem; border-radius:4px;">Sensory Trials & Taste Profiling</div>
                <h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project CLARITY</h3>
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
                </div>
            </div>

            <!-- Product 3 -->
            <div class="bento-cell product-card" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-main); border:1px solid var(--text-main); background:#e8e8e4; padding:0.25rem 0.5rem; display:inline-block; margin-bottom:1rem; border-radius:4px;">Formulation Finalized</div>
                <h3 style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Project MOMENTUM</h3>
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
                </div>
            </div>

            <!-- Protein Bar -->
            <div class="bento-cell" style="grid-column: span 12; background:var(--text-main); color:var(--bg); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:3rem 2rem;">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:#888; margin-bottom:1rem; letter-spacing:0.1em; text-transform:uppercase;">Coming Soon</div>
                <h3 style="font-family:var(--font-serif); font-size:2.5rem; margin-bottom:1rem; color:#fff;">The Honest Protein Bar</h3>
                <p style="font-size:1.125rem; line-height:1.6; color:#ccc; max-width:600px; margin-bottom:1.5rem;">
                    Real dates, real cashews, real pumpkin seeds. 300mg KSM-66 Ashwagandha in every bar. No fake protein. No compound chocolate. Coming alongside our drink range.
                </p>
            </div>
        </div>"""


new_mobile_first_design = r"""        <!-- Mobile-First Stacked Project Cards -->
        <div style="display:flex; flex-direction:column; gap:3rem; margin-top:3rem;">
            
            <!-- Project Vitality -->
            <div style="background:var(--bg); border-top:2px solid var(--text-main); padding-top:2rem; display:flex; flex-direction:column; gap:1.5rem;" class="mobile-stack-card">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
                    <div>
                        <div style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-muted); letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.5rem;">01 // Pre-Clinical Optimization</div>
                        <h3 class="display" style="font-size:var(--text-5xl); line-height:0.9; margin:0;">VITALITY</h3>
                        <div style="font-weight:600; font-size:1.1rem; margin-top:0.5rem; color:var(--text-main);">DAILY DEFICIENCIES</div>
                    </div>
                </div>
                
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;" class="mobile-stack">
                    <div>
                        <p style="font-size:var(--text-lg); line-height:1.6; color:var(--text-muted); margin-bottom:1.5rem;">For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.</p>
                        <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.5rem;">
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">Covers 50% of your daily nutrient needs</span></li>
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">Sustained energy without sugar spikes</span></li>
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">Stress adaptation with KSM-66 Ashwagandha</span></li>
                        </ul>
                    </div>
                    <div style="background:var(--bg-alt); padding:2rem; border-radius:12px; border:1px solid var(--border); display:flex; flex-direction:column; justify-content:center;">
                        <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); letter-spacing:0.05em; margin-bottom:1rem;">FORMULATION STACK</div>
                        <p style="font-size:1rem; font-weight:600; line-height:1.5; margin:0;">Finger Millet, Ashwagandha KSM-66, Lion's Mane, Moringa, 22 Chelated Nutrients</p>
                    </div>
                </div>
            </div>

            <!-- Project Clarity -->
            <div style="background:var(--bg); border-top:2px solid var(--text-main); padding-top:2rem; display:flex; flex-direction:column; gap:1.5rem;" class="mobile-stack-card">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
                    <div>
                        <div style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-muted); letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.5rem;">02 // Sensory Trials & Taste Profiling</div>
                        <h3 class="display" style="font-size:var(--text-5xl); line-height:0.9; margin:0;">CLARITY</h3>
                        <div style="font-weight:600; font-size:1.1rem; margin-top:0.5rem; color:var(--text-main);">COGNITIVE FATIGUE</div>
                    </div>
                </div>
                
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;" class="mobile-stack">
                    <div>
                        <p style="font-size:var(--text-lg); line-height:1.6; color:var(--text-muted); margin-bottom:1.5rem;">The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3PM crash.</p>
                        <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.5rem;">
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">Clean focus without caffeine crash</span></li>
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">Memory and attention support (Lion's Mane)</span></li>
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">L-Theanine:Caffeine ratio 2.5:1 (clinically studied)</span></li>
                        </ul>
                    </div>
                    <div style="background:var(--bg-alt); padding:2rem; border-radius:12px; border:1px solid var(--border); display:flex; flex-direction:column; justify-content:center;">
                        <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); letter-spacing:0.05em; margin-bottom:1rem;">FORMULATION STACK</div>
                        <p style="font-size:1rem; font-weight:600; line-height:1.5; margin:0;">Lion's Mane, Bacopa Monnieri, L-Theanine, Natural Caffeine, Active B Vitamins</p>
                    </div>
                </div>
            </div>

            <!-- Project Momentum -->
            <div style="background:var(--bg); border-top:2px solid var(--text-main); padding-top:2rem; display:flex; flex-direction:column; gap:1.5rem;" class="mobile-stack-card">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
                    <div>
                        <div style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-main); font-weight:bold; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.5rem; background:#e8e8e4; display:inline-block; padding:0.2rem 0.6rem;">03 // Formulation Finalized</div>
                        <h3 class="display" style="font-size:var(--text-5xl); line-height:0.9; margin:0; margin-top:0.5rem;">MOMENTUM</h3>
                        <div style="font-weight:600; font-size:1.1rem; margin-top:0.5rem; color:var(--text-main);">CELLULAR RECOVERY</div>
                    </div>
                </div>
                
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;" class="mobile-stack">
                    <div>
                        <p style="font-size:var(--text-lg); line-height:1.6; color:var(--text-muted); margin-bottom:1.5rem;">An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.</p>
                        <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.5rem;">
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">Faster muscle recovery (Kokum + Tart Cherry)</span></li>
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">ATP production support (Cordyceps militaris)</span></li>
                            <li style="display:flex; align-items:flex-start; gap:0.5rem;"><span style="color:var(--text-main);">→</span> <span style="font-weight:500;">Strength and endurance (Creatine HCl + Citrulline)</span></li>
                        </ul>
                    </div>
                    <div style="background:var(--bg-alt); padding:2rem; border-radius:12px; border:1px solid var(--border); display:flex; flex-direction:column; justify-content:center;">
                        <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); letter-spacing:0.05em; margin-bottom:1rem;">FORMULATION STACK</div>
                        <p style="font-size:1rem; font-weight:600; line-height:1.5; margin:0;">Cordyceps, Creatine HCl, Kokum Extract, L-Citrulline, Electrolytes</p>
                    </div>
                </div>
            </div>

            <!-- Protein Bar -->
            <div style="background:var(--text-main); color:var(--bg); border-radius:24px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:4rem 2rem; margin-top:1rem;">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:#888; margin-bottom:1rem; letter-spacing:0.1em; text-transform:uppercase; border:1px solid #555; padding:0.3rem 1rem; border-radius:40px;">Coming Soon</div>
                <h3 class="display" style="font-size:var(--text-4xl); margin-bottom:1rem; color:#fff;">The Honest Protein Bar</h3>
                <p style="font-size:1.125rem; line-height:1.6; color:#ccc; max-width:600px; margin-bottom:0;">
                    Real dates, real cashews, real pumpkin seeds. 300mg KSM-66 Ashwagandha in every bar. No fake protein. No compound chocolate. Due alongside our drink range.
                </p>
            </div>
        </div>"""

html = html.replace(original_solution_block, new_mobile_first_design)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Updated {html_path}")

# 3. Need to propagate logo change across Python build scripts & React
import glob
files_to_update = glob.glob(r'e:\OXYBIO\*.py') + glob.glob(r'e:\OXYBIO\*.html') + glob.glob(r'e:\OXYBIO\src\components\layout\Navbar.tsx')

for filepath in files_to_update:
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # HTML logo update
        content = content.replace(r'<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen Bioinnovations<span>.</span></a>', r'<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen Bioinnovations<span>.</span></a>')
        # React logo update
        content = content.replace(r'>Oxygen Bioinnovations<span className="text-cyan-ethereal">.</span></span>', r'>Oxygen Bioinnovations<span className="text-cyan-ethereal">.</span></span>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated Oxygen Bioinnovations logo across project.")
