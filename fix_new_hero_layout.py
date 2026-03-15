import re
import traceback

def rewrite_hero():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # Regex to capture from the HERO SECTION comment down to the Knowledge Partner Banner
        pattern = re.compile(
            r'(<!-- \s*-+\s*HERO SECTION.*?-->).*?(<!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->)', 
            re.DOTALL
        )
        
        new_hero = r"""\1
        <style>
        .tamil-wrapper {
            display: inline-block;
            opacity: 0;
            animation: tamilReveal 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            animation-delay: 0.1s;
        }
        .tamil-hero-text {
            display: inline-block;
            font-family: 'Noto Sans Tamil', sans-serif;
            font-weight: 900;
            font-size: clamp(3.5rem, 9vw, 8rem);
            line-height: 1.2;
            letter-spacing: -0.02em;
            padding-bottom: 0.1em; /* Prevent descender clipping */
            background: linear-gradient(135deg, #0D8A74 0%, #065B4C 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: tamilFloat 6s ease-in-out infinite;
        }

        @keyframes tamilReveal {
            0% { opacity: 0; transform: translateY(40px); filter: blur(10px); }
            100% { opacity: 1; transform: translateY(0); filter: blur(0); }
        }
        @keyframes tamilFloat {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-12px); }
        }
        </style>

        <section class="structure-section page-hero"
            style="padding-top:clamp(160px, 20vh, 200px); padding-bottom:120px; background:var(--bg); border-bottom:1px solid var(--border); overflow:hidden; position:relative; display:flex; flex-direction:column; align-items:center; text-align:center;">
            
            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->
            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>

            <!-- BACKGROUND ANIMATION (Subtle mathematical backdrop) -->
            <div class="hero-animation-wrapper reveal" style="position:absolute; top:45%; left:50%; transform:translate(-50%, -50%) scale(1.6); opacity: 0.08; z-index: 1; pointer-events: none; transition-delay: 0.2s;">
                <div class="orbit-ring orbit-ring-1"></div>
                <div class="orbit-ring orbit-ring-2"></div>
                <div class="orbit-ring orbit-ring-3"></div>
                <div class="pulse-ring"></div>
                <div class="atom atom-1">O</div>
                <div class="atom atom-2">O</div>
                <div class="molecule-result">O<sub>2</sub></div>
            </div>

            <div class="container" style="position:relative; z-index:2; display:flex; flex-direction:column; align-items:center;">

                <div class="flow-left reveal" style="width: 100%; display: flex; flex-direction: column; align-items: center;">

                    <!-- Tags -->
                    <div style="display:flex; justify-content:center; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom: 2rem;">
                        <div class="premium-tag tag-pulse">
                            <span class="pulse-dot"></span>
                            Currently in Development
                        </div>
                        <div class="premium-tag">
                            <span class="tag-icon">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                    <polyline points="14 2 14 8 20 8"></polyline>
                                    <line x1="16" y1="13" x2="8" y2="13"></line>
                                    <line x1="16" y1="17" x2="8" y2="17"></line>
                                    <polyline points="10 9 9 9 8 9"></polyline>
                                </svg>
                            </span>
                            Efficacy Study Planned
                        </div>
                    </div>

                    <!-- CORE TAMIL TEXT -->
                    <div class="tamil-wrapper">
                        <h1 class="tamil-hero-text">உணவே மருந்து.</h1>
                    </div>

                    <h2 class="v2-split-text"
                        style="font-family: var(--font-serif); font-size: clamp(1.8rem, 4vw, 2.75rem); line-height: 1.2; font-weight: 700; color: var(--text-main); margin-top: 1rem; opacity: 0; letter-spacing: -0.02em;">
                        Advanced Functional Foods.<br>Powered by Fermentation.
                    </h2>

                    <p class="subtext editorial-col"
                        style="margin-top:var(--space-md); font-size:var(--text-xl); line-height:var(--leading-relaxed); max-width: 800px; margin-left: auto; margin-right: auto;">
                        We engineer real, highly-bioavailable functional foods using <strong>traditional millet fermentation</strong> and <strong>potent medicinal mushrooms</strong>—targeted for memory, athletic recovery, and on-the-go professionals.
                    </p>

                    <div
                        style="margin-top:var(--space-lg); display:flex; gap:1rem; align-items:center; justify-content:center; flex-wrap:wrap;">
                        <a href="#join" class="btn btn-primary magnetic-btn"><span class="magnetic-content">Join
                                Waitlist</span></a>
                        <a href="problem.html" class="btn btn-outline magnetic-btn"><span class="magnetic-content">Read
                                the Science</span></a>
                    </div>

                </div>

            </div>

        </section>

        \2"""
        
        if pattern.search(idx):
            idx = pattern.sub(new_hero, idx)
            with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
                f.write(idx)
            print("Successfully rewrote Hero layout!")
        else:
            print("Regex pattern not found. Could not rewrite.")
            
    except Exception as e:
        traceback.print_exc()

rewrite_hero()
