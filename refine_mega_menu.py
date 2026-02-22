import os
import re

css_append = """
/* =========================================================
   SUPER PREMIUM MEGA DROPDOWN (V3 Override)
========================================================= */

/* Ensure desktop nav has appropriate stacking context */
.desktop-nav {
    display: flex;
    align-items: center;
    position: relative;
    z-index: 999;
}

.desktop-nav .nav-item { 
    position: relative; 
    display: flex; 
    align-items: center; 
    height: 100%; 
}
.desktop-nav .nav-item > a { 
    display: flex; 
    align-items: center; 
    gap: 0.25rem; 
}
.desktop-nav .nav-arrow { 
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1); 
}
.desktop-nav .nav-item:hover .nav-arrow { 
    transform: rotate(180deg); 
}

.mega-dropdown {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%) translateY(20px) scale(0.97);
    opacity: 0;
    pointer-events: none;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    padding-top: 1.5rem; /* invisible bridge */
    z-index: 1000;
}
.desktop-nav .nav-item:hover .mega-dropdown {
    opacity: 1;
    pointer-events: auto;
    transform: translateX(-50%) translateY(0) scale(1);
}
.mega-dropdown-inner {
    background: #ffffff;
    border-radius: 20px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.08), 0 4px 15px rgba(0,0,0,0.03);
    border: 1px solid #E5E7EB;
    display: flex;
    overflow: hidden;
    min-width: 650px;
}

/* Feature Pane (Left Side) */
.mega-feature {
    background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
    padding: 2.5rem;
    width: 42%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-right: 1px solid #E5E7EB;
    text-align: left;
}
.mega-feature .icon-wrap {
    color: #0D8A74;
    margin-bottom: 1.25rem;
    background: #ffffff;
    width: 56px;
    height: 56px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 10px 20px rgba(13, 138, 116, 0.1);
}
.mega-feature h4 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 0.75rem;
    font-family: var(--font-serif);
    line-height: 1.2;
}
.mega-feature p {
    font-size: 0.95rem;
    color: #475569;
    line-height: 1.6;
}

/* Links Pane (Right Side) */
.mega-links-col {
    padding: 1.5rem;
    width: 58%;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    justify-content: center;
}
.mega-nav-link {
    display: flex;
    flex-direction: column;
    padding: 1.25rem;
    border-radius: 16px;
    transition: all 0.25s ease;
    text-decoration: none;
    border: 1px solid transparent;
    text-align: left;
}
.mega-nav-link:hover {
    background: #F8FAFC;
    transform: translateX(6px);
    border-color: #E2E8F0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}
.mega-nav-link .link-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 0.35rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: color 0.25s;
}
.mega-nav-link:hover .link-title {
    color: #0D8A74;
}
.mega-nav-link .link-title::after {
    content: "→";
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    color: #0D8A74;
}
.mega-nav-link:hover .link-title::after {
    opacity: 1;
    transform: translateX(0);
}
.mega-nav-link .link-desc {
    font-size: 0.9rem;
    color: #64748B;
    line-height: 1.5;
}

/* Hide the old mega-menu strictly to ensure no conflicts */
.custom-nav-replaced .mega-menu { display: none !important; }
"""

new_nav = """<!-- Desktop Nav -->
            <nav class="desktop-nav custom-nav-replaced">
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

filepath_css = r'e:\OXYBIO\assets\css\styles.css'
with open(filepath_css, 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'SUPER PREMIUM MEGA DROPDOWN (V3 Override)' not in css_content:
    with open(filepath_css, 'a', encoding='utf-8') as f:
        f.write("\n\n" + css_append)
    print("Mega menu V3 CSS appended.")

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html', 'problem.html', 'ingredients.html', 'blog.html', 'privacy.html', 'terms.html']

for filename in files:
    filepath = os.path.join(r'e:\OXYBIO', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Strip the dot from the logo globally
    # "Oxygen Bioinnovations<span>.</span>" -> "Oxygen Bioinnovations"
    content = re.sub(r'Oxygen Bioinnovations<span>\.</span>', 'Oxygen Bioinnovations', content)
    
    # 2. Swap out the entire desktop nav
    content = re.sub(r'<!-- Desktop Nav -->.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")
