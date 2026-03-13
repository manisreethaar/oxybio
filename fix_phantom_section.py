import traceback

def fix_phantom_wrapper():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # The phantom outer wrapper starts at line 359 and wraps around the entire hero.
        # It contains the canvas and all the styles/inline CSS we injected into the hero.
        # We need to:
        # 1. Remove the outer <section class="structure-section" ...> tag (line 359-360)
        # 2. Move the canvas into the inner .page-hero section
        # 3. Remove the closing </section> of the outer wrapper

        # Step 1: Replace outer section opening + canvas with nothing
        # (the canvas will be naturally inside the .page-hero since page-hero comes right after)
        old_outer_start = '''        <section class="structure-section"
            style="padding-top:clamp(160px, 20vh, 200px); border-bottom:none; position:relative; overflow:hidden;">

            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->

            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>'''
        
        new_outer_start = '''        <!-- Canvas is now inside the .page-hero section below -->'''
        
        if old_outer_start in idx:
            idx = idx.replace(old_outer_start, new_outer_start)
            print("Removed phantom outer section wrapper and canvas")
        else:
            print("WARNING: Could not find exact phantom wrapper string")

        # Step 2: Now the .page-hero section is missing the canvas. Add it back inside.
        old_inner_hero_start = '''        <section class="structure-section page-hero"
            style="padding-top:clamp(40px, 8vh, 80px); padding-bottom:0; background:var(--bg); border-bottom:1px solid var(--border); position:relative;">'''

        new_inner_hero_start = '''        <section class="structure-section page-hero"
            style="padding-top:clamp(40px, 8vh, 80px); padding-bottom:0; background:var(--bg); border-bottom:1px solid var(--border); position:relative;">
            
            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->
            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>'''

        if old_inner_hero_start in idx:
            idx = idx.replace(old_inner_hero_start, new_inner_hero_start)
            print("Added canvas back inside the real .page-hero section")
        else:
            print("WARNING: Could not find exact inner hero section start")

        # Step 3: There should be a stale </section> closing the phantom outer wrapper.
        # It comes right after the inner hero section closes.
        # After </section> for .page-hero we have <!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->
        # But there's now an extra </section> from the removed outer wrapper.
        # Find the exact location and remove it.
        old_extra_close = '''        </section>

        <!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->'''
        new_extra_close = '''        <!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->'''

        if old_extra_close in idx:
            idx = idx.replace(old_extra_close, new_extra_close)
            print("Removed extra closing </section> from phantom wrapper")
        else:
            print("WARNING: Could not remove extra </section>")

        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)

    except Exception as e:
        traceback.print_exc()

fix_phantom_wrapper()
