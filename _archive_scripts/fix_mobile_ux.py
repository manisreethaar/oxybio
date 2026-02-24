import re

css_path = 'e:\\OXYBIO\\assets\\css\\v2_premium.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add mobile optimization payload
if 'MOBILE PERFORMANCE OVERRIDES' not in css_content:
    mobile_fixes = """
/* 7. MOBILE PERFORMANCE OVERRIDES */
@media (max-width: 768px) {
    /* Simplify text reveal animation for mobile to prevent staggered 3D transform lag */
    .char {
        transform: translateY(20px);
        transform-origin: center;
        animation: textFadeUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    @keyframes textFadeUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Completely kill the canvas node network on small devices to guarantee 60fps scrolling */
    #biology-mesh {
        display: none !important;
        visibility: hidden !important;
    }
}
"""
    css_content += mobile_fixes
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

html_path = 'e:\\OXYBIO\\careers.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hide tabs on mobile
html = re.sub(r'\.side-tab-container\s*\{\s*display:\s*flex;\s*overflow-x:\s*auto;.*?\}', 
              '.side-tab-container { display: none !important; }', html, flags=re.DOTALL)

# 2. Make all tab-contents display block with logical spacing
mobile_fallback_insertion = """
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
"""
if '.tab-content {' not in html:
    html = html.replace('.side-tab-container { display: none !important; }', 
                        '.side-tab-container { display: none !important; }\n' + mobile_fallback_insertion)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Mobile UX and Performance Fixes Injected.")
