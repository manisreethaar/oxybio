import os
import re

css_code = """
/* MEGA MENU STYLING */
.nav-item {
    position: relative;
    display: flex;
    align-items: center;
    height: 100%;
}

.nav-item.has-mega > a {
    display: flex;
    align-items: center;
    gap: 0.25rem;
}

.mega-menu {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%) translateY(10px);
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    border: 1px solid var(--border);
    padding: 1.5rem;
    display: flex;
    gap: 2rem;
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
    z-index: 100;
    min-width: 400px;
}

.nav-item.has-mega:hover .mega-menu {
    opacity: 1;
    pointer-events: all;
    transform: translateX(-50%) translateY(0);
}

.mega-card {
    background: var(--bg);
    padding: 1.5rem;
    border-radius: 8px;
    flex: 1;
    max-width: 200px;
}

.mega-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.mega-card h4 {
    font-size: 1rem;
    margin-bottom: 0.5rem;
    color: var(--text-main);
}

.mega-card p {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin: 0;
    line-height: 1.4;
}

.mega-links {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    justify-content: center;
    flex: 1;
}

.mega-links a {
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    color: var(--text-main) !important;
    transition: color 0.2s !important;
    text-decoration: none;
}

.mega-links a:hover {
    color: var(--accent) !important;
}

/* Mobile Sub-menu */
.mobile-submenu {
    padding-left: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 0.75rem;
    border-left: 2px solid var(--border);
}

.mobile-submenu a {
    font-size: 1.1rem !important;
    color: var(--text-muted) !important;
}

.mobile-submenu a:hover {
    color: var(--accent) !important;
}
"""

with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'MEGA MENU STYLING' not in css_content:
    with open(r'e:\OXYBIO\assets\css\styles.css', 'a', encoding='utf-8') as f:
        f.write(css_code)
    print("Mega menu CSS appended.")

html_nav = """<!-- Desktop Nav -->
            <nav class="desktop-nav">
                <a href="index.html">Home</a>
                
                <div class="nav-item has-mega">
                    <a href="about.html">About Us <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                    <div class="mega-menu">
                        <div class="mega-card">
                            <div class="mega-icon">👥</div>
                            <h4>Who is Oxygen?</h4>
                            <p>Building India's first precision nutrition system.</p>
                        </div>
                        <div class="mega-links">
                            <a href="about.html#about-vision">Vision & Mission</a>
                            <a href="about.html#about-founder">Founder & Team</a>
                        </div>
                    </div>
                </div>

                <div class="nav-item has-mega">
                    <a href="science.html">Our Science <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                    <div class="mega-menu">
                        <div class="mega-card">
                            <div class="mega-icon">🧪</div>
                            <h4>Evidence-Based</h4>
                            <p>Active forms, verified extracts, clinical proof.</p>
                        </div>
                        <div class="mega-links">
                            <a href="science.html#problem">The Problem</a>
                            <a href="science.html#science">Ingredients Index</a>
                        </div>
                    </div>
                </div>

                <a href="careers.html">Careers</a>
                <a href="contact.html">Contact</a>
                <a href="index.html#join" class="btn btn-primary" style="margin-left: 1rem;">Join Waitlist</a>
            </nav>"""

html_mobile = """<!-- Mobile Drawer Overlay & Menu -->
    <div class="mobile-overlay" id="mobileOverlay"></div>
    <nav class="mobile-menu" id="mobileMenu">
        <a href="index.html" class="menu-link">Home</a>
        
        <div style="width:100%;">
            <a href="about.html" class="menu-link" style="margin-bottom:0;">About Us</a>
            <div class="mobile-submenu">
                <a href="about.html#about-vision" class="menu-link">Vision & Mission</a>
                <a href="about.html#about-founder" class="menu-link">Founder & Team</a>
            </div>
        </div>

        <div style="width:100%;">
            <a href="science.html" class="menu-link" style="margin-bottom:0; margin-top:1rem;">Our Science</a>
            <div class="mobile-submenu">
                <a href="science.html#problem" class="menu-link">The Problem</a>
                <a href="science.html#science" class="menu-link">Ingredients Index</a>
            </div>
        </div>

        <a href="careers.html" class="menu-link" style="margin-top:1rem;">Careers</a>
        <a href="contact.html" class="menu-link">Contact</a>
        <a href="index.html#join" class="btn btn-primary menu-link">Join Waitlist</a>
    </nav>"""

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html']

for filename in files:
    filepath = os.path.join(r'e:\OXYBIO', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop
    content = re.sub(r'<!-- Desktop Nav -->.*?</nav>', html_nav, content, flags=re.DOTALL)
    
    # Mobile
    content = re.sub(r'<!-- Mobile Drawer Overlay & Menu -->.*?</nav>', html_mobile, content, flags=re.DOTALL)

    # Logo link
    content = re.sub(r'<a href="#" class="logo">OXYGEN<span>.</span></a>', r'<a href="index.html" class="logo" style="font-size:1.2rem; letter-spacing:-0.5px;">Oxygen Bioinnovations<span>.</span></a>', content)

    # Footer links (let's update these too!)
    footer_old = """<div class="footer-links">
                <a href="#about-vision">About Us</a>
                <a href="#problem">The Problem</a>
                <a href="#products">Formulas</a>
                <a href="#science">Science</a>
                <a href="mailto:hello@oxygenbio.com">Contact</a>
            </div>"""
            
    footer_new = """<div class="footer-links">
                <a href="about.html">About Us</a>
                <a href="science.html#problem">The Problem</a>
                <a href="index.html#products">Formulas</a>
                <a href="science.html">Science</a>
                <a href="contact.html">Contact</a>
            </div>"""
            
    content = content.replace(footer_old, footer_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")
