import traceback

def rewrite_deep_home():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()
            
        original = idx
        
        # 1. The Problem Area
        idx = idx.replace(
            "You are probably<br>nutritionally deficient.", 
            "You are probably<br>running on empty."
        )
        idx = idx.replace(
            "Indian health drinks fail label claims", 
            "Modern Indian diets lack functional density"
        )
        idx = idx.replace(
            "Most Indian health drinks are primarily sugar with token doses\n\n                                of vitamins your body cannot absorb.", 
            "Most Indian quick-foods and snacks are primarily empty calories\n\n                                lacking the bioavailable nutrients your body actually needs."
        )
        idx = idx.replace(
            "Cheap synthetic forms, under-dosed actives,\n\n                                misleading labels.",
            "Highly processed grains, synthetic additives,\n\n                                and misleading labels."
        )

        # 2. The Solution Area (The 3 Formulas)
        idx = idx.replace("Covers 50% of your daily nutrient needs", "Dense bio-fermented nutritional baseline")
        idx = idx.replace("22 Chelated Nutrients", "Active Millet Matrix")
        idx = idx.replace("Active B Vitamins", "Cognitive Mushroom Matrix")
        idx = idx.replace("Electrolytes", "Fermented Performance Matrix")
        idx = idx.replace("Three precision formulas.", "Three functional food formulas.")

        # 3. The Science Area
        idx = idx.replace(
            "Active forms<br>only.",
            "Active Food<br>Matrix."
        )
        
        # Replace the paragraph about synthetic vitamins
        old_science_p = """Most products use the cheapest permitted form. We use

                                    Methylcobalamin, Pyridoxal-5-Phosphate, 5-MTHF Folate, and Albion TRAACS®

                                    Chelated Minerals &mdash; the forms your body actually absorbs."""
                                    
        new_science_p = """We do not use isolated synthetic vitamins. We use

                                    traditional biological fermentation to unlock the bound nutrients in Indian

                                    millets, making them 100% bio-available to your cells."""
        
        if old_science_p in idx:
            idx = idx.replace(old_science_p, new_science_p)
        else:
            print("Could not find exact science paragraph. Trying single-line replace...")
            # fallback if linebreaks differ
            import re
            idx = re.sub(
                r"Most products use the cheapest permitted form.*?Chelated Minerals &mdash; the forms your body actually absorbs\.",
                "We do not use isolated synthetic vitamins. We use traditional biological fermentation to unlock the bound nutrients in Indian millets, making them 100% bio-available to your cells.",
                idx, flags=re.DOTALL
            )
            
        # 4. The Transparency Table
        idx = idx.replace("Vitamin Forms", "Base Ingredients")
        idx = idx.replace("Active (bioavailable) Forms", "Fermented Millet & Mushrooms")
        idx = idx.replace("Cheapest Synthetic Forms", "Highly Processed Flours")
        
        idx = idx.replace("Vitamin B12", "Nutrient Delivery")
        idx = idx.replace("Methylcobalamin", "Unlocked via Fermentation")
        idx = idx.replace("Cyanocobalamin", "Bound / Indigestible Forms")
        
        idx = idx.replace('<div class="duel-category">Minerals</div>', '<div class="duel-category">Processing Method</div>')
        idx = idx.replace("Chelated TRAACS® Amino Acid", "Biological Fermentation (48hrs)")
        idx = idx.replace("Oxide / Sulfate Forms", "Chemical Heat Extraction")
        
        if idx != original:
            with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
                f.write(idx)
            print("Successfully rewrote deep homepage copy!")
        else:
            print("No changes made. Check the string matching.")
            
    except Exception as e:
        traceback.print_exc()

rewrite_deep_home()
