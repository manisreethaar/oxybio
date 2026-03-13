import traceback

def fix_hero_spacing_and_animation():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # 1. Fix the top padding so the core text sits higher up towards the header
        old_padding = 'padding-top:clamp(150px, 18vh, 180px); padding-bottom:80px; background:var(--bg); border-bottom:1px solid var(--border); overflow:hidden; position:relative;'
        new_padding = 'padding-top:clamp(100px, 14vh, 130px); padding-bottom:80px; background:var(--bg); border-bottom:1px solid var(--border); overflow:clip; position:relative;'
        
        if old_padding in idx:
            idx = idx.replace(old_padding, new_padding)
            print("Successfully reduced padding and updated overflow.")
        else:
            print("Warning: Could not find exact padding string.")

        # 2. Remove opacity:0 from the h2 so it doesn't get stuck hidden if the JS selector misses it
        old_h2 = 'font-family: var(--font-serif); font-size: clamp(2rem, 4vw, 3rem); line-height: 1.2; font-weight: 700; color: var(--text-main); margin-top: 1rem; opacity: 0; letter-spacing: -0.02em;'
        new_h2 = 'font-family: var(--font-serif); font-size: clamp(2rem, 4vw, 3rem); line-height: 1.2; font-weight: 700; color: var(--text-main); margin-top: 1rem; letter-spacing: -0.02em;'
        
        if old_h2 in idx:
            idx = idx.replace(old_h2, new_h2)
            print("Successfully removed opacity: 0 from H2.")
        else:
            print("Warning: Could not find exact H2 inline style.")

        # 3. Increase delay on the bottom mounted O2 animation so it flows better
        old_o2 = 'hero-animation-wrapper bottom-mounted reveal" style="transition-delay: 0.4s;"'
        new_o2 = 'hero-animation-wrapper bottom-mounted reveal" style="transition-delay: 0.6s;"'
        
        if old_o2 in idx:
            idx = idx.replace(old_o2, new_o2)
            print("Successfully increased O2 animation delay.")

        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)

    except Exception as e:
        traceback.print_exc()

def patch_styles_for_sticky():
    try:
        with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
            css = f.read()
            
        # Change overflow-x: hidden to clip on mobile body to prevent breaking position:sticky
        old_overflow = 'body {\n        overflow-x: hidden !important;\n    }'
        new_overflow = 'body {\n        overflow-x: clip !important;\n    }'
        
        if old_overflow in css:
            css = css.replace(old_overflow, new_overflow)
            with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
                f.write(css)
            print("Successfully patched mobile overflow to clip.")
            
    except Exception as e:
        traceback.print_exc()

fix_hero_spacing_and_animation()
patch_styles_for_sticky()
