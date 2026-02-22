import os, re

new_footer = '''    <!-- Footer -->
    <footer id="footer" style="background: var(--bg); border-top: 1px solid var(--border); padding: 4rem 0 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; padding-bottom: 3rem; border-bottom: 1px solid var(--border);">

                <!-- Column 1: Brand -->
                <div>
                    <a href="index.html" class="logo" style="font-size: 1.5rem; margin-bottom: 0.75rem; display: inline-block;">OXYGEN<span style="color: var(--accent);">.</span></a>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.25rem; font-style: italic;">Precision nutrition for every ambitious Indian.</p>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem;">India\'s first honest precision nutrition system. Built on millet, mushrooms, and real science.</p>
                    <div style="display: flex; gap: 1rem; margin-bottom: 2rem;">
                        <a href="#" aria-label="LinkedIn" style="color: var(--text-muted); transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                        </a>
                        <a href="#" aria-label="Twitter" style="color: var(--text-muted); transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
                        </a>
                        <a href="#" aria-label="Instagram" style="color: var(--text-muted); transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                        </a>
                    </div>
                    <div>
                        <h4 style="font-size: 0.95rem; font-weight: 600; margin-bottom: 1rem; color: var(--text-main);">Contact Us</h4>
                        <div style="display: flex; flex-direction: column; gap: 0.6rem;">
                            <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); flex-shrink: 0; margin-top: 2px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                <span style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;">Cabin D, Technology Business Incubater,<br>Adhiyamaan College of Engineering Campus, Dr MGR Nagar, Hosur, tamil nadu - 635130</span>
                            </div>
                            <div style="display: flex; gap: 0.75rem; align-items: center;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                                <a href="mailto:info@oxygenbioinnovations.com" style="color: var(--text-muted); font-size: 0.85rem; text-decoration: none;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">info@oxygenbioinnovations.com</a>
                            </div>
                            <div style="display: flex; gap: 0.75rem; align-items: center;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.64 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 9.91a16 16 0 0 0 6.16 6.16l.98-.98a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                                <span style="color: var(--text-muted); font-size: 0.85rem;">+91 (800) 123-4567</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Column 2: Quick Links -->
                <div>
                    <h4 style="font-size: 0.95rem; font-weight: 600; margin-bottom: 1.25rem; color: var(--text-main);">Quick Links</h4>
                    <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                        <a href="about.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">About Us</a>
                        <a href="science.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">Our Science</a>
                        <a href="ingredients.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">Ingredients</a>
                        <a href="blog.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">Blog</a>
                    </div>
                </div>

                <!-- Column 3: Get In Touch -->
                <div>
                    <h4 style="font-size: 0.95rem; font-weight: 600; margin-bottom: 1.25rem; color: var(--text-main);">Get In Touch</h4>
                    <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                        <a href="contact.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">Contact Us</a>
                        <a href="careers.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">Careers</a>
                    </div>
                </div>

                <!-- Column 4: Legal -->
                <div>
                    <h4 style="font-size: 0.95rem; font-weight: 600; margin-bottom: 1.25rem; color: var(--text-main);">Legal</h4>
                    <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                        <a href="privacy.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">Privacy Policy</a>
                        <a href="terms.html" style="color: var(--text-muted); font-size: 0.9rem; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'var(--text-muted)\'">Terms &amp; Conditions</a>
                    </div>
                </div>

            </div>

            <!-- Bottom Bar -->
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 0; flex-wrap: wrap; gap: 1rem;">
                <p style="color: var(--text-muted); font-size: 0.85rem; margin: 0;">&copy; <span id="year"></span> Oxygen Bioinnovations. All rights reserved.</p>
                <p style="color: var(--text-muted); font-size: 0.85rem; margin: 0;">Built with science. Delivered with honesty.</p>
            </div>
        </div>
    </footer>'''

files = [
    'index.html', 'about.html', 'careers.html', 'science.html', 'contact.html',
    'problem.html', 'ingredients.html', 'blog.html', 'privacy.html', 'terms.html'
]

footer_pattern = re.compile(r'    <!-- Footer -->.*?</footer>', re.DOTALL)

for filename in files:
    filepath = os.path.join(r'e:\\OXYBIO', filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content, count = footer_pattern.subn(new_footer, content)
    if count:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {filename}")
    else:
        print(f"WARN: footer pattern not found in {filename}")

print("Done.")
