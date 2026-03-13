import glob
import re
import os

def execute_functional_food_pivot():
    html_files = glob.glob(r'e:\OXYBIO\*.html')
    tsx_files = glob.glob(r'e:\OXYBIO\src\components\**\*.tsx', recursive=True)
    all_files = [*html_files, *tsx_files]
    
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # 1. Meta Titles & Descriptions
        content = content.replace(
            "Oxygen Bioinnovations | Radically Absorbable Nutrition. India's First.",
            "Oxygen Bioinnovations | Advanced Functional Foods. Powered by Fermentation."
        )
        content = content.replace(
            "Stop paying for cheap synthetic vitamins your body can't absorb. We use 100% active, highly bioavailable clinical forms backed by public Certificates of Analysis.",
            "Real food built for absolute performance. We combine traditional millet fermentation with medicinal mushrooms for athletic regeneration, enhanced memory, and active professionals."
        )
        
        # 2. Mega Menu
        content = content.replace(
            "Engineering the highest-absorbing clinical nutrition in India.",
            "Engineering India's first bio-fermented functional foods."
        )
        content = content.replace(
            "<h4>Clinical Bioavailability</h4>",
            "<h4>The Science of Fermentation</h4>"
        )
        content = content.replace(
            "Active forms, verified extracts, and clinical proof.",
            "Unlocking millet bioavailability and mushroom fortification."
        )
        
        # 3. HTML Footer Description
        footer_regex = r"Radically bioavailable nutrition for every ambitious Indian\.<br><br>India's first honest clinical nutrition\s+system\. Built on active forms, verified extracts, and real science\."
        new_footer_html = "Advanced functional foods for every ambitious Indian.<br><br>India's first bio-fermented nutrition\n\n                    system. Built on active millets, medicinal mushrooms, and real food science."
        content = re.sub(footer_regex, new_footer_html, content)
        
        # 3b. React Footer.tsx Overrides
        content = content.replace(
            "Radically bioavailable nutrition for every ambitious Indian.",
            "Advanced functional foods for every ambitious Indian."
        )
        content = content.replace(
            "India's first honest clinical nutrition system. Built on active forms, verified extracts, and real science.",
            "India's first bio-fermented nutrition system. Built on active millets, medicinal mushrooms, and real food science."
        )
        
        # 4. Hero on Index
        if 'index.html' in file:
            hero_regex = r"Radical\s+Absorption\.\s+India's First\."
            new_hero_html = "<span style=\"font-family: 'Noto Sans Tamil', sans-serif; color: #0D8A74; font-size: 0.7em;\">உணவே மருந்து.</span><br>\n\n                        Functional Foods.\n\n                        India's First."
            content = re.sub(hero_regex, new_hero_html, content, count=1)
            
            # Additional Font Import for Noto Sans Tamil
            if 'Noto+Sans+Tamil' not in content:
                content = content.replace(
                    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
                    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n\n    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@600;700&display=swap" rel="stylesheet">'
                )
            
            # index.html subtext
            index_subtext_regex = r"90% of Indian supplements use the cheapest, inactive forms of vitamins \(like Cyanocobalamin\) and rock-dust minerals \(like Oxides\)\. Your body absorbs less than 10% of them\. We fixed it\."
            new_index_subtext = "Stop relying on synthetic supplement pills. We engineer real, highly-bioavailable functional foods using traditional millet fermentation and clinical medicinal mushrooms—targeted for memory, athletic recovery, and on-the-go professionals."
            content = re.sub(index_subtext_regex, new_index_subtext, content)
            
        # 5. Problem page intro
        if 'problem.html' in file:
            problem_regex = r"90% of Indian supplements use the cheapest, inactive forms of vitamins \(like Cyanocobalamin\) and rock-dust minerals \(like Oxides\)\. Your body absorbs less than 10% of them\. We fixed it\."
            new_problem = "Stop relying on synthetic supplement pills. We engineer real, highly-bioavailable functional foods using traditional millet fermentation and clinical medicinal mushrooms—targeted for memory, athletic recovery, and on-the-go professionals."
            content = re.sub(problem_regex, new_problem, content)

        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated functional food copy in {os.path.basename(file)}")

execute_functional_food_pivot()
