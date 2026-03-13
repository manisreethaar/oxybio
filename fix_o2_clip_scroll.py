import traceback

def fix_all():
    try:
        # ===== Fix 1: index.html =====
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # Fix A: Remove overflow:clip from hero section (clips the O2 animation)
        # and change margin-bottom on O2 from negative to 0 so it doesn't bleed and get clipped
        old_hero_section = 'style="padding-top:clamp(40px, 8vh, 80px); padding-bottom:40px; background:var(--bg); border-bottom:1px solid var(--border); overflow:clip; position:relative;"'
        new_hero_section = 'style="padding-top:clamp(40px, 8vh, 80px); padding-bottom:0; background:var(--bg); border-bottom:1px solid var(--border); position:relative;"'
        if old_hero_section in idx:
            idx = idx.replace(old_hero_section, new_hero_section)
            print("Fixed hero section overflow and padding")

        # Fix B: Remove negative margin-bottom from O2 wrapper (was causing it to bleed under border/clip)
        old_o2_margin = 'margin-bottom: -4rem; /* Help blend into next section */'
        new_o2_margin = 'margin-bottom: 0;'
        if old_o2_margin in idx:
            idx = idx.replace(old_o2_margin, new_o2_margin)
            print("Fixed O2 negative margin-bottom")

        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)

        # ===== Fix 2: styles.css =====
        with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
            css = f.read()

        # Fix C: Remove the global .apple-slide { top: 72px !important } 
        # because this was being applied globally and may affect science.html sections too
        # Replace with a more specific selector that only targets the solution section
        css = css.replace(
            '/* APPLE STICKY SCROLL: match sticky top to actual nav height (~70px) */\n.apple-slide {\n    top: 72px !important;\n}',
            '/* APPLE STICKY SCROLL: match sticky top to actual nav height (~70px) */\n#solution-cards .apple-slide {\n    top: 72px !important;\n}'
        )
        print("Scoped apple-slide sticky top to #solution-cards only")

        # Fix D: Also check if there's a JS scroll lock on science sections
        # We cannot easily remove that from CSS, so let's ensure sections don't have scroll locking via overflow
        # Remove any scroll-snap on the vertical axis (only x-axis snap was intended for the roadmap)
        if 'scroll-snap-type: y' in css:
            css = css.replace('scroll-snap-type: y mandatory', '/* scroll-snap-type: y mandatory - removed to prevent section snap-lock */')
            css = css.replace('scroll-snap-type: y', '/* scroll-snap-type: y - removed */')
            print("Removed vertical scroll-snap-type")
        else:
            print("No vertical scroll-snap found in CSS (good)")

        with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
            f.write(css)

    except Exception as e:
        traceback.print_exc()

fix_all()
