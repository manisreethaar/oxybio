import os, re

# Read header and footer from the NEW index.html
with open(r'e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Extract header (everything up to and including <main>)
header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
# Extract footer (from </main> to end)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

if not header_m or not footer_m:
    print("ERROR: Could not extract header/footer from index.html")
    exit(1)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

# New page-hero template builder
def page_hero(badge, headline_html, subtitle):
    return f"""
        <!-- Page Hero -->
        <section class="page-hero">
            <div class="container">
                <div class="badge badge-dark page-hero-badge reveal" style="transition-delay:0ms;">{badge}</div>
                <h1 class="reveal" style="transition-delay:100ms;">{headline_html}</h1>
                <p class="subtitle reveal" style="transition-delay:200ms;">{subtitle}</p>
            </div>
        </section>
"""

# For each sub-page: read the existing <main> content block (between <main> and </main>),
# then strip the old nav + hero up to the first <section id="..."> that isn't the hero.
# Strategy: just replace the section up to and including </nav> with new header,
#           replace </main>...</body></html> with new footer.

SUBPAGES = {
    'about.html': {
        'badge': 'Our Story',
        'headline': 'Building India\'s first<br><em>honest nutrition brand.</em>',
        'subtitle': 'We are a deep-tech bioformulation startup incubated at TBI, Hosur. This is not a corporate story — it\'s an honest account of a problem we couldn\'t ignore.'
    },
    'science.html': {
        'badge': 'Evidence-Based Science',
        'headline': 'The science behind<br><em>every decision we make.</em>',
        'subtitle': 'Bioavailability. Chelation. Standardized extracts. Peer-reviewed research. We do not choose ingredients because they look good on a label.'
    },
    'problem.html': {
        'badge': 'The Problem',
        'headline': 'India\'s nutrition crisis<br><em>nobody is honestly addressing.</em>',
        'subtitle': 'The data behind why India\'s urban population is deficient despite eating well — and why every existing product is failing them.'
    },
    'ingredients.html': {
        'badge': 'Ingredient Index',
        'headline': 'Every ingredient.<br><em>Every reason.</em>',
        'subtitle': 'No filler. No proprietary blends. An honest breakdown of what is in RIZE, how much, why, and in what form.'
    },
    'careers.html': {
        'badge': 'Join Our Mission',
        'headline': 'Build the future<br><em>of bio-innovation.</em>',
        'subtitle': 'We are a small, focused team building a breakthrough product. If you care deeply about nutrition science and want to do your most important work here.'
    },
    'blog.html': {
        'badge': 'Development Journal & Research',
        'headline': 'The Oxygen<br><em>Blog.</em>',
        'subtitle': 'Science deep-dives, ingredient breakdowns, and honest updates from the lab. Building India\'s first precision nutrition system — in public.'
    },
    'contact.html': {
        'badge': 'Get in Touch',
        'headline': 'We are built on<br><em>conversations.</em>',
        'subtitle': 'Whether you\'re an investor, researcher, or potential partner, we\'d love to hear from you. Let\'s explore how we can collaborate.'
    },
    'privacy.html': {
        'badge': 'Legal',
        'headline': 'Privacy<br><em>Policy.</em>',
        'subtitle': 'Oxygen Bioinnovations | Effective from: October 2026. Simple, honest, and compliant with DPDP Act 2023.'
    },
    'terms.html': {
        'badge': 'Legal',
        'headline': 'Terms &amp;<br><em>Conditions.</em>',
        'subtitle': 'Oxygen Bioinnovations | Last updated: February 2026. Everything you need to know about using our website and services.'
    },
}

for filename, meta in SUBPAGES.items():
    filepath = os.path.join(r'e:\\OXYBIO', filename)
    if not os.path.exists(filepath):
        print(f"SKIP {filename} — not found")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the main content between existing <main> and </main>
    main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
    if not main_match:
        print(f"SKIP {filename} — no <main> block found")
        continue

    raw_main = main_match.group(1)

    # Strip old hero/page-hero sections from main content
    # Remove anything matching <section class="hero..." or <section class="page-hero..."
    # up to the first subsequent <section> that is a content section.
    stripped = re.sub(
        r'<section[^>]*class="[^"]*(?:hero|page-hero)[^"]*"[^>]*>.*?</section>',
        '',
        raw_main,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Also strip the old <section class="hero"... (for contact.html which had no page-hero class)
    stripped = re.sub(
        r'<section[^>]*id="contact-hero"[^>]*>.*?</section>',
        '',
        stripped,
        flags=re.DOTALL | re.IGNORECASE
    )
    stripped = re.sub(
        r'<section[^>]*id="blog-hero"[^>]*>.*?</section>',
        '',
        stripped,
        flags=re.DOTALL | re.IGNORECASE
    )

    new_hero = page_hero(meta['badge'], meta['headline'], meta['subtitle'])
    new_main = '\n' + new_hero + stripped

    # Build: new HEADER + <main> + content + </main> + FOOTER_SECTION
    # We'll replace specific parts:
    # 1. Replace everything from start to <main> with new HEADER
    # 2. Replace </main>...$ with FOOTER

    new_content = HEADER + '<main>' + new_main + '\n</main>\n' + FOOTER

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Updated {filename}")

print("All sub-pages updated.")
