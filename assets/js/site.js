// Mobile navigation toggle and form submission confirmation.
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
})();
