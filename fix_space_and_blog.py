import traceback

def fix_all():
    try:
        # ====== Fix 1: Remove 100vh blank space after solution cards ======
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # This is the padding-bottom with 100vh I added that creates the blank space
        old_solution = 'style="background:var(--bg-alt); padding-top: 2rem; padding-bottom: calc(var(--space-lg) + 100vh); position: relative;"'
        new_solution = 'style="background:var(--bg-alt); padding-top: 2rem; padding-bottom: 4rem; position: relative;"'
        
        if old_solution in idx:
            idx = idx.replace(old_solution, new_solution)
            print("FIX 1: Removed 100vh blank space after solution section")
        else:
            print("WARNING FIX 1: Could not find solution section style")
        
        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)

        # ====== Fix 2: Blog - remove fabricated "14 facilities" text ======
        with open(r'e:\OXYBIO\blog-bootstrapping.html', 'r', encoding='utf-8') as f:
            blog = f.read()
        
        # Find and replace the fabricated text - use a broader match to handle encoding differences
        if '14 different third-party manufacturing' in blog:
            blog = blog.replace(
                'I went on what I now call the \'Manufacturer\r\n\r\n                        Rejection Tour\'. I visited 14 different third-party manufacturing facilities across three\r\n\r\n                        states.',
                "I went on what I now call the 'Manufacturer Rejection Tour'. I reached out to multiple third-party manufacturing facilities across several states."
            )
            print("FIX 2: Removed '14 facilities' fabrication")
        elif '14' in blog:
            # Fallback: find the exact line
            lines = blog.split('\n')
            for i, line in enumerate(lines):
                if '14 different third-party' in line or 'visited 14' in line:
                    lines[i] = line.replace('I visited 14 different third-party manufacturing facilities across three', 
                                           'I reached out to multiple third-party manufacturing facilities across several')
                    print(f"FIX 2: Fixed line {i}: {lines[i].strip()[:80]}")
                if 'states.' in line and i > 0 and ('14' in lines[i-1] or 'states' in lines[i-1]):
                    lines[i] = "                        states."
            blog = '\n'.join(lines)
        else:
            print("WARNING FIX 2: '14 facilities' text not found in blog")

        with open(r'e:\OXYBIO\blog-bootstrapping.html', 'w', encoding='utf-8') as f:
            f.write(blog)

    except Exception as e:
        traceback.print_exc()

fix_all()
