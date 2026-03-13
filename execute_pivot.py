import glob
import re
import os

def update_copy():
    html_files = glob.glob(r'e:\OXYBIO\*.html')
    tsx_files = glob.glob(r'e:\OXYBIO\src\components\**\*.tsx', recursive=True)
    all_files = [*html_files, *tsx_files]
    
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # 1. Meta Titles & Descriptions & Generic headers
        content = content.replace(
            "Oxygen Bioinnovations | Precision Nutrition. India's First.",
            "Oxygen Bioinnovations | Radically Absorbable Nutrition. India's First."
        )
        content = content.replace(
            "Precision Nutrition. India's First.",
            "Radically Absorbable Nutrition. India's First."
        )
        content = content.replace(
            "India's first precision nutrition system grounded in biotechnology, indigenous ingredients, and an unbreakable commitment to evidence.",
            "Stop paying for cheap synthetic vitamins your body can't absorb. We use 100% active, highly bioavailable clinical forms backed by public Certificates of Analysis."
        )
        
        # 2. Mega Menu
        content = content.replace(
            "Building India's first precision nutrition system.",
            "Engineering the highest-absorbing clinical nutrition in India."
        )
        content = content.replace(
            "<h4>Evidence-Based</h4>",
            "<h4>Clinical Bioavailability</h4>"
        )
        
        # 3. HTML Footer Description
        footer_regex = r"Precision nutrition for every ambitious Indian\.<br><br>India's first honest precision nutrition\s+system\. Built on millet, mushrooms, and real science\."
        new_footer_html = "Radically bioavailable nutrition for every ambitious Indian.<br><br>India's first honest clinical nutrition\n\n                    system. Built on active forms, verified extracts, and real science."
        content = re.sub(footer_regex, new_footer_html, content)
        
        # 3b. React Footer.tsx Overrides
        content = content.replace(
            "Precision nutrition for every ambitious Indian.",
            "Radically bioavailable nutrition for every ambitious Indian."
        )
        content = content.replace(
            "India's first honest precision nutrition system. Built on millet, mushrooms, and real science.",
            "India's first honest clinical nutrition system. Built on active forms, verified extracts, and real science."
        )
        
        # 4. Hero on Index
        if 'index.html' in file:
            hero_regex = r"Ancient(?:\s*<br>\s*|\s+)Ingredients\.(?:\s*<br>\s*|\s+)Modern Science\."
            new_hero_html = "Radical\n\n                        Absorption.\n\n                        India's First."
            content = re.sub(hero_regex, new_hero_html, content, count=1)
            
            # index.html subtext
            index_subtext_regex = r"India is building its first precision nutrition system\. Built on Millet, Medicinal Mushrooms,\s+and decades of scientific research\. Designed for ambitious Indians who deserve better than what\s+currently exists\."
            new_index_subtext = "90% of Indian supplements use the cheapest, inactive forms of vitamins (like Cyanocobalamin) and rock-dust minerals (like Oxides). Your body absorbs less than 10% of them. We fixed it."
            content = re.sub(index_subtext_regex, new_index_subtext, content)
            
        # 5. Problem page intro
        if 'problem.html' in file:
            problem_regex = r"Every formulation decision has a reason\. Every reason has a reference\. Every reference is\s+available to you\."
            new_problem = "90% of Indian supplements use the cheapest, inactive forms of vitamins (like Cyanocobalamin) and rock-dust minerals (like Oxides). Your body absorbs less than 10% of them. We fixed it."
            content = re.sub(problem_regex, new_problem, content)

        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated copy in {os.path.basename(file)}")

update_copy()
