import sys

with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove Core Values section: lines 305-404 (1-indexed), which is 304-403 (0-indexed)
# Confirmed: section id="about-values" starts at line 305, ends at line 403 with </section>
core_values_start = 304   # 0-indexed
core_values_end = 402     # 0-indexed inclusive

new_lines = lines[:core_values_start] + lines[core_values_end + 1:]

# Fix orphaned </main> tags — find all, keep only last before footer
main_indices = [i for i, l in enumerate(new_lines) if l.strip() == '</main>']
footer_idx = next((i for i, l in enumerate(new_lines) if '<footer' in l), None)

if footer_idx:
    main_before_footer = [i for i in main_indices if i < footer_idx]
    if len(main_before_footer) > 1:
        to_remove = set(main_before_footer[:-1])
        new_lines = [l for i, l in enumerate(new_lines) if i not in to_remove]

with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

sys.stderr.write("Done\n")
