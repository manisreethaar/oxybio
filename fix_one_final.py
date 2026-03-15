"""
FINAL COMPREHENSIVE FIX - single pass, no regressions
"""

FINAL_CSS = """/* ======= FINAL OVERRIDE BLOCK — do not add below this ======= */

/* Prevent horizontal scroll without breaking position:sticky */
html, body {
    overflow-x: clip !important;
}

/* Hero section: minimum 90px so both tags are visible below the fixed nav */
.page-hero {
    padding-top: clamp(90px, 12vh, 120px) !important;
}

/* Apple sticky scroll: correct offset for 72px fixed nav */
#solution-cards .apple-slide {
    top: 72px !important;
}

/* O2 animation: always visible */
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

/* ===== MOBILE OVERRIDES ===== */
@media (max-width: 768px) {

    /* Hero: tighter padding on mobile */
    .page-hero {
        padding-top: 90px !important;
        padding-bottom: 2rem !important;
    }

    /* Tamil card: smaller on mobile */
    .tamil-card-wrapper {
        padding: 1.5rem 1.25rem !important;
        border-radius: 20px !important;
        width: 90% !important;
    }

    .tamil-hero-text {
        font-size: clamp(2.5rem, 12vw, 4rem) !important;
    }

    /* O2 animation: smaller on mobile */
    .hero-animation-wrapper.bottom-mounted {
        transform: scale(0.75) !important;
        margin-top: 1rem !important;
    }

    /* Solution cards: DISABLE sticky on mobile */
    #solution-cards .apple-slide {
        position: relative !important;
        top: auto !important;
        min-height: auto !important;
        padding: 2rem 0 !important;
    }

    #solution-cards {
        padding-bottom: 1rem !important;
    }

    /* Solution card inner content: stack vertically on mobile */
    .mobile-stack-card {
        display: flex !important;
        flex-direction: column !important;
        gap: 1.5rem !important;
    }
}
"""

# === FIX 1: Remove duplicate canvas from index.html ===
with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

count_before = idx.count('id="biology-mesh"')
print(f"Canvas elements before: {count_before}")

# Remove one of the two duplicate canvas blocks
old = '''            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->
            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>
            
            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->
            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>'''

new = '''            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->
            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>'''

if old in idx:
    idx = idx.replace(old, new)
    print("FIX 1: Removed duplicate canvas")
else:
    print("Note: Duplicate canvas not found (may already be fixed)")

count_after = idx.count('id="biology-mesh"')
print(f"Canvas elements after: {count_after}")

with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# === FIX 2: Write clean CSS override block ===
with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

marker = '/* ======= FINAL OVERRIDE BLOCK'
marker_idx = css.find(marker)
if marker_idx != -1:
    css = css[:marker_idx].rstrip() + '\n\n' + FINAL_CSS
    print("FIX 2: Replaced CSS override block")
else:
    css = css.rstrip() + '\n\n' + FINAL_CSS
    print("FIX 2: Appended CSS override block")

with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("\nAll fixes applied. Verifying structure...")

# === VERIFICATION: Count open vs close section tags in index.html ===
with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
    check = f.read()

opens = check.count('<section')
closes = check.count('</section>')
print(f"<section> open tags: {opens}")
print(f"</section> close tags: {closes}")
if opens == closes:
    print("OK: Section tags balanced")
else:
    print(f"WARNING: Imbalanced tags — {opens} open vs {closes} close")

# Count duplicate IDs
import re
ids = re.findall(r'id="([^"]+)"', check)
from collections import Counter
dupes = {k:v for k,v in Counter(ids).items() if v > 1}
if dupes:
    print(f"WARNING: Duplicate IDs found: {dupes}")
else:
    print("OK: No duplicate IDs")
