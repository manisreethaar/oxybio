css_append = """
/* ── Structural Layout Engine (Bento Box & Asymmetrical) ─── */

.structure-section {
    padding: var(--section-py) 0;
    border-bottom: 1px solid var(--border);
}

.bento-grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 1px; /* Creates the strict border look */
    background: var(--border);
    border: 1px solid var(--border);
    margin-top: var(--space-lg);
}

.bento-cell {
    background: var(--bg);
    padding: var(--space-md);
    display: flex;
    flex-direction: column;
}

@media (max-width: 992px) {
    .bento-grid {
        grid-template-columns: 1fr;
    }
}

.data-num {
    font-family: var(--font-mono);
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.05em;
    color: var(--text-main);
    margin-bottom: var(--space-xs);
}

.data-label {
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
}

.editorial-col {
    max-width: 65ch; /* strict readability width */
}

/* Asymmetrical Left Flow */
.flow-left {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    max-width: 800px;
    padding-right: var(--space-xl);
}
"""

with open(r'e:\OXYBIO\assets\css\styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
print("Added structural classes to styles.css")
