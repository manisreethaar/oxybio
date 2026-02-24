import glob

files = [
    r'e:\OXYBIO\about.html',
    r'e:\OXYBIO\careers.html',
    r'e:\OXYBIO\blog.html',
    r'e:\OXYBIO\contact.html'
]

replacements = {
    'font-size:clamp(3.5rem, 7vw, 6.5rem);': 'font-size:var(--text-6xl); line-height:var(--leading-none);',
    'font-size:2.5rem;': 'font-size:var(--text-4xl); line-height:var(--leading-tight);',
    'font-size:2rem;': 'font-size:var(--text-3xl); line-height:var(--leading-tight);',
    'font-size:1.75rem;': 'font-size:var(--text-2xl); line-height:var(--leading-tight);',
    'font-size:1.5rem;': 'font-size:var(--text-2xl); line-height:var(--leading-tight);',
    'font-size:1.25rem;': 'font-size:var(--text-xl); line-height:var(--leading-tight);',
    'font-size:1.125rem;': 'font-size:var(--text-lg); line-height:var(--leading-normal);',
    'font-size:1.05rem;': 'font-size:var(--text-lg); line-height:var(--leading-normal);',
    'font-size:1rem;': 'font-size:var(--text-base); line-height:var(--leading-normal);',
    'font-size:0.95rem;': 'font-size:var(--text-base); line-height:var(--leading-relaxed);',
    'font-size:0.9rem;': 'font-size:var(--text-base); line-height:var(--leading-relaxed);',
    'font-size:0.85rem;': 'font-size:var(--text-sm); line-height:var(--leading-relaxed);',
    'font-size:0.75rem;': 'font-size:var(--text-xs); line-height:var(--leading-relaxed);',
    '<div class="bento-grid">': '<div class="bento-grid clinical-container" style="padding: 1.5rem; background: var(--bg-alt); margin-bottom: 2rem;">'
}

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Skipped {file_path}: {e}")
