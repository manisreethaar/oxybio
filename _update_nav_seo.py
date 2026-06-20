"""
Update navigation across all HTML pages:
1. Replace "Follow the Build" CTA with "Investors" link in desktop nav
2. Add Investors link to mobile menus
3. Add canonical tags + favicon to pages missing them
4. Fix unique og:url per page
5. Fix careers page title
6. Add unique meta descriptions
"""
import os, re

BASE = r'e:\OXYBIO-WEBSITE'

pages = {
    'index.html':       {'title': 'Oxygen Bioinnovations | Advanced Functional Foods',
                         'desc':  'Oxygen Bioinnovations — India\'s first evidence-based functional food R&D platform. Fermented millets, functional mushroom extracts, science-backed formulations.',
                         'url':   'https://www.oxygenbioinnovations.com/'},
    'about.html':       {'title': 'Our Story | Oxygen Bioinnovations',
                         'desc':  'The founding story, R&D platform goals, and team behind Oxygen Bioinnovations — a DPIIT-recognized biotech startup incubated at DETI@ACE TBI, Hosur.',
                         'url':   'https://www.oxygenbioinnovations.com/about'},
    'science.html':     {'title': 'Our Science | Oxygen Bioinnovations',
                         'desc':  'The formulation science behind Oxygen Bioinnovations — fermented millet bioavailability, functional mushroom extracts, and synergistic nutrition.',
                         'url':   'https://www.oxygenbioinnovations.com/science'},
    'careers.html':     {'title': 'Careers | Oxygen Bioinnovations',
                         'desc':  'Join Oxygen Bioinnovations — formulation scientists, fermentation engineers, and clinical researchers building India\'s first evidence-based functional food system.',
                         'url':   'https://www.oxygenbioinnovations.com/careers'},
    'blog.html':        {'title': 'Blog | Oxygen Bioinnovations',
                         'desc':  'Insights, research notes, and updates from the Oxygen Bioinnovations lab — functional food science explained.',
                         'url':   'https://www.oxygenbioinnovations.com/blog'},
    'contact.html':     {'title': 'Contact | Oxygen Bioinnovations',
                         'desc':  'Get in touch with the Oxygen Bioinnovations team — partnerships, press, investor inquiries, and general questions.',
                         'url':   'https://www.oxygenbioinnovations.com/contact'},
    'faq.html':         {'title': 'FAQ | Oxygen Bioinnovations',
                         'desc':  'Frequently asked questions about Oxygen Bioinnovations products, formulations, and the science behind our functional foods.',
                         'url':   'https://www.oxygenbioinnovations.com/faq'},
    'ingredients.html': {'title': 'Lab Materials | Oxygen Bioinnovations',
                         'desc':  'The raw extracts, fermented grains, and functional mushroom compounds used in Oxygen Bioinnovations formulations.',
                         'url':   'https://www.oxygenbioinnovations.com/ingredients'},
    'problem.html':     {'title': 'The Problem | Oxygen Bioinnovations',
                         'desc':  'The biological deficits, nutritional gaps, and market failures that drive Oxygen Bioinnovations\' R&D mission.',
                         'url':   'https://www.oxygenbioinnovations.com/problem'},
    'privacy.html':     {'title': 'Privacy Policy | Oxygen Bioinnovations',
                         'desc':  'Privacy policy for Oxygen Bioinnovations — how we handle your data.',
                         'url':   'https://www.oxygenbioinnovations.com/privacy'},
    'terms.html':       {'title': 'Terms & Conditions | Oxygen Bioinnovations',
                         'desc':  'Terms and conditions for use of the Oxygen Bioinnovations website and services.',
                         'url':   'https://www.oxygenbioinnovations.com/terms'},
    'life.html':        {'title': 'Life at Oxygen | Oxygen Bioinnovations',
                         'desc':  'What it\'s like to work at Oxygen Bioinnovations — culture, values, and the team behind the science.',
                         'url':   'https://www.oxygenbioinnovations.com/life'},
}

# Old nav CTA to replace
OLD_NAV_CTA_PATTERNS = [
    '<a href="index.html#updates" class="btn btn-outline" style="margin-left: 1rem;">Follow the Build</a>',
    '<a href="blog.html" class="btn btn-outline" style="margin-left: 1rem;">Follow the Build</a>',
    '<a href="index.html#updates" class="btn btn-outline"  style="margin-left: 1rem;">Follow the Build</a>',
]
NEW_NAV_CTA = '<a href="investors.html" class="btn btn-outline" style="margin-left: 1rem; border-color: rgba(13,138,116,0.5); color: #0D8A74;">Investors</a>'

# Old mobile CTA to replace
OLD_MOBILE_CTA_PATTERNS = [
    '<a href="#updates" class="btn btn-outline"\n\n                style="width:100%;justify-content:center;padding:1rem;">Follow the Build</a>',
    '<a href="index.html#updates" class="btn btn-outline" style="width:100%;justify-content:center;padding:1rem;">Follow the Build</a>',
    '<a href="#updates" class="btn btn-outline" style="width:100%;justify-content:center;padding:1rem;">Follow the Build</a>',
]

# Mobile investors link to inject BEFORE mobile-cta div if not already present
MOBILE_INVESTORS_LINK = '        <a href="investors.html" class="menu-link" style="color:#0D8A74; font-weight:600;">Investors &amp; Partners</a>\n'

updated = []
skipped = []

for filename, meta in pages.items():
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        skipped.append(filename + ' (not found)')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html
    changes = []

    # ── 1. Fix og:url ──────────────────────────────────────────────
    old_url_meta = re.search(r'<meta property="og:url" content="[^"]*">', html)
    if old_url_meta:
        old_url_str = old_url_meta.group(0)
        new_url_str = f'<meta property="og:url" content="{meta["url"]}">'
        if old_url_str != new_url_str:
            html = html.replace(old_url_str, new_url_str, 1)
            changes.append('Fixed og:url')

    # ── 2. Fix og:title ────────────────────────────────────────────
    old_ogt = re.search(r'<meta property="og:title" content="[^"]*">', html)
    if old_ogt:
        new_ogt = f'<meta property="og:title" content="{meta["title"]}">'
        if old_ogt.group(0) != new_ogt:
            html = html.replace(old_ogt.group(0), new_ogt, 1)
            changes.append('Fixed og:title')

    # ── 3. Fix og:description ──────────────────────────────────────
    old_ogd = re.search(r'<meta property="og:description" content="[^"]*">', html)
    if old_ogd:
        new_ogd = f'<meta property="og:description" content="{meta["desc"]}">'
        if old_ogd.group(0) != new_ogd:
            html = html.replace(old_ogd.group(0), new_ogd, 1)
            changes.append('Fixed og:description')

    # ── 4. Fix <title> ─────────────────────────────────────────────
    old_title = re.search(r'<title>[^<]*</title>', html)
    if old_title:
        new_title = f'<title>{meta["title"]}</title>'
        if old_title.group(0) != new_title:
            html = html.replace(old_title.group(0), new_title, 1)
            changes.append('Fixed title tag')

    # ── 5. Fix meta description ────────────────────────────────────
    old_metadesc = re.search(r'<meta name="description"\s*\n?\s*content="[^"]*">', html)
    if old_metadesc:
        new_metadesc = f'<meta name="description" content="{meta["desc"]}">'
        if old_metadesc.group(0) != new_metadesc:
            html = html.replace(old_metadesc.group(0), new_metadesc, 1)
            changes.append('Fixed meta description')

    # ── 6. Add canonical if missing ────────────────────────────────
    if 'rel="canonical"' not in html:
        canonical = f'\n    <link rel="canonical" href="{meta["url"]}">'
        html = html.replace('</head>', canonical + '\n    <link rel="icon" href="assets/images/logo-full.png?v=6" type="image/png">\n</head>', 1)
        changes.append('Added canonical + favicon')
    elif 'rel="icon"' not in html:
        html = html.replace('</head>', '    <link rel="icon" href="assets/images/logo-full.png?v=6" type="image/png">\n</head>', 1)
        changes.append('Added favicon')

    # ── 7. Replace nav desktop CTA ─────────────────────────────────
    cta_replaced = False
    for pattern in OLD_NAV_CTA_PATTERNS:
        if pattern in html:
            html = html.replace(pattern, NEW_NAV_CTA, 1)
            cta_replaced = True
            changes.append('Updated desktop nav CTA → Investors')
            break
    
    # Fallback: try regex for multiline variants
    if not cta_replaced:
        match = re.search(
            r'<a href="[^"]*" class="btn btn-outline"[^>]*>Follow the Build</a>',
            html
        )
        if match:
            html = html.replace(match.group(0), NEW_NAV_CTA, 1)
            changes.append('Updated desktop nav CTA → Investors (regex)')

    # ── 8. Add Investors link to mobile menu ───────────────────────
    if 'investors.html' not in html or ('menu-link' in html and 'Investors' not in html):
        # Inject before the mobile-cta div
        if '<div class="mobile-cta">' in html:
            html = html.replace(
                '<div class="mobile-cta">',
                MOBILE_INVESTORS_LINK + '        <div class="mobile-cta">',
                1
            )
            changes.append('Added Investors to mobile menu')

    # ── Write back if changed ──────────────────────────────────────
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated.append(f'{filename}: {", ".join(changes)}')
    else:
        skipped.append(filename + ' (no changes needed)')

print('=== NAVIGATION UPDATE COMPLETE ===\n')
print(f'UPDATED ({len(updated)} files):')
for u in updated:
    print(f'  ✓ {u}')
print(f'\nSKIPPED ({len(skipped)} files):')
for s in skipped:
    print(f'  - {s}')
