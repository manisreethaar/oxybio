ing = open('ingredients.html', encoding='utf-8').read()
print("hot water + ethanol:", 'hot water + ethanol' in ing)
print("Triterpenes:", 'Triterpenes' in ing)
print("beta-glucan:", 'beta-glucan' in ing.lower())
print("duplicate style count:", ing.count('style="word-break'))
print("overflow-wrap count:", ing.count('overflow-wrap'))

car = open('careers.html', encoding='utf-8').read()
print("Follow Our R&D Journey in careers nav:", 'Follow Our R' in car and 'Journey' in car)
