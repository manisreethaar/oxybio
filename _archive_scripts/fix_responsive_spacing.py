import re

css_path = 'e:\\OXYBIO\\assets\\css\\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# 1. Add the missing var(--space-2xl) to the main :root
if '--space-2xl:' not in css_content:
    css_content = css_content.replace('--space-xl: 8rem;', '--space-xl: 8rem;\n    --space-2xl: 12rem;')

# 2. Add global responsive spacing variables for Mobile and Tablet
responsive_variables = """
/* --- Strict Responsive Spacing Overrides --- */
@media (max-width: 1024px) {
    :root {
        --space-xl: 6rem;
        --space-2xl: 8rem;
    }
}

@media (max-width: 768px) {
    :root {
        --space-md: 1.5rem;
        --space-lg: 2.5rem;
        --space-xl: 3.5rem;
        --space-2xl: 5rem;
        --section-py: 4.5rem;
    }
}
"""

if 'Strict Responsive Spacing Overrides' not in css_content:
    # Insert right after the closing brace of the :root block
    css_content = re.sub(r'(--leading-relaxed:\s*1\.8;\s*})', r'\1\n' + responsive_variables, css_content, count=1)

# Ensure cache is busted 
css_content = css_content + "\n/* Cache bust trigger v22 */\n"

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Injected global responsive spacing variables into styles.css")
