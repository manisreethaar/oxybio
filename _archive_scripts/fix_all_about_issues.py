import sys

with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ===================================================================
# FIX 1: Restore data-target on sidebar li items (JS uses data-target)
# ===================================================================
content = content.replace('data-section="chapter-01"', 'data-target="chapter-01"')
content = content.replace('data-section="chapter-02"', 'data-target="chapter-02"')
content = content.replace('data-section="chapter-03"', 'data-target="chapter-03"')
content = content.replace('data-section="chapter-04"', 'data-target="chapter-04"')

# ===================================================================
# FIX 2 + 3 + 4 + 5: Replace the entire Who We Are chapter content
# Find the "Main Content Chapters" div in about-who section and
# replace it with correct chapters: Founder (ch-03) + Our Approach (ch-04)
# REMOVE the duplicate Journey timeline (old ch-04)
# ===================================================================

old_who_chapters = '''                    <!-- Main Content Chapters -->
                    <div>
                        <!-- The Founder -->
                        <id="chapter-03" class="chapter-section"
                            style="margin-bottom:var(--space-xl); padding-top:var(--space-xl); border-top:1px dashed var(--border);">
                            <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">
                                CHAPTER 03</div>
                            <h3 class="headline"
                                style="font-size:var(--text-3xl); line-height:var(--leading-tight); margin-bottom:1.5rem;">
                                Our Approach</h3>'''

# We can't do exact match on that due to line endings, so find a unique marker
# and replace from that point to the closing </section> of about-who

# Find the about-who "Main Content Chapters" marker
marker = '<!-- Main Content Chapters -->'
who_start = content.find('id="about-who"')
who_content_after = content.find(marker, who_start)

if who_content_after == -1:
    sys.stderr.write("ERROR: Could not find Main Content Chapters in about-who\n")
    sys.exit(1)

# Find the wrapper <div> that contains the chapters (right after the comment)
div_open_pos = content.find('<div>', who_content_after)

# Find the closing </section> of about-who section
# It should be the next </section> after our content area ends
outer_div_close = content.find('</div>\n            </div>\n        </section>', who_content_after)
if outer_div_close == -1:
    # Try alternative
    outer_div_close = content.find('\n            </div>\n        </section>\n\n\n    </main>', who_content_after)
    
section_end = content.find('</section>', who_content_after)
# Find the end of about-who section (two consecutive </section> or just the next one)
# The about-who section has structure: section > container > grid > div(chapters)
# So ending is: </div></div></div></section>
# Let's find from the end of the bento grid closing

# Better approach: find the last chapter div end and then the section close
ch04_close = content.rfind('</div>', 0, who_content_after + 10000)  # rough search

# Actually simplest: replace from marker onwards up to the section end
# Find the exact section end of about-who
# The section starts at about-who, ends at the next </section>
section_close_tag = '</section>'
section_start_pos = content.find('id="about-who"')
who_section_end = content.find(section_close_tag, section_start_pos)

sys.stderr.write(f"about-who section: {section_start_pos} to {who_section_end}\n")
sys.stderr.write(f"marker at: {who_content_after}\n")
sys.stderr.write(f"div_open at: {div_open_pos}\n")

# Replace the content between the opening <div> tag and the section end
new_chapters = '''<div>
                        <!-- CHAPTER 01: The Founder -->
                        <div id="chapter-03" class="chapter-section" style="margin-bottom:var(--space-xl);">
                            <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">CHAPTER 01</div>
                            <h3 class="headline" style="font-size:var(--text-3xl); line-height:var(--leading-tight); margin-bottom:1.5rem;">The Founder</h3>
                            <div class="editorial-col" style="font-size:var(--text-lg); line-height:1.7; color:var(--text-muted);">
                                <p style="color:var(--text-main); font-weight:600; font-family:var(--font-serif); font-size:var(--text-2xl); line-height:var(--leading-tight); margin-bottom:0.5rem;">Chief Science Officer</p>
                                <p style="margin-bottom:1.5rem;">A pharmaceutical scientist who turned fermentation into food — with the precision of a lab and the soul of a craft.</p>
                                <div style="font-family:var(--font-mono); font-size:var(--text-sm); color:var(--text-main); padding:1rem; border:1px solid var(--border); margin-bottom:2rem; background:var(--bg);">
                                    Operating at the intersection of:<br>
                                    Pharmaceutical Bioprocessing &times; Nanoscience &times; Fermented Food Science
                                </div>
                                <ul style="padding-left:1.5rem; margin-bottom:2rem;">
                                    <li style="margin-bottom:0.5rem;">Incubated at TBI — Technology Business Incubator, ACE Hosur</li>
                                    <li>Personally analyzed 200+ peer-reviewed studies for this project</li>
                                </ul>
                                <blockquote style="font-family:var(--font-serif); font-size:var(--text-2xl); line-height:1.4; color:var(--bg); background:var(--text-main); padding:2rem; margin:2rem 0; font-style:italic;">
                                    &ldquo;I am building Oxygen because I am genuinely angry at what the market currently offers people who are trying to take their health seriously. I have seen the research. I know what good nutrition science looks like. And I know that the gap between what is possible and what is being sold is not technical &mdash; it is a choice. We are choosing differently.&rdquo;
                                </blockquote>
                                <p style="font-size:var(--text-base); line-height:var(--leading-relaxed);">
                                    <strong>Responsible for:</strong> Formulation Design, Ingredient Sourcing, Clinical Study Protocol, Science Communication
                                </p>
                            </div>
                        </div>

                        <!-- CHAPTER 02: Our Approach -->
                        <div id="chapter-04" class="chapter-section" style="padding-top:var(--space-xl); border-top:1px dashed var(--border);">
                            <div style="font-family:var(--font-mono); color:var(--text-muted); margin-bottom:0.5rem;">CHAPTER 02</div>
                            <h3 class="headline" style="font-size:var(--text-3xl); line-height:var(--leading-tight); margin-bottom:1.5rem;">Our Approach</h3>
                            <div class="bento-grid" style="grid-template-columns:1fr 1fr;">
                                <div class="bento-cell" style="background:var(--bg);">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-2xl); color:var(--text-muted); margin-bottom:0.5rem;">01</div>
                                    <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.5rem;">Science Before Marketing</h4>
                                    <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.5;">We designed the formulation before we designed the brand. We chose ingredients before we chose colors. We cited our evidence before we wrote our copy. This is backwards from how most nutrition companies work. We think it is the only sensible order.</p>
                                </div>
                                <div class="bento-cell" style="background:var(--bg);">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-2xl); color:var(--text-muted); margin-bottom:0.5rem;">02</div>
                                    <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.5rem;">India Is Not a Market Segment</h4>
                                    <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.5;">We did not take a Western formula and add Ashwagandha to make it Indian. We started from India. From what Indian bodies are deficient in. From what Indian ingredients can provide. From what Indian lifestyles demand.</p>
                                </div>
                                <div class="bento-cell" style="background:var(--bg);">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-2xl); color:var(--text-muted); margin-bottom:0.5rem;">03</div>
                                    <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.5rem;">Transparency Is Not Optional</h4>
                                    <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.5;">We will publish our lab reports. We will name our ingredient suppliers. We will cite the studies behind our claims. We will tell you when a study is preliminary and when it is robust.</p>
                                </div>
                                <div class="bento-cell" style="background:var(--bg);">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-2xl); color:var(--text-muted); margin-bottom:0.5rem;">04</div>
                                    <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.5rem;">Dose Matters</h4>
                                    <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.5;">Ashwagandha at 50mg is not the same as Ashwagandha at 300mg. Lion&rsquo;s Mane at 100mg is not what the research studied. We formulate at clinically relevant doses &mdash; not at doses that allow us to put the ingredient on the label.</p>
                                </div>
                                <div class="bento-cell" style="background:var(--bg);">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-2xl); color:var(--text-muted); margin-bottom:0.5rem;">05</div>
                                    <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.5rem;">Bioavailability First</h4>
                                    <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.5;">A 100mg dose with 5% absorption delivers 5mg to your body. A 50mg dose with 35% absorption delivers 17.5mg. The nutrient that reaches your bloodstream is the only nutrient that matters.</p>
                                </div>
                                <div class="bento-cell" style="background:var(--bg);">
                                    <div style="font-family:var(--font-mono); font-size:var(--text-2xl); color:var(--text-muted); margin-bottom:0.5rem;">06</div>
                                    <h4 style="font-family:var(--font-serif); font-size:var(--text-xl); margin-bottom:0.5rem;">Clinical Evidence</h4>
                                    <p style="font-size:var(--text-base); color:var(--text-muted); line-height:1.5;">We designed our clinical study before we manufactured our first batch. Not because we are required to, but because we believe no company should sell a health product without evidence that it works.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>'''

# Replace from the opening <div> tag of "Main Content Chapters" to the section end
content = content[:div_open_pos] + new_chapters + content[who_section_end + len('</section>'):]

with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.write(content)

sys.stderr.write("Done - all 5 issues fixed\n")
