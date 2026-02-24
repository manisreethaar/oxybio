with open('e:\\OXYBIO\\assets\\css\\styles.css', 'r', encoding='cp1252') as f:
    css = f.read()

READABILITY_CSS = """

/* =========================================================
   GLOBAL READABILITY PASS
   Darker body text, better line-height, consistent sizing
   ========================================================= */

/* Body paragraphs and list items */
p, li {
    font-size: max(var(--text-base), 1rem);
    line-height: 1.75;
}

/* Section subtext — use muted but ensure readable */
.subtext, .editorial-col p {
    color: var(--text-muted);
    font-size: 1.05rem;
    line-height: 1.75;
}

/* Bento cell text */
.bento-cell p, .bento-cell span {
    font-size: 0.95rem;
    line-height: 1.65;
}

/* Pillar showcase body text */
.pillar-showcase-text {
    font-size: 1rem !important;
    line-height: 1.7 !important;
}

/* Vision cell body text */
.vision-cell p {
    font-size: 1rem;
    line-height: 1.72;
}

/* Chapter body text in about page */
.chapter-section p {
    font-size: 1.05rem;
    line-height: 1.78;
}

/* Footer body text */
.footer-brand p {
    font-size: 0.9rem;
    line-height: 1.75;
}
"""

css = css + READABILITY_CSS

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'w', encoding='cp1252') as f:
    f.write(css)

print("Done")
