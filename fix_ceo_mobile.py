import glob
import re
import os

# 1. Update CSS for mobile logo
css_path = r'e:\OXYBIO\assets\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

mobile_fix = """
/* Responsive Logo Fix added via Python */
@media (max-width: 768px) {
    .nav-logo { max-width: 65vw; overflow: hidden; white-space: nowrap; }
    .nav-logo img { height: 28px !important; }
    .nav-logo span { font-size: 1rem !important; }
    /* Ensure hamburger menu isn't pushed out */
    .nav-container { flex-wrap: nowrap !important; }
}
"""
if "Responsive Logo Fix added via Python" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + mobile_fix)


# 2. Update about.html CEO profile
about_path = r'e:\OXYBIO\about.html'
with open(about_path, 'r', encoding='utf-8') as f:
    about = f.read()

about = about.replace('Chief Science Officer', 'Chief Executive Officer')
# Replace the water mark
about = re.sub(r'(>)\s*CSO\s*(</div>)', r'\1CEO\2', about)
# Incubator detail
about = about.replace('TBI-ACE, Hosur', 'TBI - DETI@ACE, Hosur')
# Keep responsibilities the same since user didn't specify.

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(about)


# 3. Update careers.html to Past Requirements
careers_path = r'e:\OXYBIO\careers.html'
with open(careers_path, 'r', encoding='utf-8') as f:
    careers = f.read()

careers = careers.replace('>Open Position<', '>Past Requirement<')
careers = careers.replace('>Open Positions<', '>Past Requirements<')
careers = careers.replace('>Actively Recruiting<', '>Closed<')
careers = careers.replace('View Full Role →', 'Closed')
careers = careers.replace('Apply Now', 'Closed')
# Just in case there are multiple, change the green badge to gray
careers = careers.replace('background:rgba(13, 138, 116, 0.1);', 'background:rgba(100, 100, 100, 0.1);')
careers = careers.replace('box-shadow:0 0 8px #0D8A74;', 'box-shadow:0 0 8px rgba(100,100,100,0.5);')
careers = careers.replace('color:#0D8A74; font-weight:600;">Actively', 'color:#666; font-weight:600;">Closed')
careers = careers.replace('background:#0D8A74;', 'background:#888;')

with open(careers_path, 'w', encoding='utf-8') as f:
    f.write(careers)

# Also update index.html Research Associate card if it exists
index_path = r'e:\OXYBIO\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = idx_content.replace('>Open Position<', '>Past Position<')
idx_content = idx_content.replace('>Actively Recruiting<', '>Closed<')
idx_content = idx_content.replace('View Full Role →', 'Role Closed')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("CEO, Careers, and CSS Mobile fixes applied.")
