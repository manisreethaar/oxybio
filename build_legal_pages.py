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

# -- PRIVACY POLICY PAGE CONTENT --
privacy_content = """
        <!-- Hero Section -->
        <section class="hero" style="min-height: 40vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="hero-glow"></div>
            <div class="container hero-content" style="text-align: center;">
                <h1 class="reveal" style="transition-delay: 0ms; font-size: 3.5rem;">Privacy Policy</h1>
                <p class="subtitle reveal" style="transition-delay: 150ms;">
                    Company: Oxygen Bioinnovations | Brand: RIZE<br>
                    <strong>Effective from: October 2026</strong>
                </p>
            </div>
        </section>

        <!-- Content Section -->
        <section style="padding: 4rem 0 8rem;">
            <div class="container" style="max-width: 800px;">
                
                <!-- Summary Box -->
                <div class="reveal" style="background: var(--card-bg); padding: 2.5rem; border-radius: 12px; border: 1px solid var(--accent); margin-bottom: 4rem; border-left: 6px solid var(--accent);">
                    <h3 style="color: var(--accent); margin-bottom: 1rem;">Plain Language Summary</h3>
                    <ul style="color: var(--text-main); font-size: 1.1rem; line-height: 1.7; padding-left: 1.5rem; margin-bottom: 0;">
                        <li style="margin-bottom: 0.5rem;">We collect your email and name when you join our waitlist to send RIZE updates.</li>
                        <li style="margin-bottom: 0.5rem;">We do not sell your data or share it with advertisers.</li>
                        <li style="margin-bottom: 0;">You can ask us to delete it anytime. We will do it within 72 hours. No questions.</li>
                    </ul>
                </div>

                <div class="legal-content reveal" style="transition-delay: 150ms;">
                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">1. Who We Are</h3>
                    <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 2rem;">
                        <strong>Principal Place of Business:</strong> TBI, Adhiyamaan College of Engineering, Hosur, Tamil Nadu<br>
                        <strong>Email:</strong> <a href="mailto:info@oxygenbioinnovations.com" style="color: var(--accent);">info@oxygenbioinnovations.com</a>
                    </p>

                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">2. What Data We Collect</h3>
                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.5rem; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Waitlist Data:</strong> First name, Email address, City (optional), Product interest (for personalized comms and planning).</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Newsletter Data:</strong> Email address, Name, Preferences.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Contact Form Data:</strong> Name, Email address, Message content, Reason for contact.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Automatic Website Data:</strong> IP address (anonymized), Browser & Device type, Pages visited & Time, Referring website.</li>
                    </ul>
                    <div style="background: rgba(225, 29, 72, 0.05); border-left: 4px solid #E11D48; padding: 1.5rem; border-radius: 4px; margin-bottom: 2rem;">
                        <p style="margin: 0; color: var(--text-main);"><strong>Data We Do Not Collect (Currently):</strong> Payment info, Delivery addresses, Phone numbers, Government ID, Health/medical info, Biometric/Location tracking. <em>(Will be updated pre-launch).</em></p>
                    </div>


                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">3. How We Use Your Data</h3>
                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.5rem; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">To communicate with you (waitlist, newsletter, enquiries).</li>
                        <li style="margin-bottom: 0.5rem;">To improve our products and website.</li>
                        <li style="margin-bottom: 0.5rem;">To comply with legal requirements.</li>
                    </ul>
                    <p style="color: var(--text-main); font-weight: 500; line-height: 1.7; margin-bottom: 2rem;">
                        <strong>WE DO NOT:</strong> Sell to third parties, share with ad brokers, create ad profiles, send 3rd party marketing, or target you with 3rd party ads.
                    </p>

                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">4. Who We Share Data With (Service Providers)</h3>
                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.5rem; margin-bottom: 2rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Email:</strong> Mailchimp / Email Service (USA/Global)</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Analytics:</strong> Google Analytics 4 (USA/Global)</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Hosting:</strong> Vercel Inc (USA/Global)</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Legal Requirements:</strong> Shared if required by valid court order or FSSAI/regulatory bodies under Indian Law.</li>
                    </ul>

                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">5. How Long We Keep Your Data</h3>
                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.5rem; margin-bottom: 2rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Waitlist/Newsletter:</strong> Until unsubscribe + 30 days.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Contact messages:</strong> 2 years.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Website analytics:</strong> 14 months.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Future purchases:</strong> 7 years (GST law).</li>
                    </ul>

                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">6. Protection & Rights</h3>
                    <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
                        <strong>Protection:</strong> SSL/TLS encryption, restricted access. Notification within 72 hours in case of breach.
                    </p>
                    <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 2rem;">
                        <strong>Your Rights (Under DPDP Act 2023 & IT Act 2000):</strong> Right to Access, Correction, Erasure (Deletion), Withdraw Consent. Acknowledged within 24h, fulfilled within 72h.
                    </p>

                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">7. Contact - Data Protection Officer</h3>
                    <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 2rem;">
                        Privacy Team, Oxygen Bioinnovations<br>
                        Email: <a href="mailto:info@oxygenbioinnovations.com" style="color: var(--accent);">info@oxygenbioinnovations.com</a>
                    </p>
                </div>
            </div>
        </section>
"""

# -- TERMS AND CONDITIONS PAGE CONTENT --
terms_content = """
        <!-- Hero Section -->
        <section class="hero" style="min-height: 40vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="hero-glow"></div>
            <div class="container hero-content" style="text-align: center;">
                <h1 class="reveal" style="transition-delay: 0ms; font-size: 3.5rem;">Terms & Conditions</h1>
                <p class="subtitle reveal" style="transition-delay: 150ms;">
                    Company: Oxygen Bioinnovations<br>
                    <strong>Last updated: February 2026</strong>
                </p>
            </div>
        </section>

        <!-- Content Section -->
        <section style="padding: 4rem 0 8rem;">
            <div class="container" style="max-width: 800px;">
                <div class="legal-content reveal">
                    
                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">1 & 2. Agreement to Terms & About Us</h3>
                    <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
                        These agreements apply to visitors, waitlist/newsletter subscribers, and future customers of Oxygen Bioinnovations.
                    </p>
                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.5rem; margin-bottom: 2rem;">
                        <li><strong>Registered Office:</strong> TBI, Adhiyamaan College of Engineering, Hosur, Tamil Nadu</li>
                        <li><strong>Email:</strong> <a href="mailto:info@oxygenbioinnovations.com" style="color: var(--accent);">info@oxygenbioinnovations.com</a></li>
                        <li><strong>FSSAI License:</strong> [Number when issued]</li>
                    </ul>

                    <!-- Pre-Launch Box -->
                    <div style="background: rgba(13, 148, 136, 0.05); border-left: 4px solid var(--accent); padding: 1.5rem; border-radius: 4px; margin-bottom: 3rem;">
                        <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem; color: var(--text-main);">3. Pre-Launch Status</h3>
                        <p style="margin: 0; color: var(--text-muted); line-height: 1.6;">As of February 2026, Oxygen Bioinnovations is a pre-launch company. Products are in development, no purchase orders accepted, and specifications, prices, or dates are estimates only.</p>
                    </div>

                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">4. Intellectual Property</h3>
                    <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1rem;">
                        The Company owns the 'Oxygen Bioinnovations' name, 'RIZE' brand, logo, website copy, research content, and graphics.
                    </p>
                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.5rem; margin-bottom: 2rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Permitted:</strong> Reading, sharing links, quoting up to 100 words with credit/link, social sharing.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Not Permitted:</strong> Copying without permission, using brand/logos, scraping data, commercial use.</li>
                    </ul>

                    <div style="background: rgba(225, 29, 72, 0.05); border-left: 4px solid #E11D48; padding: 1.5rem; border-radius: 4px; margin-bottom: 3rem;">
                        <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem; color: var(--text-main); display:flex; align-items:center; gap:0.5rem;">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#E11D48" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg> 
                            5. Health and Medical Disclaimer
                        </h3>
                        <ul style="color: var(--text-main); line-height: 1.6; padding-left: 1.5rem; margin-bottom: 0;">
                            <li style="margin-bottom: 0.5rem;">Content is <strong>NOT</strong> medical advice, diagnosis, or treatment recommendation.</li>
                            <li style="margin-bottom: 0.5rem;">RIZE products are food supplements (FSSAI regulated), <strong>NOT</strong> medicines/drugs.</li>
                            <li style="margin-bottom: 0;">Consult doctor before use if pregnant, under 18, diagnosed condition, on meds, or scheduled for surgery.</li>
                        </ul>
                    </div>

                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-main);">6 to 11. General Terms</h3>
                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.5rem; margin-bottom: 2rem;">
                        <li style="margin-bottom: 1rem;"><strong>User Conduct:</strong> No false information, impersonation, unauthorized access, viruses, spamming, or unlawful activity on our platform.</li>
                        <li style="margin-bottom: 1rem;"><strong>Liability:</strong> No liability for indirect loss, data loss, decisions based on content, or 3rd party links. Max liability is capped at the amount paid in the last 3 months.</li>
                        <li style="margin-bottom: 0;"><strong>Governing Law:</strong> Laws of India. Disputes subject to exclusive jurisdiction of courts in Hosur, India (after 30-day amicable attempt).</li>
                    </ul>

                </div>
            </div>
        </section>
"""

with open(r'e:\\OXYBIO\\privacy.html', 'w', encoding='utf-8') as f:
    f.write(header_html + '<main>\n' + privacy_content + '\n    </main>\n' + footer_html)

with open(r'e:\\OXYBIO\\terms.html', 'w', encoding='utf-8') as f:
    f.write(header_html + '<main>\n' + terms_content + '\n    </main>\n' + footer_html)

print("Generated privacy.html and terms.html")
