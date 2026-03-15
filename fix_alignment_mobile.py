"""
Fix alignment, font, hero padding across all pages.
1. Replace old 160px padding on article/section heroes with proper 90px-120px
2. Add CSS mobile stacking rules for multi-column grids that break on mobile
"""
import os, re

# === FIX 1: Hero padding-top on all non-index pages ===
# These pages have articles or sections with padding-top:clamp(160px, 20vh, 200px)
# which was the old "phantom section" style — too much blank space at top

fix_padding_pages = [
    r'e:\OXYBIO\about.html',
    r'e:\OXYBIO\science.html',
    r'e:\OXYBIO\problem.html',
    r'e:\OXYBIO\careers.html',
    r'e:\OXYBIO\blog.html',
    r'e:\OXYBIO\contact.html',
    r'e:\OXYBIO\ingredients.html',
    r'e:\OXYBIO\blog-bootstrapping.html',
    r'e:\OXYBIO\blog-origin.html',
    r'e:\OXYBIO\blog-minerals.html',
    r'e:\OXYBIO\faq.html',
    r'e:\OXYBIO\life.html',
    r'e:\OXYBIO\privacy.html',
    r'e:\OXYBIO\terms.html',
]

for p in fix_padding_pages:
    if not os.path.exists(p): continue
    with open(p, encoding='utf-8') as f:
        content = f.read()
    original = content
    # Replace the old 160px clamp hero padding
    content = content.replace(
        'padding-top:clamp(160px, 20vh, 200px)',
        'padding-top:clamp(90px, 12vh, 120px)'
    )
    content = content.replace(
        'padding-top: clamp(160px, 20vh, 200px)',
        'padding-top: clamp(90px, 12vh, 120px)'
    )
    if content != original:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed padding: {os.path.basename(p)}')
    else:
        print(f'No 160px padding found: {os.path.basename(p)}')

print()

# === FIX 2: Add mobile CSS overrides in styles.css ===
# Key grids that break on mobile:
# - .mobile-stack-card (already has a rule but let's strengthen it)
# - contact page info+form grid
# - blog page card grid
# - careers page grid

MOBILE_GRID_CSS = """
/* ======= MOBILE GRID STACKING — prevents broken layouts ======= */
@media (max-width: 768px) {

    /* All inline-style grids with multiple columns: force single column */
    [style*="grid-template-columns:1.1fr"][style*="0.9fr"],
    [style*="grid-template-columns: 1.1fr"][style*="0.9fr"],
    [style*="grid-template-columns:1.5fr"][style*="1fr"],
    [style*="grid-template-columns: 1.5fr"][style*="1fr"],
    [style*="grid-template-columns:1fr 1.5fr"],
    [style*="grid-template-columns:350px"],
    [style*="grid-template-columns:220px"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 1.5rem !important;
    }

    /* Standard 2-col and 3-col class-based grids */
    .grid-2col, .two-col, .split-layout,
    [class*="grid"][style*="grid-template-columns:1fr 1fr"],
    [class*="grid"][style*="grid-template-columns: 1fr 1fr"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 1.5rem !important;
    }

    /* Careers: full-width form/description */
    .col-form, .col-info {
        width: 100% !important;
        max-width: 100% !important;
    }

    /* Blog: card grid — 1 column */
    .blog-grid, .article-grid {
        grid-template-columns: 1fr !important;
    }

    /* Structure section: reduce padding on mobile */
    .structure-section {
        padding-left: clamp(1rem, 5vw, 2rem) !important;
        padding-right: clamp(1rem, 5vw, 2rem) !important;
    }

    /* General: any display-font heading that's too big on mobile */
    .display {
        font-size: clamp(2.5rem, 10vw, 4rem) !important;
        letter-spacing: -0.03em !important;
    }

    /* Headlines */
    .headline {
        font-size: clamp(1.8rem, 8vw, 2.5rem) !important;
    }

    /* Reduce oversized stat numbers on mobile */
    [style*="font-size:6rem"],
    [style*="font-size: 6rem"],
    [style*="font-size:5rem"],
    [style*="font-size: 5rem"] {
        font-size: 3rem !important;
    }
}
"""

with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add before our final override block
final_marker = '/* ======= FINAL OVERRIDE BLOCK'
marker_idx = css.find(final_marker)
if marker_idx != -1:
    css = css[:marker_idx] + MOBILE_GRID_CSS + '\n\n' + css[marker_idx:]
else:
    css = css.rstrip() + MOBILE_GRID_CSS

with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Added mobile grid stacking CSS')

print('\nAll done.')
