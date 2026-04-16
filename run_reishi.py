import re

with open('ingredients.html', 'r', encoding='utf-8') as f:
    html = f.read()

reishi_html = '''
<!-- Reishi -->
<div class="bento-cell ingredient-card"
    style="grid-column: span 6; background:var(--bg-alt); position:relative; overflow:hidden;"
    id="ganoderma-lucidum">
    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); text-transform:uppercase; margin-bottom:1rem; display:flex; justify-content:space-between;">
        <span>Fungal</span><span>Phase 0 R&D</span>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.5rem;">
        <h3 style="font-family:var(--font-serif); font-size:1.75rem; color:var(--text-main); margin:0;">Reishi</h3>
        <span class="status-indicator"></span>
    </div>
    <p style="font-size:0.95rem; color:var(--text-muted); margin-bottom:1.5rem; font-style:italic;">Ganoderma lucidum (Fruiting Body)</p>
    <div style="display:flex; flex-direction:column; gap:0.5rem; font-family:var(--font-mono); font-size:0.8rem; color:var(--text-main); margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border); padding-bottom:0.25rem;">
            <span style="color:var(--text-muted);">Active Compound</span><span>Beta-Glucans</span>
        </div>
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border); padding-bottom:0.25rem;">
            <span style="color:var(--text-muted);">Extraction</span><span>Hot-Water</span>
        </div>
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border); padding-bottom:0.25rem;">
            <span style="color:var(--text-muted);">Standardised Yield</span><span>&gt;= 30%</span>
        </div>
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border); padding-bottom:0.25rem;">
            <span style="color:var(--text-muted);">Clinical Ref Dose</span><span>1,500mg</span>
        </div>
    </div>
    <p style="font-size:0.9rem; line-height:1.6; color:var(--text-muted); margin:0;">Investigating immunomodulatory pathways. Reishi (Ganoderma lucidum) operates effectively as a foundational immune adaptogen when extracted purely via hot-water protocols to isolate the long-chain polysaccharides.</p>
</div>
'''

if "Reishi" not in html:
    start_idx = html.find('Ganoderma lucidum')
    # If not there, insert after Cordyceps
    if start_idx == -1:
        c_idx = html.find('Cordyceps militaris')
        if c_idx != -1:
            div_start = html.rfind('<div class="bento-cell', 0, c_idx)
            if div_start != -1:
                # find end div
                count = 0
                i = div_start
                end_idx = -1
                while i < len(html):
                    if html.startswith('<div', i):
                        count += 1
                        i += 4
                    elif html.startswith('</div', i):
                        count -= 1
                        if count == 0:
                            end_idx = i + 6
                            break
                        i += 5
                    else:
                        i += 1
                
                if end_idx != -1:
                    html = html[:end_idx] + '\n' + reishi_html + html[end_idx:]
                    with open('ingredients.html', 'w', encoding='utf-8') as f:
                        f.write(html)
                    print("Reishi successfully injected.")
