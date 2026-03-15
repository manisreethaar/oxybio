"""
Correct faq.html content by removing all references to "cosmetics" and "bio-cosmetics".
Oxygen Bioinnovations is a functional food / fermentation company.
"""
import os

path = r'e:\OXYBIO\faq.html'
with open(path, encoding='utf-8') as f:
    faq = f.read()

fixes = [
    (
        "probiotic-based food products,\n\n                                        bio-cosmetics, and nutraceuticals",
        "bio-fermented functional foods\n\n                                        and nutraceuticals"
    ),
    (
        "probiotic-based food products,\r\n\r\n                                        bio-cosmetics, and nutraceuticals",
        "bio-fermented functional foods\r\n\r\n                                        and nutraceuticals"
    ),
    (
        "probiotic formulations for food or cosmetic applications",
        "bio-fermented functional food formulations"
    ),
    (
        "(food science + cosmetics +\n\n                                        microbiology)",
        "(food science + fermentation +\n\n                                        microbiology)"
    ),
    (
        "(food science + cosmetics +\r\n\r\n                                        microbiology)",
        "(food science + fermentation +\r\n\r\n                                        microbiology)"
    ),
    (
        "Biochemistry, or Cosmetic Science",
        "or Biochemistry"
    ),
    (
        "Food or cosmetic formulation development",
        "Functional food formulation development"
    ),
    (
        "food, cosmetics, and human health",
        "functional foods, fermentation, and human health"
    ),
    (
        "Probiotic food and cosmetic formulation",
        "Bio-fermented functional food formulation"
    )
]

changed = False
for old, new in fixes:
    if old in faq:
        faq = faq.replace(old, new)
        changed = True
        print(f"Fixed: {old.strip()[:40]}... -> {new.strip()[:40]}...")

if changed:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(faq)
    print("\nFAQ content successfully updated.")
else:
    print("\nNo matching text found to fix.")
