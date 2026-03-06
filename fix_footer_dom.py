import glob
import re

html_files = glob.glob(r'e:\OXYBIO\*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Move footer-bottom inside footer-grid
    # We want to replace `<div class="footer-column">...</div> </div> <div class="footer-bottom"...>...</div> </footer>`
    # With `<div class="footer-column">...</div> <div class="footer-bottom"...>...</div> </div> </footer>`

    # This regex looks for the closing `</div>` of `.footer-grid`, followed by `footer-bottom`
    # and places `footer-bottom` before that closing `</div>`.
    
    # We'll do a simple text replace since the structure is consistent:
    # </div> (the end of container footer-grid)
    # <div class="footer-bottom" ...>
    #  &copy; ...
    # </div>
    # </footer>
    
    # Let's extract the footer-bottom block first.
    match = re.search(r'(</div>\s*)?(<div class="footer-bottom"[^>]*>[\s\S]*?</div>)(\s*</footer>)', content)
    if match and "footer-bottom" in match.group(2) and match.group(1):
        # Already outside? Wait, match.group(1) is the closing div of container.
        # Let's cleanly replace the sequence.
        
        # A safer regex approach:
        # Find:
        # </div>
        # <div class="footer-bottom" ...
        # ...
        # </div>
        # </footer>
        
        # We will remove the </div> before footer-bottom and add it after footer-bottom.
        
        pattern = r'</div>\s*(<div class="footer-bottom"[\s\S]*?</div>)\s*</footer>'
        replacement = r'\n\1\n</div>\n</footer>'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            # Also clean up the inline styles of footer-bottom to be simpler:
            new_content = re.sub(
                r'<div class="footer-bottom"[^>]*>',
                r'<div class="footer-bottom" style="text-align: center; border-top: 1px solid rgba(0,0,0,0.1); margin-top: 2rem; padding-top: 1.5rem; font-size: 0.85rem; color: var(--text-muted); width: 100%; grid-column: 1 / -1; display: block;">',
                new_content
            )
            
            # The border should be var(--border)
            new_content = new_content.replace('rgba(0,0,0,0.1)', 'var(--border)')
            
            # Bump cache
            new_content = new_content.replace('logo-full.png?v=5', 'logo-full.png?v=6')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Moved footer-bottom inside footer-grid.")
