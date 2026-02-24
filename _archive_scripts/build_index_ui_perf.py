import os, re

index_path = r'e:\OXYBIO\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

# REWRITE THE PROBLEM SECTION TO USE THE NEW DATA VIZ BARS AND TYPOGRAPHY SCALE
problem_section_pattern = re.compile(r'<!-- KEY STATISTICS -->.*?<!-- PROBLEM DETAILS -->', re.DOTALL)

new_problem_stats = """<!-- KEY STATISTICS -->
                <div class="bento-cell" style="grid-column: span 6;">
                    <div class="data-num" data-target="73" data-suffix="%" style="font-size:var(--text-6xl); line-height:var(--leading-none);">73%</div>
                    <div class="data-label" style="font-size:var(--text-base); font-weight:600; margin-top:0.5rem; line-height:var(--leading-snug);">Vitamin D Deficiency in Urban India</div>
                    <div class="stat-bar-container" style="display:block; margin: 1rem 0;">
                        <div class="stat-bar-fill" style="width: 73%;"></div>
                    </div>
                    <p class="text-meta">(Source: ICMR National Nutrition Survey, 2022)</p>
                </div>
                
                <div class="bento-cell" style="grid-column: span 6;">
                    <div class="data-num" data-target="50" data-suffix="%" style="font-size:var(--text-6xl); line-height:var(--leading-none);">50%</div>
                    <div class="data-label" style="font-size:var(--text-base); font-weight:600; margin-top:0.5rem; line-height:var(--leading-snug);">Skip at least one primary meal/day</div>
                    <div class="stat-bar-container" style="display:block; margin: 1rem 0;">
                        <div class="stat-bar-fill" style="width: 50%;"></div>
                    </div>
                    <p class="text-meta">(Source: ASSOCHAM Health Survey)</p>
                </div>

                <div class="bento-cell" style="grid-column: span 12;">
                    <div class="data-num" data-target="68" data-suffix="%" style="font-size:var(--text-6xl); line-height:var(--leading-none); color:#DC2626;">68%</div>
                    <div class="data-label" style="font-size:var(--text-lg); font-weight:600; margin-top:0.5rem; line-height:var(--leading-snug);">Indian health drinks fail label claims</div>
                    <div class="stat-bar-container" style="display:block; margin: 1rem 0;">
                        <div class="stat-bar-fill" style="width: 68%; background:#DC2626;"></div>
                    </div>
                    <p class="text-meta">(Source: Centre for Science and Environment Report)</p>
                </div>

                <!-- PROBLEM DETAILS -->"""

idx = problem_section_pattern.sub(new_problem_stats, idx)

# UPDATE PRODUCT CARDS WITH STRICT TYPOGRAPHY
idx = idx.replace('font-size:1.75rem;', 'font-size:var(--text-2xl); line-height:var(--leading-tight);')
idx = idx.replace('font-size:0.95rem; line-height:1.5;', 'font-size:var(--text-base); line-height:var(--leading-normal);')
idx = idx.replace('font-size:0.85rem; line-height:1.6;', 'font-size:var(--text-sm); line-height:var(--leading-relaxed);')

# FIX HERO SECTION SCALING
idx = idx.replace('font-size:clamp(3.5rem, 7vw, 6.5rem);', 'font-size:var(--text-6xl); line-height:var(--leading-none);')
idx = idx.replace('font-size:1.25rem;', 'font-size:var(--text-xl); line-height:var(--leading-relaxed);')

# FIX SCIENCE STATS
idx = idx.replace('font-size:1.5rem;', 'font-size:var(--text-xl); line-height:var(--leading-tight);')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("Updated index.html with rigorous typography and visual data bars.")

