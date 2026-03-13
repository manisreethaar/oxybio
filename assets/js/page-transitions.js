/**
 * Page Transitions JS
 * Lightweight fade effect for page-to-page navigation
 */
(function () {
    'use strict';

    // Fade in on load
    document.addEventListener('DOMContentLoaded', function () {
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.4s ease';
        requestAnimationFrame(function () {
            requestAnimationFrame(function () {
                document.body.style.opacity = '1';
            });
        });
    });

    // Fade out on link click
    document.addEventListener('click', function (e) {
        var link = e.target.closest('a');
        if (!link) return;
        var href = link.getAttribute('href');
        if (!href || href.startsWith('#') || href.startsWith('mailto') || href.startsWith('tel')) return;
        if (link.target === '_blank') return;
        if (href.startsWith('http') && !href.includes(window.location.hostname)) return;

        e.preventDefault();
        document.body.style.opacity = '0';
        document.body.style.transform = 'translateY(-4px)';
        setTimeout(function () {
            window.location.href = href;
        }, 300);
    });
}());
