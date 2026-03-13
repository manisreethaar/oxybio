import traceback

def fix_sticky_scroll():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # The fix: remove the outer .container flex wrapper and let the sticky 
        # apple-slide divs be direct children of the section.
        # Each card content already has its own inner div - we'll add container class there.
        
        old_section_start = '''            <!-- CSS STICKY STACKED CARDS -->

            <section id="solution-cards"
                style="background:var(--bg-alt); padding-top: 2rem; padding-bottom:var(--space-lg); position: relative; overflow: visible !important; overflow-x: visible !important; overflow-y: visible !important; clip-path: none !important;">

                <div class="container"
                    style="display: flex; flex-direction: column; gap: 0; overflow: visible !important;">'''
        
        new_section_start = '''            <!-- CSS STICKY STACKED CARDS -->

            <section id="solution-cards"
                style="background:var(--bg-alt); padding-top: 2rem; padding-bottom:var(--space-lg); position: relative;">'''

        if old_section_start in idx:
            idx = idx.replace(old_section_start, new_section_start)
            print("Removed outer .container flex wrapper from sticky section!")
        else:
            print("WARNING: Could not find exact container wrapper. Trying alternate match...")
            # Try to find just the container div 
            old_alt = '<div class="container"\n                    style="display: flex; flex-direction: column; gap: 0; overflow: visible !important;">'
            if old_alt in idx:
                idx = idx.replace(old_alt, '<!-- cards are now direct children -->')
                print("Removed container flex wrapper with alt method.")

        # Also need to close the section properly — remove the extra </div> that closed the container
        # Find the close of the section
        old_section_end = '''                </div>



            </section>



            <!-- ---------------------------------------------------

 SCIENCE SECTION'''
        
        new_section_end = '''            </section>



            <!-- ---------------------------------------------------

 SCIENCE SECTION'''
        
        if old_section_end in idx:
            idx = idx.replace(old_section_end, new_section_end)
            print("Removed closing container div.")
        else:
            print("WARNING: Could not remove closing container div with exact match, section may have extra div.")

        # Now wrap each apple-slide's inner content with a container class
        # So the content stays centered even though the sticky element is full-width
        old_vitality_inner = '''                    <div class="apple-slide" id="slide-vitality"
                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10; min-height: 80vh;">

                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:var(--space-lg); align-items:center;"
                            class="mobile-stack-card">'''
        
        new_vitality_inner = '''                    <div class="apple-slide" id="slide-vitality"
                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10; min-height: 80vh;">

                        <div class="container">
                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:var(--space-lg); align-items:center;"
                            class="mobile-stack-card">'''
        
        if old_vitality_inner in idx:
            idx = idx.replace(old_vitality_inner, new_vitality_inner)
            # Now close that container div before the apple-slide closes
            idx = idx.replace('''                    </div>



                    <!-- CLARITY -->''', 
                              '''                        </div>
                    </div>



                    <!-- CLARITY -->''')
            print("Wrapped VITALITY content in .container.")

        old_clarity_inner = '''                    <div class="apple-slide" id="slide-clarity"
                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;">

                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:var(--space-lg); align-items:center;"
                            class="mobile-stack-card">'''
        
        new_clarity_inner = '''                    <div class="apple-slide" id="slide-clarity"
                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;">

                        <div class="container">
                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:var(--space-lg); align-items:center;"
                            class="mobile-stack-card">'''
        
        if old_clarity_inner in idx:
            idx = idx.replace(old_clarity_inner, new_clarity_inner)
            idx = idx.replace('''                    </div>



                    <!-- MOMENTUM -->''', 
                              '''                        </div>
                    </div>



                    <!-- MOMENTUM -->''')
            print("Wrapped CLARITY content in .container.")

        old_momentum_inner = '''                    <div class="apple-slide" id="slide-momentum"
                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;">

                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:var(--space-lg); align-items:center;"
                            class="mobile-stack-card">'''
        
        new_momentum_inner = '''                    <div class="apple-slide" id="slide-momentum"
                        style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;">

                        <div class="container">
                        <div style=" display:grid; grid-template-columns:1.5fr 1fr; gap:var(--space-lg); align-items:center;"
                            class="mobile-stack-card">'''
        
        if old_momentum_inner in idx:
            idx = idx.replace(old_momentum_inner, new_momentum_inner)
            print("Wrapped MOMENTUM content in .container.")

        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)
        print("\nDone! Sticky scroll should now work correctly.")

    except Exception as e:
        traceback.print_exc()

fix_sticky_scroll()
