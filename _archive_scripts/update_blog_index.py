import re

with open('e:\\OXYBIO\\blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the bento grid section with a premium chronological timeline list
old_grid_start = html.find('<!-- ═══════════════════════════════════════════════════════\n     BLOG GRID')
old_grid_end = html.find('<!-- ═══════════════════════════════════════════════════════\n     BOTTOM CTA')

NEW_BLOG_TIMELINE = '''<!-- ═══════════════════════════════════════════════════════
     BLOG TIMELINE (ENTREPRENEUR JOURNEY)
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border);">
    <div class="container reveal">
        
        <div style="max-width:800px; margin:0 auto; display:flex; flex-direction:column; gap:4rem;">

            <!-- POST 1: Origin -->
            <article style="background:var(--bg); padding:3rem; border:1px solid var(--border); border-left:4px solid var(--text-main); position:relative; overflow:hidden;">
                <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase; letter-spacing:0.05em;">
                    <span style="color:var(--text-main); font-weight:700;">Feb 01, 2026</span> ·
                    <span>Author: Founder</span> ·
                    <span>Origin Story</span> ·
                    <span>5 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:clamp(2rem, 4vw, 2.5rem); line-height:1.2; margin-bottom:1.5rem; letter-spacing:-0.02em;">The 3 AM Realization: Why India's Health Drink Market is Fundamentally Broken</h3>
                <p style="font-size:1.1rem; line-height:1.75; color:var(--text-muted); margin-bottom:2.5rem;">The exact moment I realized that building a precision nutrition system wasn't just a business idea, but a moral imperative. Why existing health drinks fail, and what Oxygen will do differently.</p>
                <a href="blog-origin.html" class="btn btn-outline" style="border-color:var(--text-main); color:var(--text-main); display:inline-flex; align-items:center; gap:0.5rem; padding:0.75rem 1.5rem;">
                    Read Article 
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="nav-arrow" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                </a>
            </article>

            <!-- POST 2: Bootstrapping -->
            <article style="background:var(--bg); padding:3rem; border:1px solid var(--border);">
                <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase; letter-spacing:0.05em;">
                    <span style="color:var(--text-main); font-weight:700;">Feb 10, 2026</span> ·
                    <span>Author: Founder</span> ·
                    <span>Startup Journey</span> ·
                    <span>6 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:clamp(1.75rem, 3.5vw, 2.25rem); line-height:1.2; margin-bottom:1.5rem; letter-spacing:-0.02em;">Bootstrapping Science: Building an Evidence-Based Startup in a World of Marketing Gimmicks</h3>
                <p style="font-size:1.1rem; line-height:1.75; color:var(--text-muted); margin-bottom:2.5rem;">How we navigated the early days of formulating Oxygen, rejecting cheap ingredients from legacy contract manufacturers, and why we chose to build our foundation at a biotech incubator.</p>
                <a href="blog-bootstrapping.html" class="btn btn-outline" style="display:inline-flex; align-items:center; gap:0.5rem; padding:0.75rem 1.5rem;">
                    Read Article 
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="nav-arrow" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                </a>
            </article>

            <!-- POST 3: Minerals -->
            <article style="background:var(--bg); padding:3rem; border:1px solid var(--border);">
                <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase; letter-spacing:0.05em;">
                    <span style="color:var(--text-main); font-weight:700;">Feb 20, 2026</span> ·
                    <span>Author: Chief Science Officer</span> ·
                    <span>Science Deep-Dive</span> ·
                    <span>7 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:clamp(1.75rem, 3.5vw, 2.25rem); line-height:1.2; margin-bottom:1.5rem; letter-spacing:-0.02em;">The Anatomy of Absorption: Why 90% of Supplements You Take Are Flushed Away</h3>
                <p style="font-size:1.1rem; line-height:1.75; color:var(--text-muted); margin-bottom:2.5rem;">Chelation isn't a marketing buzzword. It's the chemistry process that determines whether your body absorbs 8% or 28% of the minerals you consume. The cost difference per serving? About ₹2. Here is why we pay it.</p>
                <a href="blog-minerals.html" class="btn btn-outline" style="display:inline-flex; align-items:center; gap:0.5rem; padding:0.75rem 1.5rem;">
                    Read form 
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="nav-arrow" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                </a>
            </article>
            
            <div style="display:flex; align-items:center; gap:1rem; margin:2rem 0;">
                <div style="flex:1; height:1px; background:var(--border);"></div>
                <div style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--text-muted);">Upcoming Entries in the Journal</div>
                <div style="flex:1; height:1px; background:var(--border);"></div>
            </div>

            <!-- POST 4: FUTURE LOCKED -->
            <article style="background:rgba(250,250,250,0.4); padding:3rem; border:1px dashed var(--border); position:relative; overflow:hidden;">
                <!-- Blur overlay -->
                <div style="position:absolute; inset:0; backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px); background:rgba(255,255,255,0.7); display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:2; text-align:center; padding:2rem;">
                    <div style="width:48px; height:48px; border-radius:50%; background:var(--bg-alt); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--text-muted)" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                    </div>
                    <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--text-main); margin-bottom:0.5rem; font-weight:700;">Data Compiling...</h4>
                    <p style="font-size:0.95rem; color:var(--text-muted); max-width:300px;">This clinical design protocol is currently being finalized. Unlocks <strong>March 05, 2026</strong>.</p>
                </div>
                
                <div style="opacity:0.3; filter:blur(2px);">
                    <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase; letter-spacing:0.05em;">
                        <span>Mar 05, 2026</span> ·
                        <span>Author: Founder</span> ·
                        <span>Clinical Trials</span>
                    </div>
                    <h3 style="font-family:var(--font-serif); font-size:clamp(1.75rem, 3.5vw, 2.25rem); line-height:1.2; margin-bottom:1.5rem; letter-spacing:-0.02em;">Formulation X: Why We Are Running a Clinical Trial Before Launch</h3>
                    <p style="font-size:1.1rem; line-height:1.75; color:var(--text-muted); margin-bottom:2.5rem;">Most supplement brands never test their products on real human participants before launching. We are designing a 135-person double-blind study. Here is a look at the protocol.</p>
                    <a href="#" class="btn btn-outline" style="pointer-events:none;">Read Article</a>
                </div>
            </article>
            
            <!-- POST 5: FUTURE LOCKED -->
            <article style="background:rgba(250,250,250,0.4); padding:3rem; border:1px dashed var(--border); position:relative; overflow:hidden;">
                <!-- Blur overlay -->
                <div style="position:absolute; inset:0; backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px); background:rgba(255,255,255,0.7); display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:2; text-align:center; padding:2rem;">
                    <div style="width:48px; height:48px; border-radius:50%; background:var(--bg-alt); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--text-muted)" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                    </div>
                    <h4 style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--text-main); margin-bottom:0.5rem; font-weight:700;">Under NDA</h4>
                    <p style="font-size:0.95rem; color:var(--text-muted); max-width:300px;">Lab analysis of the competitor formulas is returning from the third-party tester. Unlocks <strong>March 20, 2026</strong>.</p>
                </div>
                
                <div style="opacity:0.3; filter:blur(2px);">
                    <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase; letter-spacing:0.05em;">
                        <span>Mar 20, 2026</span> ·
                        <span>Author: Research Team</span> ·
                        <span>Industry Teardown</span>
                    </div>
                    <h3 style="font-family:var(--font-serif); font-size:clamp(1.75rem, 3.5vw, 2.25rem); line-height:1.2; margin-bottom:1.5rem; letter-spacing:-0.02em;">Reverse-Engineering the Competition: What We Found in India's Top 5 Health Drinks</h3>
                    <p style="font-size:1.1rem; line-height:1.75; color:var(--text-muted); margin-bottom:2.5rem;">We spent weeks analyzing the lab reports and nutrition panels of the market leaders. The results were worse than we thought. Prepare for a full teardown.</p>
                    <a href="#" class="btn btn-outline" style="pointer-events:none;">Read Article</a>
                </div>
            </article>

        </div>
    </div>
</section>
'''

if old_grid_start != -1 and old_grid_end != -1:
    html = html[:old_grid_start] + NEW_BLOG_TIMELINE + html[old_grid_end:]
    
    with open('e:\\OXYBIO\\blog.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("blog.html updated with chronological feed and locked future posts.")
else:
    print("Error: Could not find old grid section in blog.html")
