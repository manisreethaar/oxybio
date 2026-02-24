/**
 * OXYGEN V2 - CINEMATIC SCROLLING & MASKS
 * Handles scroll-based SVG path drawing (Timelines) 
 * and Parallax Image Masks decoupled from main scroll.
 */

document.addEventListener('DOMContentLoaded', () => {
    initDrawOnScroll();
    initParallaxMasks();
});

/**
 * 1. SVG DRAW ON SCROLL
 * Animates the stroke-dashoffset of SVG paths based on the 
 * scroll depth relative to the element's position in the viewport.
 */
function initDrawOnScroll() {
    // Select all paths with the specific class
    const paths = document.querySelectorAll('.v2-draw-path');

    // Preparation: calculate the exact length of each path
    paths.forEach(path => {
        const length = path.getTotalLength();

        // Clear any previous transition
        path.style.transition = path.style.WebkitTransition = 'none';

        // Set up the starting positions
        path.style.strokeDasharray = length + ' ' + length;
        path.style.strokeDashoffset = length;

        // Store the original length as a custom property for fast access in scroll loop
        path.dataset.length = length;
    });

    // The scroll listener using requestAnimationFrame for performance
    let isDrawing = false;
    window.addEventListener('scroll', () => {
        if (!isDrawing) {
            window.requestAnimationFrame(() => {
                paths.forEach(path => {
                    const length = parseFloat(path.dataset.length);
                    // Get the bounding box of the SVG itself
                    const svg = path.closest('svg');
                    if (!svg) return;

                    const rect = svg.getBoundingClientRect();

                    // We want it to start drawing when the SVG enters the bottom of the screen
                    // and finish when it hits the middle/top
                    const windowHeight = window.innerHeight;

                    // calculate percentage (0 to 1) based on position in view
                    // 0 = just entered from bottom, 1 = fully scrolled past center
                    let scrollPercentage = (windowHeight - rect.top) / (windowHeight - rect.height / 2);

                    // Clamp between 0 and 1
                    scrollPercentage = Math.max(0, Math.min(1, scrollPercentage));

                    // Calculate the new offset
                    // If scrollPercentage is 0, offset = length (hidden)
                    // If scrollPercentage is 1, offset = 0 (fully drawn)
                    const drawLength = length * scrollPercentage;
                    path.style.strokeDashoffset = length - drawLength;
                });
                isDrawing = false;
            });
            isDrawing = true;
        }
    });

    // Initial trigger to draw elements already in view on load
    window.dispatchEvent(new Event('scroll'));
}

/**
 * 2. PARALLAX IMAGE MASKS
 * Images that move slightly slower/faster than the scroll,
 * revealed through a masked container frame.
 */
function initParallaxMasks() {
    const masks = document.querySelectorAll('.v2-parallax-mask');
    let isParallaxing = false;

    window.addEventListener('scroll', () => {
        if (!isParallaxing && window.innerWidth > 768) {
            window.requestAnimationFrame(() => {
                masks.forEach(mask => {
                    const img = mask.querySelector('img');
                    if (!img) return;

                    const rect = mask.getBoundingClientRect();
                    const windowCenter = window.innerHeight / 2;
                    const maskCenter = rect.top + (rect.height / 2);

                    // Distance from center of screen
                    const distance = windowCenter - maskCenter;

                    // Mult by a subtle factor (e.g. 0.1)
                    // Move the image inside its masking container
                    const yOffset = distance * 0.1;
                    img.style.transform = `translateY(${yOffset}px) scale(1.1)`;
                });
                isParallaxing = false;
            });
            isParallaxing = true;
        }
    });

    window.dispatchEvent(new Event('scroll'));
}
