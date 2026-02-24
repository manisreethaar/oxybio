import os, re

blog_path = r'e:\OXYBIO\blog.html'
with open(blog_path, 'r', encoding='utf-8') as f:
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
<section class="structure-section" style="padding-top:140px; border-bottom:none;">
    <div class="container">
        <div class="flow-left reveal" style="max-width:900px;">
            <div class="badge" style="margin-bottom:var(--space-md);">Development Journal & Research</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 7vw, 6.5rem);">The Oxygen<br><em>Blog.</em></h1>
            <p class="subtext editorial-col" style="margin-top:var(--space-md); font-size:1.25rem;">
                Science deep-dives, ingredient breakdowns, and honest updates from the lab. Building India's first precision nutrition system — in public.
            </p>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     BLOG GRID
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--bg-alt); border-top:1px solid var(--border);">
    <div class="container reveal">
        <div class="bento-grid">
            
            <!-- Post 1 (Featured) -->
            <div class="bento-cell" style="grid-column: span 12; background:var(--bg); border-left:4px solid var(--text-main);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Feb 20, 2026</span> ·
                    <span>Author: Founder</span> ·
                    <span>Building Oxygen</span> ·
                    <span style="color:var(--text-main);">Week 1</span> ·
                    <span>6 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:2rem; margin-bottom:1rem; line-height:1.2;">Why we built Oxygen: The Indian nutrition gap nobody is honestly addressing</h3>
                <p style="font-size:1.05rem; line-height:1.6; color:var(--text-muted); margin-bottom:1.5rem; max-width:800px;">The observation that started it all. The data behind India's nutrition crisis. Why existing health drinks fail. And what Oxygen will do differently. This is the story of why we exist.</p>
                <a href="#" class="btn btn-outline" style="border-color:var(--border);">Read Article</a>
            </div>

            <!-- Posts 2 & 3 -->
            <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Feb 20, 2026</span> ·
                    <span>Research Team</span> ·
                    <span>8 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1rem; line-height:1.3;">What chelated minerals are — and why every major Indian health drink uses cheaper forms</h3>
                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted);">Chelation isn't a marketing word. It's a chemistry process that determines whether your body absorbs 8% or 28% of the minerals you consume. The cost difference per serving? About ₹2.</p>
            </div>
            
            <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Feb 27, 2026</span> ·
                    <span>Research Team</span> ·
                    <span>10 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1rem; line-height:1.3;">Lion's Mane mushroom: What the research actually says (and what it doesn't)</h3>
                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted);">Hericenones, erinacines, and nerve growth factor. The science is promising, but incomplete. Here's an honest look at what Lion's Mane can and cannot do — and why we still chose it.</p>
            </div>

            <!-- Posts 4 & 5 -->
            <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Feb 27, 2026</span> ·
                    <span>Research Team</span> ·
                    <span>12 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1rem; line-height:1.3;">We analyzed the ingredients in India's 10 most popular health drinks. Here is what we found.</h3>
                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted);">Horlicks. Complan. Bournvita. Ensure. Protinex. Boost. We looked at their vitamin forms, actual doses, sugar content, and artificial ingredients. The results were... revealing.</p>
            </div>
            
            <div class="bento-cell" style="grid-column: span 6; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Mar 6, 2026</span> ·
                    <span>Founder</span> ·
                    <span>4 min read</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:1.5rem; margin-bottom:1rem; line-height:1.3;">Week 1 at TBI: What startup incubation actually looks like</h3>
                <p style="font-size:0.95rem; line-height:1.6; color:var(--text-muted);">No glamorous office. No Silicon Valley pitch deck. Just a lab bench, a formulation spreadsheet, and a lot of questions. Here's what the first week of building Oxygen actually involved.</p>
            </div>

            <!-- Posts 6, 7 & 8 -->
            <div class="bento-cell" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Mar 6, 2026</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.75rem; line-height:1.3;">Ragi: Why India forgot about its most nutritious grain</h3>
                <p style="font-size:0.9rem; line-height:1.5; color:var(--text-muted);">Finger millet has more calcium than milk, more iron than spinach, and a glycemic index lower than rice. It fed generations of Indians. Then we abandoned it. The story of why — and the science of its revival.</p>
            </div>
            
            <div class="bento-cell" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Mar 13, 2026</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.75rem; line-height:1.3;">The MTHFR gene: Why synthetic folic acid might not work for you</h3>
                <p style="font-size:0.9rem; line-height:1.5; color:var(--text-muted);">About 40% of Indians carry an MTHFR variant that impairs folic acid conversion. If you're one of them, your supplement might not be doing what you think. Here's what the science says.</p>
            </div>
            
            <div class="bento-cell" style="grid-column: span 4; background:var(--bg);">
                <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; text-transform:uppercase;">
                    <span>Mar 13, 2026</span>
                </div>
                <h3 style="font-family:var(--font-serif); font-size:1.25rem; margin-bottom:0.75rem; line-height:1.3;">Our clinical study design: Why we're testing before launching</h3>
                <p style="font-size:0.9rem; line-height:1.5; color:var(--text-muted);">135 participants. 8 weeks. Three arms. Most supplement brands never test their products on humans. We designed a clinical study before our first commercial batch. Here's why and how.</p>
            </div>

        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════════
     BOTTOM CTA
════════════════════════════════════════════════════════ -->
<section class="structure-section" style="background:var(--text-main); color:var(--bg); border:none;">
    <div class="container" style="text-align:center; padding:var(--space-md) 0;">
        <h4 style="font-family:var(--font-mono); font-size:0.85rem; color:#A3A3A3; margin-bottom:1rem; letter-spacing:0.1em;">JOIN THE DISCUSSION</h4>
        <h2 style="font-family:var(--font-serif); font-size:2.5rem; margin-bottom:1rem; color:#fff;">New article every week.</h2>
        <p style="font-size:1.125rem; line-height:1.6; color:#ccc; max-width:600px; margin:0 auto; margin-bottom:2rem;">
            One science deep-dive. One building update. Join the waitlist and we'll send you the highlights.
        </p>
        <form style="display:flex; justify-content:center; gap:1rem; max-width:500px; margin:0 auto;" class="mobile-stack" onsubmit="event.preventDefault(); alert('Subscribed to the journal.');">
            <input type="email" placeholder="Enter your email address" required style="flex:1; padding:1rem; border:1px solid #333; background:transparent; color:#fff; font-family:var(--font-sans); font-size:1rem; border-radius:4px; outline:none;">
            <button type="submit" class="btn" style="background:var(--bg); color:var(--text-main); padding:1rem 2rem;">Subscribe</button>
        </form>
    </div>
</section>

</main>
"""

with open(blog_path, 'w', encoding='utf-8') as f:
    f.write(HEADER + MAIN_CONTENT + FOOTER)

print("Updated blog.html with editorial post grids.")
