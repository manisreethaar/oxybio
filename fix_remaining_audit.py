import re

# =========================================================
# FIX 1 — science.html: Principle 03 D3/K2 era language
# =========================================================
with open('science.html', 'r', encoding='utf-8') as f:
    sci = f.read()

sci = sci.replace(
    "Vitamins don't work in isolation. We structure our foods to include necessary biological co-factors for absorption.",
    "Nutrients don't act in isolation. We investigate how fermentation creates a food matrix where functional compounds are delivered in their biologically coherent form."
)

with open('science.html', 'w', encoding='utf-8') as f:
    f.write(sci)
print("science.html: Principle 03 updated")

# =========================================================
# FIX 2 — about.html: "Vitamin D deficient" stat
#          Replace with a stat that reflects current focus
# =========================================================
with open('about.html', 'r', encoding='utf-8') as f:
    abt = f.read()

abt = abt.replace(
    "of urban Indians are Vitamin D deficient \ufffd driven by indoor work environments and inadequate dietary sources.",
    "of urban Indians have micronutrient deficiencies linked to poor dietary diversity and low bioavailability from processed food sources."
)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(abt)
print("about.html: stat updated")

# =========================================================
# FIX 3 — careers.html: Phase 02 Cosmetics R&D
# =========================================================
with open('careers.html', 'r', encoding='utf-8') as f:
    car = f.read()

# Phase label
car = car.replace(
    '02 // Cosmetics R&amp;D',
    '02 // Bioavailability Testing'
)
car = car.replace(
    '02 // Cosmetics R\u0026D',
    '02 // Bioavailability Testing'
)

# Phase description
car = car.replace(
    'Develop and optimize bio-fermented cosmetic and skincare systems with focus\r\n\r\n                                            on raw material efficacy.',
    'Design and execute bioavailability experiments on fermented grain matrices. Quantify absorption improvement relative to unprocessed controls using established analytical methods.'
)
car = car.replace(
    'Develop and optimize bio-fermented cosmetic and skincare systems with focus\n\n                                            on raw material efficacy.',
    'Design and execute bioavailability experiments on fermented grain matrices. Quantify absorption improvement relative to unprocessed controls using established analytical methods.'
)

# =========================================================
# FIX 4 — careers.html: Mobile sticky tab-content bleed
#          Replace the "deck/sticky" pattern with clean
#          vertical accordion-style stacking on mobile
# =========================================================

old_tab_mobile = '''                                    /* PREMIUM MOBILE STACKING CARDS (DECK EFFECT) */

                                    @media (max-width: 768px) {

                                        .side-tab-container {

                                            display: none !important;

                                        }



                                        .premium-tabs-container {

                                            position: relative;

                                            padding-bottom: var(--space-lg);

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

                                            box-shadow: 0 -20px 40px rgba(0, 0, 0, 0.06);

                                            margin-bottom: 2rem;

                                        }



                                        .tab-content:last-child {

                                            margin-bottom: 0;

                                        }



                                        /* Stagger the sticky positioning so headers stack visibly like a deck */

                                        #tab-overview {

                                            top: 90px !important;

                                            z-index: 10;

                                        }



                                        #tab-output {

                                            top: 105px !important;

                                            z-index: 20;

                                            background: #ffffff;

                                        }



                                        #tab-profile {

                                            top: 120px !important;

                                            z-index: 30;

                                            background: var(--bg-alt);

                                        }



                                        #tab-offer {

                                            top: 135px !important;

                                            z-index: 40;

                                            background: #ffffff;

                                        }



                                        .left-sticky-col>div {

                                            min-height: auto !important;

                                            position: relative !important;

                                        }



                                        /* High-end typography adjustments */

                                        .tab-content h4 {

                                            font-size: 1.15rem;

                                            padding-bottom: 1.25rem;

                                            border-bottom: 1px solid rgba(0, 0, 0, 0.06);

                                            margin-bottom: 1.75rem;

                                            color: var(--text-main);

                                            display: flex;

                                            align-items: center;

                                            justify-content: space-between;

                                        }



                                        .tab-content h4::after {

                                            content: '→';

                                            font-family: var(--font-mono);

                                            font-size: 0.85rem;

                                            opacity: 0.3;

                                            background: rgba(0, 0, 0, 0.05);

                                            border-radius: 50px;

                                            width: 24px;

                                            height: 24px;

                                            display: flex;

                                            align-items: center;

                                            justify-content: center;

                                        }

                                    }'''

new_tab_mobile = '''                                    /* MOBILE: Clean vertical stacking (no sticky/deck overflow) */

                                    @media (max-width: 768px) {

                                        .side-tab-container {
                                            display: none !important;
                                        }

                                        .premium-tabs-container {
                                            position: static;
                                            padding-bottom: 0;
                                        }

                                        .tab-content {
                                            display: block !important;
                                            opacity: 1 !important;
                                            visibility: visible !important;
                                            animation: none !important;
                                            position: relative !important;
                                            top: auto !important;
                                            z-index: auto !important;
                                            background: var(--bg-alt);
                                            border: 1px solid var(--border);
                                            border-radius: 16px;
                                            padding: 2rem 1.25rem;
                                            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
                                            margin-bottom: 1.5rem;
                                            overflow: hidden;
                                            word-break: break-word;
                                            overflow-wrap: break-word;
                                        }

                                        .tab-content:last-child {
                                            margin-bottom: 0;
                                        }

                                        #tab-overview,
                                        #tab-output,
                                        #tab-profile,
                                        #tab-offer {
                                            top: auto !important;
                                            z-index: auto !important;
                                            background: var(--bg-alt) !important;
                                        }

                                        .left-sticky-col > div {
                                            min-height: auto !important;
                                            position: relative !important;
                                        }

                                        .tab-content h4 {
                                            font-size: 1rem;
                                            padding-bottom: 1rem;
                                            border-bottom: 1px solid rgba(0,0,0,0.06);
                                            margin-bottom: 1.5rem;
                                            color: var(--text-main);
                                        }

                                        .tab-content h4::after {
                                            content: none;
                                        }

                                    }'''

if old_tab_mobile in car:
    car = car.replace(old_tab_mobile, new_tab_mobile)
    print("careers.html: mobile tab sticky fixed (exact match)")
else:
    # Try a targeted approach just for the most critical parts
    car = car.replace(
        'position: sticky !important;',
        'position: relative !important;'
    )
    car = car.replace(
        'box-shadow: 0 -20px 40px rgba(0, 0, 0, 0.06);',
        'box-shadow: 0 2px 12px rgba(0,0,0,0.05);'
    )
    print("careers.html: mobile tab: targeted fallback replacements applied")

with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(car)
print("careers.html written")
