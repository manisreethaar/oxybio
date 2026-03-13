import traceback

def replace_hero():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        start_marker = '<style>\n            .tamil-wrapper {'
        end_marker = '<!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->'
        
        start_idx = idx.find(start_marker)
        end_idx = idx.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            new_hero_html = """<style>
        @import url('https://fonts.googleapis.com/css2?family=Tiro+Tamil&display=swap');

        .tamil-wrapper {
            display: inline-block;
            opacity: 0;
            animation: tamilReveal 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            position: relative;
            margin-bottom: 0.5rem;
        }

        .tamil-hero-text {
            display: inline-block;
            font-family: 'Tiro Tamil', serif;
            font-weight: 400;
            font-size: clamp(4rem, 8vw, 7rem);
            line-height: 1.1;
            padding-bottom: 0.2em; /* Prevent descender clipping */
            
            /* Premium Emerald Gold Gradient */
            background: linear-gradient(135deg, #0D8A74 0%, #084c40 50%, #15b59a 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            
            animation: shimmerEffect 4s linear infinite;
        }

        @keyframes tamilReveal {
            0% { opacity: 0; transform: translateY(30px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes shimmerEffect {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Enlarge O2 Design smoothly */
        .hero-animation-wrapper {
            transform: scale(1.1);
            transform-origin: center right;
        }
        @media (max-width: 768px) {
            .hero-animation-wrapper {
                transform: scale(0.9);
                transform-origin: center;
                margin-top: 2rem;
            }
            .hero-grid-layout {
                grid-template-columns: 1fr !important;
                text-align: center;
            }
            .flow-left {
                align-items: center;
                text-align: center;
            }
        }
        </style>

        <section class="structure-section page-hero"
            style="padding-top:clamp(160px, 20vh, 200px); padding-bottom:120px; background:var(--bg); border-bottom:1px solid var(--border); overflow:hidden; position:relative;">
            
            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->
            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>

            <div class="container hero-grid-layout" style="position:relative; z-index:2; display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 4rem; align-items: center;">

                <!-- LEFTSIDE COPY -->
                <div class="flow-left reveal" style="display: flex; flex-direction: column; justify-content: center;">

                    <div class="hero-tags-wrapper" style="margin-bottom: 2rem; display: flex; flex-wrap: wrap; gap: 10px;">
                        <div class="premium-tag tag-pulse">
                            <span class="pulse-dot"></span>
                            Currently in Development
                        </div>
                        <div class="premium-tag">
                            <span class="tag-icon">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                    <polyline points="14 2 14 8 20 8"></polyline>
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
                        style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3vw, 2.75rem); line-height: 1.2; font-weight: 700; color: var(--text-main); margin-top: 0.5rem; opacity: 0; letter-spacing: -0.02em;">
                        Advanced Functional Foods.<br>Powered by Fermentation.
                    </h2>

                    <p class="subtext editorial-col"
                        style="margin-top:var(--space-md); font-size:var(--text-xl); line-height:var(--leading-relaxed); max-width: 600px;">
                        We engineer real, highly-bioavailable functional foods using <strong>traditional millet fermentation</strong> and <strong>potent medicinal mushrooms</strong>—targeted for memory, athletic recovery, and on-the-go professionals.
                    </p>

                    <div style="margin-top:var(--space-lg); display:flex; gap:1rem; align-items:center; flex-wrap:wrap;">
                        <a href="#join" class="btn btn-primary magnetic-btn"><span class="magnetic-content">Join
                                Waitlist</span></a>
                        <a href="problem.html" class="btn btn-outline magnetic-btn"><span class="magnetic-content">Read
                                the Science</span></a>
                    </div>

                </div>

                <!-- RIGHTSIDE ANIMATION -->
                <div class="hero-animation-wrapper reveal" style="transition-delay: 0.3s; position: relative; opacity: 1;">
                    <div class="orbit-ring orbit-ring-1"></div>
                    <div class="orbit-ring orbit-ring-2"></div>
                    <div class="orbit-ring orbit-ring-3"></div>
                    <div class="pulse-ring"></div>
                    <div class="atom atom-1">O</div>
                    <div class="atom atom-2">O</div>
                    <div class="molecule-result">O<sub>2</sub></div>
                </div>

            </div>

        </section>

        <!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->"""

            new_idx = idx[:start_idx] + new_hero_html + idx[end_idx + len(end_marker):]
            
            with open(r'e:\OXYBIO\index.html', 'w', encoding='utf-8') as f:
                f.write(new_idx)
            print("Successfully rewrote Hero exact layout to grid style!")
        else:
            print("Exact markers not found.")
            print("Start:", start_idx)
            print("End:", end_idx)
            
    except Exception as e:
        traceback.print_exc()

replace_hero()
