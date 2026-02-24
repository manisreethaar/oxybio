import re

with open('e:\\OXYBIO\\assets\\css\\v2_premium.css', 'a', encoding='utf-8') as f:
    f.write("""
/* 5. CINEMATIC SCROLL SVG MASKS */
.v2-draw-path {
    fill: none;
    stroke: var(--accent); /* Oxygen brand green */
    stroke-width: 2;
    /* JS will calculate and apply stroke-dasharray & offset */
    transition: stroke-dashoffset 0.1s linear; 
}

/* 6. PARALLAX IMAGE MASKS */
.v2-parallax-container {
    overflow: hidden;
    position: relative;
    border-radius: 20px; /* Mathematical precision masks */
    width: 100%;
    height: 100%;
}

.v2-parallax-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transform: scale(1.1); /* Give room for parallax */
    transform-origin: center center;
    will-change: transform;
}
""")

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Verify the js is loaded
if 'v2_scroll.js' not in html:
    html = html.replace('<script src="assets/js/v2_canvas.js', '<script src="assets/js/v2_scroll.js"></script>\n    <script src="assets/js/v2_canvas.js')

# Insert SVG line next to the Transparency Report Title
old_transparency_header = """                        <div>
                            <div
                                style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1rem;">
                                Transparency Report</div>
                            <h2
                                style="font-family:var(--font-serif); font-size:clamp(1.75rem,3.5vw,2.75rem); font-weight:900; color:var(--text-main); line-height:1.1; letter-spacing:-0.03em;">
                                Oxygen vs. the market.<br><em style="font-weight:400; color:var(--text-muted);">You
                                    deserve to see the difference.</em></h2>
                        </div>"""

new_transparency_header = """                        <div style="position:relative;">
                            <svg class="v2-timeline-svg" style="position:absolute; left:-40px; top:10px; height:150%; z-index:-1; overflow:visible;" preserveAspectRatio="none">
                                <path class="v2-draw-path" d="M 0 0 L 0 300" stroke-linecap="round" />
                            </svg>
                            <div
                                style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted); margin-bottom:1rem;">
                                Transparency Report</div>
                            <h2
                                style="font-family:var(--font-serif); font-size:clamp(1.75rem,3.5vw,2.75rem); font-weight:900; color:var(--text-main); line-height:1.1; letter-spacing:-0.03em;">
                                Oxygen vs. the market.<br><em style="font-weight:400; color:var(--text-muted);">You
                                    deserve to see the difference.</em></h2>
                        </div>"""

html = html.replace(old_transparency_header, new_transparency_header)

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Injected V2 Scroll elements into index.html")
