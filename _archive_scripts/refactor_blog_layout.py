import re

with open('e:\\OXYBIO\\blog.html', 'r', encoding='utf-8') as f:
    html = f.read()


# 1. ADD BENTO GRID STYLING to the Container Div
# Currently it's just a flex column. We will convert the first three posts into a CSS grid.
old_container = """<div style="max-width:800px; margin:0 auto; display:flex; flex-direction:column; gap:4rem;">"""
new_container = """<div style="max-width:1000px; margin:0 auto; display:flex; flex-direction:column; gap:4rem;">"""
html = html.replace(old_container, new_container)


# 2. Add structural CSS for the Bento Grid and the Dark Vault
script_to_inject = """

    <!-- Custom Premium Blog Layout CSS -->
    <style>
        /* Open Posts Master Grid */
        .bento-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-areas: 
                "featured featured"
                "secondary tertiary";
            gap: 2rem;
            margin-bottom: 2rem;
        }
        
        .bento-featured { grid-area: featured; }
        .bento-secondary { grid-area: secondary; }
        .bento-tertiary { grid-area: tertiary; }
        
        /* Mobile fallback for Bento Grid */
        @media (max-width: 768px) {
            .bento-grid {
                grid-template-columns: 1fr;
                grid-template-areas: 
                    "featured"
                    "secondary"
                    "tertiary";
                gap: 2rem;
            }
        }
        
        /* Premium Open Article Cards */
        .article-open {
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2.5rem;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        
        .article-open:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.04);
            border-color: #d1d5db; /* slightly darker border on hover */
        }
        
        /* The Locked Vault Area */
        .vault-container {
            position: relative;
            background: #0a0a0a; /* Deep dark vault */
            border-radius: 20px;
            padding: 4rem 3rem;
            margin-top: 4rem;
            border: 1px solid #222;
            overflow: hidden;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }
        
        /* Mobile fallback for Vault */
        @media (max-width: 768px) {
            .vault-container {
                grid-template-columns: 1fr;
                padding: 3rem 1.5rem;
            }
        }
        
        /* Vault Sub-grid cards */
        .article-locked {
            position: relative;
            background: rgba(25,25,25,0.4);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 2.5rem;
            overflow: hidden;
            height: 100%;
        }
        
        /* Glowing radar pulse for NDA badges */
        @keyframes pulse-ring {
            0% { transform: scale(0.8); opacity: 0.5; box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
            100% { transform: scale(0.8); opacity: 0.5; box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        }
        
        @keyframes pulse-ring-blue {
            0% { transform: scale(0.8); opacity: 0.5; box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(59, 130, 246, 0); }
            100% { transform: scale(0.8); opacity: 0.5; box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
        }
        
        .pulse-red { animation: pulse-ring 2s infinite cubic-bezier(0.2, 0, 0, 1); background: #ef4444; }
        .pulse-blue { animation: pulse-ring-blue 2.5s infinite cubic-bezier(0.2, 0, 0, 1) 0.5s; background: #3b82f6; }
    </style>
</body>"""

html = html.replace("</body>", script_to_inject)


# 3. REWRITE THE OPEN POSTS INTO THE BENTO GRID
old_posts = """            <!-- POST 1: Origin -->
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
            </article>"""

bento_posts = """
            <!-- ═ BENTO GRID: UNLOCKED POSTS ═ -->
            <div class="bento-grid">
                
                <!-- FEATURED POST (Spans full width) -->
                <article class="article-open bento-featured" style="border-top: 4px solid var(--text-main);">
                    <div style="font-family:var(--font-mono); font-size:var(--text-xs); color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1.25rem; text-transform:uppercase; letter-spacing:0.05em;">
                        <span style="color:var(--text-main); font-weight:700;">Feb 01, 2026</span>
                        <span>·</span>
                        <span style="display:flex; align-items:center; gap:0.4rem;">Author: Founder</span>
                        <span>·</span>
                        <span style="padding:0.2rem 0.6rem; background:var(--bg-alt); border-radius:4px; font-weight:600;">Origin Story</span>
                        <span>·</span>
                        <span>5 min read</span>
                    </div>
                    <div style="flex:1;">
                        <h3 style="font-family:var(--font-serif); font-size:clamp(2rem, 4vw, 3rem); line-height:1.15; margin-bottom:1.5rem; letter-spacing:-0.03em;">The 3 AM Realization: Why India's Health Drink Market is Fundamentally Broken</h3>
                        <p style="font-size:1.15rem; line-height:1.75; color:var(--text-muted); margin-bottom:3rem; max-width:85%;">The exact moment I realized that building a precision nutrition system wasn't just a business idea, but a moral imperative. Why existing health drinks fail, and what Oxygen will do differently.</p>
                    </div>
                    <div>
                        <a href="blog-origin.html" class="btn btn-outline" style="border-color:var(--text-main); color:var(--text-main); display:inline-flex; align-items:center; gap:0.5rem; padding:0.75rem 1.5rem;">
                            Read Article 
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                        </a>
                    </div>
                </article>

                <!-- SECONDARY POST (Half width) -->
                <article class="article-open bento-secondary">
                    <div style="font-family:var(--font-mono); font-size:10px; color:var(--text-muted); display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1.25rem; text-transform:uppercase; letter-spacing:0.05em;">
                        <span style="color:var(--text-main); font-weight:700;">Feb 10, 2026</span>
                        <span>·</span>
                        <span style="padding:0.15rem 0.5rem; background:var(--bg-alt); border-radius:4px; font-weight:600;">Startup Journey</span>
                    </div>
                    <div style="flex:1;">
                        <h3 style="font-family:var(--font-serif); font-size:1.6rem; line-height:1.2; margin-bottom:1rem; letter-spacing:-0.02em;">Bootstrapping Science: Building an Evidence-Based Startup in a World of Marketing Gimmicks</h3>
                        <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:2rem;">How we navigated the early days of formulating Oxygen, rejecting cheap ingredients from legacy contract manufacturers.</p>
                    </div>
                    <div>
                        <a href="blog-bootstrapping.html" class="btn btn-outline" style="width:100%; justify-content:center; display:flex; align-items:center; gap:0.5rem; padding:0.6rem 1rem;">
                            Read Article
                        </a>
                    </div>
                </article>

                <!-- TERTIARY POST (Half width) -->
                <article class="article-open bento-tertiary">
                    <div style="font-family:var(--font-mono); font-size:10px; color:var(--text-muted); display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1.25rem; text-transform:uppercase; letter-spacing:0.05em;">
                        <span style="color:var(--text-main); font-weight:700;">Feb 20, 2026</span>
                        <span>·</span>
                        <span style="padding:0.15rem 0.5rem; background:var(--bg-alt); border-radius:4px; font-weight:600;">Science Deep-Dive</span>
                    </div>
                    <div style="flex:1;">
                        <h3 style="font-family:var(--font-serif); font-size:1.6rem; line-height:1.2; margin-bottom:1rem; letter-spacing:-0.02em;">The Anatomy of Absorption: Why 90% of Supplements You Take Are Flushed Away</h3>
                        <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted); margin-bottom:2rem;">Chelation isn't a marketing buzzword. It's the chemistry process that determines whether your body absorbs 8% or 28% of minerals.</p>
                    </div>
                    <div>
                        <a href="blog-minerals.html" class="btn btn-outline" style="width:100%; justify-content:center; display:flex; align-items:center; gap:0.5rem; padding:0.6rem 1rem;">
                            Read Article
                        </a>
                    </div>
                </article>

            </div>"""

html = html.replace(old_posts, bento_posts)


# 4. REWRITE THE LOCKED POSTS INTO THE DARK VAULT
old_locked = """            <div style="display:flex; align-items:center; gap:1rem; margin:2rem 0;">
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
                    <a href="javascript:void(0)" class="btn btn-outline" style="pointer-events:none;">Read Article</a>
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
                    <a href="javascript:void(0)" class="btn btn-outline" style="pointer-events:none;">Read Article</a>
                </div>
            </article>"""

vault_locked = """
            <!-- ═ VAULT GRID: LOCKED/UPCOMING POSTS ═ -->
            <div class="vault-container">
                <!-- Glowing ambient background behind the vault -->
                <div style="position:absolute; top:50%; left:50%; width:600px; height:600px; background:radial-gradient(circle, rgba(59,130,246,0.08) 0%, rgba(0,0,0,0) 70%); transform:translate(-50%,-50%); pointer-events:none;"></div>
                
                <!-- Vault Header -->
                <div style="grid-column: 1 / -1; display:flex; align-items:center; justify-content:space-between; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom:1.5rem;">
                    <div style="display:flex; align-items:center; gap:0.75rem;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                        <h2 style="font-family:var(--font-mono); font-size:1.2rem; color:#fff; letter-spacing:0.2em; text-transform:uppercase; margin:0;">Encrypted Vault</h2>
                    </div>
                    <div style="font-family:var(--font-mono); font-size:0.7rem; color:rgba(255,255,255,0.4); text-transform:uppercase; letter-spacing:0.1em;">
                        2 Files Pending Access
                    </div>
                </div>

                <!-- POST 4: FUTURE LOCKED (Glassmorphism Dark Mode) -->
                <article class="article-locked">
                    <!-- Deep Frosted Glass Overlay -->
                    <div style="position:absolute; inset:0; backdrop-filter:blur(14px); -webkit-backdrop-filter:blur(14px); background:rgba(0,0,0,0.65); display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:2; text-align:center; padding:2rem;">
                        <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.5rem; background:rgba(20,20,20,0.8); padding:0.5rem 1rem; border-radius:50px; border:1px solid rgba(59,130,246,0.3);">
                            <div style="width:8px; height:8px; border-radius:50%;" class="pulse-blue"></div>
                            <span style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; text-transform:uppercase; color:#3b82f6; font-weight:700;">Data Compiling</span>
                        </div>
                        <p style="font-size:0.95rem; color:rgba(255,255,255,0.7); max-width:300px; margin-bottom:1.5rem;">This clinical design protocol is currently being finalized.</p>
                        <div style="font-family:var(--font-mono); color:#fff; font-size:0.75rem; letter-spacing:0.1em;">Unlocks <span style="font-weight:700; color:#3b82f6;">MAR 05, 2026</span></div>
                    </div>
                    
                    <div style="opacity:0.2; filter:blur(4px); pointer-events:none;">
                        <h3 style="font-family:var(--font-serif); font-size:1.6rem; line-height:1.2; margin-bottom:1rem; letter-spacing:-0.02em; color:#fff;">Formulation X: Why We Are Running a Clinical Trial Before Launch</h3>
                        <p style="font-size:0.95rem; line-height:1.6; color:#ccc; margin-bottom:2rem;">Most supplement brands never test their products on real human participants before launching. We are designing a 135-person double-blind study. Here is a look at the protocol.</p>
                    </div>
                </article>
                
                <!-- POST 5: FUTURE LOCKED (Glassmorphism Dark Mode) -->
                <article class="article-locked">
                    <!-- Deep Frosted Glass Overlay -->
                    <div style="position:absolute; inset:0; backdrop-filter:blur(14px); -webkit-backdrop-filter:blur(14px); background:rgba(0,0,0,0.65); display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:2; text-align:center; padding:2rem;">
                        <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.5rem; background:rgba(20,20,20,0.8); padding:0.5rem 1rem; border-radius:50px; border:1px solid rgba(239,68,68,0.3);">
                            <div style="width:8px; height:8px; border-radius:50%;" class="pulse-red"></div>
                            <span style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.1em; text-transform:uppercase; color:#ef4444; font-weight:700;">Under NDA</span>
                        </div>
                        <p style="font-size:0.95rem; color:rgba(255,255,255,0.7); max-width:300px; margin-bottom:1.5rem;">Lab analysis of competitor formulas is returning from the 3rd-party tester.</p>
                        <div style="font-family:var(--font-mono); color:#fff; font-size:0.75rem; letter-spacing:0.1em;">Unlocks <span style="font-weight:700; color:#ef4444;">MAR 20, 2026</span></div>
                    </div>
                    
                    <div style="opacity:0.2; filter:blur(4px); pointer-events:none;">
                        <h3 style="font-family:var(--font-serif); font-size:1.6rem; line-height:1.2; margin-bottom:1rem; letter-spacing:-0.02em; color:#fff;">Reverse-Engineering the Competition: What We Found in India's Top 5 Health Drinks</h3>
                        <p style="font-size:0.95rem; line-height:1.6; color:#ccc; margin-bottom:2rem;">We spent weeks analyzing the lab reports and nutrition panels of the market leaders. The results were worse than we thought. Prepare for a full teardown.</p>
                    </div>
                </article>

            </div>"""

html = html.replace(old_locked, vault_locked)

with open('e:\\OXYBIO\\blog.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied Bento Grid and Dark Vault glassmorphism to Blog page.")
