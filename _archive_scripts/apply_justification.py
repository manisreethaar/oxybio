import os

css_append = """
    /* 4. Global Mobile Typography & Spacing Fixes */
    /* User requested justification alignment, better spacing, and unpacking of dense text */
    p, .subtext, .editorial-col, .editorial-col p {
        text-align: justify !important;
        text-justify: inter-word !important;
        hyphens: auto !important;
        -webkit-hyphens: auto !important;
        -ms-hyphens: auto !important;
        margin-bottom: 1.75rem !important; /* Increase vertical breathing room */
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }

    /* 5. Improve list spacing for readability */
    ul li, ol li {
        margin-bottom: 1.25rem !important;
        text-align: left !important; /* Lists shouldn't be fully justified */
    }
}
"""

css_file = 'e:\\OXYBIO\\assets\\css\\styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# I will replace the closing bracket of the previous media query block I added in the previous step
if '    .flow-left {\n        max-width: 100% !important;\n        padding-right: 1rem !important;\n    }\n}' in css:
    css = css.replace('    .flow-left {\n        max-width: 100% !important;\n        padding-right: 1rem !important;\n    }\n}', 
                      '    .flow-left {\n        max-width: 100% !important;\n    }\n' + css_append)
    
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Mobile typography and spacing CSS successfully appended.")
else:
    print("Could not find the target CSS block to append to. Writing to end of file.")
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write("\n@media (max-width: 768px) {\n" + css_append)
