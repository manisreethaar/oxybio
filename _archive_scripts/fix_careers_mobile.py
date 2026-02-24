import re

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'a', encoding='utf-8') as f:
    f.write("""
/* ═══════════════════════════════════════════════════════
   EMERGENCY MOBILE FIXES FOR CAREERS & FORMS
════════════════════════════════════════════════════════ */
@media (max-width: 768px) {
    /* Fix: "Roles at the bench" grid collapses horizontally */
    .mobile-stack-card {
        grid-template-columns: 1fr !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* Fix: Left sticky column padding squishes content */
    .left-sticky-col {
        padding: 2rem 1.5rem !important;
        position: relative !important;
        border-right: none !important;
        border-bottom: 1px solid var(--border) !important;
    }
    
    /* Fix: The actual tab content pane getting squished */
    .mobile-stack-card > div:last-child {
        padding: 2rem 1.5rem !important;
    }
    
    /* Fix: Abstract background elements overflowing on mobile hero */
    .structure-section {
        overflow: hidden !important; 
    }
    
    /* Fix: Internship form Grid collapse */
    .mobile-stack {
        grid-template-columns: 1fr !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* Fix: Long Tab row text overlapping / wrapping terribly */
    .side-tab-container {
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch;
        gap: 0.5rem;
        padding-bottom: 0.5rem;
        border-top: none !important;
        margin-top: 1rem !important;
        padding-top: 0 !important;
    }
    
    .side-tab {
        flex: 0 0 auto !important;
        white-space: nowrap !important;
        padding: 0.75rem 1rem !important;
        border: 1px solid var(--border) !important;
        border-radius: 50px !important;
        background: var(--bg) !important;
        font-size: 0.7rem !important;
    }
    
    .side-tab.active {
        background: var(--text-main) !important;
        color: var(--bg) !important;
        border-color: var(--text-main) !important;
    }
    
    /* Fix form padding */
    .structure-section .container > div.mobile-stack > div:last-child {
        padding: 1.5rem !important;
    }
}
""")

# Bust Cache
with open('e:\\OXYBIO\\careers.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('styles.css?v=12', 'styles.css?v=13')

with open('e:\\OXYBIO\\careers.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected mobile layout fixes into styles.css and busted cache on careers.html")
