import re
import os

# 1. First, we need to inject the standardized premium badge style into styles.css
css_path = 'e:\\OXYBIO\\assets\\css\\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

premium_badge_css = """
/* --- UNIFIED PREMIUM HERO BADGE --- */
.page-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-main);
    border: 1px solid var(--text-main);
    padding: 0.4rem 0.8rem;
    border-radius: 50px;
    background: transparent;
    margin-bottom: 2rem;
}
"""

if 'UNIFIED PREMIUM HERO BADGE' not in css_content:
    css_content += premium_badge_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Injected .page-hero-badge into styles.css")

# 2. Now process all HTML files to unified the badge and fix blog spacing
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Standardize the badges above H1 tags. 
    # Because there are so many variations, we'll use regex to target the generic structure
    # Match: <div class="badge[anything]" style="...anything...">Text</div>
    # Before replacing broadly, let's target the exact ones we know exist above the heroes by looking near 'class="display"'
    
    # We will look for <div class="badge"... >Text</div> that appears just before an <h1>
    # This regex is a bit risky but we can target the exact known strings from the grep:
    
    replacements = [
        # About
        (r'<div class="badge"\s*style="margin-bottom:var\(--space-md\); border-color:var\(--text-main\); color:var\(--text-main\); background:transparent;">', '<div class="page-hero-badge">'),
        # Blog
        (r'<div class="badge" style="margin-bottom:var\(--space-md\);">Development Journal & Research</div>', '<div class="page-hero-badge">Development Journal & Research</div>'),
        # Careers
        (r'<div class="badge"\s*style="margin-top:2rem; margin-bottom:var\(--space-lg\); border-color:var\(--text-main\); color:var\(--text-main\); background:transparent;">\s*Join Our Mission</div>', '<div class="page-hero-badge" style="margin-top:2rem;">Join Our Mission</div>'),
        # Contact
        (r'<div class="badge" style="margin-bottom:2rem;">Partnerships & Inquiries</div>', '<div class="page-hero-badge">Partnerships & Inquiries</div>'),
        # Ingredients
        (r'<div class="badge" style="margin-bottom:var\(--space-md\);">Full Transparency</div>', '<div class="page-hero-badge">Full Transparency</div>'),
        # Problem
        (r'<div class="badge" style="margin-bottom:var\(--space-md\);">Formulation Science</div>', '<div class="page-hero-badge">Formulation Science</div>'),
        # Science (Already has it or missing? let's add a generic fallback if needed, but grep didn't show one)
        # Terms / Privacy (These were badge-dark)
        (r'<div class="badge badge-dark page-hero-badge reveal" style="transition-delay:0ms;">Legal</div>', '<div class="page-hero-badge reveal" style="transition-delay:0ms;">Legal</div>'),
        (r'<div class="badge badge-dark page-hero-badge reveal" style="transition-delay: 0ms;">Legal</div>', '<div class="page-hero-badge reveal" style="transition-delay:0ms;">Legal</div>')
    ]
    
    for old, new in replacements:
        html = re.sub(old, new, html)

    # Note: index.html has a complex pulsing tagging system, we will leave that alone for now unless it's strictly just the text badge.

    # 3. Fix the blog hero spacing
    if filename == 'blog.html':
        # The paragraph below the H1 has margin-top:var(--space-md); We want it to be 2rem for consistency
        html = html.replace('<p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:var(--text-xl); line-height:var(--leading-tight);">',
                            '<p class="subtext editorial-col" style="margin-top:2rem; font-size:var(--text-xl); line-height:var(--leading-tight);">')

    # Bump Cache
    html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=20"', html)
    html = re.sub(r'href="assets/css/v2_premium\.css\?v=\d+"', 'href="assets/css/v2_premium.css?v=20"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Unified Hero Badges and Fixed Blog Spacing.")
