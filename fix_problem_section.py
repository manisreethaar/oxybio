"""
Append the problem section CSS to styles.css
"""
import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

PROBLEM_CSS = """
/* ═══════════════════════════════════════════════════════
   PROBLEM SECTION — DARK CINEMATIC PANEL
   ═══════════════════════════════════════════════════════ */
.problem-dark-panel {
    background: #0a0a0a;
    color: #f5f5f5;
    padding: clamp(4rem, 8vw, 7rem) 0;
    position: relative;
    overflow: hidden;
}

/* Subtle grain texture overlay */
.problem-dark-panel::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
}

.problem-dark-panel .container {
    position: relative;
    z-index: 1;
}

/* ── STAT CARDS ROW ── */
.problem-stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: clamp(3rem, 6vw, 5rem);
}

.problem-stat-card {
    padding: clamp(1.5rem, 3vw, 2.5rem);
    background: rgba(255,255,255,0.03);
    text-align: center;
    transition: background 0.4s ease;
}
.problem-stat-card:hover {
    background: rgba(255,255,255,0.07);
}

.problem-stat-num {
    font-family: var(--font-sans);
    font-size: clamp(3rem, 6vw, 5rem);
    font-weight: 900;
    letter-spacing: -0.04em;
    line-height: 1;
    color: #fff;
    margin-bottom: 0.75rem;
}

.problem-stat-danger .problem-stat-num {
    color: #ef4444;
}

.problem-stat-label {
    font-family: var(--font-sans);
    font-size: clamp(0.8rem, 1.2vw, 0.95rem);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: rgba(255,255,255,0.7);
    line-height: 1.4;
    margin-bottom: 0.5rem;
}

.problem-stat-source {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: rgba(255,255,255,0.3);
    line-height: 1.3;
}

/* ── HEADLINE BLOCK ── */
.problem-headline-block {
    text-align: center;
    max-width: 800px;
    margin: 0 auto clamp(3rem, 6vw, 5rem);
}

.problem-label-tag {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.25em;
    color: rgba(255,255,255,0.4);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 0.35rem 1rem;
    border-radius: 50px;
    margin-bottom: 2rem;
}

.problem-main-title {
    font-family: var(--font-serif);
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -0.03em;
    color: #fff;
    margin: 0 0 1.5rem;
}

.problem-subtext {
    font-family: var(--font-sans);
    font-size: clamp(1rem, 1.5vw, 1.2rem);
    line-height: 1.6;
    color: rgba(255,255,255,0.55);
    max-width: 600px;
    margin: 0 auto 2rem;
}

.problem-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-mono);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #fff;
    text-decoration: none;
    padding: 0.75rem 1.5rem;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 50px;
    transition: all 0.3s ease;
}
.problem-cta:hover {
    background: #fff;
    color: #0a0a0a;
    border-color: #fff;
    transform: translateY(-1px);
}
.problem-cta svg {
    transition: transform 0.3s ease;
}
.problem-cta:hover svg {
    transform: translateX(4px);
}

/* ── PROBLEM PANELS (3 tall vertical cards) ── */
.problem-panels {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    overflow: hidden;
}

.problem-panel {
    padding: clamp(2rem, 3vw, 3rem);
    background: rgba(255,255,255,0.02);
    display: flex;
    flex-direction: column;
    transition: background 0.4s ease;
    position: relative;
}
.problem-panel:hover {
    background: rgba(255,255,255,0.06);
}

/* Top border accent on hover */
.problem-panel::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}
.problem-panel:hover::before {
    opacity: 1;
}

.problem-panel-num {
    font-family: var(--font-mono);
    font-size: clamp(3rem, 5vw, 4.5rem);
    font-weight: 900;
    color: rgba(255,255,255,0.06);
    line-height: 1;
    letter-spacing: -0.04em;
    margin-bottom: 1.5rem;
    transition: color 0.4s ease;
}
.problem-panel:hover .problem-panel-num {
    color: rgba(255,255,255,0.12);
}

.problem-panel-title {
    font-family: var(--font-serif);
    font-size: clamp(1.1rem, 1.5vw, 1.35rem);
    font-weight: 700;
    color: #fff;
    line-height: 1.3;
    margin: 0 0 1rem;
}

.problem-panel-text {
    font-size: clamp(0.85rem, 1vw, 0.95rem);
    line-height: 1.65;
    color: rgba(255,255,255,0.5);
    margin: 0;
    flex-grow: 1;
}

/* ── MOBILE STACK ── */
@media (max-width: 768px) {
    .problem-stats-row {
        grid-template-columns: 1fr;
    }
    .problem-panels {
        grid-template-columns: 1fr;
    }
    .problem-stat-card {
        text-align: left;
    }
    .problem-stat-num {
        font-size: 3rem;
    }
}
"""

if '.problem-dark-panel' not in css:
    css += PROBLEM_CSS
    print('[CSS] Added dark cinematic problem section styles')
else:
    print('[CSS] Problem section styles already exist')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bust
for page in os.listdir(ROOT):
    if page.endswith('.html'):
        path = os.path.join(ROOT, page)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'\?v=\d+"', '?v=37"', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print('[DONE] Problem section redesign complete, cache v37')
