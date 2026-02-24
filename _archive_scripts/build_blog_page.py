import os
import re

# Read template structure from index.html
with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_match = re.search(r'(.*?<main>)', html, re.DOTALL)
footer_match = re.search(r'(</main>.*)', html, re.DOTALL)

if not header_match or not footer_match:
    print("Error extracting header/footer")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

blog_css = """
<style>
.blog-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s, box-shadow 0.3s;
}
.blog-card:hover:not(.locked) {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}
.blog-card.locked {
    opacity: 0.8;
}
.blog-card.locked::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(250, 249, 246, 0.4);
    backdrop-filter: blur(2px);
    z-index: 5;
}
.lock-overlay {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    background: var(--card-bg);
    padding: 1rem 1.5rem;
    border-radius: 8px;
    border: 1px solid var(--border);
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.blog-meta {
    display: flex;
    gap: 1rem;
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-bottom: 1rem;
    flex-wrap: wrap;
}
</style>
"""

# Insert CSS into header
header_html = header_html.replace('</head>', blog_css + '\n</head>')

blog_content = """
        <!-- Blog Hero Section -->
        <section class="hero" id="blog-hero" style="min-height: 50vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="hero-glow"></div>
            <div class="container hero-content" style="text-align: center;">
                <div class="badge reveal" style="transition-delay: 0ms; margin: 0 auto 1.5rem;">Development Journal & Research</div>
                <h1 class="reveal" style="transition-delay: 150ms;">
                    The Oxygen <span style="color: var(--accent);">Blog.</span>
                </h1>
                <p class="subtitle reveal" style="transition-delay: 300ms;" style="max-width: 650px; margin-left: auto; margin-right: auto;">
                    Science deep-dives, ingredient breakdowns, and honest updates from the lab. Building India's first precision nutrition system — in public.
                </p>
            </div>
        </section>

        <!-- Blog Grid -->
        <section id="blog-list" style="background: var(--bg); padding-top: 4rem; padding-bottom: 6rem;">
            <div class="container">
                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 2.5rem;">
                    
                    <!-- Post 1: Open -->
                    <article class="blog-card reveal" style="grid-column: 1 / -1; display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; padding: 4rem; border: 2px solid var(--accent); background: #fff;">
                        <div style="display: flex; flex-direction: column; justify-content: center;">
                            <div class="blog-meta">
                                <span class="badge" style="background: rgba(13,148,136,0.1); color: var(--accent); border:none;">Featured</span>
                                <span>Feb 20, 2026</span>
                                <span>&bull;</span>
                                <span>Founder</span>
                                <span>&bull;</span>
                                <span>Week 1</span>
                                <span>&bull;</span>
                                <span>6 min read</span>
                            </div>
                            <h2 style="font-size: 2.2rem; margin-bottom: 1.5rem; line-height: 1.3;">Why we built Oxygen: The Indian nutrition gap nobody is honestly addressing</h2>
                            <p style="color: var(--text-muted); font-size: 1.1rem; line-height: 1.6; margin-bottom: 2rem;">The observation that started it all. The data behind India's nutrition crisis. Why existing health drinks fail. And what Oxygen will do differently. This is the story of why we exist.</p>
                            <a href="#" class="btn btn-outline" style="align-self: flex-start;">Read Article</a>
                        </div>
                        <div style="background: var(--bg); border-radius: 8px; display: flex; align-items: center; justify-content: center; min-height: 300px; border: 1px solid var(--border);">
                            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="color: var(--text-muted);"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        </div>
                    </article>

                    <!-- Post 2: Open -->
                    <article class="blog-card reveal">
                        <div class="blog-meta">
                            <span style="color: var(--accent); font-weight: 600;">Nutrition Science</span>
                            <span>&bull;</span>
                            <span>Feb 20, 2026</span>
                        </div>
                        <h3 style="font-size: 1.4rem; margin-bottom: 1rem; line-height: 1.4; flex: 1;">What chelated minerals are — and why every major Indian health drink uses cheaper forms</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">Chelation isn't a marketing word. It's a chemistry process that determines whether your body absorbs 8% or 28% of the minerals you consume. The cost difference per serving? About ₹2.</p>
                        <div class="blog-meta" style="margin-bottom: 0;">
                            <span>Research Team</span><span>&bull;</span><span>Week 1</span><span>&bull;</span><span>8 min read</span>
                        </div>
                    </article>

                    <!-- Post 3: Locked -->
                    <article class="blog-card locked reveal">
                        <div class="lock-overlay">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); margin-bottom: 0.5rem;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            <span style="font-weight: 600; font-size: 0.9rem;">Unlocks Feb 27</span>
                        </div>
                        <div class="blog-meta">
                            <span style="color: var(--accent); font-weight: 600;">Nutrition Science</span>
                            <span>&bull;</span>
                            <span>Feb 27, 2026</span>
                        </div>
                        <h3 style="font-size: 1.4rem; margin-bottom: 1rem; line-height: 1.4; flex: 1;">Lion's Mane mushroom: What the research actually says (and what it doesn't)</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">Hericenones, erinacines, and nerve growth factor. The science is promising, but incomplete. Here's an honest look at what Lion's Mane can and cannot do — and why we still chose it.</p>
                        <div class="blog-meta" style="margin-bottom: 0;">
                            <span>Research Team</span><span>&bull;</span><span>Week 2</span><span>&bull;</span><span>10 min read</span>
                        </div>
                    </article>

                    <!-- Post 4: Locked -->
                    <article class="blog-card locked reveal">
                        <div class="lock-overlay">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); margin-bottom: 0.5rem;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            <span style="font-weight: 600; font-size: 0.9rem;">Unlocks Feb 27</span>
                        </div>
                        <div class="blog-meta">
                            <span style="color: var(--accent); font-weight: 600;">Nutrition Science</span>
                            <span>&bull;</span>
                            <span>Feb 27, 2026</span>
                        </div>
                        <h3 style="font-size: 1.4rem; margin-bottom: 1rem; line-height: 1.4; flex: 1;">We analyzed the ingredients in India's 10 most popular health drinks. Here is what we found.</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">Horlicks. Complan. Bournvita. Ensure. Protinex. Boost. We looked at their vitamin forms, actual doses, sugar content, and artificial ingredients. The results were... revealing.</p>
                        <div class="blog-meta" style="margin-bottom: 0;">
                            <span>Research Team</span><span>&bull;</span><span>Week 2</span><span>&bull;</span><span>12 min read</span>
                        </div>
                    </article>

                    <!-- Post 5: Locked -->
                    <article class="blog-card locked reveal">
                        <div class="lock-overlay">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); margin-bottom: 0.5rem;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            <span style="font-weight: 600; font-size: 0.9rem;">Unlocks Mar 6</span>
                        </div>
                        <div class="blog-meta">
                            <span style="color: var(--accent); font-weight: 600;">Building Oxygen</span>
                            <span>&bull;</span>
                            <span>Mar 6, 2026</span>
                        </div>
                        <h3 style="font-size: 1.4rem; margin-bottom: 1rem; line-height: 1.4; flex: 1;">Week 1 at TBI: What startup incubation actually looks like</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">No glamorous office. No Silicon Valley pitch deck. Just a lab bench, a formulation spreadsheet, and a lot of questions. Here's what the first week of building Oxygen actually involved.</p>
                        <div class="blog-meta" style="margin-bottom: 0;">
                            <span>Founder</span><span>&bull;</span><span>Week 3</span><span>&bull;</span><span>4 min read</span>
                        </div>
                    </article>

                    <!-- Post 6: Locked -->
                    <article class="blog-card locked reveal">
                        <div class="lock-overlay">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); margin-bottom: 0.5rem;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            <span style="font-weight: 600; font-size: 0.9rem;">Unlocks Mar 6</span>
                        </div>
                        <div class="blog-meta">
                            <span style="color: var(--accent); font-weight: 600;">Nutrition Science</span>
                            <span>&bull;</span>
                            <span>Mar 6, 2026</span>
                        </div>
                        <h3 style="font-size: 1.4rem; margin-bottom: 1rem; line-height: 1.4; flex: 1;">Ragi: Why India forgot about its most nutritious grain</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">Finger millet has more calcium than milk, more iron than spinach, and a glycemic index lower than rice. It fed generations of Indians. Then we abandoned it. The story of why — and the science of its revival.</p>
                        <div class="blog-meta" style="margin-bottom: 0;">
                            <span>Research Team</span><span>&bull;</span><span>Week 3</span><span>&bull;</span><span>9 min read</span>
                        </div>
                    </article>

                    <!-- Post 7: Locked -->
                    <article class="blog-card locked reveal">
                        <div class="lock-overlay">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); margin-bottom: 0.5rem;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            <span style="font-weight: 600; font-size: 0.9rem;">Unlocks Mar 13</span>
                        </div>
                        <div class="blog-meta">
                            <span style="color: var(--accent); font-weight: 600;">Nutrition Science</span>
                            <span>&bull;</span>
                            <span>Mar 13, 2026</span>
                        </div>
                        <h3 style="font-size: 1.4rem; margin-bottom: 1rem; line-height: 1.4; flex: 1;">The MTHFR gene: Why synthetic folic acid might not work for you</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">About 40% of Indians carry an MTHFR variant that impairs folic acid conversion. If you're one of them, your supplement might not be doing what you think. Here's what the science says.</p>
                        <div class="blog-meta" style="margin-bottom: 0;">
                            <span>Research Team</span><span>&bull;</span><span>Week 4</span><span>&bull;</span><span>8 min read</span>
                        </div>
                    </article>

                    <!-- Post 8: Locked -->
                    <article class="blog-card locked reveal">
                        <div class="lock-overlay">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent); margin-bottom: 0.5rem;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            <span style="font-weight: 600; font-size: 0.9rem;">Unlocks Mar 13</span>
                        </div>
                        <div class="blog-meta">
                            <span style="color: var(--accent); font-weight: 600;">Building Oxygen</span>
                            <span>&bull;</span>
                            <span>Mar 13, 2026</span>
                        </div>
                        <h3 style="font-size: 1.4rem; margin-bottom: 1rem; line-height: 1.4; flex: 1;">Our clinical study design: Why we're testing before launching</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">135 participants. 8 weeks. Three arms. Most supplement brands never test their products on humans. We designed a clinical study before our first commercial batch. Here's why and how.</p>
                        <div class="blog-meta" style="margin-bottom: 0;">
                            <span>Founder</span><span>&bull;</span><span>Week 4</span><span>&bull;</span><span>6 min read</span>
                        </div>
                    </article>

                </div>
            </div>
        </section>

        <!-- Bottom CTA -->
        <section id="blog-cta" style="padding: 6rem 0; border-top: 1px solid var(--border);">
            <div class="container text-center reveal">
                <div style="background: var(--card-bg); padding: 4rem 2rem; border-radius: 16px; border: 1px solid var(--accent); max-width: 800px; margin: 0 auto; box-shadow: 0 10px 40px rgba(13,148,136,0.1);">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="color: var(--accent); margin-bottom: 1.5rem;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">New article every week.</h2>
                    <p style="font-size: 1.15rem; color: var(--text-muted); margin-bottom: 2rem;">One science deep-dive. One building update. Join the waitlist and we'll send you the highlights.</p>
                    <form action="#" style="display: flex; gap: 1rem; max-width: 500px; margin: 0 auto;">
                        <input type="email" placeholder="Enter your email" required style="flex: 1; padding: 1rem 1.5rem; border-radius: 8px; border: 1px solid var(--border); font-size: 1rem; font-family: inherit;">
                        <button type="submit" class="btn btn-primary" style="padding: 1rem 2rem;">Subscribe</button>
                    </form>
                </div>
            </div>
        </section>
"""

with open(r'e:\OXYBIO\blog.html', 'w', encoding='utf-8') as f:
    f.write(header_html + '<main>\n' + blog_content + '\n    </main>\n' + footer_html)

print("Generated blog.html")
