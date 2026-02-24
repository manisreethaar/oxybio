import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace from the old science section start to the extra closing tags
old_pattern = re.compile(
    r'<!-- ═+\s*SCIENCE & PILLARS SECTION.*?</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_section = '''<!-- ═══════════════════════════════════════════════════════
     SCIENCE & PILLARS SECTION — Premium Redesign v2
════════════════════════════════════════════════════════ -->
            <section style="padding: 6rem 0; border-bottom:1px solid var(--border);">
                <div class="container">

                    <!-- Split header -->
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:end; margin-bottom:4rem;">
                        <div>
                            <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.5rem;">
                                <div style="width:24px; height:1px; background:var(--text-main);"></div>
                                <span style="font-family:var(--font-mono); font-size:0.7rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted);">The Science</span>
                            </div>
                            <h2 style="font-family:var(--font-serif); font-size:clamp(2.5rem,5vw,3.75rem); font-weight:900; line-height:1.0; letter-spacing:-0.04em; color:var(--text-main);">We show<br><em>our work.</em></h2>
                        </div>
                        <div style="padding-bottom:0.5rem;">
                            <p style="font-size:1.05rem; line-height:1.75; color:var(--text-muted); margin-bottom:2rem; max-width:460px;">Every formulation decision has a peer-reviewed reason. Every ingredient has a verified source. Every claim is something we can prove.</p>
                            <a href="science.html" style="display:inline-flex; align-items:center; gap:0.5rem; font-family:var(--font-mono); font-size:0.8rem; letter-spacing:0.1em; border:1px solid var(--border); padding:0.75rem 1.5rem; border-radius:100px; color:var(--text-main); text-decoration:none; transition:all 0.25s;">View Ingredients Index &rarr;</a>
                        </div>
                    </div>

                    <!-- 3 Science Cards -->
                    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-bottom:4rem;">

                        <!-- Card 01 -->
                        <div style="background:#ffffff; border:1px solid var(--border); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="font-family:var(--font-mono); font-size:0.72rem; font-weight:700; letter-spacing:0.12em; color:var(--text-muted);">01</span>
                                <span style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; text-transform:uppercase; border:1px solid var(--border); border-radius:100px; padding:0.3rem 0.75rem; color:var(--text-muted);">Formulation</span>
                            </div>
                            <h3 style="font-family:var(--font-serif); font-size:1.6rem; font-weight:800; color:var(--text-main); line-height:1.15; letter-spacing:-0.02em;">Active forms<br>only.</h3>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.75; flex-grow:1;">Most products use the cheapest permitted form. We use Methylcobalamin, Pyridoxal-5-Phosphate, 5-MTHF Folate, and Albion TRAACS&reg; Chelated Minerals &mdash; the forms your body actually absorbs.</p>
                            <div style="padding-top:1.5rem; border-top:1px solid var(--border);">
                                <div style="font-family:var(--font-serif); font-size:3.5rem; font-weight:900; color:var(--text-main); line-height:1; letter-spacing:-0.04em;">3&ndash;4&times;</div>
                                <div style="font-family:var(--font-mono); font-size:0.68rem; text-transform:uppercase; letter-spacing:0.12em; color:var(--text-muted); margin-top:0.5rem;">Better absorption vs generic</div>
                            </div>
                            <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); border-top:1px solid var(--border); padding-top:1rem;">Cost diff: only &Ropf;2/serving</div>
                        </div>

                        <!-- Card 02 — Inverted Black -->
                        <div style="background:var(--text-main); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="font-family:var(--font-mono); font-size:0.72rem; font-weight:700; letter-spacing:0.12em; color:rgba(255,255,255,0.35);">02</span>
                                <span style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; text-transform:uppercase; border:1px solid rgba(255,255,255,0.15); border-radius:100px; padding:0.3rem 0.75rem; color:rgba(255,255,255,0.5);">Verification</span>
                            </div>
                            <h3 style="font-family:var(--font-serif); font-size:1.6rem; font-weight:800; color:#ffffff; line-height:1.15; letter-spacing:-0.02em;">Verified,<br>not assumed.</h3>
                            <p style="font-size:0.9rem; color:rgba(255,255,255,0.6); line-height:1.75; flex-grow:1;">Our Lion's Mane extract is verified using the Megazyme AOAC method &mdash; the gold standard for active compound content. Not marketing weight. Third-party certified.</p>
                            <div style="padding-top:1.5rem; border-top:1px solid rgba(255,255,255,0.1);">
                                <div style="font-family:var(--font-serif); font-size:3.5rem; font-weight:900; color:#ffffff; line-height:1; letter-spacing:-0.04em;">&gt;30%</div>
                                <div style="font-family:var(--font-mono); font-size:0.68rem; text-transform:uppercase; letter-spacing:0.12em; color:rgba(255,255,255,0.4); margin-top:0.5rem;">&beta;-glucan content guaranteed</div>
                            </div>
                            <div style="font-family:var(--font-mono); font-size:0.72rem; color:rgba(255,255,255,0.35); border-top:1px solid rgba(255,255,255,0.1); padding-top:1rem;">AOAC Method &middot; Megazyme Certified</div>
                        </div>

                        <!-- Card 03 -->
                        <div style="background:var(--bg-alt); border:1px solid var(--border); border-radius:24px; padding:2.5rem; display:flex; flex-direction:column; gap:1.25rem;">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="font-family:var(--font-mono); font-size:0.72rem; font-weight:700; letter-spacing:0.12em; color:var(--text-muted);">03</span>
                                <span style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; text-transform:uppercase; border:1px solid var(--border); border-radius:100px; padding:0.3rem 0.75rem; color:var(--text-muted);">Clinical</span>
                            </div>
                            <h3 style="font-family:var(--font-serif); font-size:1.6rem; font-weight:800; color:var(--text-main); line-height:1.15; letter-spacing:-0.02em;">Proving it,<br>not claiming it.</h3>
                            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.75; flex-grow:1;">We designed a clinical study for 135 participants across 8 weeks &mdash; before we launch commercially. Primary outcomes: Biomarkers and cognitive tests. All results published.</p>
                            <div style="padding-top:1.5rem; border-top:1px solid var(--border);">
                                <div style="font-family:var(--font-serif); font-size:3.5rem; font-weight:900; color:var(--text-main); line-height:1; letter-spacing:-0.04em;">135</div>
                                <div style="font-family:var(--font-mono); font-size:0.68rem; text-transform:uppercase; letter-spacing:0.12em; color:var(--text-muted); margin-top:0.5rem;">Clinical study participants</div>
                            </div>
                            <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); border-top:1px solid var(--border); padding-top:1rem;">Results published regardless of outcome</div>
                        </div>

                    </div>

                    <!-- Comparison Table — Premium Black-Header Design -->
                    <div style="border:1px solid var(--border); border-radius:20px; overflow:hidden;">
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; background:var(--text-main); padding:1.25rem 1.5rem;">
                            <div style="font-family:var(--font-mono); font-size:0.68rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.4);">METRIC</div>
                            <div style="font-family:var(--font-mono); font-size:0.68rem; letter-spacing:0.2em; text-transform:uppercase; color:#ffffff; font-weight:700;">OXYGEN BIOINNOVATIONS</div>
                            <div style="font-family:var(--font-mono); font-size:0.68rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.4);">THE INDUSTRY STANDARD</div>
                        </div>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); align-items:center;">
                            <div style="font-size:0.9rem; font-weight:600;">Vitamin Forms</div>
                            <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">Active (bioavailable) Forms ✓</div>
                            <div style="font-size:0.9rem; color:var(--text-muted);">Cheapest Synthetic Forms</div>
                        </div>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); align-items:center; background:var(--bg-alt);">
                            <div style="font-size:0.9rem; font-weight:600;">Vitamin B12</div>
                            <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">Methylcobalamin ✓</div>
                            <div style="font-size:0.9rem; color:var(--text-muted);">Cyanocobalamin</div>
                        </div>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); align-items:center;">
                            <div style="font-size:0.9rem; font-weight:600;">Minerals</div>
                            <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">Chelated TRAACS&reg; Amino Acid ✓</div>
                            <div style="font-size:0.9rem; color:var(--text-muted);">Oxide / Sulfate Forms</div>
                        </div>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); align-items:center; background:var(--bg-alt);">
                            <div style="font-size:0.9rem; font-weight:600;">Mineral Absorption</div>
                            <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">~28% ✓</div>
                            <div style="font-size:0.9rem; color:var(--text-muted);">~8% (Standard)</div>
                        </div>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); align-items:center;">
                            <div style="font-size:0.9rem; font-weight:600;">Mushroom Extracts</div>
                            <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">Verified &beta;-glucan % ✓</div>
                            <div style="font-size:0.9rem; color:var(--text-muted);">Unverified weight labels</div>
                        </div>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); align-items:center; background:var(--bg-alt);">
                            <div style="font-size:0.9rem; font-weight:600;">Efficacy Data</div>
                            <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">Pre-Launch Clinical Study ✓</div>
                            <div style="font-size:0.9rem; color:var(--text-muted);">Zero Clinical Efficacy Data</div>
                        </div>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; padding:1.25rem 1.5rem; align-items:center;">
                            <div style="font-size:0.9rem; font-weight:600;">Lab Reports</div>
                            <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">Public CoA every batch ✓</div>
                            <div style="font-size:0.9rem; color:var(--text-muted);">No Transparency</div>
                        </div>
                    </div>

                </div>
            </section>

'''

result = old_pattern.sub(new_section, content)

if result == content:
    print("ERROR: Pattern not found! Trying broader match...")
    # Try from line numbers instead
    lines = content.split('\n')
    # Find the science section start line
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if 'SCIENCE & PILLARS SECTION' in line and start_idx is None:
            start_idx = i - 1  # include the section tag line
        if start_idx and i > start_idx:
            if ('</div>' in line and '</div>' in lines[i+1] if i+1 < len(lines) else False) and ('</section>' in lines[i+2] if i+2 < len(lines) else False):
                if i > start_idx + 50:  # make sure we're past the content
                    end_idx = i + 3
                    break

    if start_idx and end_idx:
        lines[start_idx:end_idx] = [new_section]
        result = '\n'.join(lines)
        print(f"Replaced lines {start_idx} to {end_idx}")
    else:
        print(f"Could not find bounds. start={start_idx}, end={end_idx}")
else:
    print("SUCCESS: Pattern matched and replaced!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(result)

print("Done.")
