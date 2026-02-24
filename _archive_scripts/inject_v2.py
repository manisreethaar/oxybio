import sys

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject CSS (Before styles.css)
css_link = '<link rel="stylesheet" href="assets/css/v2_premium.css?v=1">\n    <link rel="stylesheet" href="assets/css/styles.css?v=11">'
if '<link rel="stylesheet" href="assets/css/styles.css?v=10">' in html:
    html = html.replace('<link rel="stylesheet" href="assets/css/styles.css?v=10">', css_link)
elif '<link rel="stylesheet" href="assets/css/styles.css?v=11">' not in html:
    print("Could not find v10 styles explicitly. Stopping to prevent duplication.")

# 2. Inject JS (Before closing body)
js_link = '<script src="assets/js/v2_premium.js"></script>\n    <!-- Mobile Apple-style Scroll Animation -->'
if '<!-- Mobile Apple-style Scroll Animation -->' in html:
    html = html.replace('<!-- Mobile Apple-style Scroll Animation -->', js_link)

# 3. Add Ambient Glows to Hero
head_wrap = '<div class="container pt-xl">'
new_head_wrap = '<div class="v2-ambient-glow top-right"></div>\n            <div class="v2-ambient-glow bottom-left"></div>\n            <div class="container pt-xl" style="position:relative; z-index:2;">'
if head_wrap in html and 'v2-ambient-glow' not in html:
    html = html.replace(head_wrap, new_head_wrap, 1)

# 4. Turn the Hero button into a Magnetic Button
btn_old = '<a href="science.html" class="btn-primary" style="font-size: 1.1rem; padding: 1rem 2.5rem; border-radius: 100px;">Explore Our Science</a>'
btn_new = '<a href="science.html" class="btn-primary magnetic-btn" style="font-size: 1.1rem; padding: 1rem 2.5rem; border-radius: 100px;"><span class="magnetic-content">Explore Our Science</span></a>'
if btn_old in html:
    html = html.replace(btn_old, btn_new)

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Injected V2 Assets and Magnetic classes into index.html')
