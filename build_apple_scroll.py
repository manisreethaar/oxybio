import codecs
import re

with codecs.open('e:\\OXYBIO\\index.html', 'r', 'utf-8') as f:
    html = f.read()

# We need to target the Solution section.
# It starts at: <!-- ═══════════════════════════════════════════════════════\n     SOLUTION / PRODUCTS SECTION
# And ends before: <!-- ═══════════════════════════════════════════════════════\n     SCIENCE & PILLARS SECTION

start_marker = r'<!-- [═]+\s*SOLUTION / PRODUCTS SECTION.*?-->'
end_marker = r'<!-- [═]+\s*SCIENCE & PILLARS SECTION'

match = re.search(f'({start_marker}.*?)</section>\\s*(?={end_marker})', html, re.DOTALL)

if match:
    # We will replace the entire matched block with our new Apple-style scroll block.
    # The actual content for Vitality, Clarity, Momentum will be placed inside a sticky container.
    
    # Let's extract the VITALITY, CLARITY, MOMENTUM blocks to reuse them accurately.
    vitality_match = re.search(r'<!-- VITALITY -->(.*?)<!-- CLARITY -->', match.group(1), re.DOTALL)
    clarity_match = re.search(r'<!-- CLARITY -->(.*?)<!-- MOMENTUM -->', match.group(1), re.DOTALL)
    momentum_match = re.search(r'<!-- MOMENTUM -->(.*?)(?=</section>)', match.group(1), re.DOTALL)
    
    if vitality_match and clarity_match and momentum_match:
        vitality_html = vitality_match.group(1).strip()
        clarity_html = clarity_match.group(1).strip()
        momentum_html = momentum_match.group(1).strip()
        
        # Modify the inner HTML to remove the inline borders and padding that expect vertical stacking
        vitality_html = vitality_html.replace('padding:3rem 0; border-top:1px solid var(--border);', '')
        clarity_html = clarity_html.replace('padding:3rem 0; border-top:1px solid var(--border);', '')
        momentum_html = momentum_html.replace('padding:3rem 0; border-top:1px solid var(--border); border-bottom:1px solid var(--border);', '')
        
        NEW_SECTION = f'''<!-- ═══════════════════════════════════════════════════════
     SOLUTION / PRODUCTS SECTION (APPLE-STYLE PINNED SCROLL)
════════════════════════════════════════════════════════ -->
            <section id="pinned-solution-wrapper" style="position:relative; height:400vh; background:var(--bg-alt); border-top:1px solid var(--border);">
                
                <!-- This sticky container locks to the screen for 400vh of scrolling -->
                <div class="sticky-product-container" style="position:sticky; top:0; height:100vh; display:flex; flex-direction:column; overflow:hidden;">
                    
                    <!-- Fixed Header inside sticky -->
                    <div class="container" style="padding-top:12vh; flex-shrink:0; position:relative; z-index:10;">
                        <div class="section-label">
                            <div class="section-label-line"></div>
                            <span class="section-label-text">The Solution</span>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:2rem; flex-wrap:wrap;">
                            <div style="max-width:800px;">
                                <h2 class="headline" style="margin-top:var(--space-sm);">So we built one. Meet Oxygen.</h2>
                                <p class="subtext editorial-col" style="margin-top:var(--space-sm);">Three precision formulas. Each scientifically designed for a specific need. All built on the same uncompromising foundation: Indian ingredients, active nutrient forms, and doses that actually work.</p>
                            </div>
                        </div>
                    </div>

                    <!-- The 3 products layered on top of each other -->
                    <div class="container" style="position:relative; flex-grow:1; display:flex; align-items:center;">
                        
                        <!-- VITALITY -->
                        <div class="apple-slide" id="slide-vitality" style="position:absolute; width:100%; top:50%; transform:translateY(-50%); opacity:1; transition:opacity 0.6s ease, transform 0.6s ease;">
                            {vitality_html}
                        </div>
                        
                        <!-- CLARITY -->
                        <div class="apple-slide" id="slide-clarity" style="position:absolute; width:100%; top:50%; transform:translateY(-30%); opacity:0; pointer-events:none; transition:opacity 0.6s ease, transform 0.6s ease;">
                            {clarity_html}
                        </div>
                        
                        <!-- MOMENTUM -->
                        <div class="apple-slide" id="slide-momentum" style="position:absolute; width:100%; top:50%; transform:translateY(-30%); opacity:0; pointer-events:none; transition:opacity 0.6s ease, transform 0.6s ease;">
                            {momentum_html}
                        </div>

                    </div>
                    
                    <!-- Scroll progress indicator -->
                    <div class="container" style="padding-bottom:5vh; flex-shrink:0;">
                        <div style="display:flex; gap:1rem; align-items:center;">
                            <div class="scroll-dot active" style="width:40px; height:4px; background:var(--text-main); border-radius:4px; transition:0.3s; opacity:1;"></div>
                            <div class="scroll-dot" style="width:40px; height:4px; background:var(--text-main); border-radius:4px; transition:0.3s; opacity:0.2;"></div>
                            <div class="scroll-dot" style="width:40px; height:4px; background:var(--text-main); border-radius:4px; transition:0.3s; opacity:0.2;"></div>
                        </div>
                    </div>

                </div>
            </section>

            <style>
                /* Prevent layout breaking on very small mobile screens by allowing scrolling inside the sticky div if needed */
                @media (max-width: 768px) {{
                    .sticky-product-container {{
                        height: auto;
                        min-height: 100vh;
                    }}
                    .apple-slide {{
                        position: relative !important;
                        opacity: 1 !important;
                        pointer-events: auto !important;
                        transform: none !important;
                        padding-top: 2rem;
                        padding-bottom: 2rem;
                        border-bottom: 1px solid var(--border);
                    }}
                    #pinned-solution-wrapper {{
                        height: auto !important; /* Disable scroll spy on mobile, revert to stack for better UX */
                    }}
                    .scroll-dot {{ display: none !important; }}
                }}
            </style>

            <script>
                // Apple-Style Pinned Scroll Logic
                document.addEventListener('DOMContentLoaded', () => {{
                    const wrapper = document.getElementById('pinned-solution-wrapper');
                    const slides = [
                        document.getElementById('slide-vitality'),
                        document.getElementById('slide-clarity'),
                        document.getElementById('slide-momentum')
                    ];
                    const dots = document.querySelectorAll('.scroll-dot');

                    if(!wrapper || window.innerWidth <= 768) return; // Disable on mobile where vertical space is too tight

                    window.addEventListener('scroll', () => {{
                        const rect = wrapper.getBoundingClientRect();
                        const scrollProgress = -rect.top / (rect.height - window.innerHeight);
                        
                        // We are scrolling through the 400vh wrapper
                        // 0 to 0.33: Slide 1
                        // 0.33 to 0.66: Slide 2
                        // 0.66 to 1: Slide 3

                        let activeIndex = 0;
                        if(scrollProgress >= 0.33 && scrollProgress < 0.66) activeIndex = 1;
                        if(scrollProgress >= 0.66) activeIndex = 2;
                        
                        // If we are before the section, lock it to slide 1
                        if(scrollProgress < 0) activeIndex = 0;
                        // If we are past the section, lock it to slide 3
                        if(scrollProgress > 1) activeIndex = 2;

                        slides.forEach((slide, index) => {{
                            if(index === activeIndex) {{
                                slide.style.opacity = '1';
                                slide.style.transform = 'translateY(-50%)';
                                slide.style.pointerEvents = 'auto';
                                dots[index].style.opacity = '1';
                            }} else if (index < activeIndex) {{
                                // Past slides scroll "up"
                                slide.style.opacity = '0';
                                slide.style.transform = 'translateY(-70%)';
                                slide.style.pointerEvents = 'none';
                                dots[index].style.opacity = '0.2';
                            }} else {{
                                // Future slides wait "down"
                                slide.style.opacity = '0';
                                slide.style.transform = 'translateY(-30%)';
                                slide.style.pointerEvents = 'none';
                                dots[index].style.opacity = '0.2';
                            }}
                        }});
                    }});
                }});
            </script>
'''
        new_html = html[:match.start()] + NEW_SECTION + html[match.end():]
        with codecs.open('e:\\OXYBIO\\index.html', 'w', 'utf-8') as f:
            f.write(new_html)
        print("Successfully rebuilt Solution section as Apple-style pinned scroll.")
    else:
        print("Failed to find inner product matches.")
else:
    print("Failed to match solution section.")
