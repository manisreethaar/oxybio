import os

css_append = """
/* =========================================================
   DEEP MOBILE LAYOUT & OVERFLOW FIXES (Final Polish)
========================================================= */
@media (max-width: 768px) {
    /* 1. Fix Product Card Horizontal Overflow (Formula Stacks) */
    .mobile-stack-card { 
        grid-template-columns: 1fr !important; 
        gap: 2rem !important; 
    }
    
    /* 2. Overrule massive inline hero paddings that cause global white-space */
    section.structure-section[style*="padding-top"] { 
        padding-top: 5rem !important; 
        padding-bottom: 4rem !important; 
    }
    .hero-grid-layout { 
        padding-top: 5rem !important; 
    }
    
    /* 3. Fix clamp minimums that force giant fonts & horizontal scroll on mobile */
    .display { 
        font-size: clamp(2.5rem, 10vw, 3.5rem) !important; 
        line-height: 1 !important; 
        word-wrap: break-word !important; 
    }
    .subtext, .editorial-col, .editorial-col p { 
        font-size: 1.1rem !important; 
        line-height: 1.6 !important; 
        max-width: 100% !important; 
    }
    
    /* Fix weird container push on some columns */
    .flow-left {
        max-width: 100% !important;
        padding-right: 1rem !important;
    }
}
"""

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

print("Mobile layout fixes applied to CSS.")
