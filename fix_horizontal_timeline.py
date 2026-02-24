"""
Convert Journey timeline from vertical 2-column grid to HORIZONTAL scrollable strip.
- Replace .mc-grid CSS from grid to horizontal flex with scroll-snap
- Cards become fixed-width side-by-side panels
- A connecting progress line runs horizontally across all cards
"""
import os, re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the mc-grid and mc-card styles for horizontal layout
OLD_GRID = """/* ── Dashboard grid ── */
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
}"""

NEW_GRID = """/* ── Horizontal scrollable dashboard ── */
.mc-grid {
    display: flex;
    gap: 1px;
    background: rgba(255,255,255,0.06);
    border-radius: 12px;
    overflow-x: auto;
    overflow-y: hidden;
    position: relative;
    z-index: 1;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    padding-bottom: 0;
}
.mc-grid::-webkit-scrollbar { display: none; }

/* Horizontal connecting line behind all cards */
.mc-grid::before {
    content: '';
    position: absolute;
    top: 28px;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, #22c55e 0%, #22c55e 35%, #f59e0b 50%, #3b82f6 70%, rgba(255,255,255,0.15) 100%);
    z-index: 0;
    pointer-events: none;
}"""

OLD_CARD = """/* ── Individual cards ── */
.mc-card {
    background: rgba(255,255,255,0.02);
    padding: clamp(1.25rem, 2.5vw, 2rem);
    display: flex;
    flex-direction: column;
    transition: background 0.4s ease;
}
.mc-card:hover {
    background: rgba(255,255,255,0.05);
}"""

NEW_CARD = """/* ── Individual cards — fixed width horizontal ── */
.mc-card {
    background: rgba(255,255,255,0.02);
    padding: clamp(1.25rem, 2vw, 1.75rem);
    display: flex;
    flex-direction: column;
    transition: background 0.4s ease, transform 0.3s ease;
    min-width: 260px;
    max-width: 280px;
    flex-shrink: 0;
    scroll-snap-align: start;
    position: relative;
    z-index: 1;
}
.mc-card:hover {
    background: rgba(255,255,255,0.06);
    transform: translateY(-4px);
}"""

# Also fix mobile — keep horizontal but allow smaller cards
OLD_MOBILE = """/* ── Mobile: single column ── */
@media (max-width: 768px) {
    .mc-grid {
        grid-template-columns: 1fr;
    }
    .mc-dashboard {
        border-radius: 14px;
        padding: 1.25rem;
    }
}"""

NEW_MOBILE = """/* ── Mobile: horizontal scroll with smaller cards ── */
@media (max-width: 768px) {
    .mc-grid {
        gap: 1px;
    }
    .mc-card {
        min-width: 220px;
        max-width: 240px;
    }
    .mc-dashboard {
        border-radius: 14px;
        padding: 1rem;
    }
    .mc-progress-label {
        font-size: 0.5rem;
    }
}"""

css = css.replace(OLD_GRID, NEW_GRID)
css = css.replace(OLD_CARD, NEW_CARD)
css = css.replace(OLD_MOBILE, NEW_MOBILE)

print('[CSS] Converted mc-grid to horizontal scrollable layout')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bust
for page in os.listdir(ROOT):
    if page.endswith('.html'):
        path = os.path.join(ROOT, page)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'\?v=\d+"', '?v=40"', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print('[DONE] Horizontal layout applied, cache v40')
