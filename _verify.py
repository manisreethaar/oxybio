import os
pages = ['index.html','about.html','science.html','careers.html','blog.html','contact.html','faq.html','ingredients.html','problem.html','privacy.html','terms.html','life.html']
BASE = r'e:\OXYBIO-WEBSITE'
for p in pages:
    path = os.path.join(BASE, p)
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            html = f.read()
        has_investors = 'investors.html' in html
        has_canonical = 'canonical' in html
        has_favicon = 'rel="icon"' in html
        has_mobile_inv = 'Investors' in html
        print(f"{p}: inv_nav={has_investors}, canonical={has_canonical}, favicon={has_favicon}, mobile_inv={has_mobile_inv}")
    else:
        print(f"{p}: NOT FOUND")
