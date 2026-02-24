import re

with open('e:\\OXYBIO\\careers.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove TBI LAB from On-site string
html = html.replace('Mode: <span style="color:var(--text-main); font-weight:600;">On-site (TBI Lab)</span>', 
                    'Mode: <span style="color:var(--text-main); font-weight:600;">On-Site</span>')

# 2. Extract and replace the mobile standard fallback block inside the embedded style
old_mobile_block = """                                    /* Mobile fallback for tabs */
                                    @media (max-width: 768px) {
                                        .side-tab-container { display: none !important; }

                                        .tab-content {
                                            display: block !important;
                                            opacity: 1 !important;
                                            visibility: visible !important;
                                            animation: none !important;
                                            margin-bottom: 4rem;
                                            padding-bottom: 3rem;
                                            border-bottom: 1px dashed var(--border);
                                        }
                                        .tab-content:last-child {
                                            border-bottom: none;
                                            padding-bottom: 0;
                                            margin-bottom: 0;
                                        }


                                        .side-tab {
                                            border-left: none !important;
                                            border-bottom: 2px solid transparent;
                                            padding: 1rem;
                                            width: auto;
                                            flex-shrink: 0;
                                            margin-bottom: 0;
                                            flex: 1;
                                            text-align: center;
                                        }

                                        .side-tab.active {
                                            border-bottom: 2px solid var(--text-main);
                                            background: transparent;
                                        }

                                        .left-sticky-col>div {
                                            min-height: auto !important;
                                            position: relative !important;
                                        }
                                    }"""

premium_mobile_block = """                                    /* PREMIUM MOBILE STACKING CARDS (DECK EFFECT) */
                                    @media (max-width: 768px) {
                                        .side-tab-container { display: none !important; }

                                        .premium-tabs-container {
                                            position: relative;
                                            padding-bottom: 4rem;
                                        }

                                        .tab-content {
                                            display: block !important;
                                            opacity: 1 !important;
                                            visibility: visible !important;
                                            animation: none !important;
                                            
                                            position: sticky !important;
                                            background: var(--bg-alt);
                                            border: 1px solid var(--border);
                                            border-radius: 24px;
                                            padding: 2.5rem 1.5rem;
                                            box-shadow: 0 -20px 40px rgba(0,0,0,0.06);
                                            margin-bottom: 100vh; /* Extremely tall margin ensures the card scrolls fully before the next one hits */
                                        }
                                        
                                        .tab-content:last-child {
                                            margin-bottom: 0;
                                        }

                                        /* Stagger the sticky positioning so headers stack visibly like a deck */
                                        #tab-overview { top: 90px !important; z-index: 10; }
                                        #tab-output { top: 105px !important; z-index: 20; background: #ffffff; }
                                        #tab-profile { top: 120px !important; z-index: 30; background: var(--bg-alt); }
                                        #tab-offer { top: 135px !important; z-index: 40; background: #ffffff; }

                                        .left-sticky-col>div {
                                            min-height: auto !important;
                                            position: relative !important;
                                        }
                                        
                                        /* High-end typography adjustments */
                                        .tab-content h4 {
                                            font-size: 1.15rem;
                                            padding-bottom: 1.25rem;
                                            border-bottom: 1px solid rgba(0,0,0,0.06);
                                            margin-bottom: 1.75rem;
                                            color: var(--text-main);
                                            display: flex;
                                            align-items: center;
                                            justify-content: space-between;
                                        }
                                        
                                        .tab-content h4::after {
                                            content: '↓';
                                            font-family: var(--font-mono);
                                            font-size: 0.85rem;
                                            opacity: 0.3;
                                            background: rgba(0,0,0,0.05);
                                            border-radius: 50px;
                                            width: 24px;
                                            height: 24px;
                                            display: flex;
                                            align-items: center;
                                            justify-content: center;
                                        }
                                    }"""

if old_mobile_block in html:
    html = html.replace(old_mobile_block, premium_mobile_block)
else:
    print("Warning: Strict string block replacement failed. Attempting regex.")
    html = re.sub(r'/\* Mobile fallback for tabs \*/.*?\}\s*\}', premium_mobile_block, html, flags=re.DOTALL)

# Ensure cache is busted for careers page
html = re.sub(r'href="assets/css/styles\.css\?v=\d+"', 'href="assets/css/styles.css?v=17"', html)

with open('e:\\OXYBIO\\careers.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Premium Deck-of-Cards interaction applied to careers.html Mobile layout.")
