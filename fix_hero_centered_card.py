import traceback

def center_hero_card():
    try:
        with open(r'e:\OXYBIO\index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        start_marker = '<style>\n        @import url(\'https://fonts.googleapis.com/css2?family=Tiro+Tamil&display=swap\');'
        end_marker = '<!-- INNOVATIVE KNOWLEDGE PARTNER BANNER -->'
        
        start_idx = idx.find(start_marker)
        end_idx = idx.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            new_hero_html = """<style>
        /* Using Arima Madurai for a highly stylistic, premium Tamil display font */
        @import url('https://fonts.googleapis.com/css2?family=Arima+Madurai:wght@800;900&display=swap');

        /* The Premium Card for the Core Text */
        .tamil-card-wrapper {
            background: linear-gradient(145deg, rgba(255,255,255,0.85), rgba(250,250,250,0.4));
            border: 1px solid rgba(13, 138, 116, 0.2);
            box-shadow: 0 30px 60px rgba(13, 138, 116, 0.08), inset 0 2px 4px rgba(255,255,255,0.8);
            border-radius: 32px;
            padding: 3rem 4rem;
            display: inline-block;
            opacity: 0;
            animation: cardReveal 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            position: relative;
            margin-bottom: 2rem;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            z-index: 5;
            transform: translateY(40px);
        }

        .tamil-hero-text {
            display: inline-block;
            font-family: 'Arima Madurai', system-ui, sans-serif;
            font-weight: 900;
            font-size: clamp(3.5rem, 8vw, 6.5rem);
            line-height: 1.1;
            padding-bottom: 0.1em;
            margin: 0;
            
            /* Premium Emerald Gold Gradient */
            background: linear-gradient(135deg, #0D8A74 0%, #084c40 50%, #15b59a 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            
            animation: shimmerEffect 4s linear infinite;
        }

        @keyframes cardReveal {
            0% { opacity: 0; transform: translateY(40px) scale(0.95); }
            100% { opacity: 1; transform: translateY(0) scale(1); }
        }

        @keyframes shimmerEffect {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Enlarge O2 Design smoothly at the bottom */
        .hero-animation-wrapper.bottom-mounted {
            position: relative;
            transform: scale(1.3);
            margin-top: 6rem;
            margin-bottom: -4rem; /* Help blend into next section */
            display: flex;
            justify-content: center;
            opacity: 1;
            z-index: 1;
        }
        
        .centered-hero-layout {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            width: 100%;
        }

        @media (max-width: 768px) {
            .tamil-card-wrapper {
                padding: 2rem 1.5rem;
                border-radius: 24px;
            }
            .hero-animation-wrapper.bottom-mounted {
                transform: scale(0.9);
                margin-top: 3rem;
                margin-bottom: -2rem;
            }
        }
        </style>

        <section class="structure-section page-hero"
            style="padding-top:clamp(150px, 18vh, 180px); padding-bottom:80px; background:var(--bg); border-bottom:1px solid var(--border); overflow:hidden; position:relative;">
            
            <!-- OXYGEN V2 INTERACTIVE BIOLOGY MESH -->
            <canvas id="biology-mesh"
                style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none;"></canvas>

            <div class="container" style="position:relative; z-index:2;">

                <!-- CENTERED COPY -->
                <div class="centered-hero-layout reveal">

                    <div class="hero-tags-wrapper" style="margin-bottom: 2rem; display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;">
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

                    <!-- CORE TAMIL TEXT IN PREMIUM CARD -->
                    <div class="tamil-card-wrapper">
                        <h1 class="tamil-hero-text">உணவே மருந்து.</h1>
                    </div>

                    <h2 class="v2-split-text"
                        style="font-family: var(--font-serif); font-size: clamp(2rem, 4vw, 3rem); line-height: 1.2; font-weight: 700; color: var(--text-main); margin-top: 1rem; opacity: 0; letter-spacing: -0.02em;">
                        Advanced Functional Foods.<br>Powered by Fermentation.
                    </h2>

                    <p class="subtext editorial-col"
                        style="margin-top:var(--space-md); font-size:var(--text-xl); line-height:var(--leading-relaxed); max-width: 750px; margin-left: auto; margin-right: auto;">
                        We engineer real, highly-bioavailable functional foods using <strong>traditional millet fermentation</strong> and <strong>potent medicinal mushrooms</strong>—targeted for memory, athletic recovery, and on-the-go professionals.
                    </p>

                    <div style="margin-top:var(--space-lg); display:flex; gap:1rem; align-items:center; justify-content:center; flex-wrap:wrap;">
                        <a href="#join" class="btn btn-primary magnetic-btn" style="padding: 1rem 2rem;"><span class="magnetic-content">Join Waitlist</span></a>
                        <a href="problem.html" class="btn btn-outline magnetic-btn" style="padding: 1rem 2rem;"><span class="magnetic-content">Read the Science</span></a>
                    </div>

                </div>

                <!-- BOTTOM MOUNTED O2 ANIMATION -->
                <div class="hero-animation-wrapper bottom-mounted reveal" style="transition-delay: 0.4s;">
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
            print("Successfully rewrote Hero layout to centered card style with bottom O2 animation!")
        else:
            print("Exact markers not found.")
            
    except Exception as e:
        traceback.print_exc()

center_hero_card()
