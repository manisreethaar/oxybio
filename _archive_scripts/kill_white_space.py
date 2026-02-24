import codecs
import re

with codecs.open('e:\\OXYBIO\\index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. TIGHTEN: "So we built one. Meet Oxygen." Section. 
# It currently has `padding: 8rem 0 4rem;` which is massive padding on top and bottom.
# We will change it to `padding: 4rem 0 0rem;` so it sits tighter below the Problem and pushes directly onto the Product cards.
html = html.replace('#pinned-solution-intro { padding: 8rem 0 4rem; background: var(--bg-alt); border-top: 1px solid var(--border); }',
                    '#pinned-solution-intro { padding: 4rem 0 0rem; background: var(--bg-alt); border-top: 1px solid var(--border); }')

# 2. TIGHTEN: The Apple Slide sticky container.
# Currently it uses `height:calc(100vh - 120px)`. On massive desktop screens, this creates crazy empty space above and below the content.
# Let's change it to `min-height: 80vh;` and adjust the flex-alignment so the content stays perfectly vertically centered without stretching to 100% of the screen height if not needed.
html = html.replace('class="sticky-product-container" style="position:sticky; top:120px; height:calc(100vh - 120px); display:flex; flex-direction:column; overflow:hidden;"',
                    'class="sticky-product-container" style="position:sticky; top:120px; min-height: 70vh; max-height:85vh; padding-top:2rem; padding-bottom:2rem; display:flex; flex-direction:column; overflow:hidden;"')


# 3. TIGHTEN: The Transparency Section (Oxygen vs the market) to CTA Section
# The user noted huge white space below the transparency table.
# The table section has `padding: 0;` but then the bottom of it is completely empty before the black CTA. Let's look at the structure.
# The "Science & Pillars" section has `padding: 6rem 0; margin-bottom: 4rem;` which creates huge gaps.
html = html.replace('<section style="padding: 6rem 0; border-bottom:1px solid var(--border);">',
                    '<section style="padding: 4rem 0; border-bottom:1px solid var(--border);">')

# Let's reduce margin-bottom on the 3 split headers and science cards
html = html.replace('margin-bottom:4rem;"', 'margin-bottom:2rem;"')
html = html.replace('padding-top:4rem; padding-bottom:2.5rem;"', 'padding-top:2rem; padding-bottom:1.5rem;"')


with codecs.open('e:\\OXYBIO\\index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Massive white-space purge complete. Layout is mathematically compacted.")
