import traceback

def revert_bad_changes():
    try:
        html_path = r'e:\OXYBIO\index.html'
        with open(html_path, 'r', encoding='utf-8') as f:
            idx = f.read()

        # 1. Remove min-height: 80vh from sticky cards — this was making the page impossibly long
        idx = idx.replace(
            'style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10; min-height: 80vh;"',
            'style="position:sticky; top:80px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 10;"'
        )
        idx = idx.replace(
            'style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;"',
            'style="position:sticky; top:80px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 20; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);"'
        )
        idx = idx.replace(
            'style="position:sticky; top:120px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05); min-height: 80vh;"',
            'style="position:sticky; top:80px; background:var(--bg-alt); padding: 2rem 0 4rem; z-index: 30; border-top: 1px solid var(--border); box-shadow: 0 -20px 40px rgba(0,0,0,0.05);"'
        )

        print("Removed min-height: 80vh from sticky cards")
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(idx)

    except Exception as e:
        traceback.print_exc()

def fix_css():
    try:
        css_path = r'e:\OXYBIO\assets\css\styles.css'
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()

        # 2. Remove .structure-section { overflow: clip } — completely breaks page scrolling on all sections
        css = css.replace('.structure-section { overflow: clip !important; }', '/* structure-section overflow removed */')

        # 3. Fix the hero padding CSS which should only override .page-hero, not all sections
        # Also ensure animations don't conflict
        # The reveal class animations — make them smoother
        old_animations = '''@keyframes tamilReveal {
            0% { opacity: 0; transform: translateY(40px); filter: blur(10px); }
            100% { opacity: 1; transform: translateY(0); filter: blur(0); }
        }'''
        new_animations = '''@keyframes tamilReveal {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }'''
        if old_animations in css:
            css = css.replace(old_animations, new_animations)
            print("Smoothed tamilReveal animation")

        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css)
            
        print("Removed .structure-section overflow: clip")

    except Exception as e:
        traceback.print_exc()

revert_bad_changes()
fix_css()
