import codecs

with codecs.open('e:\\OXYBIO\\careers.html', 'r', 'utf-8') as f:
    html = f.read()

# We need to target the entire section from `<div class="container" style="position:relative; z-index:2;">`
# Down to the `<!-- Abstract background element -->`
start_marker = '<div class="container" style="position:relative; z-index:2;">'
end_marker = '<!-- Abstract background element -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    old_section = html[start_idx:end_idx]
    
    # We will replace the entire corrupted block with a fresh, clean hero block
    # The user thought "high-agency builders" and "obsessive" was too aggressive, so we'll soften it to be
    # highly ambitious but more professional.
    NEW_BLOCK = '''<div class="container" style="position:relative; z-index:2;">
        <div class="flow-left reveal" style="max-width:1000px;">
            <div class="badge" style="margin-bottom:var(--space-lg); border-color:var(--text-main); color:var(--text-main); background:transparent;">Join Our Mission</div>
            <h1 class="display" style="font-size:clamp(3.5rem, 8vw, 6.5rem); line-height:0.9; letter-spacing:-0.03em; margin-bottom:2rem;">
                A biotech startup.<br><em style="color:var(--text-muted); font-weight:400;">Challenging the status quo.</em>
            </h1>
            <p class="subtext editorial-col" style="font-size:clamp(1.25rem, 2vw, 1.5rem); line-height:1.6; color:var(--text-main); max-width:800px;">
                We are looking for dedicated formulation scientists, fermentation engineers, and clinical researchers to innovate a stagnant industry. Fast-paced, science-first, and mission-driven. Help us build India's very first evidence-based precision nutrition system from the ground up at TBI, Adhiyamaan College of Engineering.
            </p>
        </div>
    </div>
    
    '''
    
    new_html = html[:start_idx] + NEW_BLOCK + html[end_idx:]
    with codecs.open('e:\\OXYBIO\\careers.html', 'w', 'utf-8') as f:
        f.write(new_html)
    print("Fixed duplication and softened aggressive startup copy.")
else:
    print("Failed to find section markers.")
