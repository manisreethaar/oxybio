import os, re

index_path = r'e:\OXYBIO\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_CONTENT = """
<main>

<!-- ═══════════════════════════════════════════════════════
     HERO SECTION (Strict Asymmetrical Flow)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="padding-top:140px; border-bottom:none;">
    <div class="container">
        <div class="flow-left reveal" style="max-width:900px;">
            <div class="badge" style="margin-bottom:var(--space-md);">Now in Development · TBI, Hosur</div>
            <h1 class="display">Nutrition that actually works.<br><em>For India.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                India's first precision nutrition system — built on millet, mushrooms, and adaptogens. Ancient wisdom combined with pure, bioavailable science. 
            </p>
            <div style="margin-top:var(--space-md); display:flex; gap:1rem;">
                <a href="#join" class="btn btn-primary">Join Waitlist</a>
                <a href="problem.html" class="btn btn-outline">Read the Science</a>
            </div>
        </div>

        <!-- Strict Bento Grid for High-Impact Stats -->
        <div class="bento-grid reveal" style="transition-delay:200ms;">
            <div class="bento-cell" style="grid-column: span 3;">
                <div class="data-num" data-target="73" data-suffix="%">73%</div>
                <div class="data-label">Urban Indians are Vitamin D deficient</div>
            </div>
            <div class="bento-cell" style="grid-column: span 3;">
                <div class="data-num" data-target="47" data-suffix="%">47%</div>
                <div class="data-label">Indian women with iron deficiency</div>
            </div>
            <div class="bento-cell" style="grid-column: span 3;">
                <div class="data-num">₹2</div>
                <div class="data-label">Cost difference for chelated minerals</div>
            </div>
            <div class="bento-cell" style="grid-column: span 3; background:var(--bg-alt); justify-content:center;">
                <div style="font-family:var(--font-mono); font-weight:700; font-size:1.25rem; margin-bottom:0.5rem;">RIZE</div>
                <div class="data-label">Millet · Mushroom · Science</div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     MARQUEE SECTION (Technical)
════════════════════════════════════════════════════════ -->
<div class="marquee-section" style="border-top:1px solid var(--border); background:var(--bg-alt);">
    <div class="marquee-track" style="font-family:var(--font-mono); text-transform:uppercase; font-size:0.85rem;">
        <span class="marquee-item">Chelated Minerals <span class="marquee-dot"></span></span>
        <span class="marquee-item">Lion's Mane Extract — β-Glucan 30%+ <span class="marquee-dot"></span></span>
        <span class="marquee-item">Ragi Millet Base <span class="marquee-dot"></span></span>
        <span class="marquee-item">MTHFR-Safe Methylfolate <span class="marquee-dot"></span></span>
        <span class="marquee-item">135 Clinical Study Participants <span class="marquee-dot"></span></span>
        <span class="marquee-item">FSSAI Compliant <span class="marquee-dot"></span></span>
        <span class="marquee-item">CoA for Every Batch <span class="marquee-dot"></span></span>
        <span class="marquee-item">Iron Bisglycinate — 58% Absorption <span class="marquee-dot"></span></span>
        <!-- Duplicate -->
        <span class="marquee-item">Chelated Minerals <span class="marquee-dot"></span></span>
        <span class="marquee-item">Lion's Mane Extract — β-Glucan 30%+ <span class="marquee-dot"></span></span>
        <span class="marquee-item">Ragi Millet Base <span class="marquee-dot"></span></span>
        <span class="marquee-item">MTHFR-Safe Methylfolate <span class="marquee-dot"></span></span>
        <span class="marquee-item">135 Clinical Study Participants <span class="marquee-dot"></span></span>
        <span class="marquee-item">FSSAI Compliant <span class="marquee-dot"></span></span>
        <span class="marquee-item">CoA for Every Batch <span class="marquee-dot"></span></span>
        <span class="marquee-item">Iron Bisglycinate — 58% Absorption <span class="marquee-dot"></span></span>
    </div>
</div>

<!-- ═══════════════════════════════════════════════════════
     PROBLEM SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" id="problem">
    <div class="container">
        <div style="display:grid;grid-template-columns:1fr 2fr;gap:var(--space-lg);align-items:start;">
            <div style="position:sticky;top:120px;" class="flow-left reveal">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">The Problem</span>
                </div>
                <h2 class="headline" style="margin-top:var(--space-sm);">The health drink matrix is broken.</h2>
                <p class="subtext editorial-col" style="margin-top:var(--space-sm);">Most Indian health drinks use the cheapest chemical mineral forms available. They look identical on the nutrition label, but provide a fraction of the physiological benefit.</p>
                <div style="margin-top:var(--space-md);">
                    <a href="problem.html" class="btn btn-outline">See Clinical Data</a>
                </div>
            </div>

            <!-- Bento Structure for Problem Cards -->
            <div class="bento-grid reveal" style="margin-top:0;">
                <div class="bento-cell" style="grid-column: span 12;">
                    <div class="data-num" data-target="8" data-suffix="%">8%</div>
                    <div class="data-label">Inorganic Iron Absorption Rate</div>
                    <p class="editorial-col" style="margin-top:var(--space-sm); color:var(--text-muted); line-height:1.6;">Ferrous sulfate (the standard iron in popular drinks) is absorbed at just 8%. Compare this to Iron Bisglycinate (our form) which absorbs at 58%.</p>
                </div>
                
                <div class="bento-cell" style="grid-column: span 6;">
                    <div class="data-num" data-target="73" data-suffix="%">73%</div>
                    <div class="data-label">Vitamin D Deficiency</div>
                    <p style="margin-top:var(--space-sm); color:var(--text-muted); line-height:1.6; font-size:0.95rem;">Despite abundant sunlight, D3 deficiency is rampant. We refuse cheap D2 plant analogs.</p>
                </div>
                
                <div class="bento-cell" style="grid-column: span 6;">
                    <div class="data-num" data-target="40" data-suffix="%">40%</div>
                    <div class="data-label">MTHFR Gene Variant</div>
                    <p style="margin-top:var(--space-sm); color:var(--text-muted); line-height:1.6; font-size:0.95rem;">Synthetic folic acid fails in 40% of the Indian population. Only active Methylfolate works.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     RIZE SYSTEM — INGREDIENTS
════════════════════════════════════════════════════════ -->
<section class="structure-section" id="products" style="background:var(--bg-alt);">
    <div class="container">
        <div class="flow-left reveal" style="margin-bottom:var(--space-lg);">
            <div class="section-label">
                <div class="section-label-line"></div>
                <span class="section-label-text">Formulation Architecture</span>
            </div>
            <h2 class="headline" style="margin-top:var(--space-sm);">
                Four stacks.<br><em>One complete system.</em>
            </h2>
        </div>

        <div class="bento-grid reveal">
            <!-- Stack 1 -->
            <div class="bento-cell" style="grid-column: span 6;">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; border-bottom:1px solid var(--border); padding-bottom:1rem;">STACK 01 / MILLET BASE</div>
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:1rem;">The forgotten supergrains</h3>
                <p class="editorial-col" style="color:var(--text-muted); line-height:1.6; margin-bottom:1.5rem;">
                    Ragi (3.5x calcium of milk), Bajra (Zinc-dense), and Jowar (Gluten-free matrix). A far superior delivery mechanism compared to standard malted barley or cheap whey isolates.
                </p>
            </div>

            <!-- Stack 2 -->
            <div class="bento-cell" style="grid-column: span 6;">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; border-bottom:1px solid var(--border); padding-bottom:1rem;">STACK 02 / MUSHROOM COMPLEX</div>
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:1rem;">β-glucan standardized</h3>
                <p class="editorial-col" style="color:var(--text-muted); line-height:1.6; margin-bottom:1.5rem;">
                    Lion's Mane (NGF stimulation), Reishi (Immune modulation), and Cordyceps (ATP production). Hot water extracted for maximum bioavailability.
                </p>
            </div>

            <!-- Stack 3 -->
            <div class="bento-cell" style="grid-column: span 6;">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; border-bottom:1px solid var(--border); padding-bottom:1rem;">STACK 03 / MICRONUTRIENTS</div>
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:1rem;">Precision chelation</h3>
                <p class="editorial-col" style="color:var(--text-muted); line-height:1.6; margin-bottom:1.5rem;">
                    Iron Bisglycinate (58% abs), Methylcobalamin B12 (active neural availability), and 5-MTHF Methylfolate. The exact chemical forms your body evolved to use.
                </p>
            </div>

            <!-- Stack 4 -->
            <div class="bento-cell" style="grid-column: span 6;">
                <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem; border-bottom:1px solid var(--border); padding-bottom:1rem;">STACK 04 / ADAPTOGENS</div>
                <h3 style="font-family:var(--font-serif); font-size:1.75rem; margin-bottom:1rem;">Clinical concentrations</h3>
                <p class="editorial-col" style="color:var(--text-muted); line-height:1.6; margin-bottom:1.5rem;">
                    KSM-66 Ashwagandha (300mg, 24+ trials), Brahmi (45% bacosides), and L-Theanine. Proven reductions in cortisol and improvements in cognitive velocity.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     WAITLIST CTA
════════════════════════════════════════════════════════ -->
<section class="structure-section" id="join" style="background:var(--text-main); color:var(--bg); border:none;">
    <div class="container cta-inner">
        <div class="badge" style="background:rgba(255,255,255,0.1); color:#fff; border:1px solid rgba(255,255,255,0.2); margin:0 auto 1.5rem;" class="reveal">
            Currently in development
        </div>
        <h2 class="display reveal" style="color:#fff;">
            Be first.<br><em>Join the waitlist.</em>
        </h2>
        <p class="reveal" style="margin-top:var(--space-sm); color:rgba(255,255,255,0.7); max-width:600px; margin-left:auto; margin-right:auto;">
            We are building this in public. Join our waitlist to follow the clinical trials, secure early access to the formulation, and hold us accountable.
        </p>
        <form class="waitlist-form reveal" style="margin-top:var(--space-md);" action="#" method="POST">
            <input type="email" class="waitlist-input" style="background:transparent; border-color:rgba(255,255,255,0.3); color:#fff;" placeholder="your@email.com" required>
            <button type="submit" class="btn btn-white" style="border-radius:0;">Join Now →</button>
        </form>
    </div>
</section>

"""

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + '\n</main>\n' + FOOTER)

print("Updated index.html with new structure.")
