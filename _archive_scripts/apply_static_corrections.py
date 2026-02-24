import os
import re

css_code = """
/* MEGA MENU OVERRIDE */
.nav-item.has-mega > .mega-menu {
    min-width: 700px;
    padding: 0.75rem;
    flex-direction: row;
    gap: 0;
    border-radius: 24px;
    box-shadow: 0 40px 100px rgba(0,0,0,0.15);
    background: #fff;
    border: none;
}
.mega-menu-left {
    width: 45%;
    background: linear-gradient(135deg, #FFF8F0 0%, #fff 100%);
    padding: 2rem;
    border-radius: 16px;
    border: 1px solid rgba(255, 120, 0, 0.05);
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.mega-menu-right {
    width: 55%;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1.5rem;
}
.mega-link-block {
    display: block;
    padding: 1rem;
    margin: -1rem;
    border-radius: 12px;
    text-decoration: none;
    transition: background 0.2s;
}
.mega-link-block:hover {
    background: #F8FAFC;
}
.mega-link-block h5 {
    font-size: 1rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 0.25rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: color 0.2s;
}
.mega-link-block:hover h5 {
    color: #0D8A74;
}
.mega-link-block h5 span {
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.2s;
    color: #0D8A74;
}
.mega-link-block:hover h5 span {
    opacity: 1;
    transform: translateX(0);
}
.mega-link-block p {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin: 0;
}

/* FOOTER 4-COLUMN STYLING */
.site-footer {
    background: #fff;
    border-top: 1px solid var(--border);
    padding: 4rem 0;
    margin-top: 4rem;
}
.footer-grid {
    display: grid;
    grid-template-columns: 5fr 2fr 2fr 2fr;
    gap: 3rem;
}
@media(max-width: 768px) {
    .footer-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}
.footer-brand h3 {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    letter-spacing: -0.5px;
}
.footer-brand h3 span {
    color: #0D8A74;
}
.footer-brand p {
    font-size: 0.95rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 1.5rem;
    max-width: 300px;
}
.footer-socials {
    display: flex;
    gap: 1rem;
}
.footer-socials a {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    transition: all 0.2s;
}
.footer-socials a:hover {
    color: #0D8A74;
    border-color: #0D8A74;
    background: rgba(13, 138, 116, 0.05);
}
.footer-column h4 {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 1.5rem;
}
.footer-column ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
}
.footer-column ul a {
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.95rem;
    font-weight: 500;
    transition: color 0.2s;
}
.footer-column ul a:hover {
    color: #0D8A74;
}
.footer-contact-item {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    color: var(--text-muted);
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 1.25rem;
}
.footer-contact-item svg {
    color: #0D8A74;
    flex-shrink: 0;
    margin-top: 0.25rem;
}
"""

with open(r'e:\OXYBIO\assets\css\styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'MEGA MENU OVERRIDE' not in css_content:
    with open(r'e:\OXYBIO\assets\css\styles.css', 'a', encoding='utf-8') as f:
        f.write("\n\n" + css_code)
    print("Mega menu & Footer CSS appended.")

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
                    <div class="mega-menu" style="min-width: 700px; padding: 0.75rem; flex-direction: row; gap: 0;">
                        <div class="mega-menu-left">
                            <div class="mega-icon" style="color:#D97706; margin-bottom:1rem; font-size:2rem;">
                                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2v7.31M14 9.31V2M8.5 2h7M14 9.31l6.5 11.17c.39.66-.08 1.5-.85 1.5H4.35c-.77 0-1.24-.84-.85-1.5L10 9.31M8.5 16.5h7"/></svg>
                            </div>
                            <h4 style="font-size:1.5rem; font-family:var(--font-heading); font-weight:700; color:#431407; margin-bottom:0.75rem;">Evidence-Based</h4>
                            <p style="color:#78350F; font-size:0.95rem; font-weight:500;">We formulate with clinical precision and indigenous botanical wisdom.</p>
                        </div>
                        <div class="mega-menu-right">
                            <a href="problem.html" class="mega-link-block">
                                <h5>The Problem <span>→</span></h5>
                                <p>Understand the nutritional breakdown in urban India.</p>
                            </a>
                            <a href="ingredients.html" class="mega-link-block">
                                <h5>Ingredients Index <span>→</span></h5>
                                <p>Deep dive into every component of our formulations.</p>
                            </a>
                        </div>
                    </div>
                </div>

                <a href="blog.html">Blog</a>
                <a href="careers.html">Careers</a>
                <a href="contact.html">Contact</a>
                <a href="index.html#join" class="btn btn-primary" style="margin-left: 1rem;">Join Waitlist</a>
            </nav>"""

footer_html = """
    <!-- Site Footer -->
    <footer class="site-footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <h3>Oxygen Bioinnovations<span>.</span></h3>
                <p>Precision nutrition for every ambitious Indian.<br><br>India's first honest precision nutrition system. Built on millet, mushrooms, and real science.</p>
                <div class="footer-socials">
                    <a href="#" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
                    <a href="#" aria-label="Twitter"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path></svg></a>
                    <a href="#" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                </div>
            </div>
            
            <div class="footer-column">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="science.html">Our Science</a></li>
                    <li><a href="ingredients.html">Ingredients</a></li>
                    <li><a href="blog.html">Blog</a></li>
                </ul>
            </div>
            
            <div class="footer-column">
                <h4>Get In Touch</h4>
                <ul>
                    <li><a href="contact.html">Contact Us</a></li>
                    <li><a href="careers.html">Careers</a></li>
                </ul>
            </div>
            
            <div class="footer-column">
                <h4>Legal</h4>
                <ul>
                    <li><a href="privacy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms & Conditions</a></li>
                </ul>
            </div>
        </div>
    </footer>
"""

files = ['index.html', 'about.html', 'careers.html', 'science.html', 'contact.html', 'problem.html', 'ingredients.html', 'blog.html', 'privacy.html', 'terms.html']

for filename in files:
    filepath = os.path.join(r'e:\OXYBIO', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Nav
    content = re.sub(r'<!-- Desktop Nav -->.*?</nav>', html_nav, content, flags=re.DOTALL)
    
    # Remove old footer links if they exist (were manually added or injected by old script)
    # The old footer-links div might be scattered or at the bottom.
    content = re.sub(r'<div class="footer-links">.*?</div>', '', content, flags=re.DOTALL)
    
    # Inject our new Footer right before the mobile sticky CTA or closing body tag
    if '<!-- Site Footer -->' not in content:
        if '<!-- Mobile Sticky CTA -->' in content:
            content = content.replace('<!-- Mobile Sticky CTA -->', footer_html + '\n    <!-- Mobile Sticky CTA -->')
        elif '<script src="assets/js/main.js"></script>' in content:
            content = content.replace('<script src="assets/js/main.js"></script>', footer_html + '\n    <script src="assets/js/main.js"></script>')
        else:
            content = content.replace('</body>', footer_html + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")
