import re

with open('E:\\OXYBIO-WEBSITE\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire problem section
pattern = r'<section id="problem" class="problem-dark-panel">.*?</section>'
replacement = '''<section id="problem" class="problem-dark-panel">

                <!-- TOP ROW: Three simple text blocks -->
                <div class="container reveal">
                    <div class="problem-stats-row">
                        <div class="problem-stat-card">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">The Market Gap</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Consumers are overwhelmed by synthetic supplements that prioritize marketing over biological compatibility, leaving fundamental absorption problems unsolved.</div>
                        </div>
                        <div class="problem-stat-card">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">The Scientific Gap</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Standard extraction methods fail to isolate verifiable active compounds, relying instead on gross weight claims that cannot guarantee functional efficacy.</div>
                        </div>
                        <div class="problem-stat-card problem-stat-danger">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">The Price Gap</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Functional foods are priced as luxury imports, excluding the vast majority of the Indian demographic from science-backed nutritional protocols.</div>
                        </div>
                    </div>
                </div>

                <!-- CENTER: dramatic heading + subtext -->
                <div class="container reveal">
                    <div class="problem-headline-block" style="max-width:800px; margin:0 auto;">
                        <div class="problem-label-tag">The Functional Market Gap</div>
                        <h2 class="problem-main-title">Unvalidated synthetic formulations dominate.</h2>
                        <p class="problem-subtext" style="font-size: 1.15rem; color:var(--text-muted);">We evaluated the current functional food landscape against DPIIT Phase 0 thresholds and identified three critical failure points in the Indian market.</p>
                        <a href="problem.html" class="problem-cta">Explore the Data
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                                <polyline points="12 5 19 12 12 19"></polyline>
                            </svg>
                        </a>
                    </div>
                </div>

                <!-- BOTTOM: Three vertical problem panels -->
                <div class="container reveal">
                    <div class="problem-panels">
                        <div class="problem-panel">
                            <div class="problem-panel-num">01</div>
                            <h4 class="problem-panel-title">The Science Gap</h4>
                            <p class="problem-panel-text">Clinical trials consistently show that synthetic isolates suffer from poor cellular bioavailability. The industry ignores fermentation-driven metabolic pre-digestion.</p>
                        </div>
                        <div class="problem-panel">
                            <div class="problem-panel-num">02</div>
                            <h4 class="problem-panel-title">The Extraction Gap</h4>
                            <p class="problem-panel-text">Current medicinal compounds often contain up to 70% starch because manufacturers do not utilize species-specific fruiting-body liquid extraction.</p>
                        </div>
                        <div class="problem-panel">
                            <div class="problem-panel-num">03</div>
                            <h4 class="problem-panel-title">The Price Gap</h4>
                            <p class="problem-panel-text">Scientifically backed functional health currently requires importing products at a 600% markup. There is no &#8377;65 indigenous equivalent.</p>
                        </div>
                    </div>
                </div>

            </section>'''

html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('E:\\OXYBIO-WEBSITE\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html safely")
