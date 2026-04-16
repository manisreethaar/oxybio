import re

with open('ingredients.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig_divs_open = html.count('<div')
orig_divs_close = html.count('</div')

# -----------------------------------------------------------------------
# 1. Remove the "EXP_02 Co-factors" section entirely.
#    It lives in a <section ...> block we can identify by the unique text.
# -----------------------------------------------------------------------
targets_sections = [
    "EXP_02 Co-factors",
    "STRESS & RESILIENCE",        # legacy Ashwagandha section heading
    "Ashwagandha",
    "Bacopa monnieri",
    "L-Theanine",
    "Methylcobalamin (B12)",
    "Vitamin D3 + K2",
    "NEUROLOGICAL BASELINE",
    "CALCIUM UTILIZATION",
]

def remove_section_containing(html_str, marker):
    idx = html_str.find(marker)
    if idx == -1:
        return html_str, False
    # Walk backwards to find the opening <section
    sec_start = html_str.rfind('<section', 0, idx)
    if sec_start == -1:
        return html_str, False
    # Now count nesting to find matching </section>
    count = 0
    i = sec_start
    end_idx = -1
    while i < len(html_str):
        if html_str.startswith('<section', i):
            count += 1
            i += 8
        elif html_str.startswith('</section', i):
            count -= 1
            if count == 0:
                end_idx = i + 10  # length of "</section>"
                break
            i += 9
        else:
            i += 1
    if end_idx != -1:
        return html_str[:sec_start] + html_str[end_idx:], True
    return html_str, False

# Remove EXP_02 section (which contains B12 and D3+K2)
html, removed = remove_section_containing(html, "EXP_02 Co-factors")
print(f"EXP_02 section removed: {removed}")

# Remove Stress & Resilience / Ashwagandha section
for marker in ["STRESS & RESILIENCE", "Ashwagandha", "STRESS &amp; RESILIENCE"]:
    html, removed = remove_section_containing(html, marker)
    if removed:
        print(f"Removed section containing: {marker}")
        break

# -----------------------------------------------------------------------
# 2. Fix the About hero padding (image 1 issue)
#    "padding-top:clamp(60px, 10vh, 90px)" on the <section class="hero-section">
#    The left side looks unpadded - the container likely lacks horizontal padding on mobile.
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# 3. Fix "Join Waitlist" still in the About page desktop nav
# -----------------------------------------------------------------------

new_divs_open = html.count('<div')
new_divs_close = html.count('</div')
print(f"DIV balance before: {orig_divs_open - orig_divs_close}")
print(f"DIV balance after:  {new_divs_open - new_divs_close}")

with open('ingredients.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done.")
