import glob, re

# Replace the entire nav-logo anchor content with just the image tag
# The logo image sits in the same height as the existing text logo

IMG_LOGO = '<img src="assets/images/logo-full.png" alt="Oxygen Bioinnovations" style="height:36px; width:auto; display:block;">'

html_files = glob.glob('e:/OXYBIO/*.html')
replaced = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match the entire nav-logo anchor tag with all its children
    # Replace the inner content with just the image
    new_content = re.sub(
        r'(<a [^>]*class="nav-logo"[^>]*>).*?(</a>)',
        lambda m: m.group(1) + IMG_LOGO + m.group(2),
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        replaced += 1

print(f"Replaced logo in {replaced} HTML files.")
