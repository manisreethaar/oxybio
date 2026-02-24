
import re

# ============================================================
# FIX 1: Fix broken Rupee symbol &Ropf; -> ₹
# FIX 2: Remove duplicate inline comparison table in science section
# FIX 3: Remove orphaned </div></div></section> at lines 623-625
# FIX 4: Fix about.html duplicate class attribute
# ============================================================

# --- index.html fixes ---
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# Fix 1: Broken rupee symbol
content = content.replace('&Ropf;', '&#8377;')
content = content.replace('Cost diff: only &#8377;2/serving', 'Cost diff: only ₹2/serving')
# Also fix any literal broken Ropf
content = content.replace('&Ropf;2/serving', '₹2/serving')

# Fix 3: Remove the orphaned closing divs/section after science section
# These are the lone </div></div></section> at the 3 blank lines + closing block
# Pattern: blank lines followed by </div>\n        </div>\n        </section>
orphan_pattern = r'\n\n\n\n\n\n\n        </div>\n        </div>\n        </section>'
if orphan_pattern in content:
    content = content.replace(orphan_pattern, '')
    print("Fixed orphan closing tags (multi-newline pattern)")
else:
    # Try simpler pattern
    orphan_pattern2 = '\n\n\n\n\n\n\n        </div>\n        </div>\n        </section>'
    simpler = '        </div>\n        </div>\n        </section>'
    # Find after the science section closes
    science_close = '</section>\n\n\n\n\n\n\n        </div>\n        </div>\n        </section>'
    if science_close in content:
        content = content.replace(science_close, '</section>')
        print("Fixed orphan closing tags (science_close pattern)")
    else:
        # Find and count orphaned closing divs near science section
        idx = content.find('<section style="padding: 6rem 0; border-bottom:1px solid var(--border);">')
        if idx != -1:
            close_idx = content.find('</section>', idx)
            if close_idx != -1:
                snippet = content[close_idx:close_idx+200]
                print(f"After science close: {repr(snippet)}")

# Fix 2: Remove the FIRST comparison table (inside science section, lines 571-613)
# Keep the DUEL section comparison, remove the old inline one
old_table_pattern = r'\s*<!-- Comparison Table — Premium Black-Header Design -->\s*<div style="border:1px solid var\(--border\); border-radius:20px; overflow:hidden;">.*?</div>\s*\n\s*</div>\s*\n\s*</section>'
match = re.search(old_table_pattern, content, re.DOTALL)
if match:
    # Replace the whole section ending (table + section close) with just section close
    section_end = '\n                </div>\n            </section>'
    content = content[:match.start()] + section_end + content[match.end():]
    print("Removed duplicate inline comparison table from science section")
else:
    print("Could not find inline comparison table pattern")
    # Manual approach - find "Comparison Table — Premium Black-Header Design" and remove through </section>
    marker = '<!-- Comparison Table — Premium Black-Header Design -->'
    marker_idx = content.find(marker)
    if marker_idx != -1:
        # Find the matching section end
        section_end_search = content.find('</section>', marker_idx)
        if section_end_search != -1:
            # Replace from marker to end of that section
            content = content[:marker_idx] + '\n                </div>\n            </section>' + content[section_end_search + len('</section>'):]
            print(f"Removed comparison table starting at {marker_idx}")

# Fix: 3PM -> 3 pm 
content = content.replace('dreaded 3PM crash', 'dreaded 3 pm crash')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

new_len = len(content)
print(f"index.html: {original_len} -> {new_len} bytes (diff: {new_len - original_len})")

# --- about.html fixes ---
with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix duplicate class attribute on values section grid div
# <div class="reveal" style="display:grid..." class="mobile-stack">
# The second class= is ignored; replace with a combined class
content = content.replace(
    'style="display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:end; margin-bottom:4rem;"\n                    class="mobile-stack"',
    'style="display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:end; margin-bottom:4rem;"'
)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("about.html: fixed duplicate class attribute")
print("All fixes applied!")
