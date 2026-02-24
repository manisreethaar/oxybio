import os

html_file = 'e:\\OXYBIO\\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Disable the sticky stacking on mobile in styles.css so they can flow naturally and be animated
css_append = """
/* ─────────────────────────────────────────────────────────
   Mobile Apple-Style Reveal Animation for Products
───────────────────────────────────────────────────────── */
@media (max-width: 768px) {
    /* Disable sticky vertical stacking which ruins mobile height/scroll constraints */
    .apple-slide {
        position: relative !important;
        top: 0 !important;
        margin-bottom: 2rem !important;
        border-radius: 20px !important;
        border: 1px solid var(--border) !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.03) !important;
        /* Start state for the JS animation */
        opacity: 0;
        transform: translateY(40px) scale(0.97);
        transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .apple-slide.is-revealed {
        opacity: 1 !important;
        transform: translateY(0) scale(1) !important;
    }
}
"""

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)


# 2. Inject the IntersectionObserver script directly into index.html
js_inject = """
    <!-- Mobile Apple-style Scroll Animation -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Only strictly apply on mobile viewports
            if (window.innerWidth <= 768) {
                const slides = document.querySelectorAll('.apple-slide');
                
                const observerOptions = {
                    root: null,
                    rootMargin: '0px 0px -10% 0px', // Trigger when card is 10% into view from bottom
                    threshold: 0.1
                };

                const slideObserver = new IntersectionObserver((entries, observer) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('is-revealed');
                            // Optional: unobserve after reveal if you only want it to happen once
                            // observer.unobserve(entry.target); 
                        } else {
                            // Let it hide again when scrolled past so it re-animates on scroll up/down
                            const rect = entry.target.getBoundingClientRect();
                            if(rect.top > 0) { // Only reset if it went off the bottom
                                entry.target.classList.remove('is-revealed');
                            }
                        }
                    });
                }, observerOptions);

                slides.forEach(slide => {
                    slideObserver.observe(slide);
                });
            }
        });
    </script>
</body>
"""

html = html.replace('</body>', js_inject)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Injected Apple-style scroll reveal animation logic for mobile cards.")
