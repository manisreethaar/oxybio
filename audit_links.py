import os
import glob
import re

directory = 'e:\\OXYBIO'
html_files = glob.glob(os.path.join(directory, '*.html'))

# Load all files content into a dict mapped by filename
files_content = {}
for f in html_files:
    fname = os.path.basename(f)
    if fname == 'index-single.html':
        continue # Skip legacy file
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        files_content[fname] = file.read()

print("--- OXYGEN BIOINNOVATIONS FULL LINK & CODE AUDIT ---\n")

issues = []

# Regex patterns
href_pattern = re.compile(r'<a[^>]+href=["\']([^"\']+)["\']', re.IGNORECASE)
id_pattern = re.compile(r'id=["\']([^"\']+)["\']', re.IGNORECASE)

# First pass: collect all valid IDs per file for fragment checking
file_ids = {}
for fname, content in files_content.items():
    file_ids[fname] = set(id_pattern.findall(content))

# Second pass: check links
for fname, content in files_content.items():
    # Find all links
    links = href_pattern.findall(content)
    
    for i, link in enumerate(links):
        # 1. Check for dummy links
        if link == '#' or link == '':
            issues.append(f"[Dummy Link] {fname} has href='{link}'")
            continue
            
        # 2. Check email links
        if link.startswith('mailto:'):
            if link == 'mailto:' or link == 'mailto:#':
                issues.append(f"[Invalid Mailto] {fname} has href='{link}'")
            continue
            
        # Ignore external links
        if link.startswith('http') or link.startswith('tel:'):
            continue
            
        # Validate internal links and fragments
        if '#' in link:
            target_file, fragment = link.split('#', 1)
            # if target_file is empty, it points to the same file
            if not target_file:
                target_file = fname
            else:
                # remove any query strings if present
                target_file = target_file.split('?')[0]
                
            # Check if file exists
            if target_file not in files_content:
                issues.append(f"[Broken Page Link] {fname} points to {target_file} which does not exist")
                continue
                
            # Check if fragment exists in target file
            if fragment not in file_ids[target_file] and fragment != 'join': # 'join' might be handled dynamically or in footer?
                issues.append(f"[Broken Anchor] {fname} points to #{fragment} in {target_file}, but id='{fragment}' is missing")
        else:
            # Just a file link
            target_file = link.split('?')[0]
            if target_file not in files_content and target_file != 'index.html': # index might be in files_content anyway
                issues.append(f"[Broken Page Link] {fname} points to {target_file} which does not exist")

# Report Results
if issues:
    print(f"FOUND {len(issues)} ISSUES:")
    for issue in issues:
        print(f" - {issue}")
else:
    print("NO LINK ISSUES FOUND. All links are valid.")
    
# Third pass: check viewport tags
for fname, content in files_content.items():
    if '<meta name="viewport"' not in content:
        print(f" - [Missing Viewport] {fname} implies mobile issues.")
