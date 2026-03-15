/**
 * PAGE TRANSITIONS — smooth, no-flash navigation
 *
 * Strategy:
 *   CSS sets body { opacity: 0 } so page is NEVER painted visible first.
 *   This JS adds .page-ready class to fade in smoothly.
 *   On link clicks: brief fade-out, then navigate.
 */
(function () {
    'use strict';

    // ── Fade IN on page load ─────────────────────────────────
    // Use 'load' event (not DOMContentLoaded) so images don't pop in after
    // the fade has already started. On fast connections, 'load' fires quickly.
    // On slow connections we use a 200ms max-wait fallback.
    var fadeInTimer = setTimeout(function () {
        document.body.classList.add('page-ready');
    }, 200); // fallback: show page after 200ms regardless

    window.addEventListener('load', function () {
        clearTimeout(fadeInTimer);
        // Double-rAF ensures the transition property is active before opacity changes
        requestAnimationFrame(function () {
            requestAnimationFrame(function () {
                document.body.classList.add('page-ready');
            });
        });
    });

    // ── Fade OUT on navigation ───────────────────────────────
    document.addEventListener('click', function (e) {
        var link = e.target.closest('a[href]');
        if (!link) return;

        var href = link.getAttribute('href');

        // Skip: anchors, mail, tel, external sites, new tabs
        if (!href) return;
        if (href.startsWith('#')) return;
        if (href.startsWith('mailto:') || href.startsWith('tel:')) return;
        if (link.target === '_blank') return;
        if (href.startsWith('http') && !href.includes(window.location.hostname)) return;

        e.preventDefault();

        // Fade out — clean, no transform shift
        document.body.classList.add('page-exit');
        document.body.classList.remove('page-ready');

        setTimeout(function () {
            window.location.href = href;
        }, 220); // match the CSS exit transition: 0.2s
    }, false);

}());
