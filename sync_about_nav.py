import os, glob

# The old mega-menu dropdown block for About Us (in non-about pages)
# It had 2 items: Vision & Mission + Founder & Team
# The desktop mega-menu block AND the mobile submenu both need updating

FILES = glob.glob('e:\\OXYBIO\\*.html')

# What the OLD desktop mega-menu About dropdown looks like (without "Our Story" first item)
OLD_MEGA_2ITEM = '''<a href="about.html#about-vision" class="mega-nav-link">
                            <span class="link-title">Vision &amp; Mission</span>
                            <span class="link-desc">Why we started and where we are heading.</span>
                        </a>
                        <a href="about.html#about-founder" class="mega-nav-link">
                            <span class="link-title">Founder &amp; Team</span>
                            <span class="link-desc">Meet the researchers and scientists behind the brand.</span>
                        </a>'''

# Also handle the variant with & (not &amp;) since some pages use it raw
OLD_MEGA_2ITEM_RAW = '''<a href="about.html#about-vision" class="mega-nav-link">
                            <span class="link-title">Vision & Mission</span>
                            <span class="link-desc">Why we started and where we are heading.</span>
                        </a>
                        <a href="about.html#about-founder" class="mega-nav-link">
                            <span class="link-title">Founder & Team</span>
                            <span class="link-desc">Meet the researchers and scientists behind the brand.</span>
                        </a>'''

NEW_MEGA_3ITEM = '''<a href="about.html#about-story" class="mega-nav-link">
                            <span class="link-title">Our Story</span>
                            <span class="link-desc">The origin, the frustration, and the journey so far.</span>
                        </a>
                        <a href="about.html#about-vision" class="mega-nav-link">
                            <span class="link-title">Vision &amp; Mission</span>
                            <span class="link-desc">Where we are going and how we get there.</span>
                        </a>
                        <a href="about.html#about-who" class="mega-nav-link">
                            <span class="link-title">Who We Are</span>
                            <span class="link-desc">The founder, the science, and our operating principles.</span>
                        </a>'''

# Old mobile menu submenu
OLD_MOBILE_VISION = '<a href="about.html#about-vision" class="menu-link">Vision &amp; Mission</a>'
OLD_MOBILE_FOUNDER = '<a href="about.html#about-founder" class="menu-link">Founder &amp; Team</a>'

NEW_MOBILE_STORY   = '<a href="about.html#about-story" class="menu-link">Our Story</a>'
NEW_MOBILE_VISION  = '<a href="about.html#about-vision" class="menu-link">Vision &amp; Mission</a>'
NEW_MOBILE_WHO     = '<a href="about.html#about-who" class="menu-link">Who We Are</a>'

updated = []
for fpath in FILES:
    fname = os.path.basename(fpath)
    if fname == 'about.html':
        continue  # already correct
    if fname in ('index-single.html',):
        continue  # old standalone file, skip

    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content
    changed = False

    # Fix desktop mega-menu
    if OLD_MEGA_2ITEM in content:
        content = content.replace(OLD_MEGA_2ITEM, NEW_MEGA_3ITEM)
        changed = True
    elif OLD_MEGA_2ITEM_RAW in content:
        content = content.replace(OLD_MEGA_2ITEM_RAW, NEW_MEGA_3ITEM)
        changed = True

    # Fix mobile menu: replace old vision + founder with story + vision + who
    if OLD_MOBILE_VISION in content and OLD_MOBILE_FOUNDER in content:
        content = content.replace(
            OLD_MOBILE_VISION + '\n                <a href="about.html#about-founder" class="menu-link">Founder &amp; Team</a>',
            NEW_MOBILE_STORY + '\n                ' + NEW_MOBILE_VISION + '\n                ' + NEW_MOBILE_WHO
        )
        if content != original:
            changed = True

    # Fallback: replace individually if pattern didn't match above
    if OLD_MOBILE_FOUNDER in content:
        # Replace founder line with who we are
        content = content.replace(
            '<a href="about.html#about-founder" class="menu-link">Founder &amp; Team</a>',
            NEW_MOBILE_WHO
        )
        # Insert Our Story before Vision & Mission
        content = content.replace(
            '<a href="about.html#about-vision" class="menu-link">Vision &amp; Mission</a>',
            NEW_MOBILE_STORY + '\n                ' + NEW_MOBILE_VISION
        )
        changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(fname)
        print(f"UPDATED: {fname}")

print(f"\nDone. Updated {len(updated)} files: {updated}")
