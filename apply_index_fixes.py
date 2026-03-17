import os
import re

files = ['e:/OXYBIO/index.html', 'e:/OXYBIO/index-single.html']

problem_new = """            <section id="problem" class="problem-dark-panel">

                <!-- TOP ROW: Three simple text blocks -->
                <div class="container reveal">
                    <div class="problem-stats-row">
                        <div class="problem-stat-card">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">Unnave Marundhu</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">"Food is Medicine" — We have forgotten this ancient wisdom in the rush of modern life.</div>
                        </div>
                        <div class="problem-stat-card">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">The Modern Reality</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Processed, low-quality, and chemical-filled foods have replaced real, bioavailable nutrition.</div>
                        </div>
                        <div class="problem-stat-card problem-stat-danger">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">The Daily Deficit</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Skipped breakfasts and nutrient-poor convenience foods leave professionals and athletes depleted.</div>
                        </div>
                    </div>
                </div>

                <!-- CENTER: dramatic heading + subtext -->
                <div class="container reveal">
                    <div class="problem-headline-block">
                        <div class="problem-label-tag">The Problem</div>
                        <h2 class="problem-main-title">You are probably<br>running on empty.</h2>
                        <p class="problem-subtext">Not because you are careless. Because modern life makes proper nutrition almost impossible. The core problem revolves around the food we are eating.</p>
                        <a href="problem.html" class="problem-cta">Read the Science
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
                            <h4 class="problem-panel-title">No time for real nutrition</h4>
                            <p class="problem-panel-text">Working professionals work 8 to 10 hours a day and barely have time for lunch. Students skip meals before exams. Athletes eat whatever is convenient after training. The food system was not designed for how we actually live.</p>
                        </div>
                        <div class="problem-panel">
                            <div class="problem-panel-num">02</div>
                            <h4 class="problem-panel-title">Fake Promises &amp; Poor Quality</h4>
                            <p class="problem-panel-text">The market is saturated with highly processed foods, synthetic additives, and fake promises. Consumers are sold marketing rather than science, leaving them with memory lag, recovery problems, and chronic fatigue.</p>
                        </div>
                        <div class="problem-panel">
                            <div class="problem-panel-num">03</div>
                            <h4 class="problem-panel-title">The Scientific Approach</h4>
                            <p class="problem-panel-text">We are turning back to millets and medicinal mushrooms, but applying modern biotechnology—like probiotics, fermentation, and nano-encapsulation—to maximize their bioavailability and efficacy for the modern Indian body.</p>
                        </div>
                    </div>
                </div>

            </section>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace The Problem section
    # Find start and end of problem-dark-panel section
    pattern = re.compile(r'<section id="problem" class="problem-dark-panel">.*?</section>', re.DOTALL)
    content = pattern.sub(problem_new, content)

    # Solution intro tweaks
    content = content.replace('Three functional food formulas. Each scientifically designed for a specific need. All built on', 
                              'Three functional food formulation targets under research. Each designed for a specific need. All built on')
    content = content.replace('So we built one. Meet Oxygen.', 'So we are building one in the lab. Meet Oxygen.')
    
    # Scientifically proven tweaks
    content = content.replace('(scientifically proven)', '(targeting evidence-based ratios)')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed 2 files.")
