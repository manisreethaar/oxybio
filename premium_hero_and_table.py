import re

html_file = 'e:\\OXYBIO\\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Hero Badge with Premium Tags
old_badge_regex = r'<div class="badge" style="margin-bottom:var\(--space-md\);">\s*🌱\s*Currently in Development\s*•\s*TBI\s*Incubated\s*•\s*Clinical Study Designed\s*</div>'

new_tags = """<div class="hero-tags-wrapper">
                        <div class="premium-tag tag-pulse">
                            <span class="pulse-dot"></span>
                            Currently in Development
                        </div>
                        <div class="premium-tag">
                            <span class="tag-icon">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><path d="M9 22v-4h6v4"></path><path d="M8 6h.01"></path><path d="M16 6h.01"></path><path d="M12 6h.01"></path><path d="M12 10h.01"></path><path d="M12 14h.01"></path><path d="M16 10h.01"></path><path d="M16 14h.01"></path><path d="M8 10h.01"></path><path d="M8 14h.01"></path></svg>
                            </span>
                            TBI Incubated
                        </div>
                        <div class="premium-tag">
                            <span class="tag-icon">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                            </span>
                            Clinical Study Designed
                        </div>
                    </div>"""

html = re.sub(old_badge_regex, new_tags, html, count=1)


# 2. Replace the Comparison Table
table_start_marker = '<!-- Column labels and Table Wrapper -->'
table_end_marker = '<!-- End container wrapper -->'
if table_start_marker in html and table_end_marker in html:
    start_idx = html.find(table_start_marker)
    end_idx = html.find(table_end_marker) + len(table_end_marker)

    new_table = """<!-- New Premium Responsive Comparison Table -->
                <div class="container pb-xl">
                    <div class="duel-table-wrapper">
                        <!-- Desktop Header (Hidden on Mobile) -->
                        <div class="duel-table-header">
                            <div class="duel-category-header">Category</div>
                            <div class="duel-us-header">✦ Oxygen Bioinnovations</div>
                            <div class="duel-them-header">Industry Standard</div>
                        </div>

                        <!-- Row 1 -->
                        <div class="duel-row">
                            <div class="duel-category">Vitamin Forms</div>
                            <div class="duel-vs-grid">
                                <div class="duel-us">
                                    <span class="duel-icon good">✓</span>
                                    <span class="duel-text">Active (bioavailable) Forms</span>
                                </div>
                                <div class="duel-them">
                                    <span class="duel-icon bad">✖</span>
                                    <span class="duel-text">Cheapest Synthetic Forms</span>
                                </div>
                            </div>
                        </div>

                        <!-- Row 2 -->
                        <div class="duel-row bg-alt">
                            <div class="duel-category">Vitamin B12</div>
                            <div class="duel-vs-grid">
                                <div class="duel-us">
                                    <span class="duel-icon good">✓</span>
                                    <span class="duel-text">Methylcobalamin</span>
                                </div>
                                <div class="duel-them">
                                    <span class="duel-icon bad">✖</span>
                                    <span class="duel-text">Cyanocobalamin</span>
                                </div>
                            </div>
                        </div>

                        <!-- Row 3 -->
                        <div class="duel-row">
                            <div class="duel-category">Minerals</div>
                            <div class="duel-vs-grid">
                                <div class="duel-us">
                                    <span class="duel-icon good">✓</span>
                                    <span class="duel-text">Chelated TRAACS® Amino Acid</span>
                                </div>
                                <div class="duel-them">
                                    <span class="duel-icon bad">✖</span>
                                    <span class="duel-text">Oxide / Sulfate Forms</span>
                                </div>
                            </div>
                        </div>

                        <!-- Row 4 -->
                        <div class="duel-row bg-alt">
                            <div class="duel-category">Mineral Absorption</div>
                            <div class="duel-vs-grid">
                                <div class="duel-us">
                                    <span class="duel-icon good">✓</span>
                                    <span class="duel-text">~28% Absorbed</span>
                                </div>
                                <div class="duel-them">
                                    <span class="duel-icon bad">✖</span>
                                    <span class="duel-text">~8% Absorbed (Standard)</span>
                                </div>
                            </div>
                        </div>

                        <!-- Row 5 -->
                        <div class="duel-row">
                            <div class="duel-category">Mushroom Extracts</div>
                            <div class="duel-vs-grid">
                                <div class="duel-us">
                                    <span class="duel-icon good">✓</span>
                                    <span class="duel-text">Verified β-glucan %</span>
                                </div>
                                <div class="duel-them">
                                    <span class="duel-icon bad">✖</span>
                                    <span class="duel-text">Unverified weight labels</span>
                                </div>
                            </div>
                        </div>

                        <!-- Row 6 -->
                        <div class="duel-row bg-alt">
                            <div class="duel-category">Efficacy Data</div>
                            <div class="duel-vs-grid">
                                <div class="duel-us">
                                    <span class="duel-icon good">✓</span>
                                    <span class="duel-text">Pre-Launch Clinical Study</span>
                                </div>
                                <div class="duel-them">
                                    <span class="duel-icon bad">✖</span>
                                    <span class="duel-text">Zero Clinical Efficacy Data</span>
                                </div>
                            </div>
                        </div>

                        <!-- Row 7 -->
                        <div class="duel-row">
                            <div class="duel-category">Lab Reports</div>
                            <div class="duel-vs-grid">
                                <div class="duel-us">
                                    <span class="duel-icon good">✓</span>
                                    <span class="duel-text">Public CoA every batch</span>
                                </div>
                                <div class="duel-them">
                                    <span class="duel-icon bad">✖</span>
                                    <span class="duel-text">No Transparency</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>"""

    html = html[:start_idx] + new_table + html[end_idx:]
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("DOM updates for tags and tables applied successfully to index.html.")
else:
    print("Error: Could not find table boundaries in index.html")
    print(f"Table start found: {table_start_marker in html}")
    print(f"Table end found: {table_end_marker in html}")
