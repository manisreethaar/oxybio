"""
Fix Phase Stepper:
1. Remove vacuum space — detail panels use absolute positioning creating phantom height.
   Fix by making .phase-details have a fixed min-height and panels use display:none/block
2. Monochrome palette — replace all color dots (green/amber/blue) with var(--text-main) black/grey
3. Auto-scroll — JS cycles through phases every 3s, pauses on hover
"""
import os, re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# ── Remove the old phase stepper CSS block and replace it entirely ──
OLD = css[css.find('/* ═'*1 + '══════════════════════════════════════\n   PHASE STEPPER'):css.find('/* ── Mobile ── */\n@media (max-width: 768px) {\n    .phase-node-num {\n        width: 34px;')]

# Simpler approach — just find and replace the relevant color declarations
replacements = [
    # Dot colors → monochrome
    ('.mc-dot-green {\n    background: #22c55e;\n    box-shadow: 0 0 8px rgba(34,197,94,0.5);\n}',
     '.mc-dot-green {\n    background: var(--text-main);\n}'),
    ('.mc-dot-amber {\n    background: #f59e0b;\n    box-shadow: 0 0 8px rgba(245,158,11,0.5);\n    animation: mcDotPulse 2s ease-in-out infinite;\n}',
     '.mc-dot-amber {\n    background: var(--text-main);\n    opacity: 0.6;\n}'),
    ('.mc-dot-blue {\n    background: #3b82f6;\n    box-shadow: 0 0 8px rgba(59,130,246,0.5);\n    animation: mcDotPulse 1.5s ease-in-out infinite;\n}',
     '.mc-dot-blue {\n    background: var(--text-main);\n    opacity: 0.4;\n}'),
    # Phase node status → monochrome
    ('.phase-node-done .phase-node-num {\n    background: #22c55e;\n    border-color: #22c55e;\n    color: #fff;\n}',
     '.phase-node-done .phase-node-num {\n    background: var(--text-main);\n    border-color: var(--text-main);\n    color: var(--bg);\n}'),
    ('.phase-node-wip .phase-node-num {\n    border-color: #f59e0b;\n    color: #f59e0b;\n    animation: phaseGlow 2s ease-in-out infinite;\n}',
     '.phase-node-wip .phase-node-num {\n    border-color: var(--text-main);\n    color: var(--text-main);\n    opacity: 0.65;\n}'),
    ('.phase-node-active .phase-node-num {\n    border-color: #3b82f6;\n    color: #3b82f6;\n    animation: phaseGlow 1.5s ease-in-out infinite;\n}',
     '.phase-node-active .phase-node-num {\n    border-color: var(--text-main);\n    color: var(--text-main);\n    opacity: 0.45;\n}'),
    # Phase node active ring → monochrome
    ('.phase-node.is-active .phase-node-num {\n    transform: scale(1.2);\n    box-shadow: 0 0 0 4px rgba(13,138,116,0.15);\n}',
     '.phase-node.is-active .phase-node-num {\n    transform: scale(1.2);\n    box-shadow: 0 0 0 4px rgba(0,0,0,0.1);\n}'),
    # Badge colors → monochrome
    ('.phase-badge-green { background: rgba(34,197,94,0.12); color: #22c55e; }',
     '.phase-badge-green { background: var(--bg-alt); color: var(--text-main); border: 1px solid var(--border); }'),
    ('.phase-badge-amber { background: rgba(245,158,11,0.12); color: #f59e0b; }',
     '.phase-badge-amber { background: var(--bg-alt); color: var(--text-muted); border: 1px solid var(--border); }'),
    ('.phase-badge-blue  { background: rgba(59,130,246,0.12); color: #3b82f6; }',
     '.phase-badge-blue  { background: var(--bg-alt); color: var(--text-muted); border: 1px solid var(--border); }'),
    # Stat number → monochrome
    ('.phase-stat-num {\n    font-family: var(--font-serif);\n    font-size: 1.5rem;\n    font-weight: 900;\n    color: #22c55e;\n    letter-spacing: -0.02em;\n}',
     '.phase-stat-num {\n    font-family: var(--font-serif);\n    font-size: 1.5rem;\n    font-weight: 900;\n    color: var(--text-main);\n    letter-spacing: -0.02em;\n}'),
    # Progress bar fill → monochrome
    ('.phase-detail-bar-fill {\n    height: 100%;\n    background: #f59e0b;\n    border-radius: 4px;\n    transition: width 1s ease;\n}',
     '.phase-detail-bar-fill {\n    height: 100%;\n    background: var(--text-main);\n    border-radius: 4px;\n    transition: width 1s ease;\n    opacity: 0.4;\n}'),
    ('.phase-bar-blue { background: #3b82f6; }',
     '.phase-bar-blue { background: var(--text-main); opacity: 0.25; }'),
    # Phase line fill → single dark stroke
    ('.phase-line-fill {\n    height: 100%;\n    width: 45%;\n    background: linear-gradient(90deg, #22c55e 0%, #f59e0b 70%, #3b82f6 100%);\n    border-radius: 2px;\n    transition: width 0.6s ease;\n}',
     '.phase-line-fill {\n    height: 100%;\n    width: 45%;\n    background: var(--text-main);\n    border-radius: 2px;\n    transition: width 0.6s ease;\n}'),
    # mc-progress-fill → monochrome
    ('.mc-progress-fill {\n    height: 100%;\n    background: linear-gradient(90deg, #22c55e 0%, #0D8A74 60%, #3b82f6 100%);\n    border-radius: 4px;\n    position: relative;\n    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);\n}',
     '.mc-progress-fill {\n    height: 100%;\n    background: var(--text-main);\n    border-radius: 4px;\n    position: relative;\n    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);\n}'),
    # Remove the glow on mc-progress-fill::after
    ('/* Glowing tip */\n.mc-progress-fill::after {\n    content: \'\';\n    position: absolute;\n    right: -3px;\n    top: -4px;\n    width: 12px;\n    height: 12px;\n    background: #3b82f6;\n    border-radius: 50%;\n    box-shadow: 0 0 12px rgba(59,130,246,0.6), 0 0 4px rgba(59,130,246,0.8);\n    animation: mcPulse 2s ease-in-out infinite;\n}',
     '/* Tip dot */\n.mc-progress-fill::after {\n    content: \'\';\n    position: absolute;\n    right: -4px;\n    top: -4px;\n    width: 12px;\n    height: 12px;\n    background: var(--text-main);\n    border-radius: 50%;\n}'),
    # mc metric num → monochrome
    ('.mc-metric-num {\n    font-family: var(--font-serif);\n    font-size: 1.75rem;\n    font-weight: 900;\n    color: #22c55e;\n    letter-spacing: -0.03em;\n}',
     '.mc-metric-num {\n    font-family: var(--font-serif);\n    font-size: 1.75rem;\n    font-weight: 900;\n    color: var(--text-main);\n    letter-spacing: -0.03em;\n}'),
    # proof dot → monochrome  
    ('.proof-dot {\n    width: 6px;\n    height: 6px;\n    border-radius: 50%;\n    background: #0D8A74;\n    display: inline-block;\n    animation: proofPulse 2s ease-in-out infinite;\n}',
     '.proof-dot {\n    width: 6px;\n    height: 6px;\n    border-radius: 50%;\n    background: var(--text-main);\n    display: inline-block;\n    opacity: 0.5;\n}'),
]

for old, new in replacements:
    if old in css:
        css = css.replace(old, new)
        print(f'[CSS] Replaced: {old[:60].strip()[:50]}...')
    else:
        print(f'[MISS] Not found: {old[:60].strip()[:50]}...')

# ── Fix the vacuum: switch .phase-detail from absolute to display:none ──
css = css.replace(
    '.phase-detail {\n    position: absolute;\n    inset: 0;\n    opacity: 0;\n    visibility: hidden;\n    transform: translateY(8px);\n    transition: opacity 0.35s ease, transform 0.35s ease, visibility 0.35s ease;\n    background: var(--bg-alt);\n    border: 1px solid var(--border);\n    border-radius: 16px;\n    padding: clamp(1.25rem, 2vw, 2rem);\n}',
    '.phase-detail {\n    display: none;\n    background: var(--bg-alt);\n    border: 1px solid var(--border);\n    border-radius: 16px;\n    padding: clamp(1.25rem, 2vw, 2rem);\n    animation: fadeSlideUp 0.35s ease;\n}'
)
css = css.replace(
    '.phase-detail.is-visible {\n    opacity: 1;\n    visibility: visible;\n    transform: translateY(0);\n    position: relative;\n}',
    '.phase-detail.is-visible {\n    display: block;\n}'
)
# ── Remove .phase-details min-height ──
css = css.replace(
    '.phase-details {\n    position: relative;\n    min-height: 160px;\n}',
    '.phase-details {\n    position: relative;\n}'
)

# Add fadeSlideUp keyframe if not present
if 'fadeSlideUp' not in css:
    css += """
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
"""

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)
print('[CSS] All monochrome replacements done + vacuum fix')

# ── Update the inline JS to add auto-scroll ──
ABOUT = os.path.join(ROOT, 'about.html')
with open(ABOUT, 'r', encoding='utf-8') as f:
    html = f.read()

OLD_JS = """                            <script>
                            (function() {
                                document.querySelectorAll('.phase-node').forEach(function(btn) {
                                    btn.addEventListener('click', function() {
                                        var phase = this.getAttribute('data-phase');
                                        document.querySelectorAll('.phase-node').forEach(function(n) { n.classList.remove('is-active'); });
                                        btn.classList.add('is-active');
                                        document.querySelectorAll('.phase-detail').forEach(function(d) { d.classList.remove('is-visible'); });
                                        document.querySelector('.phase-detail[data-detail="' + phase + '"]').classList.add('is-visible');
                                    });
                                });
                            })();
                            </script>"""

NEW_JS = """                            <script>
                            (function() {
                                var nodes = document.querySelectorAll('.phase-node');
                                var details = document.querySelectorAll('.phase-detail');
                                var current = 0;
                                var autoTimer = null;

                                function showPhase(idx) {
                                    nodes.forEach(function(n) { n.classList.remove('is-active'); });
                                    details.forEach(function(d) { d.classList.remove('is-visible'); });
                                    nodes[idx].classList.add('is-active');
                                    details[idx].classList.add('is-visible');
                                    current = idx;
                                }

                                function startAuto() {
                                    autoTimer = setInterval(function() {
                                        current = (current + 1) % nodes.length;
                                        showPhase(current);
                                    }, 3000);
                                }

                                function stopAuto() {
                                    clearInterval(autoTimer);
                                }

                                // Click handler
                                nodes.forEach(function(btn, idx) {
                                    btn.addEventListener('click', function() {
                                        stopAuto();
                                        showPhase(idx);
                                        startAuto(); // restart timer from this point
                                    });
                                });

                                // Pause on hover
                                var stepper = document.querySelector('.phase-stepper');
                                if (stepper) {
                                    stepper.addEventListener('mouseenter', stopAuto);
                                    stepper.addEventListener('mouseleave', startAuto);
                                }

                                showPhase(0);
                                startAuto();
                            })();
                            </script>"""

if OLD_JS in html:
    html = html.replace(OLD_JS, NEW_JS)
    print('[JS] Auto-scroll injected')
else:
    print('[MISS] JS block not found exactly')

# cache bust
html = re.sub(r'\?v=\d+"', '?v=42"', html)
with open(ABOUT, 'w', encoding='utf-8') as f:
    f.write(html)

# cache bust other pages
for page in os.listdir(ROOT):
    if page.endswith('.html') and page != 'about.html':
        path = os.path.join(ROOT, page)
        with open(path, 'r', encoding='utf-8') as f:
            h = f.read()
        h = re.sub(r'\?v=\d+"', '?v=42"', h)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(h)

print('[DONE] v42')
