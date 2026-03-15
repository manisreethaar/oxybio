import os, re

pages = {
    'index.html': r'e:\OXYBIO\index.html',
    'about.html': r'e:\OXYBIO\about.html',
    'science.html': r'e:\OXYBIO\science.html',
    'problem.html': r'e:\OXYBIO\problem.html',
    'careers.html': r'e:\OXYBIO\careers.html',
    'blog.html': r'e:\OXYBIO\blog.html',
    'contact.html': r'e:\OXYBIO\contact.html',
    'ingredients.html': r'e:\OXYBIO\ingredients.html',
}

print('=== MOBILE GRID ISSUES (no media query override) ===')
for name, path in pages.items():
    with open(path, encoding='utf-8') as f:
        content = f.read()
    # Find inline style grids with multiple columns that might not stack on mobile
    grids = re.findall(r'grid-template-columns\s*:[^;"]+', content)
    fixed_multi = [g for g in grids if ('fr' in g or 'repeat' in g) and not '1fr' == g.strip().split(':')[-1].strip()]
    if fixed_multi:
        print(f'  {name}: {len(fixed_multi)} multi-column grids')
        for g in fixed_multi[:3]:
            print(f'    -> {g.strip()[:80]}')

print()
print('=== PADDING-TOP on sections (hero overlap risk) ===')
for name, path in pages.items():
    with open(path, encoding='utf-8') as f:
        content = f.read()
    # Sections with padding-top less than nav height ~70px
    smalls = re.findall(r'padding-top\s*:\s*(\d+px)', content)
    too_small = [p for p in smalls if int(p.replace('px','')) < 70]
    if too_small:
        print(f'  {name}: padding-top values that may be under nav: {too_small}')

print()
print('=== HARDCODED FONT FAMILIES (not using CSS vars) ===')
for name, path in pages.items():
    with open(path, encoding='utf-8') as f:
        content = f.read()
    hardcoded = re.findall(r"font-family\s*:\s*'([^']+)'", content)
    # exclude known used fonts
    ok_fonts = {'Arima Madurai', 'Playfair Display', 'Inter', 'Plus Jakarta Sans', 'Outfit'}
    bad = [f for f in set(hardcoded) if f not in ok_fonts]
    if bad:
        print(f'  {name}: non-standard fonts: {bad}')

print()
print('=== MISSING ALT TEXT on images ===')
for name, path in pages.items():
    with open(path, encoding='utf-8') as f:
        content = f.read()
    imgs_no_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', content)
    if imgs_no_alt:
        print(f'  {name}: {len(imgs_no_alt)} images missing alt text')

print()
print('=== HERO SECTION padding-top analysis ===')
for name, path in pages.items():
    with open(path, encoding='utf-8') as f:
        content = f.read()
    # Check if articles/mains have clamp for large padding  
    if 'clamp(160px' in content:
        print(f'  WARNING {name}: Has old 160px padding-top (was phantom section)')
    elif 'clamp(90px' in content or 'padding-top:90px' in content:
        print(f'  OK {name}: 90px hero padding')
    elif 'clamp(120px' in content or 'clamp(100px' in content:
        print(f'  OK {name}: 100-120px article padding (blog style)')
    else:
        pt = re.search(r'<(?:article|section|main)[^>]+padding-top\s*[:=]\s*([^;"]+)', content)
        if pt:
            print(f'  {name}: padding is {pt.group(1).strip()[:60]}')
