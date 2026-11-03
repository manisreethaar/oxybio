// Motion layer: smooth scroll, page curtain, word-by-word headings, grain fields and scroll
// scenes. Everything here is progressive: without GSAP or under reduced motion, the page stays
// fully readable and static.
(function () {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var finePointer = window.matchMedia('(pointer: fine)').matches;
    var hasGsap = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';
    var root = document.documentElement;

    // ---------- Grain fields (hero and the formats scene) ----------

    // On touch screens fields are livelier: bigger finger radius, deeper breathing, and a
    // wandering wind so they keep moving without a hovering cursor.
    function tuned(o) {
        if (finePointer) return o;
        o.autoWander = true;
        o.breathe = 3;
        o.pushRadius = (o.pushRadius || 110) * 1.5;
        return o;
    }

    function heroField() {
        var hero = document.querySelector('[data-hero-field]');
        if (!hero || !window.GrainField) return null;
        var canvas = hero.querySelector('canvas');
        var anchor = hero.querySelector('[data-ring-anchor]');
        if (!anchor) {
            var drift = new GrainField(canvas, tuned({ pointerTarget: hero, density: finePointer ? 0.0007 : 0.0016, max: 1100, pushRadius: 140 }));
            drift.setShapes([GrainShapes.field(), GrainShapes.fall()]);
            return { el: hero, field: drift };
        }
        var field = new GrainField(canvas, tuned({ pointerTarget: hero, density: finePointer ? 0.0024 : 0.0034, max: 2800 }));
        field.setShapes([
            GrainShapes.ring(function (w, h) {
                var c = canvas.getBoundingClientRect(), a = anchor.getBoundingClientRect();
                var R = w < 760
                    ? Math.min(a.width * 0.58, w * 0.4)
                    : Math.min(Math.max(a.width * 0.62, 120), Math.min(w, h) * 0.42);
                return { cx: a.left - c.left + a.width / 2, cy: a.top - c.top + a.height / 2, R: R };
            }),
            GrainShapes.fall()
        ]);
        return { el: hero, field: field };
    }

    function sceneField() {
        var scene = document.querySelector('[data-formats-scene]');
        if (!scene || !window.GrainField) return null;
        var canvas = scene.querySelector('canvas');
        var field = new GrainField(canvas, tuned({ pointerTarget: scene, density: finePointer ? 0.0016 : 0.0026, max: 2000, pushRadius: 90 }));
        var narrow = function (w) { return w < 760; };
        field.setShapes([
            GrainShapes.field(),
            function (n, w, h) {
                return GrainShapes.disc(narrow(w) ? 0.5 : 0.68, 0.5, narrow(w) ? 0.34 : 0.26)(n, w, h);
            },
            function (n, w, h) {
                return narrow(w)
                    ? GrainShapes.pair(0.22, 0.5, 0.26)(n, w, h)
                    : function (n2, w2, h2) {
                        var pts = GrainShapes.pair(0.12, 0.5, 0.22)(n2, w2, h2);
                        for (var i = 0; i < pts.length; i++) pts[i].x += w2 * 0.18;
                        return pts;
                    }(n, w, h);
            }
        ]);
        return { el: scene, field: field };
    }

    function grainNumbers() {
        if (!window.GrainField) return [];
        return Array.prototype.map.call(document.querySelectorAll('[data-grain-number]'), function (box) {
            var field = new GrainField(box.querySelector('canvas'), tuned({ pointerTarget: box, density: 0.02, max: 1800, pushRadius: 50 }));
            field.setShapes([GrainShapes.field(), GrainShapes.text(box.getAttribute('data-grain-number'), '"Source Serif 4", Georgia, serif')]);
            return { el: box, field: field };
        });
    }

    // Need-area cards: each runs its own grain motion (swirl, rise, bloom or wave).
    function cardFields() {
        if (!window.GrainField) return [];
        return Array.prototype.map.call(document.querySelectorAll('[data-grain-card]'), function (box) {
            var field = new GrainField(box.querySelector('canvas'), tuned({
                pointerTarget: box.closest('.card') || box, flow: box.getAttribute('data-grain-card') || 'swirl',
                palette: ['#E0CDB2', '#CDB08A', '#B48C61', '#9C6E45', '#8E5A32'],
                density: 0.006, min: 260, max: 900, pushRadius: 60
            }));
            field.options.autoWander = false;
            return { el: box, field: field };
        });
    }

    // How it's made: loose grains on dark navy gather into one body as the section arrives.
    function madeField() {
        var box = document.querySelector('[data-made-field]');
        if (!box || !window.GrainField) return null;
        var field = new GrainField(box.querySelector('canvas'), tuned({
            pointerTarget: box, palette: ['#E0CDB2', '#CDB08A', '#B48C61', '#9C6E45', '#8E5A32'],
            density: finePointer ? 0.0018 : 0.0026, max: 2200, pushRadius: 120
        }));
        field.setShapes([GrainShapes.field(), function (n, w, h) {
            return GrainShapes.disc(0.5, 0.5, w < 760 ? 0.62 : 0.5)(n, w, h);
        }]);
        return { el: box, field: field };
    }

    // Home hero: a turning sphere of grains around the calligraphy.
    function sphereField() {
        var box = document.querySelector('[data-grain-sphere]');
        if (!box || !window.GrainSphere) return null;
        return { el: box, field: new GrainSphere(box.querySelector('canvas'), { pointerTarget: box, count: finePointer ? 1100 : 800 }) };
    }

    // Our standard: loose grains settle into an even, aligned grid.
    function measureField() {
        var box = document.querySelector('[data-measure-field]');
        if (!box || !window.GrainField) return null;
        var field = new GrainField(box.querySelector('canvas'), {
            pointerTarget: box, align: true, palette: ['#CDB08A', '#B48C61', '#9C6E45', '#8E5A32'],
            density: 0.0016, min: 160, max: 330, pushRadius: 50, breathe: 0.6
        });
        field.setShapes([GrainShapes.field(), GrainShapes.grid(0.1)]);
        return { el: box, field: field };
    }

    var sphere = sphereField();
    var measure = measureField();
    var hero = heroField();
    var scene = sceneField();
    var numbers = grainNumbers();
    var cards = cardFields();
    var made = madeField();

    if (reduce || !hasGsap) {
        if (hero) { hero.field.progress = 0; reduce ? hero.field.still() : hero.field.start(); }
        if (scene) { scene.field.progress = 1; scene.field.still(); }
        numbers.forEach(function (n) { n.field.progress = 1; n.field.still(); n.el.classList.add('is-drawn'); });
        cards.forEach(function (c) { reduce ? c.field.still() : c.field.start(); });
        if (sphere) { reduce ? sphere.field.draw() : sphere.field.start(); }
        if (measure) { measure.field.progress = 1; reduce ? measure.field.still() : measure.field.start(); }
        if (made) { made.field.progress = 1; reduce ? made.field.still() : made.field.start(); }
        return;
    }

    var gsap = window.gsap;
    gsap.registerPlugin(ScrollTrigger);
    root.classList.add('has-gsap');

    // ---------- Smooth scroll ----------

    var lenis = null;
    if (window.Lenis) {
        lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
        gsap.ticker.lagSmoothing(0);
        document.querySelectorAll('a[href^="#"], a[href^="/#"]').forEach(function (a) {
            a.addEventListener('click', function (e) {
                var id = a.getAttribute('href').split('#')[1];
                var target = id && document.getElementById(id);
                if (!target || (a.pathname !== location.pathname && a.getAttribute('href').charAt(0) === '/')) return;
                e.preventDefault();
                lenis.scrollTo(target, { offset: -80 });
            });
        });
    }

    // ---------- Page curtain ----------

    var curtain = document.createElement('div');
    curtain.className = 'curtain';
    curtain.setAttribute('aria-hidden', 'true');
    curtain.innerHTML = '<img src="/assets/images/logo-full.png?v=3" alt="" width="56" height="56">';
    document.body.appendChild(curtain);
    // Arriving from another page of the site: the head script has already covered the page.
    if (root.classList.contains('curtain-in')) {
        gsap.set(curtain, { yPercent: 0 });
        root.classList.remove('curtain-in');
        gsap.to(curtain, { yPercent: -100, duration: 0.75, ease: 'expo.inOut', delay: 0.05 });
    } else {
        gsap.set(curtain, { yPercent: 100 });
    }

    document.addEventListener('click', function (e) {
        var a = e.target.closest('a');
        if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
        if (a.target && a.target !== '_self') return;
        if (a.origin !== location.origin || a.hash && a.pathname === location.pathname) return;
        if (/\.(pdf|png|jpg)$/i.test(a.pathname) || a.protocol === 'mailto:') return;
        e.preventDefault();
        try { sessionStorage.setItem('obi-curtain', '1'); } catch (err) { /* storage blocked: no intro curtain */ }
        gsap.fromTo(curtain, { yPercent: 100 }, {
            yPercent: 0, duration: 0.55, ease: 'expo.inOut',
            onComplete: function () { location.href = a.href; }
        });
    });
    // Coming back through history restores the page from cache with the curtain down.
    window.addEventListener('pageshow', function (e) {
        if (e.persisted) gsap.set(curtain, { yPercent: 100 });
    });

    // ---------- Headings rise word by word ----------

    function splitWords(el) {
        if (el.dataset.split) return;
        el.dataset.split = '1';
        var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
        var nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        nodes.forEach(function (node) {
            var frag = document.createDocumentFragment();
            node.textContent.split(/(\s+)/).forEach(function (part) {
                if (!part) return;
                if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
                var outer = document.createElement('span');
                outer.className = 'w';
                var inner = document.createElement('span');
                inner.className = 'wi';
                inner.textContent = part;
                outer.appendChild(inner);
                frag.appendChild(outer);
            });
            node.parentNode.replaceChild(frag, node);
        });
    }

    document.querySelectorAll('main h1, main h2:not(.visually-hidden):not(.notice-title)').forEach(function (h) {
        splitWords(h);
        var words = h.querySelectorAll('.wi');
        gsap.from(words, {
            yPercent: 105, duration: 1.1, ease: 'expo.out', stagger: 0.03,
            delay: h.tagName === 'H1' ? 0.35 : 0,
            scrollTrigger: h.tagName === 'H1' ? null : { trigger: h, start: 'top 88%', once: true }
        });
    });

    // ---------- Hero: ring of grains that scatters as you scroll ----------

    if (hero) {
        hero.field.start();
        ScrollTrigger.create({
            trigger: hero.el, start: 'top top', end: 'bottom top', scrub: true,
            onUpdate: function (st) { hero.field.progress = st.progress; }
        });
        if (hero.el.querySelector('.hero-copy')) gsap.to(hero.el.querySelector('.hero-copy'), {
            yPercent: -18, opacity: 0.2, ease: 'none',
            scrollTrigger: { trigger: hero.el, start: 'top top', end: 'bottom top', scrub: true }
        });
        if (hero.el.querySelector('.hero-mark')) gsap.from('.hero-mark', { opacity: 0, scale: 0.85, duration: 1.4, delay: 0.7, ease: 'expo.out' });
        gsap.from('.hero .lede, .hero .actions, .hero .eyebrow', {
            y: 24, opacity: 0, duration: 1, delay: 0.9, stagger: 0.12, ease: 'expo.out'
        });
    }

    // ---------- Scroll-scrubbed statement: words light up as you read ----------

    document.querySelectorAll('[data-scrub-text]').forEach(function (el) {
        splitWords(el);
        gsap.fromTo(el.querySelectorAll('.wi'), { opacity: 0.14 }, {
            opacity: 1, ease: 'none', stagger: 0.08,
            scrollTrigger: { trigger: el, start: 'top 80%', end: 'bottom 45%', scrub: true }
        });
    });

    // ---------- Formats scene: grains gather into one base, then two formats ----------

    if (scene) {
        scene.field.start();
        var steps = scene.el.querySelectorAll('[data-step]');
        root.classList.add('scene-ready');
        var current = -1;
        function showStep(i) {
            if (i === current) return;
            current = i;
            steps.forEach(function (s, k) { s.classList.toggle('is-active', k === i); });
        }
        showStep(0);
        ScrollTrigger.create({
            trigger: scene.el, start: 'top top', end: '+=220%', pin: scene.el.querySelector('.scene-pin'),
            scrub: 0.6, anticipatePin: 1,
            onUpdate: function (st) {
                var p = st.progress * 2.4 - 0.2;
                scene.field.progress = Math.max(0, Math.min(2, p));
                showStep(p < 0.6 ? 0 : p < 1.5 ? 1 : 2);
                scene.el.style.setProperty('--scene-progress', st.progress.toFixed(3));
            }
        });
    }

    // ---------- Grain numbers assemble as they scroll in ----------

    numbers.forEach(function (n) {
        n.el.classList.add('is-drawn');
        n.field.start();
        ScrollTrigger.create({
            trigger: n.el, start: 'top 85%', end: 'center 50%', scrub: 0.8,
            onUpdate: function (st) { n.field.progress = st.progress; }
        });
    });

    // ---------- Product cards and the made section ----------

    cards.forEach(function (c) { c.field.start(); });
    if (made) {
        made.field.start();
        ScrollTrigger.create({
            trigger: made.el, start: 'top 85%', end: 'center 50%', scrub: 0.8,
            onUpdate: function (st) { made.field.progress = st.progress; }
        });
        gsap.fromTo(made.el.querySelector('.made-copy'), { scale: 0.92, opacity: 0 }, {
            scale: 1, opacity: 1, ease: 'none',
            scrollTrigger: { trigger: made.el, start: 'top 75%', end: 'center 55%', scrub: true }
        });
    }

    // ---------- Home hero: the sphere turns, and scatters as the page scrolls on ----------

    if (sphere) {
        sphere.field.start();
        var homeHero = sphere.el.closest('.hero-home');
        ScrollTrigger.create({
            trigger: homeHero, start: 'top top', end: 'bottom top', scrub: 0.6,
            onUpdate: function (st) { sphere.field.scatter = st.progress; }
        });
        gsap.fromTo(sphere.el, { opacity: 0, scale: 0.9 }, { opacity: 1, scale: 1, duration: 1.6, ease: 'expo.out', delay: 0.2 });
        gsap.from('.hero-home .lede, .hero-home .actions, .hero-home .eyebrow', {
            y: 18, opacity: 0, duration: 1, delay: 0.6, stagger: 0.1, ease: 'expo.out'
        });
    }

    // ---------- Hairlines draw across as their columns arrive ----------

    gsap.utils.toArray('.rule-grid').forEach(function (grid) {
        gsap.fromTo(grid.querySelectorAll('.rule-col'), { '--rule': 0, y: 24, opacity: 0 }, {
            '--rule': 1, y: 0, opacity: 1, duration: 1.2, ease: 'expo.out', stagger: 0.15,
            scrollTrigger: { trigger: grid, start: 'top 85%', once: true }
        });
    });

    gsap.utils.toArray('.index-links').forEach(function (list) {
        gsap.fromTo(list.querySelectorAll('li'), { y: 30, opacity: 0 }, {
            y: 0, opacity: 1, duration: 1, ease: 'expo.out', stagger: 0.1,
            scrollTrigger: { trigger: list, start: 'top 88%', once: true }
        });
    });

    // ---------- What we're building: a pinned horizontal track on wide screens ----------

    document.querySelectorAll('[data-track]').forEach(function (section) {
        var viewport = section.querySelector('.track-viewport');
        var track = section.querySelector('.track');
        var bar = section.querySelector('.track-progress span');
        var mm = gsap.matchMedia();
        mm.add('(min-width: 900px)', function () {
            section.classList.add('is-pinned');
            var distance = function () { return Math.max(0, track.scrollWidth - viewport.clientWidth); };
            gsap.to(track, {
                x: function () { return -distance(); }, ease: 'none',
                scrollTrigger: {
                    trigger: section, start: 'top top', end: function () { return '+=' + distance(); },
                    pin: section.querySelector('.track-pin'), scrub: 0.8, anticipatePin: 1, invalidateOnRefresh: true,
                    onUpdate: function (st) { if (bar) bar.style.transform = 'scaleX(' + st.progress.toFixed(3) + ')'; }
                }
            });
            return function () { section.classList.remove('is-pinned'); };
        });
        mm.add('(max-width: 899px)', function () {
            var onScroll = function () {
                var max = viewport.scrollWidth - viewport.clientWidth;
                if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? viewport.scrollLeft / max : 0).toFixed(3) + ')';
            };
            viewport.addEventListener('scroll', onScroll, { passive: true });
            onScroll();
            return function () { viewport.removeEventListener('scroll', onScroll); };
        });
    });

    // ---------- Our standard: grains settle into a measured grid ----------

    if (measure) {
        measure.field.start();
        ScrollTrigger.create({
            trigger: measure.el, start: 'top 85%', end: 'center 50%', scrub: 0.8,
            onUpdate: function (st) { measure.field.progress = st.progress; }
        });
    }

    // ---------- Platform flow: connectors draw and steps light in order ----------

    document.querySelectorAll('.flow').forEach(function (flow) {
        var steps = flow.querySelectorAll('.flow-step');
        var tl = gsap.timeline({ scrollTrigger: { trigger: flow, start: 'top 75%', end: 'bottom 55%', scrub: 0.6 } });
        steps.forEach(function (step, i) {
            tl.fromTo(step, { opacity: 0.25, y: 20 }, { opacity: 1, y: 0, duration: 1 }, i * 1.2);
            tl.fromTo(step.querySelector('.icon'), { scale: 0.6 }, { scale: 1, duration: 0.8, ease: 'back.out(2)' }, i * 1.2);
            if (i < steps.length - 1) tl.fromTo(step, { '--connector': 0 }, { '--connector': 1, duration: 1.2 }, i * 1.2 + 0.4);
        });
    });

    // ---------- Roadmap: the line grows with the reader, stages light as it passes ----------

    document.querySelectorAll('.timeline:not(.timeline--mini)').forEach(function (tl) {
        var current = tl.querySelector('.is-current');
        var full = current ? current.offsetTop + 8 : tl.offsetHeight;
        gsap.fromTo(tl, { '--fill': '0px' }, {
            '--fill': full + 'px', ease: 'none',
            scrollTrigger: { trigger: tl, start: 'top 70%', end: function () { return '+=' + full; }, scrub: true }
        });
        tl.querySelectorAll('li').forEach(function (li) {
            ScrollTrigger.create({
                trigger: li, start: 'top 72%',
                onEnter: function () { li.classList.add('is-lit'); },
                onLeaveBack: function () { li.classList.remove('is-lit'); }
            });
        });
    });

    // ---------- Cards and advisors fall into place in batches ----------

    ScrollTrigger.batch('.card, .advisor, .team-facts > div, .flow-step .icon, .need-card', {
        start: 'top 88%', once: true,
        onEnter: function (batch) {
            // fromTo with explicit end values: a repeated trigger can never leave cards hidden.
            gsap.fromTo(batch, { y: 36, opacity: 0 },
                { y: 0, opacity: 1, duration: 1.1, ease: 'expo.out', stagger: 0.08, overwrite: 'auto' });
        }
    });

    // ---------- Facts and leave tables: rows slide in ----------

    gsap.utils.toArray('.facts').forEach(function (table) {
        gsap.fromTo(table.querySelectorAll('tr'), { x: -24, opacity: 0 }, {
            x: 0, opacity: 1, duration: 0.6, ease: 'power3.out', stagger: 0.06,
            scrollTrigger: { trigger: table, start: 'top 85%', once: true }
        });
    });

    // ---------- Checklists tick themselves ----------

    gsap.utils.toArray('.checklist').forEach(function (list) {
        ScrollTrigger.create({
            trigger: list, start: 'top 80%', once: true,
            onEnter: function () {
                list.querySelectorAll('li').forEach(function (li, i) {
                    setTimeout(function () { li.classList.add('is-ticked'); }, i * 220);
                });
            }
        });
    });

    // ---------- Parallax on large figures and statements ----------

    gsap.utils.toArray('.figure-stat .value, .statement').forEach(function (el) {
        gsap.fromTo(el, { y: 30 }, {
            y: -30, ease: 'none',
            scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: true }
        });
    });

    // ---------- Header hides on the way down, returns on the way up ----------

    var header = document.querySelector('.site-header');
    if (header) {
        ScrollTrigger.create({
            start: 120, end: 'max',
            onUpdate: function (st) { header.classList.toggle('is-hidden', st.direction === 1); }
        });
    }
})();
