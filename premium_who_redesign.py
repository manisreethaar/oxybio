import sys

with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Who We Are section boundaries
section_start = content.find('<!-- SECTION 3')
section_end_marker = '</section>'
section_end = content.find(section_end_marker, content.find('id="about-who"')) + len(section_end_marker)

PREMIUM_WHO_SECTION = '''<!-- SECTION 3 — WHO WE ARE (Founder + Operating Principles) -->
        <section class="structure-section" id="about-who"
            style="background:var(--bg-alt); border-top:1px solid var(--border); overflow:hidden;">
            <div class="container">

                <!-- Section Header -->
                <div class="flow-left reveal" style="max-width:900px; margin-bottom:var(--space-xl);">
                    <div class="badge" style="margin-bottom:var(--space-md); border-color:var(--text-main);">Who We Are</div>
                    <h1 class="display" style="font-size:var(--text-6xl); line-height:var(--leading-none);">Built by<br><em>scientists.</em></h1>
                    <p class="subtext editorial-col"
                        style="margin-top:var(--space-md); font-size:var(--text-xl); line-height:var(--leading-tight);">
                        Not nutritionists who became entrepreneurs. Scientists who were frustrated by what existed and decided to build something the market refused to.
                    </p>
                </div>

                <!-- Two-col sticky layout -->
                <div style="display:grid; grid-template-columns:1fr 2fr; gap:var(--space-xl); align-items:start;"
                    class="mobile-stack reveal">

                    <!-- Sticky Sidebar with progress bar -->
                    <div style="position:sticky; top:120px;" class="editorial-col">
                        <div style="font-family:var(--font-mono); font-size:var(--text-xs); letter-spacing:0.12em; color:var(--text-muted); margin-bottom:1.5rem; text-transform:uppercase;">Chapters</div>
                        <div style="position:relative; padding-left:1.5rem;">
                            <!-- Active track line -->
                            <div style="position:absolute; left:0; top:0; bottom:0; width:1px; background:var(--border);"></div>
                            <div style="display:flex; flex-direction:column; gap:2rem;">
                                <div class="index-nav-item" data-target="chapter-03"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem;">01</div>
                                    <div style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-main); font-weight:600; line-height:var(--leading-tight);">The Founder</div>
                                </div>
                                <div class="index-nav-item" data-target="chapter-04"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem;">02</div>
                                    <div style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-muted); line-height:var(--leading-tight);">Our Approach</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Chapters content -->
                    <div>

                        <!-- ═══ CHAPTER 01: THE FOUNDER ═══ -->
                        <div id="chapter-03" class="chapter-section" style="margin-bottom:var(--space-xl);">

                            <!-- Chapter label -->
                            <div style="display:flex; align-items:center; gap:1rem; margin-bottom:2rem;">
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); text-transform:uppercase;">Chapter 01</div>
                                <div style="height:1px; flex:1; background:var(--border);"></div>
                            </div>

                            <!-- Premium founder card -->
                            <div style="background:var(--text-main); color:#fff; padding:2.5rem; margin-bottom:2rem; position:relative; overflow:hidden;">
                                <!-- Ghost watermark -->
                                <div style="position:absolute; right:-0.5rem; bottom:-1rem; font-family:var(--font-serif); font-size:8rem; font-weight:900; color:rgba(255,255,255,0.04); line-height:1; pointer-events:none; user-select:none;">CSO</div>
                                <div style="position:relative; z-index:1;">
                                    <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:rgba(255,255,255,0.4); margin-bottom:1rem;">PROFILE / 001</div>
                                    <h3 style="font-family:var(--font-serif); font-size:var(--text-3xl); color:#fff; line-height:var(--leading-tight); margin-bottom:0.25rem;">Chief Science Officer</h3>
                                    <p style="font-size:var(--text-base); color:rgba(255,255,255,0.55); margin-bottom:2rem; line-height:1.6;">A pharmaceutical scientist who turned fermentation into food — with the precision of a lab and the soul of a craft.</p>

                                    <!-- 3 expertise pills -->
                                    <div style="display:flex; flex-wrap:wrap; gap:0.75rem; margin-bottom:2rem;">
                                        <span style="font-family:var(--font-mono); font-size:0.7rem; padding:0.4rem 0.9rem; border:1px solid rgba(255,255,255,0.25); color:rgba(255,255,255,0.8); letter-spacing:0.08em; text-transform:uppercase;">Pharmaceutical Bioprocessing</span>
                                        <span style="font-family:var(--font-mono); font-size:0.7rem; padding:0.4rem 0.9rem; border:1px solid rgba(255,255,255,0.25); color:rgba(255,255,255,0.8); letter-spacing:0.08em; text-transform:uppercase;">Nanoscience</span>
                                        <span style="font-family:var(--font-mono); font-size:0.7rem; padding:0.4rem 0.9rem; border:1px solid rgba(255,255,255,0.25); color:rgba(255,255,255,0.8); letter-spacing:0.08em; text-transform:uppercase;">Fermented Food Science</span>
                                    </div>

                                    <!-- Credentials row -->
                                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; padding-top:1.5rem; border-top:1px solid rgba(255,255,255,0.12);">
                                        <div>
                                            <div style="font-family:var(--font-mono); font-size:0.65rem; color:rgba(255,255,255,0.4); letter-spacing:0.1em; margin-bottom:0.3rem;">INCUBATOR</div>
                                            <div style="font-size:var(--text-sm); color:#fff; font-weight:500;">TBI-ACE, Hosur</div>
                                        </div>
                                        <div>
                                            <div style="font-family:var(--font-mono); font-size:0.65rem; color:rgba(255,255,255,0.4); letter-spacing:0.1em; margin-bottom:0.3rem;">RESEARCH</div>
                                            <div style="font-size:var(--text-sm); color:#fff; font-weight:500;">200+ Peer-reviewed studies</div>
                                        </div>
                                        <div>
                                            <div style="font-family:var(--font-mono); font-size:0.65rem; color:rgba(255,255,255,0.4); letter-spacing:0.1em; margin-bottom:0.3rem;">RESPONSIBLE FOR</div>
                                            <div style="font-size:var(--text-sm); color:#fff; font-weight:500; line-height:1.5;">Formulation · Sourcing · Clinical Protocol · Science Comm.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Full-width quote -->
                            <div style="border-left:3px solid var(--text-main); padding:2rem 2rem 2rem 2.5rem; background:var(--bg); margin-bottom:0;">
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); margin-bottom:1rem; text-transform:uppercase;">In their words</div>
                                <blockquote style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:1.6; color:var(--text-main); font-style:italic; margin:0;">
                                    &ldquo;I am building Oxygen because I am genuinely angry at what the market currently offers people who are trying to take their health seriously. I have seen the research. I know what good nutrition science looks like. And I know that the gap between what is possible and what is being sold is not technical &mdash; it is a choice. We are choosing differently.&rdquo;
                                </blockquote>
                            </div>
                        </div>

                        <!-- ═══ CHAPTER 02: OUR APPROACH ═══ -->
                        <div id="chapter-04" class="chapter-section" style="padding-top:var(--space-xl);">

                            <!-- Chapter label -->
                            <div style="display:flex; align-items:center; gap:1rem; margin-bottom:2rem;">
                                <div style="font-family:var(--font-mono); font-size:0.65rem; letter-spacing:0.15em; color:var(--text-muted); text-transform:uppercase;">Chapter 02</div>
                                <div style="height:1px; flex:1; background:var(--border);"></div>
                            </div>

                            <h3 class="headline" style="font-size:var(--text-3xl); line-height:var(--leading-tight); margin-bottom:0.75rem;">Our Approach</h3>
                            <p style="font-size:var(--text-base); color:var(--text-muted); margin-bottom:2.5rem; max-width:560px; line-height:1.7;">Six principles that separate evidence-based nutrition from everything else on the market.</p>

                            <!-- Premium numbered approach list -->
                            <div style="display:flex; flex-direction:column;">
                                <div style="display:grid; grid-template-columns:3rem 1fr; gap:1.5rem; padding:1.75rem 0; border-top:1px solid var(--border); align-items:start;">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-3xl); font-weight:700; color:var(--border); line-height:1; padding-top:0.1rem;">01</div>
                                    <div>
                                        <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.4rem;">Science Before Marketing</h4>
                                        <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.65;">We designed the formulation before we designed the brand. We chose ingredients before we chose colors. This is backwards from how most nutrition companies work. We think it is the only sensible order.</p>
                                    </div>
                                </div>
                                <div style="display:grid; grid-template-columns:3rem 1fr; gap:1.5rem; padding:1.75rem 0; border-top:1px solid var(--border); align-items:start;">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-3xl); font-weight:700; color:var(--border); line-height:1; padding-top:0.1rem;">02</div>
                                    <div>
                                        <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.4rem;">India Is Not a Market Segment</h4>
                                        <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.65;">We did not take a Western formula and add Ashwagandha to make it Indian. We started from India. From what Indian bodies are deficient in. From what Indian ingredients can provide.</p>
                                    </div>
                                </div>
                                <div style="display:grid; grid-template-columns:3rem 1fr; gap:1.5rem; padding:1.75rem 0; border-top:1px solid var(--border); align-items:start;">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-3xl); font-weight:700; color:var(--border); line-height:1; padding-top:0.1rem;">03</div>
                                    <div>
                                        <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.4rem;">Transparency Is Not Optional</h4>
                                        <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.65;">We publish our lab reports. We name our ingredient suppliers. We cite the studies behind our claims. We tell you when a study is preliminary and when it is robust.</p>
                                    </div>
                                </div>
                                <div style="display:grid; grid-template-columns:3rem 1fr; gap:1.5rem; padding:1.75rem 0; border-top:1px solid var(--border); align-items:start;">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-3xl); font-weight:700; color:var(--border); line-height:1; padding-top:0.1rem;">04</div>
                                    <div>
                                        <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.4rem;">Dose Matters</h4>
                                        <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.65;">Ashwagandha at 50mg is not the same as Ashwagandha at 300mg. We formulate at clinically relevant doses &mdash; not at doses that merely allow us to list the ingredient on the label.</p>
                                    </div>
                                </div>
                                <div style="display:grid; grid-template-columns:3rem 1fr; gap:1.5rem; padding:1.75rem 0; border-top:1px solid var(--border); align-items:start;">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-3xl); font-weight:700; color:var(--border); line-height:1; padding-top:0.1rem;">05</div>
                                    <div>
                                        <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.4rem;">Bioavailability First</h4>
                                        <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.65;">A 100mg dose with 5% absorption delivers 5mg to your body. A 50mg dose with 35% absorption delivers 17.5mg. The nutrient that reaches your bloodstream is the only one that matters.</p>
                                    </div>
                                </div>
                                <div style="display:grid; grid-template-columns:3rem 1fr; gap:1.5rem; padding:1.75rem 0; border-top:1px solid var(--border); border-bottom:1px solid var(--border); align-items:start;">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-3xl); font-weight:700; color:var(--border); line-height:1; padding-top:0.1rem;">06</div>
                                    <div>
                                        <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.4rem;">Clinical Evidence</h4>
                                        <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.65;">We designed our clinical study before we manufactured our first batch. Not because we are required to, but because no company should sell a health product without evidence that it works.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </section>'''

content = content[:section_start] + PREMIUM_WHO_SECTION + content[section_end:]

with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.write(content)

sys.stderr.write("Done - premium redesign complete\n")
