import glob
import re

html_files = glob.glob('e:/OXYBIO/*.html')

# Regex for the entire sticky CTA block
sticky_block_regex = re.compile(r'<!-- Mobile Sticky CTA -->\s*<div class="mobile-sticky-cta"[^>]*>.*?</div>', re.DOTALL)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove mobile sticky CTA completely
    content = sticky_block_regex.sub('', content)

    # 2. Strip "magnetic-btn" and "btn-primary" to tone down the slickness
    # A lab should not have magnetic, bouncy red buttons.
    content = content.replace('btn btn-primary magnetic-btn', 'btn btn-outline')
    content = content.replace('btn btn-white magnetic-btn', 'btn btn-outline')
    content = content.replace('btn-primary', 'btn-outline') # For any remaining primary buttons
    content = content.replace('magnetic-btn', '') # for any remaining magnetic scripts

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Aggressive CTAs and sticky buttons obliterated in {len(html_files)} files.")
