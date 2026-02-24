import os

css_append = """
/* ─────────────────────────────────────────────────────────
   Premium Hero Tags
───────────────────────────────────────────────────────── */
.hero-tags-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: var(--space-md);
    align-items: center;
}

.premium-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 0.85rem;
    background: #f4f4f5;
    color: var(--text-main);
    border: 1px solid #e4e4e7;
    border-radius: 100px;
    font-family: var(--font-mono);
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    transition: all 0.3s ease;
}

.tag-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
}

.tag-pulse .pulse-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #16a34a;
    animation: pulse 2s ease-in-out infinite;
}

/* ─────────────────────────────────────────────────────────
   Premium Comparison Table (Responsive Cards)
───────────────────────────────────────────────────────── */
.duel-table-wrapper {
    border: 1px solid var(--border);
    border-radius: 20px;
    background: var(--bg);
    overflow: hidden;
    margin-bottom: 6rem;
}
.duel-table-header {
    display: grid;
    grid-template-columns: 1fr 1.5fr 1.5fr;
    background: var(--bg-alt);
    border-bottom: 1px solid var(--border);
}
.duel-row {
    display: grid;
    grid-template-columns: 1fr 1.5fr 1.5fr;
    border-bottom: 1px solid var(--border);
}
.duel-row:last-child {
    border-bottom: none;
}
.duel-row.bg-alt {
    background: #fafafa;
}
.duel-category-header, .duel-us-header, .duel-them-header {
    padding: 1rem 1.5rem;
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
}
.duel-us-header {
    background: #1a1a1a;
    color: rgba(255,255,255,0.75);
    font-weight: 700;
}
.duel-category-header, .duel-them-header {
    color: var(--text-muted);
}
.duel-category {
    padding: 1.5rem;
    display: flex;
    align-items: center;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-main);
    border-right: 1px solid var(--border);
}
.duel-vs-grid {
    display: contents;
}
.duel-us, .duel-them {
    padding: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.duel-us {
    background: rgba(255,255,255,0.5);
    border-right: 1px solid var(--border);
}
.duel-us .duel-icon { color: #16a34a; font-size: 1.1rem; flex-shrink: 0; }
.duel-us .duel-text { font-size: 0.95rem; font-weight: 700; color: var(--text-main); }

.duel-them .duel-icon { color: var(--text-muted); font-size: 1.1rem; flex-shrink: 0; }
.duel-them .duel-text { font-size: 0.95rem; color: var(--text-muted); }

/* MOBILE COMPARISON CARDS */
@media (max-width: 768px) {
    .duel-table-header {
        display: none !important;
    }
    .duel-table-wrapper {
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        margin-bottom: 4rem !important;
    }
    .duel-row {
        display: flex !important;
        flex-direction: column !important;
        background: var(--card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 16px !important;
        margin-bottom: 1.25rem !important;
        overflow: hidden !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important;
    }
    .duel-row.bg-alt {
        background: var(--card) !important;
    }
    .duel-category {
        border-right: none !important;
        border-bottom: 1px solid var(--border) !important;
        background: var(--bg-alt) !important;
        padding: 1rem !important;
        font-size: 0.75rem !important;
        font-family: var(--font-mono) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        justify-content: center !important;
        text-align: center !important;
    }
    .duel-vs-grid {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
    }
    .duel-us, .duel-them {
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        padding: 1.5rem 1rem !important;
        border-right: none !important;
        gap: 0.5rem !important;
    }
    .duel-us {
        border-right: 1px dashed var(--border) !important;
        background: transparent !important;
    }
    .duel-us::before {
        content: 'OXYGEN' !important;
        font-family: var(--font-mono) !important;
        font-size: 0.6rem !important;
        letter-spacing: 0.15em !important;
        color: var(--text-muted) !important;
        margin-bottom: 0.25rem !important;
    }
    .duel-them::before {
        content: 'INDUSTRY' !important;
        font-family: var(--font-mono) !important;
        font-size: 0.6rem !important;
        letter-spacing: 0.15em !important;
        color: var(--text-muted) !important;
        margin-bottom: 0.25rem !important;
    }
    .duel-us .duel-text, .duel-them .duel-text {
        font-size: 0.85rem !important;
        line-height: 1.4 !important;
    }
}
"""

with open('e:\\OXYBIO\\assets\\css\\styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
print("Appended premium CSS classes and responsive layout logic.")
