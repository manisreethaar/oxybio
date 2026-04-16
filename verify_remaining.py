sci = open('science.html', encoding='utf-8').read()
abt = open('about.html', encoding='utf-8').read()
car = open('careers.html', encoding='utf-8').read()

print("=== science.html ===")
print("Old phrase gone:", "Vitamins don't work in isolation" not in sci)
print("New phrase present:", "biologically coherent form" in sci)

print("\n=== about.html ===")
print("Vitamin D deficient gone:", "Vitamin D deficient" not in abt)
print("New stat present:", "micronutrient deficiencies" in abt)

print("\n=== careers.html ===")
print("Cosmetics R&D gone:", "Cosmetics R" not in car)
print("Bioavailability Testing present:", "Bioavailability Testing" in car)
print("position: sticky in mobile CSS:", "position: sticky" in car)  # should be False
print("box-shadow -20px bleed gone:", "-20px 40px" not in car)
