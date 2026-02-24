import os, re

contact_path = r'e:\OXYBIO\contact.html'
with open(contact_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_CONTENT = """
<main>

<!-- ═══════════════════════════════════════════════════════
     HERO SECTION
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="padding-top:140px; border-bottom:1px solid var(--border);">
    <div class="container">
        <div class="flow-left reveal" style="max-width:900px; margin-bottom:var(--space-md);">
            <div class="badge" style="margin-bottom:var(--space-md);">Partnerships & Inquiries</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">Get in<br><em>Touch.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                Whether you're an investor, researcher, or potential partner, we'd love to hear from you. Let's explore how we can collaborate.
            </p>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     CONTACT FORM & INFO
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt);">
    <div class="container reveal">
        <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;" class="mobile-stack">
            
            <!-- Address and Details -->
            <div style="position:sticky; top:120px;" class="flow-left">
                <div class="section-label" style="margin-bottom:var(--space-md);">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Contact Information</span>
                </div>
                
                <div style="display:flex; flex-direction:column; gap:2rem;">
                    <div>
                        <h4 style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem; text-transform:uppercase;">Email</h4>
                        <a href="mailto:info@oxygenbioinnovations.com" style="font-family:var(--font-sans); font-size:1.05rem; color:var(--text-main); text-decoration:none; font-weight:500;">info@oxygenbioinnovations.com</a>
                    </div>
                    
                    <div>
                        <h4 style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem; text-transform:uppercase;">Phone</h4>
                        <a href="tel:+919344467260" style="font-family:var(--font-sans); font-size:1.05rem; color:var(--text-main); text-decoration:none; font-weight:500;">+91 93444 67260</a>
                    </div>
                    
                    <div>
                        <h4 style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem; text-transform:uppercase;">Address</h4>
                        <address style="font-family:var(--font-sans); font-size:1.05rem; color:var(--text-main); font-style:normal; line-height:1.6;">
                            Cabin D, Technology Business Incubator<br>
                            Adhiyamaan College of Engineering Campus<br>
                            Dr MGR Nagar, Hosur<br>
                            Tamil Nadu - 635130
                        </address>
                    </div>
                    
                    <div>
                        <h4 style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem; text-transform:uppercase;">Business Hours</h4>
                        <p style="font-family:var(--font-sans); font-size:1.05rem; color:var(--text-main);">Mon - Fri: 9:00 AM - 6:00 PM PST</p>
                    </div>
                    
                    <div>
                        <h4 style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-bottom:0.5rem; text-transform:uppercase;">Social Links</h4>
                        <div style="display:flex; gap:1rem;">
                            <a href="#" style="font-family:var(--font-sans); font-size:1.05rem; color:var(--text-main); text-decoration:none; font-weight:500; border-bottom:1px solid var(--text-main);">LinkedIn</a>
                            <a href="#" style="font-family:var(--font-sans); font-size:1.05rem; color:var(--text-main); text-decoration:none; font-weight:500; border-bottom:1px solid var(--text-main);">Twitter</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Form Structure -->
            <div class="bento-grid">
                <div class="bento-cell" style="grid-column: span 12; background:var(--bg);">
                    <h2 class="headline" style="font-size:2rem; margin-bottom:2rem;">Send a Message</h2>
                    <form style="display:flex; flex-direction:column; gap:1.5rem;" onsubmit="event.preventDefault(); alert('Message submitted successfully.');">
                        
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">I am a... *</label>
                            <select required style="padding:1rem; border:1px solid var(--border); background:var(--bg-alt); border-radius:4px; font-family:var(--font-sans); appearance:none; color:var(--text-main);">
                                <option value="" disabled selected>Select your profile</option>
                                <option value="Investor/VC">Investor/VC</option>
                                <option value="Researcher/Academic">Researcher/Academic</option>
                                <option value="Distributor/Retailer">Distributor/Retailer</option>
                                <option value="Customer">Customer</option>
                                <option value="Student/Job Seeker">Student/Job Seeker</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>

                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;" class="mobile-stack">
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Full Name *</label>
                                <input type="text" required style="padding:1rem; border:1px solid var(--border); background:var(--bg-alt); border-radius:4px; font-family:var(--font-sans); color:var(--text-main);">
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Email Address *</label>
                                <input type="email" required style="padding:1rem; border:1px solid var(--border); background:var(--bg-alt); border-radius:4px; font-family:var(--font-sans); color:var(--text-main);">
                            </div>
                        </div>
                        
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;" class="mobile-stack">
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Company <span style="font-family:var(--font-sans); text-transform:none;">(Optional)</span></label>
                                <input type="text" style="padding:1rem; border:1px solid var(--border); background:var(--bg-alt); border-radius:4px; font-family:var(--font-sans); color:var(--text-main);">
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.5rem;">
                                <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Subject *</label>
                                <input type="text" required style="padding:1rem; border:1px solid var(--border); background:var(--bg-alt); border-radius:4px; font-family:var(--font-sans); color:var(--text-main);">
                            </div>
                        </div>
                        
                        <div style="display:flex; flex-direction:column; gap:0.5rem;">
                            <label style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Message *</label>
                            <textarea rows="6" required style="padding:1rem; border:1px solid var(--border); background:var(--bg-alt); border-radius:4px; font-family:var(--font-sans); color:var(--text-main);"></textarea>
                        </div>

                        <button type="submit" class="btn btn-outline" style="align-self:flex-start; margin-top:1rem;">Send Inquiry</button>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</section>

</main>
"""

with open(contact_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + FOOTER)

print("Updated contact.html with precise contact details and inquiry form.")
