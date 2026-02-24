import os
import glob

# 1. FIX PADDING ON MAIN BLOG PAGE
with open('e:\\OXYBIO\\blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Reduce gap between hero and first bento post
html = html.replace(
    '<section class="structure-section" style="padding-top:140px; border-bottom:none;">',
    '<section class="structure-section" style="padding-top:140px; padding-bottom:2rem; border-bottom:none;">'
)
html = html.replace(
    '<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border);">',
    '<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border); padding-top:4rem;">'
)

with open('e:\\OXYBIO\\blog.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed blog hero spacing.")


# 2. ALIGN & JUSTIFY TEXT IN ALL BLOG ARTICLES
blog_files = glob.glob('e:\\OXYBIO\\blog-*.html')

old_style = """.blog-content p { margin-bottom: 2rem; font-size: 1.15rem; line-height: 1.8; color: var(--text-main); }
        .blog-content h3 { font-family: var(--font-serif); font-size: 2rem; margin-top: 3.5rem; margin-bottom: 1.5rem; line-height: 1.3; }"""

new_style = """/* Enforce structured, justified typography for reading */
        .blog-content { max-width: 680px; margin: 0 auto; }
        .blog-content p { 
            margin-bottom: 2rem; 
            font-size: 1.15rem; 
            line-height: 1.85; 
            color: var(--text-main); 
            text-align: justify; 
            hyphens: auto; 
            -webkit-hyphens: auto; 
            text-justify: inter-word;
        }
        .blog-content h3 { 
            font-family: var(--font-serif); 
            font-size: 2rem; 
            margin-top: 3.5rem; 
            margin-bottom: 1.5rem; 
            line-height: 1.3; 
            color: var(--text-main); 
            text-align: left;
        }"""

for file_path in blog_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We replace the CSS block to format existing pages
        if old_style in content:
            content = content.replace(old_style, new_style)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated typography in {os.path.basename(file_path)}")
        else:
            print(f"Could not find exact CSS match in {os.path.basename(file_path)}, skipping.")
    except Exception as e:
        print(f"Error on {file_path}: {e}")

print("Applied typography updates to all articles.")
