import os

# 1. ADD CSS to v2_premium.css
css_append = """
/* 4. TEXT STAGGER REVEAL
   Splits text into characters/words that spin/fade up sequentially.
*/
.text-reveal-wrapper {
    display: inline-block;
    overflow: hidden;
    vertical-align: top;
}

.char {
    display: inline-block;
    opacity: 0;
    transform: translateY(100%) rotateX(-90deg);
    transform-origin: bottom center;
    will-change: transform, opacity;
    animation: textSpinUp 1s cubic-bezier(0.19, 1, 0.22, 1) forwards;
}

@keyframes textSpinUp {
    0% { opacity: 0; transform: translateY(100%) rotateX(-90deg); }
    100% { opacity: 1; transform: translateY(0) rotateX(0); }
}
"""

with open('e:\\OXYBIO\\assets\\css\\v2_premium.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

# 2. ADD JS to v2_premium.js
js_append = """
/**
 * 3. ADVANCED TEXT REVEAL
 * Splits target elements into individually animatable character spans
 * with calculated mathematical stagger delays.
 */
document.addEventListener('DOMContentLoaded', () => {
    initTextReveal();
});

function initTextReveal() {
    const splitTargets = document.querySelectorAll('.v2-split-text');
    
    splitTargets.forEach(target => {
        const text = target.innerText;
        target.innerHTML = '';
        
        let charIndex = 0;
        
        // Handle breaks separately to preserve layout
        const lines = text.split('\\n');
        
        lines.forEach((line, lIndex) => {
            const words = line.split(' ');
            
            words.forEach((word, wIndex) => {
                const wordWrap = document.createElement('span');
                wordWrap.style.display = 'inline-block';
                wordWrap.style.whiteSpace = 'nowrap';
                
                for(let i = 0; i < word.length; i++) {
                    const charWrap = document.createElement('span');
                    charWrap.className = 'text-reveal-wrapper';
                    
                    const charInner = document.createElement('span');
                    charInner.className = 'char';
                    charInner.innerText = word[i];
                    // Stagger the animation timing based on character index
                    charInner.style.animationDelay = `${charIndex * 0.03}s`;
                    
                    charWrap.appendChild(charInner);
                    wordWrap.appendChild(charWrap);
                    charIndex++;
                }
                
                target.appendChild(wordWrap);
                // Add space after word if not the last
                if(wIndex < words.length - 1) {
                    const space = document.createElement('span');
                    space.innerHTML = '&nbsp;';
                    target.appendChild(space);
                }
            });
            
            // Add line break if not the last line
            if(lIndex < lines.length - 1) {
                target.appendChild(document.createElement('br'));
            }
        });
        
        // Remove the invisible placeholder class
        target.style.opacity = 1;
    });
}
"""

with open('e:\\OXYBIO\\assets\\js\\v2_premium.js', 'a', encoding='utf-8') as f:
    f.write(js_append)

# 3. APPLY TO INDEX.HTML HERO
with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_h1 = '<h1 class="display" style="font-size:var(--text-6xl); line-height:var(--leading-none);">Ancient\n                        Ingredients.<br>Modern Science.</h1>'
new_h1 = '<h1 class="display v2-split-text" style="font-size:var(--text-6xl); line-height:var(--leading-none); opacity:0;">Ancient Ingredients.\\nModern Science.</h1>'

if 'Ancient\n                        Ingredients.<br>Modern Science.' in html:
    html = html.replace('Ancient\n                        Ingredients.<br>Modern Science.', 'Ancient Ingredients.\nModern Science.')

html = html.replace('<h1 class="display" style="font-size:var(--text-6xl); line-height:var(--leading-none);">Ancient Ingredients.\nModern Science.</h1>', '<h1 class="display v2-split-text" style="font-size:var(--text-6xl); line-height:var(--leading-none); opacity:0;">Ancient Ingredients.\nModern Science.</h1>')

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected Splitting Text Reveal routines for Phase 2!")
