// Mobile navigation, header shadow, scroll reveal, roadmap fill, reading progress and form confirmation.
(function () {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.getElementById('site-nav');

    if (toggle && nav) {
        toggle.addEventListener('click', function () {
            var open = toggle.getAttribute('aria-expanded') === 'true';
            toggle.setAttribute('aria-expanded', String(!open));
            nav.classList.toggle('is-open', !open);
        });

        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && nav.classList.contains('is-open')) {
                toggle.setAttribute('aria-expanded', 'false');
                nav.classList.remove('is-open');
                toggle.focus();
            }
        });
    }

    // Forms marked data-gform post to Google Forms through a hidden iframe so the page does not
    // navigate away; once the iframe loads after a submit, the form is swapped for its status message.
    document.querySelectorAll('form[data-gform]').forEach(function (form) {
        var frame = document.querySelector('iframe[name="' + form.target + '"]');
        var status = document.getElementById(form.dataset.status);
        if (!frame || !status) return;

        var submitted = false;
        form.addEventListener('submit', function () {
            submitted = true;
        });
        frame.addEventListener('load', function () {
            if (!submitted) return;
            form.hidden = true;
            status.hidden = false;
            status.focus();
        });
    });

    // Header gains a shadow once content scrolls beneath it; posts also show a reading-progress bar.
    var header = document.querySelector('.site-header');
    var progress = document.querySelector('.read-progress span');
    var ticking = false;
    function onScroll() {
        ticking = false;
        if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
        if (progress) {
            var max = document.documentElement.scrollHeight - window.innerHeight;
            progress.style.width = (max > 0 ? Math.min(100, (window.scrollY / max) * 100) : 0) + '%';
        }
    }
    window.addEventListener('scroll', function () {
        if (!ticking) {
            ticking = true;
            requestAnimationFrame(onScroll);
        }
    }, { passive: true });
    onScroll();

    // Roadmap line stops at the current stage.
    document.querySelectorAll('.timeline').forEach(function (tl) {
        var current = tl.querySelector('.is-current');
        if (current) tl.style.setProperty('--fill', (current.offsetTop + 8) + 'px');
    });

    // Scroll reveal. The head script adds .js-motion only when motion is welcome; without it,
    // everything is already visible and this does nothing.
    var root = document.documentElement;
    if (root.classList.contains('js-motion')) {
        var selector = '.section-head, .split > *, .card, .figure-stat, .flow-step, .point, .facts, ' +
            '.advisor, .post-list li, .statements > div, .notice, .quote-card, .timeline, .team-facts';
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                var el = entry.target;
                var siblings = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
                el.style.transitionDelay = Math.min(siblings, 4) * 80 + 'ms';
                el.classList.add('is-in');
                // Drop the stagger delay once revealed so hover effects respond immediately.
                el.addEventListener('transitionend', function () {
                    el.style.transitionDelay = '';
                }, { once: true });
                observer.unobserve(el);
            });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
        document.querySelectorAll(selector).forEach(function (el) {
            observer.observe(el);
        });
    }
})();
