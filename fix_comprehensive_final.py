"""
COMPREHENSIVE FIX:
1. Fix sticky scroll — each card needs min-height so there's scroll space between them
2. The 'after MOMENTUM' issue needs the section to have enough padding for the last card to unstick
3. Fix mobile layout for solution cards
4. Fix all accumulated CSS drift from previous fix attempts
"""
import re

def fix_everything():
    # =========================================================
    # FIX 1: Sticky scroll proper implementation
    # Each card needs min-height so stacking has visual scroll space
    # PLUS the section needs padding-bottom equal to 2 card heights
    # so the last card can actually unstick and the next section appears
    # =========================================================
    with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
        idx = f.read()

    # Add min-height to each sticky card (100svh = true viewport height on mobile)
    # The card fills the full screen so it feels like distinct slides
    idx = idx.replace(
        'style="position:sticky; top:80px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10;"',
        'style="position:sticky; top:72px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10; min-height: 100svh;"'
    )
    idx = idx.replace(
        'style="position:sticky; top:80px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);"',
        'style="position:sticky; top:72px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 100svh;"'
    )
    idx = idx.replace(
        'style="position:sticky; top:80px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);"',
        'style="position:sticky; top:72px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 100svh;"'
    )

    # The section padding-bottom: 4rem is fine — the cards have their own height now
    # BUT the section AFTER solution-cards needs a higher z-index to properly pull itself out
    # We give the Science section a higher z-index and background to cover the sticky card
    old_science_sec = 'section style="padding:var(--space-lg) 0; border-bottom:1px solid var(--border);">'
    new_science_sec = 'section style="padding:var(--space-lg) 0; border-bottom:1px solid var(--border); position:relative; z-index:50; background:var(--bg);">'
    if old_science_sec in idx:
        idx = idx.replace(old_science_sec, new_science_sec, 1)  # Only first occurrence
        print("Fixed science section z-index")

    with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print("HTML sticky scroll fix applied.")

    # =========================================================
    # FIX 2: CSS — clean accumulated overrides from all previous scripts
    # Replace the entire bottom override block with one clean, minimal version
    # =========================================================
    with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # Find and replace the entire override block we've kept modifying
    # Find the start marker
    marker = '/* ======= SCROLL & LAYOUT OVERRIDES ======= */'
    marker_idx = css.find(marker)
    if marker_idx != -1:
        # Replace everything from the marker to end of file
        css = css[:marker_idx] + CLEAN_CSS_OVERRIDE
        print("Replaced accumulated CSS override block with clean version.")
    else:
        css += '\n' + CLEAN_CSS_OVERRIDE
        print("Appended clean CSS override block.")

    with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS fix applied.")

CLEAN_CSS_OVERRIDE = """/* ======= FINAL OVERRIDE BLOCK — do not add below this ======= */

/* Prevent horizontal scroll without breaking position:sticky */
html, body {
    overflow-x: clip !important;
}

/* Hero section: tight padding so tags show below nav */
.page-hero {
    padding-top: clamp(90px, 12vh, 120px) !important;
}

/* Apple sticky scroll: correct offset for ~72px fixed nav */
#solution-cards .apple-slide {
    top: 72px !important;
}

/* O2 animation: always visible, centered below hero content */
.hero-animation-wrapper.bottom-mounted {
    position: relative !important;
    opacity: 1 !important;
    visibility: visible !important;
    display: flex !important;
    justify-content: center !important;
    transform: scale(1.1) !important;
    margin-top: 3rem !important;
    z-index: 2 !important;
}

/* Mobile: solution cards scroll vertically, not sticky */
@media (max-width: 768px) {
    #solution-cards .apple-slide {
        position: relative !important;
        top: 0 !important;
        min-height: auto !important;
        padding: 2rem 0 !important;
    }
    #solution-cards {
        padding-bottom: 2rem !important;
    }
    .tamil-card-wrapper {
        padding: 1.5rem !important;
        border-radius: 20px !important;
    }
    .tamil-hero-text {
        font-size: clamp(2.5rem, 12vw, 4rem) !important;
    }
    .hero-animation-wrapper.bottom-mounted {
        transform: scale(0.85) !important;
        margin-top: 1.5rem !important;
    }
    /* Science cards stack vertically on mobile */
    [style*="grid-template-columns:repeat(3,1fr)"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 1rem !important;
    }
    /* Mobile-stack-card already handled but ensure grid is vertical */
    .mobile-stack-card {
        grid-template-columns: 1fr !important;
    }
}
"""

fix_everything()
