import sys

file_path = "e:/OXYBIO/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Edit 4: Top level intro
old_4 = """                            <h2 class="headline" style="margin-top:var(--space-sm);">So we are building one in the lab. Meet Oxygen.</h2>

                            <p class="subtext"
                                style="font-size: 1.15rem; line-height: 1.8; color: var(--text-muted); margin-top:var(--space-sm); max-width:800px;">

                                Three functional food formulation targets under research. Each designed for a specific need. All built on

                                the same uncompromising foundation: Indian ingredients, active nutrient forms, and doses

                                that actually work.</p>"""

new_4 = """                            <h2 class="headline" style="margin-top:var(--space-sm);">Incubating Solutions in the Biological Laboratory.</h2>

                            <p class="subtext"
                                style="font-size: 1.15rem; line-height: 1.8; color: var(--text-muted); margin-top:var(--space-sm); max-width:800px;">

                                Three distinct formulation protocols currently undergoing bioavailability modeling and active efficacy research. All compounds strictly enforce clinically transparent dosing thresholds and indigenous sourcing mandates.</p>"""

# Edit 5: EXP_02
old_5 = """                                <p
                                    style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">

                                    For when you cannot eat well but refuse to function sub-optimally. An everyday

                                    nutritional baseline.</p>

                                <ul
                                    style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Covers

                                        50% of your daily nutrient needs

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Sustained

                                        energy without sugar spikes

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Stress

                                        adaptation with KSM-66 Ashwagandha

                                    </li>

                                </ul>"""

new_5 = """                                <p
                                    style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">

                                    Engineered to resolve ubiquitous baseline micronutrient deficits identified in urban Indian populations.</p>

                                <ul
                                    style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Formulated to target 50% RDA fulfillment thresholds

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Designed to bypass simple carbohydrate glycemic responses

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Evaluated for serum cortisol modulation (KSM-66)

                                    </li>

                                </ul>"""

# Edit 6: EXP_01
old_6 = """                                <p
                                    style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">

                                    The honest alternative to high-sugar energy drinks. Built for sustained focus and

                                    the dreaded 3 pm crash.</p>

                                <ul
                                    style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Clean

                                        focus without caffeine crash

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Memory

                                        and attention support (Lion's Mane)

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>L-Theanine:Caffeine

                                        ratio 2.5:1 (targeting evidence-based ratios)

                                    </li>

                                </ul>"""

new_6 = """                                <p
                                    style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">

                                    A multi-compound substrate evaluated for extended cognitive endurance and the mitigation of acute adrenaline depletion.</p>

                                <ul
                                    style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Investigating sustained neurotransmitter modulation

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Targeting Nerve Growth Factor activation (Lion's Mane)

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Formulating L-Theanine:Caffeine at exact 2.5:1 clinical ratios

                                    </li>

                                </ul>"""


# Edit 7: EXP_03
old_7 = """                                <p
                                    style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">

                                    An athletic recovery matrix built around ATP production and true muscle repair,

                                    rather than synthetic stimulation.</p>

                                <ul
                                    style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Faster

                                        muscle recovery (Kokum + Tart Cherry)

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>ATP

                                        production support (Cordyceps militaris)

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Strength

                                        and endurance (Creatine HCl + Citrulline)

                                    </li>

                                </ul>"""

new_7 = """                                <p
                                    style="font-size:1.1rem; line-height:1.8; color:var(--text-muted); margin-bottom:2rem; max-width:90%;">

                                    A post-exertion physiological intervention intended to accelerate mitochondrial ATP synthesis and muscular hypertrophy.</p>

                                <ul
                                    style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.6rem;">

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">01</span>Targeted attenuation of delayed onset muscle soreness

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">02</span>Investigating cordycepin-mediated cellular oxygenation

                                    </li>

                                    <li
                                        style="display:flex; gap:0.75rem; align-items:flex-start; font-size:1rem; color:var(--text-main); line-height:1.6;">

                                        <span
                                            style="font-family:var(--font-mono); color:var(--text-muted); flex-shrink:0;">03</span>Engineering non-stimulant stamina substrates

                                    </li>

                                </ul>"""

content = content.replace(old_4, new_4)
content = content.replace(old_5, new_5)
content = content.replace(old_6, new_6)
content = content.replace(old_7, new_7)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Modifications applied to {file_path}")
