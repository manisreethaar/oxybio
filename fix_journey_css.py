"""
Add Mission Control Dashboard CSS to styles.css + cache bust
"""
import os, re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

MC_CSS = """
/* ═══════════════════════════════════════════════════════
   MISSION CONTROL DASHBOARD — Journey Timeline
   ═══════════════════════════════════════════════════════ */
.mc-dashboard {
    background: #0a0a0a;
    border-radius: 20px;
    padding: clamp(1.5rem, 3vw, 2.5rem);
    position: relative;
    overflow: hidden;
}

/* Subtle scan-line overlay */
.mc-dashboard::before {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(255,255,255,0.01) 2px,
        rgba(255,255,255,0.01) 4px
    );
    pointer-events: none;
    z-index: 0;
}

/* ── Top progress bar ── */
.mc-progress-track {
    position: relative;
    height: 4px;
    background: rgba(255,255,255,0.08);
    border-radius: 4px;
    margin-bottom: 2rem;
    overflow: visible;
}

.mc-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #22c55e 0%, #0D8A74 60%, #3b82f6 100%);
    border-radius: 4px;
    position: relative;
    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Glowing tip */
.mc-progress-fill::after {
    content: '';
    position: absolute;
    right: -3px;
    top: -4px;
    width: 12px;
    height: 12px;
    background: #3b82f6;
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(59,130,246,0.6), 0 0 4px rgba(59,130,246,0.8);
    animation: mcPulse 2s ease-in-out infinite;
}

@keyframes mcPulse {
    0%, 100% { box-shadow: 0 0 8px rgba(59,130,246,0.4); transform: scale(1); }
    50% { box-shadow: 0 0 20px rgba(59,130,246,0.8); transform: scale(1.2); }
}

.mc-progress-label {
    position: absolute;
    right: 0;
    top: 12px;
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.2em;
    color: rgba(255,255,255,0.35);
}

/* ── Dashboard grid ── */
.mc-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1px;
    background: rgba(255,255,255,0.06);
    border-radius: 12px;
    overflow: hidden;
    position: relative;
    z-index: 1;
}

/* Last card spans full width if odd */
.mc-grid .mc-card:last-child:nth-child(odd) {
    grid-column: 1 / -1;
}

/* ── Individual cards ── */
.mc-card {
    background: rgba(255,255,255,0.02);
    padding: clamp(1.25rem, 2.5vw, 2rem);
    display: flex;
    flex-direction: column;
    transition: background 0.4s ease;
}
.mc-card:hover {
    background: rgba(255,255,255,0.05);
}

/* Card header row */
.mc-card-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

/* Status dot */
.mc-status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}
.mc-dot-green {
    background: #22c55e;
    box-shadow: 0 0 8px rgba(34,197,94,0.5);
}
.mc-dot-amber {
    background: #f59e0b;
    box-shadow: 0 0 8px rgba(245,158,11,0.5);
    animation: mcDotPulse 2s ease-in-out infinite;
}
.mc-dot-blue {
    background: #3b82f6;
    box-shadow: 0 0 8px rgba(59,130,246,0.5);
    animation: mcDotPulse 1.5s ease-in-out infinite;
}
.mc-dot-grey {
    background: rgba(255,255,255,0.3);
}

@keyframes mcDotPulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

/* Phase label */
.mc-phase {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.15em;
    color: rgba(255,255,255,0.35);
}

/* Status badge */
.mc-badge {
    font-family: var(--font-mono);
    font-size: 0.55rem;
    letter-spacing: 0.12em;
    padding: 0.2rem 0.5rem;
    border-radius: 50px;
    margin-left: auto;
}
.mc-badge-green { background: rgba(34,197,94,0.15); color: #22c55e; }
.mc-badge-amber { background: rgba(245,158,11,0.15); color: #f59e0b; }
.mc-badge-blue  { background: rgba(59,130,246,0.15); color: #3b82f6; }
.mc-badge-grey  { background: rgba(255,255,255,0.08); color: rgba(255,255,255,0.4); }

/* Title */
.mc-title {
    font-family: var(--font-serif);
    font-size: clamp(1rem, 1.5vw, 1.25rem);
    font-weight: 700;
    color: #fff;
    line-height: 1.3;
    margin: 0 0 0.75rem;
}

/* Description */
.mc-desc {
    font-size: clamp(0.8rem, 1vw, 0.9rem);
    line-height: 1.6;
    color: rgba(255,255,255,0.45);
    margin: 0;
    flex-grow: 1;
}

/* Metric block (for completed cards) */
.mc-metric {
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
    margin-top: 1.25rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(255,255,255,0.06);
}

.mc-metric-num {
    font-family: var(--font-serif);
    font-size: 1.75rem;
    font-weight: 900;
    color: #22c55e;
    letter-spacing: -0.03em;
}

.mc-metric-label {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.3);
}

/* Mini progress bar (for in-progress/active/growing cards) */
.mc-mini-bar {
    height: 3px;
    background: rgba(255,255,255,0.08);
    border-radius: 3px;
    margin-top: 1.25rem;
    overflow: hidden;
}
.mc-mini-fill {
    height: 100%;
    background: #f59e0b;
    border-radius: 3px;
    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.mc-fill-blue { background: #3b82f6; }
.mc-fill-grey { background: rgba(255,255,255,0.2); }

/* ── Mobile: single column ── */
@media (max-width: 768px) {
    .mc-grid {
        grid-template-columns: 1fr;
    }
    .mc-dashboard {
        border-radius: 14px;
        padding: 1.25rem;
    }
}
"""

if '.mc-dashboard' not in css:
    css += MC_CSS
    print('[CSS] Added Mission Control Dashboard styles')
else:
    print('[CSS] MC styles already exist')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bust all pages
for page in os.listdir(ROOT):
    if page.endswith('.html'):
        path = os.path.join(ROOT, page)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'\?v=\d+"', '?v=39"', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print('[DONE] Mission Control Dashboard deployed, cache v39')
