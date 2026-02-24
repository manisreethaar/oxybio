"""
ENHANCE SOLUTION CARDS
======================
1. Add CSS classes for hover tilt/lift + subtle glow effects
2. Add staggered entrance animation (fade up)
3. Rewrite confusing "Cost diff: only ₹2/serving" to something impactful
4. Add a shimmer scan effect on hover
"""
import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')
INDEX = os.path.join(ROOT, 'index.html')

# ─── 1. CSS: Add solution card animation classes ────────────
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

SOLUTION_CSS = """
/* ═══════════════════════════════════════════════════════
   SOLUTION CARDS — HOVER EFFECTS + ANIMATIONS
   ═══════════════════════════════════════════════════════ */

/* Staggered reveal on scroll */
.solution-card {
    transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), 
                box-shadow 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
}

/* Shimmer sweep on hover */
.solution-card::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 60%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,0.07),
        transparent
    );
    transition: none;
    pointer-events: none;
    z-index: 1;
}
.solution-card:hover::after {
    left: 150%;
    transition: left 0.7s ease;
}

/* Card 01 (white) — lift + shadow */
.solution-card-light:hover {
    transform: translateY(-8px);
    box-shadow: 0 24px 48px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04);
}

/* Card 02 (dark) — lift + green glow */
.solution-card-dark:hover {
    transform: translateY(-8px);
    box-shadow: 0 24px 48px rgba(13,138,116,0.2), 0 4px 12px rgba(0,0,0,0.3);
}
.solution-card-dark::after {
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,0.04),
        transparent
    );
}

/* Card 03 (alt) — lift + warm shadow */
.solution-card-alt:hover {
    transform: translateY(-8px);
    box-shadow: 0 24px 48px rgba(107,82,68,0.1), 0 4px 12px rgba(0,0,0,0.05);
}

/* Stagger entrance delays */
.solution-card:nth-child(1) { transition-delay: 0s; }
.solution-card:nth-child(2) { transition-delay: 0.1s; }
.solution-card:nth-child(3) { transition-delay: 0.2s; }

/* Bottom badge — the "proof point" at the bottom of each card */
.card-proof-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.06em;
    border-top: 1px solid var(--border);
    padding-top: 1rem;
    color: var(--text-muted);
}

.card-proof-badge-dark {
    border-top-color: rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.35);
}

/* Proof badge icon dot */
.proof-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #0D8A74;
    display: inline-block;
    animation: proofPulse 2s ease-in-out infinite;
}

@keyframes proofPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.3); }
}

/* Bottom stat number — animated counter effect */
.solution-stat-num {
    font-family: var(--font-serif);
    font-size: 3.5rem;
    font-weight: 900;
    line-height: 1;
    letter-spacing: -0.04em;
    position: relative;
}

/* Glow pulse behind the big number on hover */
.solution-card:hover .solution-stat-num::after {
    content: attr(data-value);
    position: absolute;
    top: 0;
    left: 0;
    color: inherit;
    filter: blur(12px);
    opacity: 0.3;
    animation: numGlow 1.5s ease-in-out infinite;
}

@keyframes numGlow {
    0%, 100% { opacity: 0.15; }
    50% { opacity: 0.4; }
}
"""

if '.solution-card' not in css:
    css += SOLUTION_CSS
    print('[CSS] Added solution card animation styles')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# ─── 2. HTML: Add classes + rewrite confusing footer texts ────
with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

# Card 01: Add solution-card class
html = html.replace(
    'style="background:#ffffff; border:1px solid var(--border); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">',
    'class="solution-card solution-card-light" style="background:#ffffff; border:1px solid var(--border); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">'
)

# Card 02: Add solution-card class
html = html.replace(
    'style="background:var(--text-main); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">',
    'class="solution-card solution-card-dark" style="background:var(--text-main); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">'
)

# Card 03: Add solution-card class
html = html.replace(
    'style="background:var(--bg-alt); border:1px solid var(--border); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">',
    'class="solution-card solution-card-alt" style="background:var(--bg-alt); border:1px solid var(--border); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">'
)

# Rewrite confusing "Cost diff: only ₹2/serving" to something impactful
# The ₹ might be encoded as â‚¹ due to encoding issues
html = re.sub(
    r'<div\s+style="font-family:var\(--font-mono\); font-size:0\.72rem; color:var\(--text-muted\); border-top:1px solid var\(--border\); padding-top:1rem;">[\s]*Cost diff: only [^<]*</div>',
    '<div class="card-proof-badge"><span class="proof-dot"></span> Premium bioavailable forms · Just ₹2 more per serving</div>',
    html
)

# Card 02 footer — keep but add class
html = re.sub(
    r'<div\s+style="font-family:var\(--font-mono\); font-size:0\.72rem; color:rgba\(255,255,255,0\.35\); border-top:1px solid rgba\(255,255,255,0\.1\); padding-top:1rem;">[\s]*AOAC Method[^<]*</div>',
    '<div class="card-proof-badge card-proof-badge-dark"><span class="proof-dot"></span> AOAC Method · Megazyme Certified</div>',
    html
)

# Card 03 footer — keep but add class
html = re.sub(
    r'<div\s+style="font-family:var\(--font-mono\); font-size:0\.72rem; color:var\(--text-muted\); border-top:1px solid var\(--border\); padding-top:1rem;">[\s]*Results published[^<]*</div>',
    '<div class="card-proof-badge"><span class="proof-dot"></span> Results published regardless of outcome</div>',
    html
)

# Cache bust
html = re.sub(r'\?v=\d+"', '?v=38"', html)

with open(INDEX, 'w', encoding='utf-8') as f:
    f.write(html)
print('[HTML] Solution cards enhanced with classes and rewritten footers')

# Cache bust remaining pages
for page in os.listdir(ROOT):
    if page.endswith('.html') and page != 'index.html':
        path = os.path.join(ROOT, page)
        with open(path, 'r', encoding='utf-8') as f:
            h = f.read()
        h = re.sub(r'\?v=\d+"', '?v=38"', h)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(h)

print('[DONE] Cache v38')
