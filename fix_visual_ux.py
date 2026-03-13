import traceback

def fix_visual_ux():
    try:
        # 1. Update index.html
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()
            
        # Add font-weight: 700 to Tamil Quote for better rendering
        idx = idx.replace(
            "font-family: 'Noto Sans Tamil', sans-serif; color: #0D8A74; font-size: 0.7em;",
            "font-family: 'Noto Sans Tamil', sans-serif; font-weight: 700; color: #0D8A74; font-size: 0.7em;"
        )
        
        # Bold UVP in index hero
        idx = idx.replace(
            "using traditional millet fermentation and potent medicinal mushrooms",
            "using <strong>traditional millet fermentation</strong> and <strong>potent medicinal mushrooms</strong>"
        )
        
        # Scrub remaining clinical button text
        idx = idx.replace(
            "Read the Clinical Data",
            "Read the Science"
        )
        
        with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
            f.write(idx)
            
        # 2. Update problem.html
        with open(r'e:\OXYBIO\problem.html', 'r', encoding='utf-8') as f:
            prob = f.read()
            
        prob = prob.replace(
            "using traditional millet fermentation and potent medicinal mushrooms",
            "using <strong>traditional millet fermentation</strong> and <strong>potent medicinal mushrooms</strong>"
        )
        
        with open(r'e:\OXYBIO\problem.html', 'w', encoding='utf-8') as f:
            f.write(prob)

        # 3. Update styles.css padding for the header
        with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
            css = f.read()
            
        css = css.replace(
            ".nav-container {\n    display: flex;",
            ".nav-container {\n    display: flex;\n    padding-left: clamp(1rem, 3vw, 2rem);\n    padding-right: clamp(1rem, 3vw, 2rem);"
        )
        
        with open(r'e:\OXYBIO\assets\css\styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
            
        print("Visual UX corrections successfully applied!")
        
    except Exception as e:
        traceback.print_exc()

fix_visual_ux()
