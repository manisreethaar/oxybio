import os

css_append = """
/* ─────────────────────────────────────────────────────────
   8. About Us Mobile Overhauls (Typography, Grids, Animations)
───────────────────────────────────────────────────────── */
@media (max-width: 768px) {
    /* Hard-clamp the massive dynamic headers that break layouts */
    .headline, .display, h1.display, h3.headline {
        font-size: clamp(2rem, 8vw, 2.75rem) !important;
        line-height: 1.1 !important;
        word-break: break-word !important;
    }
    
    /* Origin Protocol & Vision headers were explicitly overflowing */
    #about-vision h1.display, #about-story h1.display {
        font-size: 2.75rem !important;
    }
    
    #about-vision h3 {
        font-size: 2rem !important;
        line-height: 1.2 !important;
        margin-bottom: 1rem !important;
    }

    /* Vision Pillars - Fix Number vs Text alignment */
    .vision-pillar-row {
        display: flex !important;
        flex-direction: row !important;
        align-items: flex-start !important;
        gap: 1rem !important;
        padding: 1rem 0 !important;
    }
    .pillar-index {
        position: static !important;
        transform: none !important;
        opacity: 1 !important;
        font-size: 0.85rem !important;
        margin-top: 0.2rem !important;
    }
    .pillar-content h5 {
        font-size: 1.1rem !important;
        margin-bottom: 0.5rem !important;
    }
    .pillar-content p {
        font-size: 0.95rem !important;
        margin-bottom: 0 !important;
        text-align: left !important;
    }

    /* Fix the "Diagnostic Result" Info Container Width */
    /* Many inline styles set arbitrary max-widths that squash content */
    div[style*="max-width:320px"], div[style*="max-width: 320px"] {
        max-width: 100% !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
    }
    
    .chapter-section p {
        text-align: justify !important;
        hyphens: auto !important;
    }
    
    /* Make Timeline and Archives blocks left flush and fix spacing */
    .development-timeline h3, .clinical-data h3 {
        font-size: 2.25rem !important;
        margin-bottom: 0.25rem !important;
    }
    
    /* Mobile Fade-up Animations for About Sections */
    .reveal, .vision-cell, .chapter-section, .timeline-content, .mobile-left-align {
        opacity: 0;
        transform: translateY(30px);
        animation: fadeUpMobile 0.8s forwards;
        animation-play-state: paused; /* Will trigger via JS or pseudo class if possible, else just let them run */
    }
    
    @keyframes fadeUpMobile {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
}
"""

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
print("Injected mobile layout fixes for about.html")
