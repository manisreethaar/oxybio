import codecs
import re

with codecs.open('e:\\OXYBIO\\index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Reduce the height of the pinned-solution-wrapper from 400vh to 250vh (much faster scroll)
html = html.replace('id="pinned-solution-wrapper" style="position:relative; height:400vh;', 'id="pinned-solution-wrapper" style="position:relative; height:250vh;')

# 2. Update the javascript scroll calculation logic to run faster through the slides
old_js = """                        let activeIndex = 0;
                        if(scrollProgress >= 0.33 && scrollProgress < 0.66) activeIndex = 1;
                        if(scrollProgress >= 0.66) activeIndex = 2;"""

new_js = """                        let activeIndex = 0;
                        if(scrollProgress >= 0.33 && scrollProgress < 0.66) activeIndex = 1;
                        if(scrollProgress >= 0.66) activeIndex = 2;"""
html = html.replace(old_js, new_js)

# 3. Increase the width of the cards from a narrow stack to a wide, premium 2-column grid
# We find: class="mobile-stack-card" inside the slides
old_card_style = '<div style=" display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:start;" class="mobile-stack-card">'
# We want the text on left, and the visual lockup on right to stretch across the container
new_card_style = '<div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:4rem; align-items:center;" class="mobile-stack-card">'
html = html.replace(old_card_style, new_card_style)

# 4. Make the text bigger and more spread out to take up horizontal width beautifully
old_p = '<p style="font-size:var(--text-base); line-height:1.7; color:var(--text-muted); margin-bottom:1.5rem;">'
new_p = '<p style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">'
html = html.replace(old_p, new_p)

# We also want to increase the size of the 01/02/03 lists slightly to fill the grid horizontally
html = html.replace('font-size:0.9rem; color:var(--text-main);', 'font-size:1rem; color:var(--text-main); line-height:1.6;')

# 5. Bring the fixed header "So we built one. Meet Oxygen" OUT of the sticky container and let it just sit above the sticky section 
# This removes the weird "empty top" space inside the sticky frame where the header takes up 20% of the screen permanently
old_header_block = '''                    <!-- Fixed Header inside sticky -->
                    <div class="container" style="padding-top:8vh; flex-shrink:0; position:relative; z-index:10;">
                        <div class="section-label">
                            <div class="section-label-line"></div>
                            <span class="section-label-text">The Solution</span>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:2rem; flex-wrap:wrap;">
                            <div style="max-width:800px;">
                                <h2 class="headline" style="margin-top:var(--space-sm);">So we built one. Meet Oxygen.</h2>
                                <p class="subtext editorial-col" style="margin-top:var(--space-sm);">Three precision formulas. Each scientifically designed for a specific need. All built on the same uncompromising foundation: Indian ingredients, active nutrient forms, and doses that actually work.</p>
                            </div>
                        </div>
                    </div>'''

# We remove it from inside <div class="sticky-product-container">
html = html.replace(old_header_block, "")

# And we insert it ABOVE the sticky section wrapper, as a standard section block so the sticky container only has the changing cards inside it
new_header_outside = '''
            <style>
            #pinned-solution-intro { padding: 8rem 0 4rem; background: var(--bg-alt); border-top: 1px solid var(--border); }
            </style>
            <section id="pinned-solution-intro">
                <div class="container">
                        <div class="section-label">
                            <div class="section-label-line"></div>
                            <span class="section-label-text">The Solution</span>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:2rem; flex-wrap:wrap;">
                            <div style="max-width:800px;">
                                <h2 class="headline" style="margin-top:var(--space-sm);">So we built one. Meet Oxygen.</h2>
                                <p class="subtext" style="font-size: 1.15rem; line-height: 1.8; color: var(--text-muted); margin-top:var(--space-sm); max-width:800px;">Three precision formulas. Each scientifically designed for a specific need. All built on the same uncompromising foundation: Indian ingredients, active nutrient forms, and doses that actually work.</p>
                            </div>
                        </div>
                </div>
            </section>
'''

html = html.replace('<section id="pinned-solution-wrapper"', new_header_outside + '\n            <!-- Added via python to fix spacing -->\n            <section id="pinned-solution-wrapper"')

# Also remove the border-top from the wrapper since it's on the intro now
html = html.replace('id="pinned-solution-wrapper" style="position:relative; height:250vh; background:var(--bg-alt); border-top:1px solid var(--border);"',
                    'id="pinned-solution-wrapper" style="position:relative; height:250vh; background:var(--bg-alt);"')

# Update sticky container height mathematically
html = html.replace('class="sticky-product-container" style="position:sticky; top:0; height:100vh; display:flex; flex-direction:column; overflow:hidden;"',
                    'class="sticky-product-container" style="position:sticky; top:120px; height:calc(100vh - 120px); display:flex; flex-direction:column; overflow:hidden;"')


with codecs.open('e:\\OXYBIO\\index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Apple scroll layout widened and mathematically optimized.")
