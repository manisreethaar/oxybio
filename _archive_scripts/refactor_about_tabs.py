import re

with open('e:\\OXYBIO\\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------
# SECTION 1: OUR STORY (Chapters 01 & 02)
# ---------------------------------------------------------

# 1. Update the sidebar index to add active classes and click handlers
story_sidebar_old = """                            <li class="index-nav-item" data-target="chapter-01"
                                style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-main); font-weight:600; cursor:pointer; transition:color 0.3s ease;">
                                01. The Hook</li>
                            <li class="index-nav-item" data-target="chapter-02"
                                style="font-family:var(--font-serif); font-size:1.5rem; color:var(--text-muted); cursor:pointer; transition:color 0.3s ease;">
                                02. The Journey</li>"""

story_sidebar_new = """                            <li class="index-nav-item active-tab" data-target="chapter-01" onclick="switchTab('story', 'chapter-01')"
                                style="font-family:var(--font-serif); font-size:1.5rem; font-weight:600; cursor:pointer; transition:all 0.3s ease;">
                                01. The Hook</li>
                            <li class="index-nav-item" data-target="chapter-02" onclick="switchTab('story', 'chapter-02')"
                                style="font-family:var(--font-serif); font-size:1.5rem; font-weight:600; cursor:pointer; transition:all 0.3s ease;">
                                02. The Journey</li>"""

html = html.replace(story_sidebar_old, story_sidebar_new)

# 2. Wrap the chapters in a CSS Grid container to force overlap
# We'll find the start of the "Chapters Content" div and replace it
story_content_start_old = """                    <!-- Chapters Content (Light Premium) -->
                    <div>
                        <!-- Chapter 01: The Hook (Clinical Aesthetic) -->
                        <div id="chapter-01" class="chapter-section" style="margin-bottom:6rem;">"""

story_content_start_new = """                    <!-- Chapters Content (Light Premium) -->
                    <div id="story-tab-container" style="display:grid; grid-template-columns:1fr; grid-template-rows:1fr; align-items:start; position:relative;">
                        <!-- Chapter 01: The Hook (Clinical Aesthetic) -->
                        <div id="chapter-01" class="chapter-section tab-pane active" style="grid-area: 1 / 1; opacity: 1; visibility: visible; transition: opacity 0.5s ease, visibility 0.5s ease; pointer-events: auto;">"""

html = html.replace(story_content_start_old, story_content_start_new)

# 3. Update Chapter 02 to be an overlapping hidden tab
story_ch2_start_old = """                        <!-- Chapter 02: The Journey (Clinical Timeline) -->
                        <div id="chapter-02" class="chapter-section"
                            style="padding-top:6rem; border-top:1px dashed var(--border);">"""

story_ch2_start_new = """                        <!-- Chapter 02: The Journey (Clinical Timeline) -->
                        <div id="chapter-02" class="chapter-section tab-pane"
                            style="grid-area: 1 / 1; opacity: 0; visibility: hidden; transition: opacity 0.5s ease, visibility 0.5s ease; pointer-events: none;">"""

html = html.replace(story_ch2_start_old, story_ch2_start_new)


# ---------------------------------------------------------
# SECTION 2: WHO WE ARE (Chapters 03 & 04)
# ---------------------------------------------------------

# 1. Update the sidebar index
who_sidebar_old = """                                <div class="index-nav-item" data-target="chapter-03"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div
                                        style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem;">
                                        01</div>
                                    <div
                                        style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-main); font-weight:600; line-height:var(--leading-tight);">
                                        The Founder</div>
                                </div>
                                <div class="index-nav-item" data-target="chapter-04"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div
                                        style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem;">
                                        02</div>
                                    <div
                                        style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-muted); line-height:var(--leading-tight);">
                                        Our Approach</div>
                                </div>"""

who_sidebar_new = """                                <div class="index-nav-item active-tab" data-target="chapter-03" onclick="switchTab('who', 'chapter-03')"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div class="tab-num" style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; transition:color 0.3s ease;">01</div>
                                    <div class="tab-title" style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-main); font-weight:600; line-height:var(--leading-tight); transition:color 0.3s ease;">The Founder</div>
                                </div>
                                <div class="index-nav-item" data-target="chapter-04" onclick="switchTab('who', 'chapter-04')"
                                    style="cursor:pointer; transition:all 0.3s ease;">
                                    <div class="tab-num" style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted); letter-spacing:0.1em; margin-bottom:0.25rem; transition:color 0.3s ease;">02</div>
                                    <div class="tab-title" style="font-family:var(--font-serif); font-size:var(--text-lg); color:var(--text-muted); line-height:var(--leading-tight); font-weight:600; transition:color 0.3s ease;">Our Approach</div>
                                </div>"""
html = html.replace(who_sidebar_old, who_sidebar_new)


# 2. Wrap Chapters 03 & 04 in Grid
who_content_start_old = """                    <!-- Chapters content -->
                    <div>

                        <!-- ═══ CHAPTER 01: THE FOUNDER ═══ -->
                        <div id="chapter-03" class="chapter-section" style="margin-bottom:var(--space-xl);">"""

who_content_start_new = """                    <!-- Chapters content -->
                    <div id="who-tab-container" style="display:grid; grid-template-columns:1fr; grid-template-rows:1fr; align-items:start; position:relative;">

                        <!-- ═══ CHAPTER 01: THE FOUNDER ═══ -->
                        <div id="chapter-03" class="chapter-section tab-pane active" style="grid-area: 1 / 1; opacity: 1; visibility: visible; transition: opacity 0.5s ease, visibility 0.5s ease; pointer-events: auto;">"""
html = html.replace(who_content_start_old, who_content_start_new)


# 3. Update Chapter 04 to be an overlapping hidden tab
who_ch4_start_old = """                        <!-- ═══ CHAPTER 02: OUR APPROACH ═══ -->
                        <div id="chapter-04" class="chapter-section" style="padding-top:4rem; border-top:1px dashed var(--border);">"""

who_ch4_start_new = """                        <!-- ═══ CHAPTER 02: OUR APPROACH ═══ -->
                        <div id="chapter-04" class="chapter-section tab-pane" style="grid-area: 1 / 1; opacity: 0; visibility: hidden; transition: opacity 0.5s ease, visibility 0.5s ease; pointer-events: none;">"""
html = html.replace(who_ch4_start_old, who_ch4_start_new)


# ---------------------------------------------------------
# INJECT CSS & JS
# ---------------------------------------------------------

script_to_inject = """

    <!-- Master-Detail Tab Logic for About Page -->
    <style>
        /* Unselected Tab States */
        .index-nav-item { opacity: 0.5; }
        .index-nav-item:hover { opacity: 0.8; }
        /* Selected Tab States */
        .index-nav-item.active-tab { opacity: 1; color: var(--text-main) !important; }
        .index-nav-item.active-tab .tab-title { color: var(--text-main) !important; }
        .index-nav-item.active-tab .tab-num { color: var(--text-main) !important; }
        
        /* Stop native grid overlapping on mobile screens so it defaults back to scrolling */
        @media (max-width: 768px) {
            #story-tab-container, #who-tab-container { display: flex !important; flex-direction: column !important; }
            .tab-pane { grid-area: auto !important; opacity: 1 !important; visibility: visible !important; pointer-events: auto !important; margin-bottom: 4rem; }
            .index-nav-item { display: none !important; } /* Hide the sidebar clicks on mobile */
        }
    </style>
    
    <script>
        function switchTab(group, targetId) {
            if (window.innerWidth <= 768) return; // Disable tab logic on mobile stacking
            
            // 1. Identify context container based on group
            const containerId = group === 'story' ? 'about-story' : 'about-who';
            const context = document.getElementById(containerId);
            if (!context) return;
            
            // 2. Clear active state from sidebar items in this section
            const navItems = context.querySelectorAll('.index-nav-item');
            navItems.forEach(item => {
                item.classList.remove('active-tab');
                if (item.getAttribute('data-target') === targetId) {
                    item.classList.add('active-tab');
                }
            });
            
            // 3. Fade out all panes in this container, fade in the target
            const panes = context.querySelectorAll('.tab-pane');
            panes.forEach(pane => {
                if (pane.id === targetId) {
                    pane.style.opacity = '1';
                    pane.style.visibility = 'visible';
                    pane.style.pointerEvents = 'auto';
                    pane.classList.add('active');
                } else {
                    pane.style.opacity = '0';
                    pane.style.visibility = 'hidden';
                    pane.style.pointerEvents = 'none';
                    pane.classList.remove('active');
                }
            });
        }
    </script>
</body>"""

html = html.replace("</body>", script_to_inject)

with open('e:\\OXYBIO\\about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied Master-Detail interactive tabs to About Us page.")
