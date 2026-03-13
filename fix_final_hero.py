import traceback
import re

def final_hero_polish():
    try:
        # --- 1. Fix Index.html Hero Layout and Subtext ---
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # Fix Tamil Layout Alignment inside H1
        old_hero_title = """<div class="reveal" style="font-family: 'Noto Sans Tamil', sans-serif; font-weight: 700; color: #0D8A74; font-size: clamp(2rem, 4vw, 3.5rem); margin-bottom: 0.5rem; letter-spacing: -0.02em;">உணவே மருந்து.</div>
                    <h1 class="display v2-split-text"
                        style="font-size:var(--text-6xl); line-height:var(--leading-none); opacity:0;">
                        Functional Foods.<br>
                        India's First.</h1>"""

        new_hero_title = """<h1 class="display" style="font-size:var(--text-6xl); line-height:var(--leading-none);">
                        <span class="reveal" style="display:block; font-family: 'Noto Sans Tamil', sans-serif; font-weight: 700; color: #0D8A74; font-size: 0.6em; margin-bottom: 0.15em; letter-spacing: -0.02em; animation-delay: 0.2s;">உணவே மருந்து.</span>
                        <span class="v2-split-text" style="display:block; opacity:0;">Functional Foods.<br>India's First.</span>
                    </h1>"""

        if old_hero_title in idx:
            idx = idx.replace(old_hero_title, new_hero_title)
        else:
            print("Warning: old_hero_title not found exactly. Using regex.")
            pattern_title = re.compile(r'<div class="reveal"[^>]*>உணவே மருந்து\.</div>\s*<h1 class="display v2-split-text"[^>]*>\s*Functional Foods\.<br>\s*India\'s First\.</h1>')
            idx = pattern_title.sub(new_hero_title, idx)

        # Fix Subtext (Remove "supplement pills")
        old_subtext = "Stop relying on synthetic supplement pills. We engineer real, highly-bioavailable functional foods using"
        new_subtext = "We engineer real, highly-bioavailable functional foods using"
        idx = idx.replace(old_subtext, new_subtext)

        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)
            print("Successfully updated index.html hero layout and subtext.")


        # --- 2. Fix Problem.html Subtext ---
        with open(r'e:\OXYBIO\problem.html', 'r', encoding='utf-8') as f:
            prob = f.read()
            
        prob = prob.replace(old_subtext, new_subtext)

        with open(r'e:\OXYBIO\problem.html', 'w', encoding='utf-8') as f:
            f.write(prob)
            print("Successfully updated problem.html subtext.")

    except Exception as e:
        traceback.print_exc()

final_hero_polish()
