import os
import glob
from bs4 import BeautifulSoup

def extract_content(filepath):
    print(f"\n--- AUDITING: {os.path.basename(filepath)} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # We want to look at substantial text blocks (h2, h3, h4, p, li)
    # inside the main sections (excluding nav/footer for this deep dive).
    main_tag = soup.find('main')
    if not main_tag:
        main_tag = soup
        
    tags_to_audit = main_tag.find_all(['h2', 'h3', 'h4', 'p'])
    
    for tag in tags_to_audit:
        text = tag.get_text(strip=True)
        if len(text) > 30: # Skip very short labels
            print(f"[{tag.name.upper()}]: {text}")

files_to_audit = [
    'e:/OXYBIO/index.html',
    'e:/OXYBIO/problem.html',
    'e:/OXYBIO/about.html',
    'e:/OXYBIO/science.html',
    'e:/OXYBIO/ingredients.html'
]

for file in files_to_audit:
    extract_content(file)
