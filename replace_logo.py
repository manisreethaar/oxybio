import os

target_dir = r"e:\OXYBIO"
# The string we are looking to replace
old_str_1 = '<span class="logo-bio">Bioinnovations</span>'
old_str_2 = '<span class="logo-bio">Bioinnovations<span'

new_str_svg = '<span class="logo-bio"><svg viewBox="0 0 100 130" class="logo-b-svg" xmlns="http://www.w3.org/2000/svg"><defs><path id="b-path" d="M 25 25 Q 25 0 45 0 L 60 0 C 90 0 92 60 55 60 C 105 55 105 130 60 130 L 45 130 Q 25 130 25 105 Z M 48 20 C 35 20 35 45 48 45 C 60 45 60 20 48 20 Z" fill-rule="evenodd"/><clipPath id="b-clip"><use href="#b-path"/></clipPath></defs><g clip-path="url(#b-clip)"><rect width="100%" height="100%" fill="#0a2e5c"/><ellipse cx="60" cy="10" rx="90" ry="100" fill="#1460aa"/><ellipse cx="40" cy="-20" rx="90" ry="90" fill="#2096d2"/><ellipse cx="20" cy="-40" rx="80" ry="80" fill="#3ac4e7"/></g></svg>ioinnovations</span>'
new_str_svg_2 = '<span class="logo-bio"><svg viewBox="0 0 100 130" class="logo-b-svg" xmlns="http://www.w3.org/2000/svg"><defs><path id="b-path" d="M 25 25 Q 25 0 45 0 L 60 0 C 90 0 92 60 55 60 C 105 55 105 130 60 130 L 45 130 Q 25 130 25 105 Z M 48 20 C 35 20 35 45 48 45 C 60 45 60 20 48 20 Z" fill-rule="evenodd"/><clipPath id="b-clip"><use href="#b-path"/></clipPath></defs><g clip-path="url(#b-clip)"><rect width="100%" height="100%" fill="#0a2e5c"/><ellipse cx="60" cy="10" rx="90" ry="100" fill="#1460aa"/><ellipse cx="40" cy="-20" rx="90" ry="90" fill="#2096d2"/><ellipse cx="20" cy="-40" rx="80" ry="80" fill="#3ac4e7"/></g></svg>ioinnovations</span><span'

count = 0
for filename in os.listdir(target_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        if old_str_1 in content:
            content = content.replace(old_str_1, new_str_svg)
            updated = True
            
        if old_str_2 in content:
            content = content.replace(old_str_2, new_str_svg_2)
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
            count += 1
            
print(f"Total HTML files updated: {count}")
