"""
Add Phase Stepper CSS + cache bust
"""
import os, re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

STEPPER_CSS = """
/* ═══════════════════════════════════════════════════════
   PHASE STEPPER — Horizontal clickable journey
   ═══════════════════════════════════════════════════════ */
.phase-stepper {
    position: relative;
}

/* ── Track: horizontal row of nodes ── */
.phase-track {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    position: relative;
    padding: 0 0.5rem;
    margin-bottom: 2rem;
}

/* Connecting line behind nodes */
.phase-line {
    position: absolute;
    top: 20px;
    left: 30px;
    right: 30px;
    height: 2px;
    background: var(--border);
    z-index: 0;
}
.phase-line-fill {
    height: 100%;
    width: 45%;
    background: linear-gradient(90deg, #22c55e 0%, #f59e0b 70%, #3b82f6 100%);
    border-radius: 2px;
    transition: width 0.6s ease;
}

/* ── Individual node button ── */
.phase-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    background: none;
    border: none;
    cursor: pointer;
    position: relative;
    z-index: 1;
    padding: 0;
    outline: none;
}

.phase-node-num {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    border: 2px solid var(--border);
    background: var(--bg);
    color: var(--text-muted);
}

.phase-node-label {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    transition: color 0.3s ease;
    white-space: nowrap;
}

/* Status variants */
.phase-node-done .phase-node-num {
    background: #22c55e;
    border-color: #22c55e;
    color: #fff;
}
.phase-node-wip .phase-node-num {
    border-color: #f59e0b;
    color: #f59e0b;
    animation: phaseGlow 2s ease-in-out infinite;
}
.phase-node-active .phase-node-num {
    border-color: #3b82f6;
    color: #3b82f6;
    animation: phaseGlow 1.5s ease-in-out infinite;
}
.phase-node-pending .phase-node-num {
    border-color: var(--border);
    color: var(--text-muted);
    opacity: 0.5;
}

@keyframes phaseGlow {
    0%, 100% { box-shadow: 0 0 0px transparent; }
    50% { box-shadow: 0 0 12px rgba(59,130,246,0.3); }
}
.phase-node-wip .phase-node-num {
    animation-name: phaseGlowAmber;
}
@keyframes phaseGlowAmber {
    0%, 100% { box-shadow: 0 0 0px transparent; }
    50% { box-shadow: 0 0 12px rgba(245,158,11,0.3); }
}

/* Active (selected) state — ring + scale */
.phase-node.is-active .phase-node-num {
    transform: scale(1.2);
    box-shadow: 0 0 0 4px rgba(13,138,116,0.15);
}
.phase-node.is-active .phase-node-label {
    color: var(--text-main);
    font-weight: 600;
}

/* Hover */
.phase-node:hover .phase-node-num {
    transform: scale(1.1);
}

/* ── Detail panel area ── */
.phase-details {
    position: relative;
    min-height: 160px;
}

.phase-detail {
    position: absolute;
    inset: 0;
    opacity: 0;
    visibility: hidden;
    transform: translateY(8px);
    transition: opacity 0.35s ease, transform 0.35s ease, visibility 0.35s ease;
    background: var(--bg-alt);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: clamp(1.25rem, 2vw, 2rem);
}
.phase-detail.is-visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
    position: relative;
}

.phase-detail-badge {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    padding: 0.25rem 0.6rem;
    border-radius: 50px;
    margin-bottom: 0.75rem;
}
.phase-badge-green { background: rgba(34,197,94,0.12); color: #22c55e; }
.phase-badge-amber { background: rgba(245,158,11,0.12); color: #f59e0b; }
.phase-badge-blue  { background: rgba(59,130,246,0.12); color: #3b82f6; }
.phase-badge-grey  { background: rgba(0,0,0,0.06); color: var(--text-muted); }

.phase-detail-title {
    font-family: var(--font-serif);
    font-size: clamp(1.2rem, 2vw, 1.5rem);
    font-weight: 800;
    color: var(--text-main);
    line-height: 1.25;
    margin: 0 0 0.75rem;
}

.phase-detail-text {
    font-size: 0.95rem;
    line-height: 1.65;
    color: var(--text-muted);
    margin: 0 0 1rem;
    max-width: 600px;
}

/* Stat line for completed phases */
.phase-detail-stat {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    display: flex;
    align-items: baseline;
    gap: 0.4rem;
}
.phase-stat-num {
    font-family: var(--font-serif);
    font-size: 1.5rem;
    font-weight: 900;
    color: #22c55e;
    letter-spacing: -0.02em;
}

/* Mini progress bar for in-progress phases */
.phase-detail-bar {
    height: 4px;
    background: var(--border);
    border-radius: 4px;
    overflow: hidden;
    max-width: 300px;
}
.phase-detail-bar-fill {
    height: 100%;
    background: #f59e0b;
    border-radius: 4px;
    transition: width 1s ease;
}
.phase-bar-blue { background: #3b82f6; }
.phase-bar-grey { background: var(--text-muted); opacity: 0.4; }

/* ── Mobile ── */
@media (max-width: 768px) {
    .phase-node-num {
        width: 34px;
        height: 34px;
        font-size: 0.6rem;
    }
    .phase-node-label {
        font-size: 0.5rem;
    }
    .phase-track {
        padding: 0;
    }
    .phase-line {
        left: 20px;
        right: 20px;
        top: 17px;
    }
}
"""

if '.phase-stepper' not in css:
    css += STEPPER_CSS
    print('[CSS] Added Phase Stepper styles')
else:
    print('[CSS] Phase Stepper styles already present')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bust
for page in os.listdir(ROOT):
    if page.endswith('.html'):
        path = os.path.join(ROOT, page)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'\?v=\d+"', '?v=41"', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print('[DONE] Phase Stepper deployed, cache v41')
