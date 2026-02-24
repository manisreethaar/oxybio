import os
import re

new_nav = """<nav class="desktop-nav custom-nav-replaced">
                <a href="index.html">Home</a>
                
                <div class="nav-item">
                    <a href="about.html">About Us <svg width="12" height="12" viewBox="0 0 24 24" fill="none" class="nav-arrow" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                    <div class="mega-dropdown">
                        <div class="mega-dropdown-inner">
                            <div class="mega-feature">
                                <div class="icon-wrap">
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
                                </div>
                                <h4>Who is Oxygen?</h4>
                                <p>Building India's first precision nutrition system.</p>
                            </div>
                            <div class="mega-links-col">
                                <a href="about.html#about-vision" class="mega-nav-link">
                                    <span class="link-title">Vision & Mission</span>
                                    <span class="link-desc">Why we started and where we are heading.</span>
                                </a>
                                <a href="about.html#about-founder" class="mega-nav-link">
                                    <span class="link-title">Founder & Team</span>
                                    <span class="link-desc">Meet the researchers and scientists behind the brand.</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="nav-item">
                    <a href="science.html">Our Science <svg width="12" height="12" viewBox="0 0 24 24" fill="none" class="nav-arrow" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                    <div class="mega-dropdown">
                        <div class="mega-dropdown-inner">
                            <div class="mega-feature">
                                <div class="icon-wrap">
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2v7.31M14 9.31V2M8.5 2h7M14 9.31l6.5 11.17c.39.66-.08 1.5-.85 1.5H4.35c-.77 0-1.24-.84-.85-1.5L10 9.31M8.5 16.5h7"/></svg>
                                </div>
                                <h4>Evidence-Based</h4>
                                <p>Active forms, verified extracts, and clinical proof.</p>
                            </div>
                            <div class="mega-links-col">
                                <a href="problem.html" class="mega-nav-link">
                                    <span class="link-title">The Problem</span>
                                    <span class="link-desc">Understand the nutritional breakdown in urban India.</span>
                                </a>
                                <a href="ingredients.html" class="mega-nav-link">
                                    <span class="link-title">Ingredients Index</span>
                                    <span class="link-desc">Deep dive into every component of our formulations.</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <a href="blog.html">Blog</a>
                <a href="careers.html">Careers</a>
                <a href="contact.html">Contact</a>
                <a href="index.html#join" class="btn btn-primary" style="margin-left: 1rem;">Join Waitlist</a>
            </nav>"""

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html', 'problem.html', 'ingredients.html', 'blog.html', 'privacy.html', 'terms.html']

for filename in files:
    filepath = os.path.join(r'e:\OXYBIO', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Strip the dot from the logo globally
    content = re.sub(r'(Oxygen\s*Bioinnovations)<span>\.</span>', r'\g<1>', content)
    
    # 2. Swap out the entire desktop nav
    content = re.sub(r'<nav class="desktop-nav(?: custom-nav-replaced)?">.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")
