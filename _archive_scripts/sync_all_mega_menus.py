import os
import glob
import re
import codecs

# We want to replace the About Us mega-links-col in every HTML file with the one from about.html
NEW_MEGA_ABOUT = '''<div class="mega-links-col">
                                <a href="about.html#about-story" class="mega-nav-link">
                                    <span class="link-title">Our Story</span>
                                    <span class="link-desc">Why we started and what we built before launch.</span>
                                </a>
                                <a href="about.html#about-vision" class="mega-nav-link">
                                    <span class="link-title">Vision &amp; Mission</span>
                                    <span class="link-desc">The strategic framework and three pillars guiding us.</span>
                                </a>
                                <a href="about.html#about-who" class="mega-nav-link">
                                    <span class="link-title">Who We Are</span>
                                    <span class="link-desc">The founder, the science, and our operating principles.</span>
                                </a>
                            </div>'''

# The pattern looks for the `<h4>Who is Oxygen?</h4>` block and matches the `mega-links-col` right after it
pattern = re.compile(
    r'(<h4>Who is Oxygen\?</h4>\s*<p>.*?</p>\s*</div>\s*)<div class="mega-links-col">.*?</div>\s*</div>',
    re.DOTALL
)

html_files = glob.glob('e:\\OXYBIO\\*.html')

for file in html_files:
    try:
        with codecs.open(file, 'r', 'utf-8') as f:
            content = f.read()
        
        # Replace
        new_content = pattern.sub(r'\1' + NEW_MEGA_ABOUT + '\n                        </div>', content)
        
        if content != new_content:
            with codecs.open(file, 'w', 'utf-8') as f:
                f.write(new_content)
            print(f"Updated mega menu in: {os.path.basename(file)}")
            
    except Exception as e:
        print(f"Error processing {file}: {e}")

print("Mega menu sync complete.")
