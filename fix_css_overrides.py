with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_block = "/* OVERRIDE FOR STICKY SCROLL */\nhtml,\nbody {\n    overflow-x: clip !important;\n    overflow-y: auto !important;\n}\n\n.structure-section {\n    overflow: clip !important;\n}"

new_block = """/* ======= SCROLL & LAYOUT OVERRIDES ======= */

/* Allow horizontal clip without disrupting vertical-sticky */
html, body {
    overflow-x: clip !important;
    overflow-y: auto !important;
}

/* HERO PADDING - tighten gap between nav and core text */
.page-hero {
    padding-top: clamp(40px, 8vh, 80px) !important;
}

/* APPLE STICKY SCROLL: match sticky top to actual nav height (~70px) */
.apple-slide {
    top: 72px !important;
}

/* O2 ANIMATION visibility fix */
.hero-animation-wrapper.bottom-mounted {
    position: relative !important;
    opacity: 1 !important;
    visibility: visible !important;
    display: flex !important;
    justify-content: center !important;
    transform: scale(1.15) !important;
    margin-top: 4rem !important;
    z-index: 2 !important;
}

/* SMOOTH REVEAL ANIMATIONS - remove jarring transforms */
.reveal {
    transition: opacity 0.7s ease, transform 0.7s ease !important;
}

@keyframes cardReveal {
    0%   { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes tamilReveal {
    0%   { opacity: 0; transform: translateY(16px); }
    100% { opacity: 1; transform: translateY(0); }
}"""

if old_block in css:
    css = css.replace(old_block, new_block)
    print("Replaced old block successfully!")
else:
    print("Block not found, appending...")
    # Just append since we know the file has extra old block
    # Find the HERO PADDING OVERRIDE section and replace everything from there
    hero_marker = "/* HERO PADDING OVERRIDE - reduce gap between nav and core text */"
    hero_idx = css.find(hero_marker)
    if hero_idx != -1:
        css = css[:hero_idx].rstrip() + "\n\n" + new_block
        print("Appended correctly from hero marker position")
    else:
        css += "\n" + new_block
        print("Appended at end")

with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Done!")
