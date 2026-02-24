import os
import re

components_dir = r"e:\OXYBIO\src\components\home"

def strip_framer_motion_stagger(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all complex whileInView logic simply by changing it to basic opacity fade with no translation
    # or just remove Framer motion for internal cards entirely.
    
    # 1. Remove giant blurs which destroy fill rate
    content = re.sub(r'blur-\[.*?\]', 'blur-sm', content) # tone down all giant blur to small
    content = re.sub(r'blur-2xl', 'blur-sm', content)
    content = re.sub(r'blur-3xl', 'blur-sm', content)
    
    # 2. Revert TrustBar to pure CSS marquee instead of framer motion to prevent frame drops
    if 'TrustBar.tsx' in filepath:
        content = content.replace('motion.div', 'div')
        content = re.sub(r'animate=\{\{(.*?)\}\}', '', content)
        content = re.sub(r'transition=\{\{(.*?)\}\}', '', content, flags=re.DOTALL)
        content = content.replace('className="flex whitespace-nowrap items-center will-change-transform"', 
                                  'className="flex whitespace-nowrap items-center animate-[marquee_25s_linear_infinite]"')

    # 3. Simplify animations in other files
    if 'Problem.tsx' in filepath or 'Solution.tsx' in filepath or 'Science.tsx' in filepath:
        # Instead of heavy stagger on cards, just change them to simple divs
        content = content.replace('<motion.div', '<div')
        content = content.replace('</motion.div>', '</div>')
        content = re.sub(r'initial=\{\{.*?\}\}', '', content)
        content = re.sub(r'whileInView=\{\{.*?\}\}', '', content)
        content = re.sub(r'viewport=\{\{.*?\}\}', '', content)
        content = re.sub(r'transition=\{\{.*?\}\}', '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir(components_dir):
    if filename.endswith(".tsx"):
        filepath = os.path.join(components_dir, filename)
        strip_framer_motion_stagger(filepath)

# Also fix index.css to add marquee and remove Lenis
css_path = r"e:\OXYBIO\src\index.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Remove lenis completely
css_content = re.sub(r'html\.lenis.*?\}', '', css_content, flags=re.DOTALL)
css_content = re.sub(r'\.lenis.*?\}', '', css_content, flags=re.DOTALL)

if '@keyframes marquee' not in css_content:
    css_content += '''
@layer utilities {
  @keyframes marquee {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-33.33%); }
  }
}
'''

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Simplified aggressively.")
