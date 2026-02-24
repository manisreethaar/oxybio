import codecs
import re

# 1. Update styles.css with premium button fix and contact page tweaks
with codecs.open('e:\\OXYBIO\\assets\\css\\styles.css', 'r', 'cp1252') as f:
    css = f.read()

PREMIUM_BTN_CSS = '''
/* Premium Join Waitlist Button Fix */
.btn-primary, .desktop-nav > a.btn-primary, .mobile-menu .btn-primary {
    background: #000 !important;
    color: #fff !important;
    border: 1px solid #333 !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative;
    overflow: hidden;
    z-index: 1;
}
.btn-primary::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition: width 0.6s ease, height 0.6s ease;
    z-index: -1;
}
.btn-primary:hover::after {
    width: 300px;
    height: 300px;
}
.btn-primary:hover {
    transform: translateY(-3px) scale(1.03) !important;
    box-shadow: 0 10px 30px rgba(10,10,10,0.3) !important;
    border-color: #666 !important;
}

/* Premium Contact Input Styles */
.premium-input {
    padding: 1.25rem;
    border: 1px solid #e0e0e0;
    background: #fdfdfd;
    border-radius: 8px;
    font-family: var(--font-sans);
    color: var(--text-main);
    transition: all 0.3s ease;
    outline: none;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
}
.premium-input:focus {
    border-color: var(--text-main);
    background: #fff;
    box-shadow: 0 0 0 4px rgba(10,10,10,0.05);
}
.contact-label {
    font-family: var(--font-mono); 
    font-size: 0.75rem; 
    line-height: var(--leading-relaxed); 
    text-transform: uppercase; 
    color: var(--text-main);
    font-weight: 600;
    letter-spacing: 0.05em;
}
'''

if 'Premium Join Waitlist Button Fix' not in css:
    css += PREMIUM_BTN_CSS
    with codecs.open('e:\\OXYBIO\\assets\\css\\styles.css', 'w', 'cp1252') as f:
        f.write(css)
    print("Styles updated for buttons and inputs.")

# 2. Rewrite contact.html to be ultra-premium
with codecs.open('e:\\OXYBIO\\contact.html', 'r', 'utf-8') as f:
    html = f.read()

# Fix spacing in Hero
html = html.replace('<div class="badge" style="margin-bottom:var(--space-md);">', '<div class="badge" style="margin-bottom:2rem;">')
html = html.replace('<h1 class="display" style="font-size:var(--text-6xl); line-height:var(--leading-none);">Get in<br><em>Touch.</em></h1>', '<h1 class="display" style="font-size:clamp(4rem, 8vw, 6rem); line-height:0.95; letter-spacing:-0.03em;">Get in<br><em>Touch.</em></h1>')
# Ensure margin-top is larger for the paragraph below it
html = html.replace('<p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:var(--text-xl); line-height:var(--leading-tight);">', '<p class="subtext editorial-col" style="margin-top:2.5rem; font-size:1.25rem; line-height:1.6;">')

start_marker = r'<section class="structure-section" style="background:var\(--bg-alt\);">'
pattern = re.compile(start_marker + r'.*?(?=</main>)', re.DOTALL)

NEW_CONTACT = '''<section class="structure-section" style="background:var(--bg-alt); padding:var(--space-2xl) 0;">
    <div class="container reveal">
        
        <div style="background:var(--bg); border:1px solid var(--border); border-radius:16px; overflow:hidden; box-shadow:0 20px 40px rgba(0,0,0,0.04); display:grid; grid-template-columns:1fr 1.5fr;" class="mobile-stack-card">
            
            <!-- Left Info Panel (Dark Mode) -->
            <div style="background:var(--text-main); color:var(--bg); padding:4rem; display:flex; flex-direction:column; justify-content:space-between; position:relative; overflow:hidden;">
                
                <!-- Abstract Background -->
                <div style="position:absolute; bottom:-10%; right:-10%; width:300px; height:300px; background:radial-gradient(circle, rgba(255,255,255,0.05) 0%, transparent 70%); pointer-events:none;"></div>
                
                <div style="position:relative; z-index:2;">
                    <h3 style="font-family:var(--font-serif); font-size:2rem; margin-bottom:1rem; color:#fff;">Let's build the future together.</h3>
                    <p style="font-size:1.05rem; line-height:1.6; color:#a3a3a3; margin-bottom:4rem;">Whether you are looking to invest, partner on research, or distribute our precision formulations, our founders read every message.</p>
                    
                    <div style="display:flex; flex-direction:column; gap:2.5rem;">
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#666; text-transform:uppercase; display:block; margin-bottom:0.5rem;">Direct Email</span>
                            <a href="mailto:info@oxygenbioinnovations.com" style="font-size:1.15rem; color:#fff; text-decoration:none; border-bottom:1px solid #444; padding-bottom:4px; font-weight:500;">info@oxygenbioinnovations.com</a>
                        </div>
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#666; text-transform:uppercase; display:block; margin-bottom:0.5rem;">Corporate Headquarters</span>
                            <address style="font-size:1.1rem; line-height:1.6; color:#ccc; font-style:normal;">
                                TBI, Cabin D<br>
                                Adhiyamaan College of Engineering<br>
                                Hosur, Tamil Nadu – 635130
                            </address>
                        </div>
                        <div>
                            <span style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; color:#666; text-transform:uppercase; display:block; margin-bottom:0.5rem;">Social Channels</span>
                            <div style="display:flex; gap:1.5rem;">
                                <a href="https://linkedin.com/company/oxygenbioinnovations" target="_blank" style="color:#fff; text-decoration:none; font-family:var(--font-sans); font-weight:500;">LinkedIn ↗</a>
                                <a href="https://twitter.com/oxygenbio" target="_blank" style="color:#fff; text-decoration:none; font-family:var(--font-sans); font-weight:500;">Twitter ↗</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Form Panel -->
            <div style="padding:4rem; background:#fff;">
                <h3 style="font-family:var(--font-serif); font-size:2rem; color:var(--text-main); margin-bottom:0.5rem;">Send an Inquiry.</h3>
                <p style="font-size:1rem; color:var(--text-muted); margin-bottom:3rem;">Fill out the brief form below and we will route your inquiry to the correct team member.</p>
                
                <form style="display:flex; flex-direction:column; gap:2rem;" onsubmit="event.preventDefault(); alert('Message submitted successfully.');">
                    
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;" class="mobile-stack">
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label class="contact-label">Full Name *</label>
                            <input type="text" required class="premium-input" placeholder="e.g. Dr. Ashok Kumar">
                        </div>
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label class="contact-label">Email Address *</label>
                            <input type="email" required class="premium-input" placeholder="ashok@example.com">
                        </div>
                    </div>
                    
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem;" class="mobile-stack">
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label class="contact-label">Inquiry Type *</label>
                            <select required class="premium-input">
                                <option value="" disabled selected>Select a topic...</option>
                                <option value="Investor/VC">Investment & VC</option>
                                <option value="Researcher/Academic">Academic/Clinical Research</option>
                                <option value="Distributor/Retailer">Distribution & Retail</option>
                                <option value="Press">Press & Media</option>
                                <option value="Other">Other Inquiry</option>
                            </select>
                        </div>
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label class="contact-label">Company / Institution</label>
                            <input type="text" class="premium-input" placeholder="Optional">
                        </div>
                    </div>
                    
                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <label class="contact-label">Message *</label>
                        <textarea rows="5" required class="premium-input" placeholder="How can we help you?"></textarea>
                    </div>

                    <div style="margin-top:1rem;">
                        <button type="submit" class="btn btn-primary" style="padding:1.2rem 3rem; font-size:1rem; width:100%; justify-content:center;">Submit Inquiry</button>
                    </div>
                </form>
            </div>
            
        </div>
    </div>
</section>
\n'''

if pattern.search(html):
    new_html = pattern.sub(NEW_CONTACT, html, count=1)
    with codecs.open('e:\\OXYBIO\\contact.html', 'w', 'utf-8') as f:
        f.write(new_html)
    print("contact.html regex replacement successful.")
else:
    print("Could not find regex pattern.")
