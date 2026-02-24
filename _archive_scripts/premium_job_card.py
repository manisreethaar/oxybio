import codecs
import re

with codecs.open('e:\\OXYBIO\\careers.html', 'r', 'utf-8') as f:
    html = f.read()

start_idx = html.find('<!-- Role Outline Card -->')
end_idx = html.find('<!-- ═══════════════════════════════════════════════════════', start_idx + 10)

if start_idx != -1 and end_idx != -1:
    NEW_CARD = '''<!-- Role Outline Card -->
        <div style="background:var(--bg); border:1px solid var(--border); display:grid; grid-template-columns:350px 1fr; gap:0; border-radius:12px; overflow:hidden;" class="mobile-stack-card">
            
            <!-- Left Sticky Header -->
            <div style="padding:4rem 3rem; border-right:1px solid var(--border); background:var(--bg-alt); display:flex; flex-direction:column; justify-content:space-between; position:relative;">
                <div style="position:sticky; top:120px;">
                    <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:2rem; text-transform:uppercase; letter-spacing:0.05em;">
                        <span style="color:var(--text-main); font-weight:700;">Full Time</span>
                        <span style="color:#ccc;">|</span>
                        <span>0-1 YR EXP</span>
                    </div>
                    <h3 class="display" style="font-size:clamp(2rem, 3vw, 2.75rem); line-height:1.1; letter-spacing:-0.02em; margin-bottom:1rem;">Research<br>Associate</h3>
                    <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-main); border:1px solid var(--text-main); border-radius:50px; display:inline-block; padding:0.4rem 0.8rem; margin-bottom:3rem;">Bio / Food Tech</div>
                    
                    <a href="mailto:careers@oxygenbioinnovations.com?subject=Application%20for%20Research%20Associate" class="btn btn-primary" style="padding:1.2rem; width:100%; justify-content:center; border-radius:8px;">Apply via Email →</a>
                    <p style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); text-align:center; margin-top:1.5rem;">careers@oxygenbioinnovations.com</p>
                </div>
            </div>
            
            <!-- Right Details (Extensive) -->
            <div style="padding:4rem;">
                
                <!-- Editorial Intro -->
                <div style="margin-bottom:4rem; padding-bottom:3rem; border-bottom:1px solid var(--border);">
                    <p style="font-size:1.5rem; line-height:1.6; color:var(--text-main); margin-bottom:2rem; font-weight:500; letter-spacing:-0.01em;">
                        We are seeking ambitious and research-driven individuals who aspire to build—not just join—a company.
                    </p>
                    <p style="font-size:1.15rem; line-height:1.7; color:var(--text-muted); margin-bottom:2rem;">
                        This opportunity is ideal for candidates who are passionate about deep-tech innovation and are prepared to grow as the organization scales from laboratory research to full-scale commercialization.
                    </p>
                    <div style="padding:2rem; background:var(--bg-alt); border-left:4px solid var(--text-main); font-family:var(--font-serif); font-style:italic; font-size:1.25rem; color:var(--text-main);">
                        "This is not a routine laboratory role. It is a high-ownership position within a performance-driven startup ecosystem, where scientific rigor meets entrepreneurial execution."
                    </div>
                </div>

                <!-- Role Overview -->
                <div style="margin-bottom:4rem;">
                    <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:var(--text-main); text-transform:uppercase; margin-bottom:1.5rem; display:flex; align-items:center; gap:0.5rem;">
                        <span style="width:12px; height:12px; background:var(--text-main); border-radius:50%; display:inline-block;"></span> 01 / Role Overview
                    </h4>
                    <p style="font-size:1.15rem; line-height:1.7; color:var(--text-main);">
                        As a Junior Research Associate / Research Associate, you will contribute to the development, validation, and scale-up of advanced probiotic formulations, functional beverages, nutraceutical systems, and bio-fermented cosmetic products. You will work across R&D, regulatory alignment, pilot production, and commercialization strategy.
                    </p>
                </div>

                <!-- Key Responsibilities -->
                <div style="margin-bottom:4rem;">
                    <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:var(--text-main); text-transform:uppercase; margin-bottom:1.5rem; display:flex; align-items:center; gap:0.5rem;">
                        <span style="width:12px; height:12px; background:var(--text-main); border-radius:50%; display:inline-block;"></span> 02 / The Output
                    </h4>
                    <div style="display:grid; grid-template-columns:1fr; gap:0.75rem;">
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Design and develop innovative probiotic and functional food formulations grounded in fermentation science.</span>
                        </div>
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Develop and optimize bio-fermented cosmetic and skincare systems with stability and efficacy focus.</span>
                        </div>
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Execute laboratory-scale fermentation studies, formulation optimization, and analytical validation.</span>
                        </div>
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Conduct structured shelf-life, stability, and sensory evaluation studies following scientific protocols.</span>
                        </div>
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Prepare and maintain SOPs, batch manufacturing records, and regulatory documentation (FSSAI/CDSCO aligned).</span>
                        </div>
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Support pilot-scale trials, technology transfer, and scale-up processes.</span>
                        </div>
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Contribute to IP documentation, technical dossiers, and innovation pipeline development.</span>
                        </div>
                        <div style="display:flex; gap:1.5rem; align-items:flex-start; padding:1.25rem; border:1px solid var(--border); border-radius:8px; background:var(--bg-alt);">
                            <span style="color:#0D8A74; font-weight:bold; margin-top:2px;">✓</span>
                            <span style="color:var(--text-main); font-size:1.1rem; line-height:1.5;">Actively participate in research problem-solving, process refinement, and continuous improvement initiatives.</span>
                        </div>
                    </div>
                </div>

                <!-- Who We Are Looking For -->
                <div style="margin-bottom:4rem;">
                    <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:var(--text-main); text-transform:uppercase; margin-bottom:1.5rem; display:flex; align-items:center; gap:0.5rem;">
                        <span style="width:12px; height:12px; background:var(--text-main); border-radius:50%; display:inline-block;"></span> 03 / The Profile
                    </h4>
                    <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:1.5rem; border-top:1px dashed var(--border); padding-top:2rem;">
                        <li style="display:flex; align-items:baseline; gap:1rem;">
                            <div style="width:6px; height:6px; background:#000; border-radius:50%; flex-shrink:0;"></div>
                            <span style="font-size:1.15rem; line-height:1.6; color:var(--text-muted);"><strong style="color:var(--text-main);">Degree:</strong> B.Tech / B.Sc. / M.Sc. in Food Technology, Biotechnology, Cosmetic Science, or a related discipline.</span>
                        </li>
                        <li style="display:flex; align-items:baseline; gap:1rem;">
                            <div style="width:6px; height:6px; background:#000; border-radius:50%; flex-shrink:0;"></div>
                            <span style="font-size:1.15rem; line-height:1.6; color:var(--text-muted);"><strong style="color:var(--text-main);">Foundation:</strong> Strong core in microbial fermentation, food process engineering, or emulsion chemistry.</span>
                        </li>
                        <li style="display:flex; align-items:baseline; gap:1rem;">
                            <div style="width:6px; height:6px; background:#000; border-radius:50%; flex-shrink:0;"></div>
                            <span style="font-size:1.15rem; line-height:1.6; color:var(--text-muted);"><strong style="color:var(--text-main);">Mindset:</strong> Analytical thinker with strong documentation discipline and scientific integrity.</span>
                        </li>
                        <li style="display:flex; align-items:baseline; gap:1rem;">
                            <div style="width:6px; height:6px; background:#000; border-radius:50%; flex-shrink:0;"></div>
                            <span style="font-size:1.15rem; line-height:1.6; color:var(--text-muted);"><strong style="color:var(--text-main);">Drive:</strong> Entrepreneurial mindset with willingness to work in a fast-paced, evolving startup environment.</span>
                        </li>
                        <li style="display:flex; align-items:baseline; gap:1rem;">
                            <div style="width:6px; height:6px; background:#000; border-radius:50%; flex-shrink:0;"></div>
                            <span style="font-size:1.15rem; line-height:1.6; color:var(--text-muted);"><strong style="color:var(--text-main);">Ambition:</strong> Self-driven, adaptable, and motivated to take ownership beyond defined job boundaries, aspiring to build long-term leadership roles as the company grows.</span>
                        </li>
                    </ul>
                </div>

                <!-- What We Offer -->
                <div style="background:var(--text-main); color:var(--bg); padding:4rem; border-radius:12px; margin-top:2rem;">
                    <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; color:#a3a3a3; text-transform:uppercase; margin-bottom:3rem; display:flex; align-items:center; gap:0.5rem; border-bottom:1px solid #333; padding-bottom:1rem;">
                        <span style="width:12px; height:12px; background:var(--bg); border-radius:50%; display:inline-block;"></span> 04 / The Offer
                    </h4>
                    
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem;" class="mobile-stack">
                        <div>
                            <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:#fff; margin-bottom:0.75rem;">Deep-Tech Exposure</h5>
                            <p style="font-size:1rem; color:#aaa; line-height:1.6;">Work on high-impact R&D projects with real commercialization pathways.</p>
                        </div>
                        <div>
                            <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:#fff; margin-bottom:0.75rem;">Accelerated Career Growth</h5>
                            <p style="font-size:1rem; color:#aaa; line-height:1.6;">Performance-based responsibility expansion with leadership opportunities.</p>
                        </div>
                        <div>
                            <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:#fff; margin-bottom:0.75rem;">End-to-End Experience</h5>
                            <p style="font-size:1rem; color:#aaa; line-height:1.6;">From lab-scale concept to regulatory approval and market launch.</p>
                        </div>
                        <div>
                            <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:#fff; margin-bottom:0.75rem;">Innovation & IP Participation</h5>
                            <p style="font-size:1rem; color:#aaa; line-height:1.6;">Exposure to patent drafting, technology validation, and commercialization.</p>
                        </div>
                        <div>
                            <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:#fff; margin-bottom:0.75rem;">Founder-Level Mentorship</h5>
                            <p style="font-size:1rem; color:#aaa; line-height:1.6;">Direct collaboration with leadership in a high-visibility growth environment.</p>
                        </div>
                        <div>
                            <h5 style="font-family:var(--font-serif); font-size:1.35rem; color:#fff; margin-bottom:0.75rem;">Incentive Aligned</h5>
                            <p style="font-size:1rem; color:#aaa; line-height:1.6;">Competitive compensation structured with capability, contribution, and milestones.</p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
<!-- 
'''
    html = html[:start_idx] + NEW_CARD + "\n        </div>\n\n    </div>\n</section>\n" + html[end_idx:]
    with codecs.open('e:\\OXYBIO\\careers.html', 'w', 'utf-8') as f:
        f.write(html)
    print("Careers job profile upgraded to premium layout.")
else:
    print(f"Failed to locate insertion markers. Start: {start_idx}, End: {end_idx}")
