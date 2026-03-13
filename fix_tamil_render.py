import traceback

def fix_tamil_rendering():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # The exact string we want to replace
        old_hero = """<h1 class="display v2-split-text"
                        style="font-size:var(--text-6xl); line-height:var(--leading-none); opacity:0;"><span style="font-family: 'Noto Sans Tamil', sans-serif; font-weight: 700; color: #0D8A74; font-size: 0.7em;">உணவே மருந்து.</span><br>

                        Functional Foods.

                        India's First.</h1>"""
        
        # New structure: Tamil quote is outside the h1 so the JS doesn't destroy its spans
        new_hero = """<div class="reveal" style="font-family: 'Noto Sans Tamil', sans-serif; font-weight: 700; color: #0D8A74; font-size: clamp(2rem, 4vw, 3.5rem); margin-bottom: 0.5rem; letter-spacing: -0.02em;">உணவே மருந்து.</div>
                    <h1 class="display v2-split-text"
                        style="font-size:var(--text-6xl); line-height:var(--leading-none); opacity:0;">
                        Functional Foods.<br>
                        India's First.</h1>"""
                        
        if old_hero in content:
            content = content.replace(old_hero, new_hero)
            with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully extracted Tamil quote to protect it from JS splitting!")
        else:
            print("Could not find the exact old hero string. Attempting regex...")
            import re
            
            # Alternative using regex if exact match fails due to whitespace
            pattern = re.compile(r'<h1 class="display v2-split-text"[^>]*><span[^>]*>உணவே மருந்து\.</span><br>\s*Functional Foods\.\s*India\'s First\.</h1>', re.DOTALL)
            if pattern.search(content):
                content = pattern.sub(new_hero, content)
                with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Successfully extracted Tamil quote using regex!")
            else:
                print("Regex failed to find the block as well.")
                
    except Exception as e:
        traceback.print_exc()

fix_tamil_rendering()
