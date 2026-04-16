import re

with open('ingredients.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig_len = len(html)

def remove_div_by_id(html_str, div_id):
    """Remove <div id="X" ...> ... </div> block."""
    marker = f'id="{div_id}"'
    idx = html_str.find(marker)
    if idx == -1:
        return html_str, False
    div_start = html_str.rfind('<div', 0, idx)
    if div_start == -1:
        return html_str, False
    count = 0; i = div_start; end_idx = -1
    while i < len(html_str):
        if html_str.startswith('<div', i): count += 1; i += 4
        elif html_str.startswith('</div>', i):
            count -= 1
            if count == 0: end_idx = i + 6; break
            i += 6
        else: i += 1
    if end_idx != -1:
        return html_str[:div_start] + html_str[end_idx:], True
    return html_str, False

def remove_div_containing_text(html_str, marker, keep_if=None):
    """Remove innermost <div> containing marker, skipping if keep_if text also present."""
    idx = html_str.find(marker)
    if idx == -1:
        return html_str, False
    div_start = html_str.rfind('<div', 0, idx)
    if div_start == -1:
        return html_str, False
    count = 0; i = div_start; end_idx = -1
    while i < len(html_str):
        if html_str.startswith('<div', i): count += 1; i += 4
        elif html_str.startswith('</div>', i):
            count -= 1
            if count == 0: end_idx = i + 6; break
            i += 6
        else: i += 1
    if end_idx != -1:
        block = html_str[div_start:end_idx]
        if keep_if and any(k in block for k in keep_if):
            print(f"SKIPPED '{marker}' -- block has keep markers")
            return html_str, False
        return html_str[:div_start] + html_str[end_idx:], True
    return html_str, False

# 1. Remove entire baseline (B12 + D3+K2) div block by ID
html, removed = remove_div_by_id(html, 'baseline')
print(f"Remove #baseline block: {removed}")

# 2. Remove adaptogens div block (Ashwagandha)
html, removed = remove_div_by_id(html, 'adaptogens')
print(f"Remove #adaptogens block: {removed}")

# 3. Remove any remaining D3 card
while "D3 + K2" in html or "Vitamin D3" in html:
    target = "D3 + K2" if "D3 + K2" in html else "Vitamin D3"
    html, removed = remove_div_containing_text(html, target, keep_if=['Lion', 'Cordyceps', 'Ragi', 'Lion\u2019s Mane'])
    print(f"Remove '{target}' card: {removed}")
    if not removed:
        break

# 4. Remove Bacopa if still present
while "Bacopa monnieri" in html:
    html, removed = remove_div_containing_text(html, "Bacopa monnieri", keep_if=['Lion', 'Cordyceps', 'Ragi'])
    print(f"Remove Bacopa: {removed}")
    if not removed: break

# 5. Remove Ashwagandha text if still present
while "Ashwagandha" in html:
    html, removed = remove_div_containing_text(html, "Ashwagandha", keep_if=['Lion', 'Cordyceps', 'Ragi'])
    print(f"Remove Ashwagandha: {removed}")
    if not removed: break

# 6. Remove orphaned comment HTML markers
html = re.sub(r'\s*<!-- Category: Baseline Protocol.*?-->', '', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Category: Synthesis Stack.*?-->', '', html, flags=re.DOTALL)

# 7. Fix remaining Waitlist and dual-extract strings
html = re.sub(r'>Join[\s\n]+Waitlist<', '>Follow the Build<', html)
html = html.replace('>Join Waitlist<', '>Follow the Build<')

# Safety check
for must_have in ['Lion', 'Cordyceps', 'Ragi']:
    if must_have not in html:
        print(f"CRITICAL ERROR: '{must_have}' is missing! Aborting.")
        exit(1)

for must_not in ['L-Theanine', 'Methylcobalamin (B12)', 'Vitamin D3 + K2', 'Ashwagandha', 'Bacopa monnieri']:
    if must_not in html:
        print(f"WARNING: '{must_not}' still present")

print(f"\nDone. {orig_len} -> {len(html)} chars")
print("Markers remaining:", [h for h in ['Lion','Cordyceps','Reishi','Ragi','Bacopa','L-Theanine','Ashwagandha','B12','D3'] if h in html])

with open('ingredients.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Written OK")
