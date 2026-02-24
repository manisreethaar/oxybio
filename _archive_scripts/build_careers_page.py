import os
import re

with open(r'e:\OXYBIO\careers.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_match = re.search(r'(.*?<main>)', html, re.DOTALL)
footer_match = re.search(r'(</main>.*)', html, re.DOTALL)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

careers_content = """
        <!-- Careers Hero Section -->
        <section class="hero" id="careers-hero" style="min-height: 60vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="hero-glow"></div>
            <div class="container hero-content" style="text-align: center;">
                <div class="badge reveal" style="transition-delay: 0ms; margin: 0 auto 1.5rem;">Join Our Mission</div>
                <h1 class="reveal" style="transition-delay: 150ms;">
                    Build the Future of <br>
                    <span style="color: var(--accent);">Bio-Innovation.</span>
                </h1>
                <p class="subtitle reveal" style="transition-delay: 300ms;" style="max-width: 600px; margin-left: auto; margin-right: auto;">
                    We are looking for passionate researchers and students to join our team at TBI, Adhiyamaan College of Engineering.
                </p>
            </div>
        </section>

        <!-- Current Openings -->
        <section id="open-roles" style="background: var(--bg); padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container">
                <div class="section-header reveal">
                    <h2>Current <span style="color: var(--accent);">Openings</span></h2>
                    <p style="font-size: 1.125rem; margin-top: 1rem;">We are building a next-generation bio-innovation platform at the intersection of probiotic science, functional nutrition, and bio-based cosmetic technology.</p>
                </div>

                <div class="roles-grid" style="display: grid; gap: 2rem; margin-top: 3rem;">
                    <!-- Role Card: Junior Research Associate -->
                    <div class="role-card reveal" style="background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 3rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 2rem;">
                            <div>
                                <h3 style="margin-bottom: 0.75rem; font-size: 1.8rem; color: var(--text-main);">Junior Research Associate / Research Associate <span style="font-size: 1.1rem; color: var(--text-muted); font-weight: normal;">(Bio/Food Technology)</span></h3>
                                <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                                    <span class="badge" style="background: rgba(13, 148, 136, 0.1); color: var(--accent); border: none;">Full Time</span>
                                    <span class="badge" style="background: rgba(13, 148, 136, 0.1); color: var(--accent); border: none;">0-1 Year Exp</span>
                                    <span class="badge" style="background: rgba(13, 148, 136, 0.1); color: var(--accent); border: none;">Hosur, Tamil Nadu</span>
                                </div>
                            </div>
                        </div>
                        
                        <div style="margin-bottom: 2rem;">
                            <h4 style="color: var(--accent); margin-bottom: 1rem; font-size: 1.2rem;">Who we are seeking:</h4>
                            <p style="color: var(--text-muted); line-height: 1.7;">Seeking ambitious and research-driven individuals who aspire to build—not just join—a company. This is not a routine laboratory role. It is a high-ownership position within a performance-driven startup ecosystem. You will contribute to the development, validation, and scale-up of products spanning R&D, regulatory alignment, and pilot production.</p>
                        </div>

                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2.5rem; margin-bottom: 2rem;">
                            <div>
                                <h4 style="color: var(--accent); margin-bottom: 1rem; font-size: 1.2rem;">Key Responsibilities:</h4>
                                <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.2rem;">
                                    <li style="margin-bottom: 0.5rem;">Design and develop probiotic and functional food formulations grounded in fermentation science.</li>
                                    <li style="margin-bottom: 0.5rem;">Develop and optimize bio-fermented cosmetic and skincare systems with stability and efficacy focus.</li>
                                    <li style="margin-bottom: 0.5rem;">Execute laboratory-scale fermentation studies, formulation optimization, and analytical validation.</li>
                                    <li style="margin-bottom: 0.5rem;">Conduct structured shelf-life, stability, and sensory evaluation studies.</li>
                                    <li style="margin-bottom: 0.5rem;">Prepare and maintain SOPs, batch manufacturing records, and regulatory documentation.</li>
                                    <li style="margin-bottom: 0.5rem;">Support pilot-scale trials, technology transfer, and scale-up processes.</li>
                                    <li style="margin-bottom: 0.5rem;">Contribute to IP documentation, technical dossiers, and innovation pipeline development.</li>
                                </ul>
                            </div>
                            <div>
                                <div style="margin-bottom: 2rem;">
                                    <h4 style="color: var(--accent); margin-bottom: 1rem; font-size: 1.2rem;">Who We Are Looking For:</h4>
                                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.2rem;">
                                        <li style="margin-bottom: 0.5rem;">B.Tech / B.Sc. / M.Sc. in Food Technology, Biotechnology, Cosmetic Science, or related.</li>
                                        <li style="margin-bottom: 0.5rem;">Strong foundation in microbial fermentation, food process engineering, or emulsion chemistry.</li>
                                        <li style="margin-bottom: 0.5rem;">Analytical thinker with strong documentation discipline and entrepreneurial mindset.</li>
                                        <li style="margin-bottom: 0.5rem;">Self-driven, adaptable, aspiring to build long-term leadership roles.</li>
                                    </ul>
                                </div>
                                <div>
                                    <h4 style="color: var(--accent); margin-bottom: 1rem; font-size: 1.2rem;">What We Offer:</h4>
                                    <ul style="color: var(--text-muted); line-height: 1.7; padding-left: 1.2rem;">
                                        <li style="margin-bottom: 0.5rem;">Deep-Tech Innovation Exposure & Accelerated Career Growth.</li>
                                        <li style="margin-bottom: 0.5rem;">End-to-End Product Development Experience.</li>
                                        <li style="margin-bottom: 0.5rem;">Innovation & IP Participation with Founder-Level Mentorship.</li>
                                        <li style="margin-bottom: 0.5rem;">Performance-Linked Incentives.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div style="margin-top: 3rem; text-align: center; border-top: 1px solid var(--border); padding-top: 2rem;">
                            <p style="margin-bottom: 1rem; color: var(--text-main); font-weight: 500;">Ready to build with us?</p>
                            <a href="mailto:careers@oxygenbioinnovations.com?subject=Application: Junior Research Associate" class="btn btn-primary" style="padding: 1rem 3rem; font-size: 1.1rem;">Send CV to careers@oxygenbioinnovations.com</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Student Internship Portal -->
        <section id="internship-portal" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container">
                <div class="form-container reveal" style="max-width: 800px; margin: 0 auto; padding: 3rem; background: var(--card-bg); border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <div class="text-center" style="margin-bottom: 3rem;">
                        <div class="badge badge-accent" style="margin-bottom: 1rem;">Student Initiative</div>
                        <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">Student Internship Portal</h2>
                        <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Open to Final Year B.Tech / B.Sc Students to work on live R&D projects.</p>
                    </div>
                    
                    <form action="mailto:info@oxygenbioinnovations.com" method="POST" enctype="text/plain">
                        <div class="form-group" style="margin-bottom: 1.5rem;">
                            <label for="name" class="form-label">Full Name <span style="color: #E11D48;">*</span></label>
                            <input type="text" id="name" name="name" class="form-input" required placeholder="John Doe">
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                            <div class="form-group">
                                <label for="year" class="form-label">Year of Passing <span style="color: #E11D48;">*</span></label>
                                <input type="text" id="year" name="year" class="form-input" required placeholder="e.g. 2024">
                            </div>
                            <div class="form-group">
                                <label for="college" class="form-label">College / University <span style="color: #E11D48;">*</span></label>
                                <input type="text" id="college" name="college" class="form-input" required placeholder="Your Institution">
                            </div>
                        </div>
                        
                        <div class="form-group" style="margin-bottom: 1.5rem;">
                            <label for="degree" class="form-label">Degree & Branch <span style="color: #E11D48;">*</span></label>
                            <input type="text" id="degree" name="degree" class="form-input" required placeholder="B.Tech Biotechnology">
                        </div>
                        
                        <div class="form-group" style="margin-bottom: 1.5rem;">
                            <label for="interest" class="form-label">Area of Interest <span style="color: #E11D48;">*</span></label>
                            <select id="interest" name="interest" class="form-input" required>
                                <option value="" disabled selected>Select an area</option>
                                <option value="Research/Fermentation">Research / Fermentation</option>
                                <option value="Product Formulation">Product Formulation</option>
                                <option value="Marketing & Design">Marketing & Design</option>
                            </select>
                        </div>
                        
                        <div class="form-group" style="margin-bottom: 2rem;">
                            <label for="message" class="form-label">Message / Cover Letter <span style="color: #E11D48;">*</span></label>
                            <textarea id="message" name="message" class="form-input" rows="5" required placeholder="Tell us why you want to intern with us..."></textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center; font-size: 1.1rem; padding: 1rem;">
                            Submit Internship Application
                        </button>
                    </form>

                    <div style="margin-top: 2rem; text-align: center;">
                        <p style="color: var(--text-muted); font-size: 0.95rem;">You can also email your internship submissions directly to <a href="mailto:info@oxygenbioinnovations.com" style="color: var(--accent);">info@oxygenbioinnovations.com</a></p>
                    </div>
                </div>
            </div>
        </section>
"""

with open(r'e:\OXYBIO\careers.html', 'w', encoding='utf-8') as f:
    f.write(header_html + '<main>\n' + careers_content + '\n    </main>\n' + footer_html)

print("Updated careers.html")
