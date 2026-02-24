import os, re
from datetime import datetime

index_path = r'e:\OXYBIO\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

header_m = re.search(r'^.*?(?=<main>)', idx, re.DOTALL)
footer_m = re.search(r'</main>.*$', idx, re.DOTALL)

HEADER = header_m.group(0)
FOOTER = footer_m.group(0)

MAIN_PRIVACY = """
<main>
    <!-- HERO SECTION -->
    <section class="structure-section" style="padding-top:140px; background:var(--bg-alt); border-bottom:1px solid var(--border);">
        <div class="container">
            <div class="flow-left reveal">
                <div class="section-label">
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Legal & Transparency</span>
                </div>
                <h1 class="display" style="font-size:clamp(3.5rem, 8vw, 6rem);">Privacy<br><em>Policy.</em></h1>
                <p class="subtext editorial-col" style="margin-top:var(--space-md);">
                    Oxygen Bioinnovations Private Limited (Brand: RIZE)
                </p>
                <div style="font-family:var(--font-mono); font-size:0.875rem; color:var(--text-muted); margin-top:var(--space-sm);">
                    Last updated: """ + datetime.now().strftime("%B %d, %Y") + """<br>
                    Effective from: """ + datetime.now().strftime("%B %d, %Y") + """
                </div>
            </div>
        </div>
    </section>

    <!-- PLAIN LANGUAGE SUMMARY -->
    <section class="structure-section" style="border-bottom:none;">
        <div class="container">
            <div class="bento-grid reveal" style="margin-top:0;">
                <div class="bento-cell" style="grid-column: span 12; background:var(--text-main); color:var(--bg); padding:clamp(2rem, 5vw, 4rem);">
                    <div style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; margin-bottom:var(--space-md); color:#A3A3A3;">00 / SUMMARY IN PLAIN LANGUAGE</div>
                    <h2 style="font-family:var(--font-serif); font-size:clamp(1.5rem, 3vw, 2.5rem); line-height:1.4; max-width:800px;">
                        Before the legal details — here is what matters in simple words. We collect your email and name when you join our waitlist. We use it only to send you RIZE updates.
                    </h2>
                    <ul style="margin-top:var(--space-md); font-family:var(--font-sans); font-size:1.125rem; line-height:1.8; color:#E8E8E4; list-style:none; padding-left:0;">
                        <li style="margin-bottom:0.5rem;">— We do not sell your data.</li>
                        <li style="margin-bottom:0.5rem;">— We do not share it with advertisers.</li>
                        <li style="margin-bottom:0.5rem;">— We do not do anything weird with it.</li>
                        <li style="margin-top:1.5rem; font-weight:600; color:#fff;">You can ask us to delete it anytime. We will. Within 72 hours. No questions.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- FULL LEGAL DETAILS -->
    <section class="structure-section" style="padding-top:var(--space-lg);">
        <div class="container" style="display:grid; grid-template-columns:1fr; gap:var(--space-xl);">
            
            <!-- Section 1 -->
            <div class="reveal">
                <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:var(--space-sm);">01 / WHO WE ARE</div>
                <h3 class="headline" style="font-size:2rem; margin-bottom:var(--space-md);">Issuer Details</h3>
                <div class="editorial-col" style="font-size:1.125rem; line-height:1.7; color:var(--text-main);">
                    <p>This Privacy Policy is issued by:<br><strong>Oxygen Bioinnovations Private Limited</strong> ('Oxygen Bioinnovations', 'RIZE', 'we', 'us', 'our')</p>
                    <div style="padding-left:1.5rem; border-left:2px solid var(--border); margin:1.5rem 0; color:var(--text-muted);">
                        <p><strong>CIN:</strong> Registration in process</p>
                        <p class="mt-2"><strong>Registered Office:</strong><br>[Your registered address]<br>[City, State, PIN Code]</p>
                        <p class="mt-2"><strong>Principal Place of Business:</strong><br>[TBI Name and Address]<br>[City, State, PIN Code]</p>
                        <p class="mt-2"><strong>Email:</strong> privacy@drinkrize.in</p>
                    </div>
                    <p>We develop precision nutrition products under the brand name RIZE. This policy applies to all personal data collected through our current website, our future website (drinkrize.in), any forms, surveys, or communications operated by us, and any future mobile applications.</p>
                </div>
            </div>

            <!-- Section 2 -->
            <div class="reveal">
                <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:var(--space-sm);">02 / WHAT DATA WE COLLECT</div>
                <h3 class="headline" style="font-size:2rem; margin-bottom:var(--space-md);">Targeted Collection</h3>
                <p class="editorial-col" style="font-size:1.125rem; line-height:1.7; margin-bottom:var(--space-lg);">We only collect data that we actually need. Here is exactly what we collect and why:</p>
                
                <div class="bento-grid" style="margin-top:0;">
                    <!-- Waitlist Data -->
                    <div class="bento-cell" style="grid-column: span 12;">
                        <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:1rem;">2.1 Waitlist Registration Data</h4>
                        <div style="overflow-x:auto;">
                            <table style="width:100%; text-align:left; border-collapse:collapse; font-size:0.95rem;">
                                <thead>
                                    <tr style="border-bottom:1px solid var(--text-main); font-family:var(--font-mono);">
                                        <th style="padding:1rem 0; width:30%;">WHAT WE COLLECT</th>
                                        <th style="padding:1rem 0;">WHY WE NEED IT</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid var(--border);">
                                        <td style="padding:1rem 0; font-weight:600;">First name</td>
                                        <td style="padding:1rem 0; color:var(--text-muted);">To address you personally in our communications.</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid var(--border);">
                                        <td style="padding:1rem 0; font-weight:600;">Email address</td>
                                        <td style="padding:1rem 0; color:var(--text-muted);">To send you launch updates, development news, and early access notifications.</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid var(--border);">
                                        <td style="padding:1rem 0; font-weight:600;">City (if shared)</td>
                                        <td style="padding:1rem 0; color:var(--text-muted);">To understand audience location and plan future distribution.</td>
                                    </tr>
                                    <tr>
                                        <td style="padding:1rem 0; font-weight:600;">Product interest</td>
                                        <td style="padding:1rem 0; color:var(--text-muted);">To understand which formula interests you most and improve our products.</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Automatic Data -->
                    <div class="bento-cell" style="grid-column: span 12;">
                        <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:1rem;">2.4 Automatic Website Data</h4>
                        <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:1rem;">When you visit our website, we automatically collect certain technical data through cookies and analytics tools.</p>
                        <div style="overflow-x:auto;">
                            <table style="width:100%; text-align:left; border-collapse:collapse; font-size:0.95rem;">
                                <thead>
                                    <tr style="border-bottom:1px solid var(--text-main); font-family:var(--font-mono);">
                                        <th style="padding:1rem 0; width:30%;">WHAT WE COLLECT</th>
                                        <th style="padding:1rem 0;">WHY WE NEED IT</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid var(--border);">
                                        <td style="padding:1rem 0; font-weight:600;">IP address (anonymized)</td>
                                        <td style="padding:1rem 0; color:var(--text-muted);">Security and to understand approximate visitor location.</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid var(--border);">
                                        <td style="padding:1rem 0; font-weight:600;">Browser / Device type</td>
                                        <td style="padding:1rem 0; color:var(--text-muted);">To ensure our website works correctly and is optimized for your screen.</td>
                                    </tr>
                                    <tr>
                                        <td style="padding:1rem 0; font-weight:600;">Pages visited / Time</td>
                                        <td style="padding:1rem 0; color:var(--text-muted);">To understand which content is useful and improve our platform.</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div style="padding:1rem; background:var(--bg-alt); margin-top:1.5rem; font-size:0.85rem; font-family:var(--font-mono);">
                            IMPORTANT: We anonymize IP addresses before processing. We cannot identify you personally from this automatic data alone.
                        </div>
                    </div>
                    
                    <!-- Not collected -->
                    <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                        <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:1rem;">2.5 Data We Do NOT Collect</h4>
                        <p style="color:var(--text-muted); font-size:0.95rem;">We do NOT currently collect payment information, delivery addresses, phone numbers, government ID numbers, health/medical information, biometric data, or location tracking data.</p>
                    </div>
                </div>
            </div>

            <!-- Section 3 & 4 -->
            <div class="reveal">
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:var(--space-lg);">
                    <div>
                        <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:var(--space-sm);">03 / HOW WE USE IT</div>
                        <h3 class="headline" style="font-size:2rem; margin-bottom:var(--space-md);">Usage & Boundaries</h3>
                        <ul style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); padding-left:1.5rem;">
                            <li>Send waitlist updates and newsletters</li>
                            <li>Respond to your questions</li>
                            <li>Improve website and product decisions</li>
                            <li>Comply with legal requirements</li>
                        </ul>
                        <div style="margin-top:2rem; padding-left:1rem; border-left:2px solid var(--text-main);">
                            <strong>WE DO NOT:</strong> Sell to third parties, share with ad brokers, create targeting profiles, or make automated decisions.
                        </div>
                    </div>
                    <div>
                        <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:var(--space-sm);">04 / WHO WE SHARE IT WITH</div>
                        <h3 class="headline" style="font-size:2rem; margin-bottom:var(--space-md);">Strict Partners</h3>
                        <p style="font-size:1.125rem; line-height:1.7; color:var(--text-muted);">We share data ONLY with service providers who operated our business:</p>
                        <ul style="font-size:1.125rem; line-height:1.7; color:var(--text-muted); padding-left:1.5rem;">
                            <li><strong>Email Provider:</strong> For sending updates.</li>
                            <li><strong>Google Analytics 4:</strong> Anonymized browsing data.</li>
                            <li><strong>Vercel Inc:</strong> Website hosting logs.</li>
                            <li><strong>Law Enforcement:</strong> If required by valid court order or Indian Law.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Section 7 -->
            <div class="reveal">
                <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:var(--space-sm);">07 / YOUR RIGHTS</div>
                <h3 class="headline" style="font-size:2rem; margin-bottom:var(--space-md);">Control your data</h3>
                <p class="editorial-col" style="font-size:1.125rem; line-height:1.7; margin-bottom:var(--space-lg);">Under Indian law (DPDP Act 2023, IT Act 2000), you have total control.</p>
                
                <div class="bento-grid" style="margin-top:0;">
                    <div class="bento-cell" style="grid-column: span 4;">
                        <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Right to Access</h4>
                        <p style="font-size:0.9rem; color:var(--text-muted);">Ask us what data we hold. We deliver in 72h.</p>
                    </div>
                    <div class="bento-cell" style="grid-column: span 4;">
                        <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Right to Erasure</h4>
                        <p style="font-size:0.9rem; color:var(--text-muted);">Ask us to delete everything. We wipe it in 72h.</p>
                    </div>
                    <div class="bento-cell" style="grid-column: span 4;">
                        <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">Withdraw Consent</h4>
                        <p style="font-size:0.9rem; color:var(--text-muted);">Unsubscribe via email link or contact us directly.</p>
                    </div>
                    <div class="bento-cell" style="grid-column: span 12; background:var(--bg-alt);">
                        <h4 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.5rem;">How to exercise rights:</h4>
                        <p style="font-family:var(--font-mono); font-size:0.9rem; color:var(--text-main);">Email: privacy@drinkrize.in | Subject: Data Rights Request</p>
                    </div>
                </div>
            </div>

        </div>
    </section>
</main>
"""

with open(r'e:\OXYBIO\privacy.html', 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_PRIVACY + '\n</main>\n' + FOOTER)

print("Created privacy.html in premium Bento format.")
