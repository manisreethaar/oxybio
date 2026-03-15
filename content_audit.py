"""
Content audit script — extract visible text from each page to review.
Looks for:
1. Old language that doesn't match functional food pivot
2. Fabricated or unverified claims
3. Content that should have been updated but wasn't
"""
import os, re

PAGES = [
    ('index.html', r'e:\OXYBIO\index.html'),
    ('about.html', r'e:\OXYBIO\about.html'),
    ('science.html', r'e:\OXYBIO\science.html'),
    ('problem.html', r'e:\OXYBIO\problem.html'),
    ('careers.html', r'e:\OXYBIO\careers.html'),
    ('blog.html', r'e:\OXYBIO\blog.html'),
    ('blog-origin.html', r'e:\OXYBIO\blog-origin.html'),
    ('blog-bootstrapping.html', r'e:\OXYBIO\blog-bootstrapping.html'),
    ('blog-minerals.html', r'e:\OXYBIO\blog-minerals.html'),
    ('contact.html', r'e:\OXYBIO\contact.html'),
]

# Phrases that signal old/wrong content
RED_FLAGS = [
    'supplement', 'protein powder', 'capsule', 'tablet', 'pill',
    'No compromise',  # old tagline that was removed from meta
    '14 different', '14 facilities', 'visited 14',
    'India first',  # was flagged as wrong
    'first in India',
    'imported solution',  # was old content
    'FSSAI approved',  # may be unverified
    'FDA',
    '100% natural',  # overly generic claim
    'clinically proven',  # need to verify
    'scientifically proven',
    'guaranteed',
]

for name, path in PAGES:
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        content = f.read()

    # Strip tags to get visible text
    text = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<!--.*?-->', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    flags_found = []
    for flag in RED_FLAGS:
        if flag.lower() in text.lower():
            # Get context
            idx = text.lower().find(flag.lower())
            ctx = text[max(0, idx-40):idx+80].strip()
            flags_found.append(f'  "{flag}": ...{ctx}...')

    if flags_found:
        print(f'\n=== {name} ===')
        for f in flags_found:
            print(f)
