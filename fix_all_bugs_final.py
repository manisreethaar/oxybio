import traceback

def fix_all_bugs():
    try:
        print("=== Reading index.html ===")
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # =============================================
        # FIX 1: Hero padding too low (tags behind nav)
        # Nav is ~70px. We need at least 80px + some space before tags show.
        # Set to 90px minimum so tags are comfortably below the nav.
        # =============================================
        old_hero_padding = 'padding-top:clamp(40px, 8vh, 80px); padding-bottom:0; background:var(--bg); border-bottom:1px solid var(--border); position:relative;'
        new_hero_padding = 'padding-top:clamp(90px, 12vh, 120px); padding-bottom:0; background:var(--bg); border-bottom:1px solid var(--border); position:relative;'
        if old_hero_padding in idx:
            idx = idx.replace(old_hero_padding, new_hero_padding)
            print("FIX 1: Increased hero padding-top to 90px minimum (was 40px, nav height is ~70px)")
        else:
            print("WARNING FIX 1: Could not find hero padding string")

        # =============================================
        # FIX 2: Add closing </section> for .page-hero
        # Line 512: </div> closes the .container
        # Line 513: </div> should close nothing (already gone) 
        # Then at line 515: <!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->
        # Without a </section>, the next banner section is INSIDE the hero section
        # =============================================
        old_hero_close = '''            </div>

        <!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->'''
        new_hero_close = '''            </div>

        </section>

        <!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->'''
        if old_hero_close in idx:
            idx = idx.replace(old_hero_close, new_hero_close, 1)  # Only first occurrence
            print("FIX 2: Added missing closing </section> tag for .page-hero")
        else:
            print("WARNING FIX 2: Could not find hero close pattern")

        # =============================================
        # FIX 3: Give #solution-cards enough padding-bottom 
        # so the user can scroll past the last sticky card.
        # padding-bottom needs to be at least 150vh (3 cards * ~50vh each)
        # =============================================
        old_solution_section = 'style="background:var(--bg-alt); padding-top: 2rem; padding-bottom:var(--space-lg); position: relative;"'
        new_solution_section = 'style="background:var(--bg-alt); padding-top: 2rem; padding-bottom: calc(var(--space-lg) + 100vh); position: relative;"'
        if old_solution_section in idx:
            idx = idx.replace(old_solution_section, new_solution_section)
            print("FIX 3: Added padding-bottom 100vh to #solution-cards for scroll exit room")
        else:
            print("WARNING FIX 3: Could not find solution section style")

        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)
        print("\n=== index.html fixes complete ===\n")

    except Exception as e:
        traceback.print_exc()

fix_all_bugs()
