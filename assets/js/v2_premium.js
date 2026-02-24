/**
 * OXYGEN V2 PREMIUM INTERACTIONS
 * Cinematic Textures, Magnetic Interactions, and Smooth Scrolling
 */

window.addEventListener('DOMContentLoaded', () => {
    initMagneticButtons();
    initFilmGrain();
});

/**
 * 1. FILM GRAIN INJECTION
 * Injects a noise filter div over the entire site.
 */
function initFilmGrain() {
    // Only inject once
    if (document.querySelector('.v2-film-grain')) return;

    const grain = document.createElement('div');
    grain.className = 'v2-film-grain';
    document.body.appendChild(grain);
}

/**
 * 2. MAGNETIC BUTTONS (Linear Interpolation Physics)
 * Top tier sites use math to "pull" buttons toward the mouse, 
 * giving physical weight to the digital UI.
 */
function initMagneticButtons() {
    // Disable intensive physics calculations on mobile/touch screens
    if (window.matchMedia("(pointer: coarse)").matches || window.innerWidth <= 768) return;

    const magneticItems = document.querySelectorAll('.magnetic-btn');

    magneticItems.forEach(item => {
        // The inner span holding the text/icon
        const content = item.querySelector('.magnetic-content');

        // Target coordinates
        let x = 0;
        let y = 0;

        // Current coordinates (interpolated)
        let cx = 0;
        let cy = 0;

        // Is mouse hovering?
        let hover = false;

        item.addEventListener('mouseenter', () => {
            hover = true;
            item.style.transition = 'background 0.4s ease, color 0.4s ease, box-shadow 0.4s ease'; // Remove transform transition to let JS control it
            if (content) content.style.transition = 'none';
        });

        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            // Calculate distance of cursor from the center of the button
            const hx = (e.clientX - rect.left) - rect.width / 2;
            const hy = (e.clientY - rect.top) - rect.height / 2;

            // The pull strength (higher is stronger). Adjust based on btn size.
            const strength = 0.4;
            const contentStrength = 0.2; // Inner content moves slightly less for parallax

            x = hx * strength;
            y = hy * strength;
        });

        item.addEventListener('mouseleave', () => {
            hover = false;
            // Instantly transition back to center using smooth CSS
            item.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s ease, color 0.4s ease, box-shadow 0.4s ease';
            item.style.transform = `translate(0px, 0px)`;

            if (content) {
                content.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
                content.style.transform = `translate(0px, 0px)`;
            }

            x = 0;
            y = 0;
            cx = 0;
            cy = 0;
        });

        // The animation loop predicting smooth physics using Linear Interpolation (Lerp)
        function render() {
            if (hover) {
                // Lerp formula: current = current + (target - current) * ease
                cx += (x - cx) * 0.15;
                cy += (y - cy) * 0.15;

                // Move the whole button container
                item.style.transform = `translate(${cx}px, ${cy}px) scale(1.05)`;

                // Move the inner content slightly differently for 3D parallax
                if (content) {
                    content.style.transform = `translate(${cx * 0.5}px, ${cy * 0.5}px)`;
                }
            }
            requestAnimationFrame(render);
        }

        // Start the loop
        requestAnimationFrame(render);
    });
}

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
        const lines = text.split('\n');

        lines.forEach((line, lIndex) => {
            const words = line.split(' ');

            words.forEach((word, wIndex) => {
                const wordWrap = document.createElement('span');
                wordWrap.style.display = 'inline-block';
                wordWrap.style.whiteSpace = 'nowrap';

                for (let i = 0; i < word.length; i++) {
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
                if (wIndex < words.length - 1) {
                    const space = document.createElement('span');
                    space.innerHTML = '&nbsp;';
                    target.appendChild(space);
                }
            });

            // Add line break if not the last line
            if (lIndex < lines.length - 1) {
                target.appendChild(document.createElement('br'));
            }
        });

        // Remove the invisible placeholder class
        target.style.opacity = 1;
    });
}
