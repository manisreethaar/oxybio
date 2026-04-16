import os
import re

BASE_DIR = r"E:\OXYBIO-WEBSITE"

def modify_file(filename, replacements):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for target, replacement in replacements:
        if callable(target):
            content = target(content)
        else:
            content = re.sub(target, replacement, content, flags=re.DOTALL)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")


# 1. Update index.html
index_replacements = [
    # Hero status badge
    (r'Currently in Development', r'Phase 0 Lab Validation'),
    (r'Research & Development Phase', r'DPIIT Incubated Model'),
    # Hero H1
    (r'Advanced Functional Foods\.<br>Powered by Fermentation\.', r'Indigenous Fermentation Platform.<br>Engineering Functional Bioavailability.'),
    (r'Fermented indigenous grains\. Functional mushroom extracts\. Science-backed\. Tradition-rooted\.', r'Biotechnological models unlocking ancient Indian food matrices. Science-backed. Evidence-first.'),
    # Trust Bar items
    (r'<div class="marquee-track".*?</div>', lambda m: re.sub(r'<div class="marquee-track".*?</div>', 
'''<div class="marquee-track"
                    style="font-family:var(--font-mono); text-transform:uppercase; font-size:0.85rem;">
                    <span class="marquee-item">Phase 0 Lab Validation <span class="marquee-dot"></span></span>
                    <span class="marquee-item">FSSAI Licensing In Progress <span class="marquee-dot"></span></span>
                    <span class="marquee-item">DPIIT Applied <span class="marquee-dot"></span></span>
                    <span class="marquee-item">100% Indian Ingredients <span class="marquee-dot"></span></span>
                    <span class="marquee-item">Fermentation Platform <span class="marquee-dot"></span></span>
                    <span class="marquee-item">Third-Party Testing Planned <span class="marquee-dot"></span></span>

                    <span class="marquee-item">Phase 0 Lab Validation <span class="marquee-dot"></span></span>
                    <span class="marquee-item">FSSAI Licensing In Progress <span class="marquee-dot"></span></span>
                    <span class="marquee-item">DPIIT Applied <span class="marquee-dot"></span></span>
                    <span class="marquee-item">100% Indian Ingredients <span class="marquee-dot"></span></span>
                    <span class="marquee-item">Fermentation Platform <span class="marquee-dot"></span></span>
                    <span class="marquee-item">Third-Party Testing Planned <span class="marquee-dot"></span></span>
                </div>''', m.group(0), flags=re.DOTALL)),
    # Problem section
    (r'The Exhaustion Epidemic', r'The Market Gap'),
    (r'Professionals and students operating on negative energy reserves, fighting brain fog, driven by severe but invisible nutrient depletion\.', 
     r'Consumers are overwhelmed by synthetic supplements that prioritize marketing over biological compatibility, leaving fundamental absorption problems unsolved.'),
    (r'The Target Market Trap', r'The Scientific Gap'),
    (r'The industry calls you a "target demographic" to sell you premium wellness fluff and fake promises that never move the needle\.', 
     r'Standard extraction methods fail to isolate verifiable active compounds, relying instead on gross weight claims that cannot guarantee functional efficacy.'),
    (r'The Synthetic Illusion', r'The Price Gap'),
    (r'Isolated synthetic forms frequently underperform whole-food matrices — particularly for fat-soluble vitamins and trace minerals\. Label decoration instead of actual absorption\.', 
     r'Functional foods are priced as luxury imports, excluding the vast majority of the Indian demographic from science-backed nutritional protocols.'),
    (r'Modern lifestyle is breaking our biology\.', r'The industry is built on bad biology.'),
    (r'We skip breakfast\. We run on adrenaline and coffee\. We buy supplements based on marketing confidence, and we wonder why we never actually get better\. We forgot what our grandmothers knew\.', 
     r'Products are formulated for shelf appeal, not cellular absorption. The result is an illusion of health, built on synthetic isolates and biologically unusable materials.'),
    (r'There is an ancient Tamil quote, "Unnave marundhu" \(food is medicine\), but we have completely forgotten it\. We replaced traditional logic with chemical isolates\.',
     r'The market is flooded with unverified imported synthetic isolates, aggressively ignoring indigenous Indian knowledge frameworks.'),
    # Solution section
    (r'Three distinct formulation protocols currently undergoing bioavailability modeling and active efficacy research\. All compounds strictly enforce scientifically rigorous nutrient thresholds and indigenous sourcing mandates\.',
     r'A robust fermentation-driven platform leveraging indigenous Ragi and Karuppu Kavuni to dramatically enhance the bioavailability of target functional compounds.'),
    # Cleanup Comments
    (r'<!-- CLARITY \(Now EXP_01\) -->', ''),
    # Waitlist removal
    (r'<section class="structure-section" id="join".*?</section>', lambda m: '''<section class="structure-section" id="join"
                    style="background:var(--text-main); color:var(--bg); border:none;">
                    <div class="container" style="text-align:center; padding:var(--space-xl) 0;">
                        <h2 class="display" style="color:var(--bg); font-size:clamp(3rem, 6vw, 5rem);">Follow our
                            build<br><em>closely.</em></h2>
                        <p class="subtext" style="color:#A3A3A3; margin:var(--space-md) auto; max-width:600px;">
                            Join our community to receive updates on lab validation runs, FSSAI approvals, and our clinical study progress.
                        </p>
                        <form style="display:flex; flex-direction:column; gap:1rem; max-width:400px; margin:0 auto;"
                            onsubmit="event.preventDefault(); alert('Successfully joined. Check console log for integration.');">
                            <input type="email" placeholder="Enter your email address" required
                                style="width:100%; padding:1rem; border:1px solid #333; background:transparent; color:#fff; font-family:var(--font-sans); font-size:1rem; border-radius:4px; outline:none;">
                            <button type="submit" class="btn"
                                style="background:var(--bg); color:var(--text-main); width:100%; justify-content:center; padding:1.25rem;">Follow the Build</button>
                        </form>
                    </div>
                </section>'''),
    (r'comparison table', r'')
]

modify_file('index.html', index_replacements)

# Global replacements
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

for hfile in html_files:
    reps = [
        # Disclaimers
        (r'Secondary research data\. Not evaluated by FSSAI\.',
         r'Oxygen Bioinnovations is an R&D pre-revenue stage company. The formulations and methodologies described represent internally modelled protocols and have not been independently evaluated by FSSAI.'),
        (r'The products and claims made about specific products on or through this Site have not been evaluated by the Food Safety and Standards Authority of India \(FSSAI\) or the United States Food and Drug Administration \(FDA\) and are not approved to diagnose, treat, cure or prevent disease\.', 
         r'Oxygen Bioinnovations is an R&D pre-revenue stage company. The formulations and methodologies described represent internally modelled protocols and have not been independently evaluated by FSSAI.'),
        (r'not independently evaluated by FSSAI or the US FDA', r'not independently evaluated by FSSAI.'),
        (r'Join\s*Waitlist', r'Follow the Build'),
        (r'Join the Waitlist', r'Follow the Build'),
        (r'>\s*Waitlist\s*<', r'>Follow the Build<'),
    ]
    modify_file(hfile, reps)
