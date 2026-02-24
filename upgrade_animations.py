import re

# 1. UPGRADE ABOUT.HTML
with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

# Replace the CSS
old_css = r"""    <style>
        /\* Mobile Fade-up Animations for About Sections \*/
        @media \(max-width: 768px\) \{
            \.mobile-fade-up \{
                opacity: 0;
                transform: translateY\(30px\);
                transition: opacity 0\.8s cubic-bezier\(0\.16, 1, 0\.3, 1\), transform 0\.8s cubic-bezier\(0\.16, 1, 0\.3, 1\);
            \}
            \.mobile-fade-up\.is-revealed \{
                opacity: 1;
                transform: translateY\(0\);
            \}
        \}
    </style>"""

new_css = """    <style>
        /* Mobile Premium Fade-up Animations for About Sections */
        @media (max-width: 768px) {
            .mobile-fade-up {
                opacity: 0;
                transform: translateY(50px) scale(0.97);
                filter: blur(5px);
                will-change: transform, opacity, filter;
                transition: opacity 1s cubic-bezier(0.22, 1, 0.36, 1), 
                            transform 1.2s cubic-bezier(0.19, 1, 0.22, 1),
                            filter 1s cubic-bezier(0.22, 1, 0.36, 1);
            }
            .mobile-fade-up.is-revealed {
                opacity: 1;
                transform: translateY(0) scale(1);
                filter: blur(0);
            }
        }
    </style>"""

about_html = re.sub(old_css, new_css, about_html)

# Replace the JS
old_js = r"""                const fadeObserver = new IntersectionObserver\(\(entries, observer\) => \{
                    entries\.forEach\(entry => \{
                        if \(entry\.isIntersecting\) \{
                            entry\.target\.classList\.add\('is-revealed'\);
                        \}
                    \}\);
                \}, observerOptions\);"""

new_js = """                let delay = 0;
                let lastIntersectTime = 0;
                const fadeObserver = new IntersectionObserver((entries, observer) => {
                    const now = Date.now();
                    if(now - lastIntersectTime > 100) { delay = 0; }
                    
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.style.transitionDelay = `${delay}ms`;
                            
                            // Force reflow
                            void entry.target.offsetWidth;
                            
                            entry.target.classList.add('is-revealed');
                            delay += 150;
                            lastIntersectTime = now;
                            observer.unobserve(entry.target);
                        }
                    });
                }, observerOptions);"""

about_html = re.sub(old_js, new_js, about_html)

with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)


# 2. UPGRADE INDEX.HTML (JS side)
with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_old_js = r"""                const slideObserver = new IntersectionObserver\(\(entries, observer\) => \{
                    entries\.forEach\(entry => \{
                        if \(entry\.isIntersecting\) \{
                            entry\.target\.classList\.add\('is-revealed'\);
                            // Optional: unobserve after reveal if you only want it to happen once
                            // observer\.unobserve\(entry\.target\); 
                        \} else \{
                            // Let it hide again when scrolled past so it re-animates on scroll up/down
                            const rect = entry\.target\.getBoundingClientRect\(\);
                            if \(rect\.top > 0\) \{ // Only reset if it went off the bottom
                                entry\.target\.classList\.remove\('is-revealed'\);
                            \}
                        \}
                    \}\);
                \}, observerOptions\);"""

index_new_js = """                let delay = 0;
                let lastIntersectTime = 0;
                const slideObserver = new IntersectionObserver((entries, observer) => {
                    const now = Date.now();
                    if(now - lastIntersectTime > 100) { delay = 0; }
                    
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.style.transitionDelay = `${delay}ms`;
                            void entry.target.offsetWidth;
                            entry.target.classList.add('is-revealed');
                            delay += 200;
                            lastIntersectTime = now;
                            observer.unobserve(entry.target);
                        }
                    });
                }, observerOptions);"""

index_html = re.sub(index_old_js, index_new_js, index_html)

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# 3. UPGRADE STYLES.CSS
with open('e:\\OXYBIO\\assets\\css\\styles.css', 'r', encoding='utf-8') as f:
    styles_css = f.read()

css_old = r"""        /\* Start state for the JS animation \*/
        opacity: 0;
        transform: translateY\(40px\) scale\(0\.97\);
        transition: all 0\.8s cubic-bezier\(0\.16, 1, 0\.3, 1\) !important;
    \}
    \.apple-slide\.is-revealed \{
        opacity: 1 !important;
        transform: translateY\(0\) scale\(1\) !important;
    \}"""

css_new = """        /* Start state for the JS animation */
        opacity: 0;
        transform: translateY(60px) scale(0.95);
        filter: blur(8px);
        transform-origin: center bottom;
        will-change: transform, opacity, filter;
        transition: opacity 1s cubic-bezier(0.22, 1, 0.36, 1) !important, 
                    transform 1.2s cubic-bezier(0.19, 1, 0.22, 1) !important,
                    filter 1s cubic-bezier(0.22, 1, 0.36, 1) !important;
    }
    .apple-slide.is-revealed {
        opacity: 1 !important;
        transform: translateY(0) scale(1) !important;
        filter: blur(0) !important;
    }"""

styles_css = re.sub(css_old, css_new, styles_css)

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'w', encoding='utf-8') as f:
    f.write(styles_css)

print("Ultra-Premium Apple Reveal animations applied to index.html, about.html, and styles.css")
