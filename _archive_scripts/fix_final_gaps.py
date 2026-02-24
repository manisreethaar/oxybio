import codecs
import re

with codecs.open('e:\\OXYBIO\\index.html', 'r', 'utf-8') as f:
    html = f.read()

# =========================================================
# FIX 1: GAP BETWEEN TRANSPARENCY TABLE AND BLACK CTA
# =========================================================
# The bottom of the transparency section currently has no margin. 
# We need to add margin-bottom to the final container of the duel section.
old_duel_container = '<div class="container"\n                    style="border:1px solid var(--border); border-top:none; border-radius:0 0 20px 20px; overflow:hidden;">'
new_duel_container = '<div class="container"\n                    style="border:1px solid var(--border); border-top:none; border-radius:0 0 20px 20px; overflow:hidden; margin-bottom: 6rem;">'

if old_duel_container not in html:
    # try variations
    old_duel_container = 'style="border:1px solid var(--border); border-top:none; border-radius:0 0 20px 20px; overflow:hidden;"'
    new_duel_container = 'style="border:1px solid var(--border); border-top:none; border-radius:0 0 20px 20px; overflow:hidden; margin-bottom: 6rem;"'

html = html.replace(old_duel_container, new_duel_container)


# =========================================================
# FIX 2: HUGE GAP ABOVE PRODUCTS IN THE APPLE SCROLL SECTION
# =========================================================
# The JS and CSS are currently using top:50%; transform:translateY(-50%) to vertically center the products in the space.
# We will rip out this centering logic and force them to pin directly to the TOP of the container, killing the white space.

# 1. Sticky container - make it push up tighter
html = html.replace('style="position:sticky; top:120px; min-height: 60vh; max-height:85vh; padding-top:0rem; padding-bottom:2rem; display:flex; flex-direction:column; overflow:hidden;"',
                    'style="position:sticky; top:40px; min-height: 40vh; max-height:85vh; padding-top:0rem; padding-bottom:0rem; display:flex; flex-direction:column; overflow:hidden;"')

html = html.replace('<section id="pinned-solution-wrapper" style="position:relative; height:250vh; background:var(--bg-alt);">',
                    '<section id="pinned-solution-wrapper" style="position:relative; height:200vh; background:var(--bg-alt);">')

# 2. Fix the initial CSS transform styles on the 3 slides
html = html.replace('style="position:absolute; width:100%; top:50%; transform:translateY(-50%); opacity:1; transition:opacity 0.6s ease, transform 0.6s ease;"',
                    'style="position:absolute; width:100%; top:0; transform:translateY(0); opacity:1; transition:opacity 0.4s ease, transform 0.4s ease;"')

html = html.replace('style="position:absolute; width:100%; top:50%; transform:translateY(-30%); opacity:0; pointer-events:none; transition:opacity 0.6s ease, transform 0.6s ease;"',
                    'style="position:absolute; width:100%; top:0; transform:translateY(20px); opacity:0; pointer-events:none; transition:opacity 0.4s ease, transform 0.4s ease;"')

# 3. Update the Javascript that handles the scroll animation to stop pushing it to -50%
old_js_1 = "slide.style.transform = 'translateY(-50%)';"
new_js_1 = "slide.style.transform = 'translateY(0)';"
html = html.replace(old_js_1, new_js_1)

old_js_2 = "slide.style.transform = 'translateY(-70%)';"
new_js_2 = "slide.style.transform = 'translateY(-20px)';"
html = html.replace(old_js_2, new_js_2)

old_js_3 = "slide.style.transform = 'translateY(-30%)';"
new_js_3 = "slide.style.transform = 'translateY(20px)';"
html = html.replace(old_js_3, new_js_3)


with codecs.open('e:\\OXYBIO\\index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Exact spacing metrics applied successfully.")
