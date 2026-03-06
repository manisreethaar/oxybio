import re
import os

# 1. Update CSS for footer brand logo to prevent layout blowout
css_path = r'e:\OXYBIO\assets\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

footer_mobile_fix = """
/* Safety constraints for footer logo on all viewports */
.footer-brand img {
    height: 32px !important;
    max-width: 100% !important;
    object-fit: contain;
}
.footer-brand span {
    font-size: 1.25rem !important;
}

@media (max-width: 768px) {
    .footer-brand { text-align: left; }
    .footer-brand > a { flex-wrap: nowrap; max-width: 100%; overflow: hidden; }
    .footer-brand img { height: 28px !important; }
    .footer-brand span { 
        font-size: 1.1rem !important; 
        text-overflow: ellipsis; 
        overflow: hidden; 
        white-space: nowrap; 
    }
}
"""

if "Safety constraints for footer logo" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + footer_mobile_fix)

# 2. Update about.html Phase 3 Incubator text
about_path = r'e:\OXYBIO\about.html'
with open(about_path, 'r', encoding='utf-8') as f:
    about = f.read()

# Replace chapter 2 details
about = about.replace('TBI Incubation at ACE, Hosur', 'TBI - DETI@ACE, Hosur')
about = about.replace('Accepted by the Technology Business Incubator', 'Accepted by the TBI - DETI@ACE')

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(about)

print("Footer logo constraint added and About page Phase 3 updated.")
