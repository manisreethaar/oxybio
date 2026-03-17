import sys

file_path = "e:/OXYBIO/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Edit 1
old_1 = """                        <div class="problem-stat-card">
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
                        </div>"""

new_1 = """                        <div class="problem-stat-card">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">Endogenous Decline</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Indian baseline physiological targets reflect widespread micronutrient and metabolic deterioration.</div>
                        </div>
                        <div class="problem-stat-card">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">The Isolation Error</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Synthetic singular isolates consistently fail to achieve hypothesized serum concentrations.</div>
                        </div>
                        <div class="problem-stat-card problem-stat-danger">
                            <div class="problem-stat-label" style="font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">Mitochondrial Deficit</div>
                            <div class="problem-stat-source" style="font-size: 1rem; color: var(--text-muted); line-height: 1.6;">Accelerated cellular fatigue observed across high-output cognitive and physical protocols.</div>
                        </div>"""

# Edit 2
old_2 = """                    <div class="problem-headline-block">
                        <div class="problem-label-tag">The Problem</div>
                        <h2 class="problem-main-title">You are probably<br>running on empty.</h2>
                        <p class="problem-subtext">Not because you are careless. Because modern life makes proper nutrition almost impossible. The core problem revolves around the food we are eating.</p>
                        <a href="problem.html" class="problem-cta">Read the Science
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                                <polyline points="12 5 19 12 12 19"></polyline>
                            </svg>
                        </a>
                    </div>"""

new_2 = """                    <div class="problem-headline-block">
                        <div class="problem-label-tag">The Baseline Pathologies</div>
                        <h2 class="problem-main-title">Identifying the<br>Biological Deficits.</h2>
                        <p class="problem-subtext">Our lab does not formulate for demographic segments. We engineer solutions exclusively targeted at clinically established absorption and systemic deficits.</p>
                        <a href="problem.html" class="problem-cta">Read the Clinical Targets
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                                <polyline points="12 5 19 12 12 19"></polyline>
                            </svg>
                        </a>
                    </div>"""

# Edit 3
old_3 = """                        <div class="problem-panel">
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
                        </div>"""

new_3 = """                        <div class="problem-panel">
                            <div class="problem-panel-num">01</div>
                            <h4 class="problem-panel-title">Pathology of Depletion</h4>
                            <p class="problem-panel-text">Evaluating physiological endpoints affected by modern metabolic disruptions, prioritizing cognitive endurance and muscular kinematic recovery over generalized wellness paradigms.</p>
                        </div>
                        <div class="problem-panel">
                            <div class="problem-panel-num">02</div>
                            <h4 class="problem-panel-title">The Absorption Dilemma</h4>
                            <p class="problem-panel-text">Documenting the systemic failure of generic exogenous isolates (e.g., standard ferrous sulfate) due to heavy gastrointestinal disruption and poor intracellular transport mechanics.</p>
                        </div>
                        <div class="problem-panel">
                            <div class="problem-panel-num">03</div>
                            <h4 class="problem-panel-title">Engineering Hybrids</h4>
                            <p class="problem-panel-text">Testing novel methodologies—specifically the integration of medicinal fungi with sprouted/fermented ancient millet structures—to bypass standard absorption bottlenecks.</p>
                        </div>"""

content = content.replace(old_1, new_1)
content = content.replace(old_2, new_2)
content = content.replace(old_3, new_3)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Modifications applied to {file_path}")
