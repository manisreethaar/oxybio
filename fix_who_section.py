import sys

with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The "Who We Are" section (id=about-who) still has old chapter-01 and chapter-02 blocks
# inside it (The Hook and The Journey - which belong to "Our Story" section).
# These need to be removed. The section should only have chapter-03 (Founder) and chapter-04 (Our Approach).

# Find the Who We Are section
who_section_start = content.find('id="about-who"')
if who_section_start == -1:
    sys.stderr.write("FAIL: about-who not found\n")
    sys.exit(1)

# Within the Who We Are section, find and remove the duplicate chapter-01 and chapter-02 divs
# These are the old "The Hook" and "The Founder" chapters that got duplicated

# Find "Main Content Chapters" comment inside who section
chapters_start = content.find('<!-- Main Content Chapters -->', who_section_start)
# Find the wrapper div opening
wrapper_open = content.find('<div>', chapters_start)

# Find chapter-03 (the real Founder chapter in this section)
ch03_start = content.find('id="chapter-03"', who_section_start)

# Remove everything between the chapters wrapper div open and chapter-03 start
# but keep the opening <div> tag
if chapters_start != -1 and wrapper_open != -1 and ch03_start != -1:
    # Get everything before the duplicate chapters
    before = content[:wrapper_open + 5]  # include the <div>
    # Get from chapter-03 onwards
    after = content[ch03_start:]
    content = before + '\n                        <!-- The Founder -->\n                        <' + after
    sys.stderr.write("Removed duplicate chapter-01 and chapter-02 from Who We Are section\n")
else:
    sys.stderr.write(f"Could not find markers: chapters_start={chapters_start}, wrapper_open={wrapper_open}, ch03_start={ch03_start}\n")
    sys.exit(1)

# Also fix the chapter-03 display text (was "CHAPTER 01" internally)
content = content.replace(
    'id="chapter-03" class="chapter-section" style="margin-bottom:var(--space-xl);">\n                            <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">\n                                CHAPTER 01',
    'id="chapter-03" class="chapter-section" style="margin-bottom:var(--space-xl);">\n                            <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">\n                                CHAPTER 01'
)

# Fix chapter-04 internal label if needed
# (already should say CHAPTER 04 from original)

with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.write(content)

sys.stderr.write("Done\n")
