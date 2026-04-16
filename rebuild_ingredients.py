import subprocess
import re

# Get the pristine ingredient file from git
result = subprocess.run(
    ['git', 'show', '3530329:ingredients.html'],
    capture_output=True
)
html = result.stdout.decode('utf-8', errors='replace')

print(f"Got {len(html)} chars from git")
print("Markers found:", [h for h in ['Lion','Cordyceps','Reishi','Ragi','Bacopa','L-Theanine','Ashwagandha','B12','D3','K2'] if h in html])

# Items to REMOVE (by unique text in their card)
REMOVE_MARKERS = [
    "Bacopa monnieri",
    "L-Theanine",
    "Methylcobalamin (B12)",
    "Vitamin D3",
    "Ashwagandha",
    "EXP_02 Co-factors",
    "STRESS & RESILIENCE",
    "STRESS &amp; RESILIENCE",
]

# Items to KEEP (sanity check)
KEEP_MARKERS = ["Lion", "Cordyceps", "Ragi"]

def remove_div_containing(html_str, marker):
    """Remove the innermost <div ...> block that contains marker text."""
    idx = html_str.find(marker)
    if idx == -1:
        return html_str, False
    
    # Walk backwards to find the nearest opening <div
    div_start = html_str.rfind('<div', 0, idx)
    if div_start == -1:
        return html_str, False
    
    # Count nesting forward to find the matching </div>
    count = 0
    i = div_start
    end_idx = -1
    while i < len(html_str):
        if html_str.startswith('<div', i):
            count += 1
            i += 4
        elif html_str.startswith('</div>', i):
            count -= 1
            if count == 0:
                end_idx = i + 6
                break
            i += 6
        else:
            i += 1
    
    if end_idx != -1:
        removed_block = html_str[div_start:end_idx]
        # Safety: don't remove if it also contains a KEEP marker
        for keep in KEEP_MARKERS:
            if keep in removed_block:
                print(f"  SKIPPED removal of '{marker}' — block also contains '{keep}'")
                return html_str, False
        return html_str[:div_start] + html_str[end_idx:], True
    return html_str, False

def remove_section_containing(html_str, marker):
    """Remove a full <section> block containing marker."""
    idx = html_str.find(marker)
    if idx == -1:
        return html_str, False
    sec_start = html_str.rfind('<section', 0, idx)
    if sec_start == -1:
        return html_str, False
    count = 0
    i = sec_start
    end_idx = -1
    while i < len(html_str):
        if html_str.startswith('<section', i):
            count += 1
            i += 8
        elif html_str.startswith('</section>', i):
            count -= 1
            if count == 0:
                end_idx = i + 10
                break
            i += 9
        else:
            i += 1
    if end_idx != -1:
        removed_block = html_str[sec_start:end_idx]
        # Safety: don't remove if it also contains a KEEP marker
        for keep in KEEP_MARKERS:
            if keep in removed_block:
                print(f"  BLOCK too large - also contains '{keep}'. Trying div removal instead.")
                return html_str, False
        return html_str[:sec_start] + html_str[end_idx:], True
    return html_str, False

# Try section-level removal first for the big blocks
for marker in ['EXP_02 Co-factors', 'STRESS & RESILIENCE', 'STRESS &amp; RESILIENCE']:
    html, removed = remove_section_containing(html, marker)
    print(f"Section removal '{marker}': {removed}")

# Then div-level removal for individual ingredient cards
for marker in REMOVE_MARKERS:
    while marker in html:
        html, removed = remove_div_containing(html, marker)
        print(f"Div removal '{marker}': {removed}")
        if not removed:
            break

# Add Reishi card if missing
if "Reishi" not in html and "Ganoderma lucidum" not in html:
    reishi_card = '''
    <div style="background:#111; border:1px solid #333; border-radius:12px; padding: clamp(1.25rem, 5vw, 2.5rem); position:relative; overflow:hidden;">
        <div style="font-family:monospace; font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.35); text-transform:uppercase; margin-bottom:1rem; display:flex; justify-content:space-between; align-items:center;">
            <span>Fungal Extract</span><span>Phase 0 R&amp;D</span>
        </div>
        <div style="margin-bottom:0.25rem;">
            <span style="font-family:serif; font-size:1.75rem; font-weight:700; color:#fff;">Reishi</span>
        </div>
        <div style="font-size:0.9rem; color:rgba(255,255,255,0.4); font-style:italic; margin-bottom:1.5rem;">Ganoderma lucidum (Fruiting Body)</div>
        <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem; margin-bottom:1.5rem;">
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:0.3rem;">
                <span style="color:rgba(255,255,255,0.4);">Active Compound</span><span style="color:#fff;">Beta-Glucans</span>
            </div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:0.3rem;">
                <span style="color:rgba(255,255,255,0.4);">Extraction</span><span style="color:#fff;">Hot-Water Only</span>
            </div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:0.3rem;">
                <span style="color:rgba(255,255,255,0.4);">Standardised For</span><span style="color:#fff;">&ge;30% Beta-Glucan</span>
            </div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:0.3rem;">
                <span style="color:rgba(255,255,255,0.4);">Clinical Ref Dose</span><span style="color:#fff;">1,500 mg</span>
            </div>
        </div>
        <p style="font-size:0.875rem; color:rgba(255,255,255,0.5); line-height:1.6; margin:0;">Investigating immunomodulatory pathways. Reishi beta-glucans interact with macrophage activity and NK-cell signalling per published nutritional biochemistry.</p>
    </div>
    '''
    # Insert after Cordyceps card (find its closing div, then append)
    cord_idx = html.find('Cordyceps militaris')
    if cord_idx != -1:
        div_start = html.rfind('<div', 0, cord_idx)
        count = 0; i = div_start; end_idx = -1
        while i < len(html):
            if html.startswith('<div', i): count += 1; i += 4
            elif html.startswith('</div>', i):
                count -= 1
                if count == 0: end_idx = i + 6; break
                i += 6
            else: i += 1
        if end_idx != -1:
            html = html[:end_idx] + '\n' + reishi_card + html[end_idx:]
            print("Reishi card injected after Cordyceps")

# Fix remaining watchlist / dual-extract strings
html = html.replace('>Join\n\n                    Waitlist<', '>Follow the Build<')
html = html.replace('>Join Waitlist<', '>Follow the Build<')
html = html.replace('dual-extract', 'hot-water extract')
html = html.replace('Dual-Extract', 'Hot-Water Extract')
html = html.replace('Vision & Mission', 'R&D Platform Goals')
html = html.replace('Vision &amp; Mission', 'R&amp;D Platform Goals')

print(f"\nFinal markers: {[h for h in ['Lion','Cordyceps','Reishi','Ragi','Bacopa','L-Theanine','Ashwagandha','B12','D3'] if h in html]}")
print(f"Final size: {len(html)} chars")

# Safety check: verify important content present
for must_have in ['Lion', 'Cordyceps', 'Ragi']:
    if must_have not in html:
        print(f"ERROR: '{must_have}' missing from final output!")
        exit(1)

with open('ingredients.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("ingredients.html written successfully.")
