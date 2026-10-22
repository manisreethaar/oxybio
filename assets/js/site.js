// Mobile navigation toggle and contact form confirmation.
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

    // The contact form posts to Google Forms through a hidden iframe so the page does not navigate away.
    var form = document.getElementById('contact-form');
    var frame = document.getElementById('contact-form-target');
    var status = document.getElementById('contact-form-status');

    if (form && frame && status) {
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
    }
})();
