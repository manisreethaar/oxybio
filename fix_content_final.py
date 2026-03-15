"""
Final content corrections — only confirmed real issues:
1. blog-bootstrapping.html: Remove fabricated "14 different third-party facilities" - using bytes to avoid encoding
2. blog.html: Fix page title (duplicates homepage)
3. blog.html: Remove unused Space Mono Google Font import
"""
import os

# ===== FIX 1: blog-bootstrapping.html - fabricated "14 facilities" claim =====
path = r'e:\OXYBIO\blog-bootstrapping.html'
with open(path, 'rb') as f:
    raw = f.read()

# Find and replace in bytes to avoid any encoding mismatch
old_text = b"Rejection Tour'. I visited 14 different third-party manufacturing facilities across three\r\n\r\n                        states."
new_text = b"Rejection Tour'. I reached out to multiple third-party manufacturing facilities across several states."

if old_text in raw:
    raw = raw.replace(old_text, new_text)
    with open(path, 'wb') as f:
        f.write(raw)
    print("FIX 1: Removed fabricated '14 facilities' claim from blog-bootstrapping.html")
else:
    # Try with \n instead of \r\n
    old_text2 = b"Rejection Tour'. I visited 14 different third-party manufacturing facilities across three\n\n                        states."
    if old_text2 in raw:
        raw = raw.replace(old_text2, new_text)
        with open(path, 'wb') as f:
            f.write(raw)
        print("FIX 1: Removed fabricated '14 facilities' claim (LF variant)")
    else:
        # Try single line
        old_text3 = b"I visited 14 different third-party manufacturing facilities across three"
        new_text3 = b"I reached out to multiple third-party manufacturing facilities across several"
        if old_text3 in raw:
            raw = raw.replace(old_text3, new_text3)
            # Also fix "states" on next line
            raw = raw.replace(b"                        states. Every single", b"                        states. Every single")
            with open(path, 'wb') as f:
                f.write(raw)
            print("FIX 1: Removed fabricated '14 facilities' (single-line match)")
        else:
            print("WARNING: Could not find '14 facilities' text in binary")
            # Print surrounding context for diagnosis
            idx = raw.find(b'14 different')
            if idx != -1:
                print(f"  Found at byte {idx}: {raw[idx-10:idx+60]}")

# ===== FIX 2: blog.html - page title =====
path2 = r'e:\OXYBIO\blog.html'
with open(path2, encoding='utf-8') as f:
    blog = f.read()

old_title = '<title>Oxygen Bioinnovations | Advanced Functional Foods. Powered by Fermentation.</title>'
new_title = '<title>Journal | Oxygen Bioinnovations</title>'
if old_title in blog:
    blog = blog.replace(old_title, new_title)
    print("FIX 2: Fixed blog.html page title")

# ===== FIX 3: blog.html - remove Space Mono from font import =====
old_font_import = "family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap"
new_font_import = "display=swap"
if 'Space+Mono' in blog:
    # Remove the Space Mono part from the font URL
    import re
    blog = re.sub(r'&?family=Space\+Mono[^&"]*', '', blog)
    print("FIX 3: Removed Space Mono from blog.html font import")

with open(path2, 'w', encoding='utf-8') as f:
    f.write(blog)

# ===== FIX 4: All blog pages - fix duplicate homepage title if any  =====
for fname in ['blog-origin.html', 'blog-bootstrapping.html', 'blog-minerals.html']:
    fpath = os.path.join(r'e:\OXYBIO', fname)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    if '<title>Oxygen Bioinnovations | Advanced Functional Foods' in content:
        # These blog pages should have their article title in the page title
        import re
        h1 = re.search(r'<h1[^>]*>\s*([^<]{10,80})', content)
        if h1:
            article_title = h1.group(1).strip()[:60]
            old_t = re.search(r'<title>[^<]+</title>', content)
            if old_t:
                content = content.replace(old_t.group(0), f'<title>{article_title} | Oxygen Bioinnovations</title>')
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"FIX 4: Updated {fname} title to: {article_title[:40]}...")

print("\nAll content fixes applied.")
