import os

html_file = 'e:\\OXYBIO\\about.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS for the initial hidden state and the revealed state specifically for these about nodes
css_inject = """
    <style>
        /* Mobile Fade-up Animations for About Sections */
        @media (max-width: 768px) {
            .mobile-fade-up {
                opacity: 0;
                transform: translateY(30px);
                transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            }
            .mobile-fade-up.is-revealed {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
"""

# Place the css right before closing head
if '</head>' in html:
    html = html.replace('</head>', css_inject + '\n</head>')


# The Javascript intersection observer script
js_inject = """
    <!-- Mobile Apple-style Fade Up Animation -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (window.innerWidth <= 768) {
                // Select elements that need the premium fade up
                const animatedElements = document.querySelectorAll('.vision-cell, .vision-pillar-row, .chapter-section h3, .chapter-section p, .development-timeline, .clinical-data, div[style*="max-width:320px"]');
                
                // Add the base class to them
                animatedElements.forEach(el => {
                    el.classList.add('mobile-fade-up');
                });

                const observerOptions = {
                    root: null,
                    rootMargin: '0px 0px -5% 0px',
                    threshold: 0.1
                };

                const fadeObserver = new IntersectionObserver((entries, observer) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('is-revealed');
                        }
                    });
                }, observerOptions);

                animatedElements.forEach(el => {
                    fadeObserver.observe(el);
                });
            }
        });
    </script>
</body>
"""

# Place it before closing body
if '</body>' in html:
    html = html.replace('</body>', js_inject)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Injected mobile Apple-style fade-up script to about.html")
