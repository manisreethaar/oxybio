import os, re

# 1. Update main.js to add Hash-based Tabs and ScrollSpy
js_path = r'e:\OXYBIO\assets\js\main.js'
with open(js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js_content = f.read()

interactive_js = """
// ── Hash-based Tabbed Navigation ──────────────────────────────
function handleHashTabs() {
    const hash = window.location.hash;
    const visionSec = document.getElementById('about-vision');
    const founderSec = document.getElementById('about-founder');
    
    // Only run if we are on the about page exactly
    if (!visionSec || !founderSec) return;

    // Reset both to hidden
    visionSec.style.display = 'none';
    founderSec.style.display = 'none';

    if (hash === '#about-founder') {
        founderSec.style.display = 'block';
        window.scrollTo(0,0);
        
        // Re-initialize ScrollSpy when entering this tab
        setTimeout(initScrollSpy, 100);
    } else {
        // Default to vision if empty or #about-vision
        visionSec.style.display = 'block';
        window.scrollTo(0,0);
    }
}

// Listen for hash changes from clicking the mega-menu
window.addEventListener('hashchange', handleHashTabs);

// Run on initial load
document.addEventListener('DOMContentLoaded', () => {
    handleHashTabs();
    initScrollSpy();
});


// ── ScrollSpy for About Us Index ──────────────────────────────
function initScrollSpy() {
    const chapters = document.querySelectorAll('.chapter-section');
    const navItems = document.querySelectorAll('.index-nav-item');
    
    if (chapters.length === 0 || navItems.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove active styling from all items
                navItems.forEach(item => {
                    item.style.color = 'var(--text-muted)';
                    item.style.fontWeight = '400';
                });
                
                // Find corresponding nav item
                const id = entry.target.getAttribute('id');
                const activeLink = document.querySelector(`.index-nav-item[data-target="${id}"]`);
                if (activeLink) {
                    activeLink.style.color = 'var(--text-main)';
                    activeLink.style.fontWeight = '600';
                }
            }
        });
    }, {
        rootMargin: '-20% 0px -60% 0px',
        threshold: 0.1
    });

    chapters.forEach(chapter => {
        observer.observe(chapter);
    });
    
    // Smooth scrolling for the index clicks
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            const targetId = item.getAttribute('data-target');
            const targetEl = document.getElementById(targetId);
            if(targetEl) {
                const headerOffset = 100;
                const elementPosition = targetEl.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });
}
"""

if "handleHashTabs" not in js_content:
    with open(js_path, 'a', encoding='utf-8', errors='ignore') as f:
        f.write("\n" + interactive_js)


# 2. Update about.html Add classes and IDs for ScrollSpy
html_path = r'e:\OXYBIO\about.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Add IDs to the chapters
html = html.replace('<!-- Chapter 01 -->\n                <div style="margin-bottom:var(--space-xl);">', '<!-- Chapter 01 -->\n                <div id="chapter-01" class="chapter-section" style="margin-bottom:var(--space-xl);">')
html = html.replace('<!-- Chapter 02 -->\n                <div style="margin-bottom:var(--space-xl); padding-top:var(--space-xl); border-top:1px dashed var(--border);">', '<!-- Chapter 02 -->\n                <div id="chapter-02" class="chapter-section" style="margin-bottom:var(--space-xl); padding-top:var(--space-xl); border-top:1px dashed var(--border);">')
html = html.replace('<!-- Chapter 03 -->\n                <div style="margin-bottom:var(--space-xl); padding-top:var(--space-xl); border-top:1px dashed var(--border);">', '<!-- Chapter 03 -->\n                <div id="chapter-03" class="chapter-section" style="margin-bottom:var(--space-xl); padding-top:var(--space-xl); border-top:1px dashed var(--border);">')
html = html.replace('<!-- Chapter 04 -->\n                <div style="padding-top:var(--space-xl); border-top:1px dashed var(--border);">', '<!-- Chapter 04 -->\n                <div id="chapter-04" class="chapter-section" style="padding-top:var(--space-xl); border-top:1px dashed var(--border);">')

# Update the Index List to use data-targets and tracking classes
old_index_ul = """<ul style="list-style:none; padding:0; margin:0; border-left:1px solid var(--border); padding-left:1.5rem; display:flex; flex-direction:column; gap:1.5rem;">
                    <li style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-main);">01. The Hook</li>
                    <li style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-muted);">02. The Founder</li>
                    <li style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-muted);">03. Our Approach</li>
                    <li style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-muted);">04. The Journey</li>
                </ul>"""

new_index_ul = """<ul style="list-style:none; padding:0; margin:0; border-left:1px solid var(--border); padding-left:1.5rem; display:flex; flex-direction:column; gap:1.5rem;">
                    <li class="index-nav-item" data-target="chapter-01" style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-main); font-weight:600; cursor:pointer; transition:color 0.3s ease;">01. The Hook</li>
                    <li class="index-nav-item" data-target="chapter-02" style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-muted); cursor:pointer; transition:color 0.3s ease;">02. The Founder</li>
                    <li class="index-nav-item" data-target="chapter-03" style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-muted); cursor:pointer; transition:color 0.3s ease;">03. Our Approach</li>
                    <li class="index-nav-item" data-target="chapter-04" style="font-family:var(--font-serif); font-size:var(--text-xl); line-height:var(--leading-tight); color:var(--text-muted); cursor:pointer; transition:color 0.3s ease;">04. The Journey</li>
                </ul>"""

html = html.replace(old_index_ul, new_index_ul)

with open(html_path, 'w', encoding='utf-8', errors='ignore') as f:
    f.write(html)


# 3. Update CSS for "innovative" Mega Menu visual
css_path = r'e:\OXYBIO\assets\css\styles.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Replace the old mega-menu CSS
megamenu_pattern = re.compile(r'\.mega-menu \{.*?\n\}', re.DOTALL)
new_megamenu_css = """.mega-menu {
    position: absolute;
    top: calc(100% + 1.5rem);
    left: 50%;
    transform: translateX(-50%) translateY(10px) scale(0.98);
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 20px;
    padding: 1.5rem;
    min-width: 280px;
    display: flex;
    gap: 1.5rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.02);
    opacity: 0;
    visibility: hidden;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    pointer-events: none;
}
.nav-item:hover .mega-menu {
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) translateY(0) scale(1);
    pointer-events: auto;
}
.mega-card {
    background: linear-gradient(135deg, var(--bg) 0%, #fff 100%);
    padding: 1.25rem;
    border-radius: 12px;
    min-width: 140px;
    border: 1px solid rgba(0,0,0,0.04);
}
.mega-links a {
    position: relative;
    padding-left: 0 !important;
    transition: transform 0.2s ease, color 0.2s ease;
}
.mega-links a:hover {
    transform: translateX(4px);
    color: var(--text-main);
}
.mega-links a::after {
    content: "→";
    position: absolute;
    right: -20px;
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.2s ease;
}
.mega-links a:hover::after {
    opacity: 1;
    transform: translateX(0);
}
"""

css = megamenu_pattern.sub(new_megamenu_css, css)

with open(css_path, 'w', encoding='utf-8', errors='ignore') as f:
    f.write(css)

print("Applied interactive mega-menu, scrollspy, and hash-routing.")
