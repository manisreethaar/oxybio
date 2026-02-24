import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find & remove the orphan duplicate comparison table block (lines 622-690ish)
# It starts with "<!-- Comparison Table Component -->" and ends with "</div>" after the table
start_marker = '<!-- Comparison Table Component -->'
end_marker = None

start_line = None
for i, line in enumerate(lines):
    if start_marker in line:
        start_line = i
        break

if start_line is None:
    print("ERROR: Could not find start marker")
    exit(1)

# Find the closing </div> after the table
depth = 0
end_line = None
for i in range(start_line, len(lines)):
    depth += lines[i].count('<div') - lines[i].count('</div>')
    if i > start_line and depth <= 0:
        end_line = i
        break

print(f"Removing lines {start_line+1} to {end_line+1}")
print("Content being removed:")
print(''.join(lines[start_line:end_line+1])[:300])

# Remove the block
lines = lines[:start_line] + lines[end_line+1:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done removing duplicate table.")
