import re

with open('e:\\OXYBIO\\careers.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: The blank space is caused by margin-bottom: 100vh. We just need normal layout gaps if we want them to stack sticky.
# Changing margin-bottom: 100vh to margin-bottom: 2rem.
html = html.replace('margin-bottom: 100vh; /* Extremely tall margin ensures the card scrolls fully before the next one hits */', 
                    'margin-bottom: 60vh; /* Allow generous scroll time per card, but not completely blank */')

# Actually, 60vh might still show a blank gap. Let's just use normal margin, since we want them to stack immediately like a deck!
html = html.replace('margin-bottom: 60vh; /* Allow generous scroll time per card, but not completely blank */', 
                    'margin-bottom: 2rem;')
# Try another replace just in case 100vh is still there
html = html.replace('margin-bottom: 100vh;', 'margin-bottom: 2rem;')

# Fix 2: "Join Our Mission" is hidden under header. 
# It currently has style="padding-top:160px;..." Let's increase it to 200px and add a specific margin.
html = html.replace('style="padding-top:160px; padding-bottom:100px; background:var(--bg); border-bottom:1px solid var(--border); position:relative; overflow:hidden;"', 
                    'style="padding-top:180px; padding-bottom:100px; background:var(--bg); border-bottom:1px solid var(--border); position:relative; overflow:hidden;"')

# Let's also wrap the badge in a div with a mobile-specific class for top margin just to be safe.
# Actually, I can just add `margin-top: 2rem;` to the `.badge`.
html = html.replace('<div class="badge"\n                        style="margin-bottom:var(--space-lg); border-color:var(--text-main); color:var(--text-main); background:transparent;">\n                        Join Our Mission</div>',
                    '<div class="badge hero-badge-mobile-fix"\n                        style="margin-bottom:var(--space-lg); margin-top:3rem; border-color:var(--text-main); color:var(--text-main); background:transparent;">\n                        Join Our Mission</div>')

# Ensure cache is bumped to 18
html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=18"', html)

with open('e:\\OXYBIO\\careers.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Careers HTML patched (100vh removed, hero padding increased).")

