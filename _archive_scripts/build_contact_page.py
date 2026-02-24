import os
import re

with open(r'e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_match = re.search(r'(.*?<main>)', html, re.DOTALL)
footer_match = re.search(r'(</main>.*)', html, re.DOTALL)

if not header_match or not footer_match:
    print("Error extracting header/footer")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

contact_content = """
        <!-- Contact Hero Section -->
        <section class="hero" id="contact-hero" style="min-height: 50vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="hero-glow"></div>
            <div class="container hero-content" style="text-align: center;">
                <div class="badge reveal" style="transition-delay: 0ms; margin: 0 auto 1.5rem;">Get in Touch</div>
                <h1 class="reveal" style="transition-delay: 150ms;">
                    We are built on <br>
                    <span style="color: var(--accent);">conversations.</span>
                </h1>
                <p class="subtitle reveal" style="transition-delay: 300ms;" style="max-width: 600px; margin-left: auto; margin-right: auto;">
                    Whether you're an investor, researcher, or potential partner, we'd love to hear from you. Let's explore how we can collaborate.
                </p>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" style="padding: 4rem 0 8rem;">
            <div class="container">
                <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 4rem; max-width: 1000px; margin: 0 auto;">
                    
                    <!-- Contact Info Sidebar -->
                    <div class="form-container reveal" style="padding: 3rem; align-self: start; background: transparent; border: none; box-shadow: none;">
                        <div style="margin-bottom: 3rem;">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem; font-size: 1.2rem;">Email</h3>
                            <p style="color: var(--text-main); font-size: 1.1rem;"><a href="mailto:info@oxygenbioinnovations.com" style="color: var(--text-main); text-decoration: none;">info@oxygenbioinnovations.com</a></p>
                        </div>
                        
                        <div style="margin-bottom: 3rem;">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem; font-size: 1.2rem;">Phone</h3>
                            <p style="color: var(--text-main); font-size: 1.1rem;">+91 (800) 123-4567</p>
                        </div>

                        <div style="margin-bottom: 3rem;">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem; font-size: 1.2rem;">Address</h3>
                            <p style="color: var(--text-muted); line-height: 1.6;">
                                Cabin D, Technology Business Incubater,<br>
                                Adhiyamaan College of Engineering Campus,<br>
                                Dr MGR Nagar, Hosur,<br>
                                Tamil Nadu - 635130
                            </p>
                        </div>

                        <div style="margin-bottom: 3rem;">
                            <h3 style="color: var(--accent); margin-bottom: 0.5rem; font-size: 1.2rem;">Business Hours</h3>
                            <p style="color: var(--text-muted);">Mon - Fri: 9:00 AM - 6:00 PM PST</p>
                        </div>

                        <div>
                            <h3 style="color: var(--accent); margin-bottom: 1rem; font-size: 1.2rem;">Social Links</h3>
                            <div style="display: flex; gap: 1rem;">
                                <a href="#" style="color: var(--text-muted); transition: color 0.3s;" aria-label="LinkedIn">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                                </a>
                                <a href="#" style="color: var(--text-muted); transition: color 0.3s;" aria-label="Twitter">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Contact Form -->
                    <div class="form-container reveal" style="padding: 3rem; background: var(--card-bg); border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                        <div style="margin-bottom: 2rem;">
                            <h2 style="font-size: 2rem; margin-bottom: 0.5rem;">Let's talk.</h2>
                            <p style="color: var(--text-muted);">Fill out the form below and we'll get back to you shortly.</p>
                        </div>
                        <form action="#" method="POST">
                            <div class="form-group" style="margin-bottom: 1.5rem;">
                                <label for="role" class="form-label">I am a... <span style="color: #E11D48;">*</span></label>
                                <select id="role" name="role" class="form-input" required>
                                    <option value="" disabled selected>Select an option</option>
                                    <option value="Investor/VC">Investor/VC</option>
                                    <option value="Researcher/Academic">Researcher/Academic</option>
                                    <option value="Distributor/Retailer">Distributor/Retailer</option>
                                    <option value="Customer">Customer</option>
                                    <option value="Student/Job Seeker">Student/Job Seeker</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                                <div class="form-group">
                                    <label for="fullName" class="form-label">Full Name <span style="color: #E11D48;">*</span></label>
                                    <input type="text" id="fullName" name="fullName" class="form-input" required placeholder="John Doe">
                                </div>
                                <div class="form-group">
                                    <label for="company" class="form-label">Company</label>
                                    <input type="text" id="company" name="company" class="form-input" placeholder="Organization name">
                                </div>
                            </div>

                            <div class="form-group" style="margin-bottom: 1.5rem;">
                                <label for="email" class="form-label">Email Address <span style="color: #E11D48;">*</span></label>
                                <input type="email" id="email" name="email" class="form-input" required placeholder="john@example.com">
                            </div>

                            <div class="form-group" style="margin-bottom: 1.5rem;">
                                <label for="subject" class="form-label">Subject <span style="color: #E11D48;">*</span></label>
                                <input type="text" id="subject" name="subject" class="form-input" required placeholder="How can we help you?">
                            </div>

                            <div class="form-group" style="margin-bottom: 2rem;">
                                <label for="message" class="form-label">Message <span style="color: #E11D48;">*</span></label>
                                <textarea id="message" name="message" class="form-input" rows="5" required placeholder="Tell us more..."></textarea>
                            </div>

                            <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center; font-size: 1.1rem; padding: 1rem;">
                                Send Message
                            </button>
                        </form>
                    </div>

                </div>
            </div>
        </section>
"""

with open(r'e:\\OXYBIO\\contact.html', 'w', encoding='utf-8') as f:
    f.write(header_html + '<main>\n' + contact_content + '\n    </main>\n' + footer_html)

print("Generated contact.html")
