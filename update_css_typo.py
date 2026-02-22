import os, re

css_path = r'e:\OXYBIO\assets\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Inject typography scale and line spacing into :root
scale_css = """
    /* --- Strict Fluid Typography Scale --- */
    --text-xs: clamp(0.75rem, 0.7vw, 0.8rem);
    --text-sm: clamp(0.875rem, 0.8vw, 0.95rem);
    --text-base: clamp(1rem, 1vw, 1.125rem);
    --text-lg: clamp(1.125rem, 1.2vw, 1.25rem);
    --text-xl: clamp(1.25rem, 1.5vw, 1.5rem);
    --text-2xl: clamp(1.5rem, 2vw, 2rem);
    --text-3xl: clamp(2rem, 3vw, 2.75rem);
    --text-4xl: clamp(2.5rem, 4vw, 3.75rem);
    --text-5xl: clamp(3rem, 5vw, 4.5rem);
    --text-6xl: clamp(4rem, 7vw, 6.5rem);

    /* --- Strict Line Spacing (Leading) --- */
    --leading-none: 1;
    --leading-tight: 1.1;
    --leading-snug: 1.3;
    --leading-normal: 1.6;
    --leading-relaxed: 1.8;
}"""

css = re.sub(r'(--space-xl:\s*8rem;\s*)}', r'\1\n' + scale_css, css)

# 2. Update Typography Classes
typo_update = """/* ── Section Headlines ───────────────────────────────────── */
.display {
    font-family: var(--font-serif);
    font-size: var(--text-6xl);
    font-weight: 800;
    line-height: var(--leading-tight);
    letter-spacing: -0.04em;
    color: var(--text-main);
}

.display em {
    font-style: italic;
    color: var(--text-muted);
}

.headline {
    font-family: var(--font-serif);
    font-size: var(--text-4xl);
    font-weight: 700;
    line-height: var(--leading-tight);
    letter-spacing: -0.03em;
    color: var(--text-main);
}

.headline em {
    font-style: italic;
    color: var(--accent-mid);
}

.subtext {
    font-size: var(--text-lg);
    color: var(--text-muted);
    line-height: var(--leading-relaxed);
    max-width: 560px;
}"""

# Find the Section Headlines part and replace it
css = re.sub(r'/\* ── Section Headlines ───────────────────────────────────── \*/.*?/\* ── Hero ────────────────────────────────────────────────── \*/', typo_update + '\n\n/* ── Hero ────────────────────────────────────────────────── */', css, flags=re.DOTALL)


# 3. Add styling for the new Data Presentation (Stat progress bars, visual cues)
data_presentation_css = """
/* ── UI/UX Data Presentation Enhancements ──────────────── */
.stat-bar-container {
    width: 100%;
    height: 4px;
    background: var(--border);
    border-radius: 4px;
    margin-top: 1rem;
    overflow: hidden;
    position: relative;
    display: none; /* Only show where explicitly needed */
}

.stat-bar-fill {
    height: 100%;
    background: var(--text-main);
    border-radius: 4px;
    position: relative;
    transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.editorial-divider {
    width: 60px;
    height: 1px;
    background: var(--text-main);
    margin: 1.5rem 0;
}

.text-meta {
    font-family: var(--font-mono);
    font-size: var(--text-xs);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
}
"""

css += '\n' + data_presentation_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.css with typography system and data presentation classes.")
