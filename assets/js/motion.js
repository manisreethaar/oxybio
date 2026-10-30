// Motion layer: smooth scroll, page curtain, word-by-word headings, scroll scenes, magnetic
// buttons, cursor and tilt. Everything here is progressive: without GSAP, without a fine
// pointer, or under reduced motion, the page stays fully readable and static.
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

    // Product cards: a stirred swirl for the creamy drink, rising bubbles for the sparkling one.
    function cardFields() {
        if (!window.GrainField) return [];
        return Array.prototype.map.call(document.querySelectorAll('[data-grain-card]'), function (box) {
            var field = new GrainField(box.querySelector('canvas'), tuned({
                pointerTarget: box.closest('.card') || box, flow: box.getAttribute('data-grain-card') === 'rise' ? 'rise' : 'swirl',
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
            pointerTarget: box, palette: ['#24477F', '#2E5591', '#3A64A6', '#4F74BF', '#7F9DD0'],
            density: finePointer ? 0.0018 : 0.0026, max: 2200, pushRadius: 120
        }));
        field.setShapes([GrainShapes.field(), function (n, w, h) {
            return GrainShapes.disc(0.5, 0.5, w < 760 ? 0.62 : 0.5)(n, w, h);
        }]);
        return { el: box, field: field };
    }

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
    curtain.innerHTML = '<img src="/assets/images/logo-full.png?v=2" alt="" width="56" height="56">';
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
            yPercent: 115, rotate: 4, duration: 0.9, ease: 'expo.out', stagger: 0.045,
            delay: h.tagName === 'H1' ? 0.55 : 0,
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

    ScrollTrigger.batch('.card, .advisor, .team-facts > div, .flow-step .icon', {
        start: 'top 88%', once: true,
        onEnter: function (batch) {
            // fromTo with explicit end values: a repeated trigger can never leave cards hidden.
            if (!finePointer) {
                gsap.fromTo(batch,
                    { x: function (i) { return i % 2 ? 90 : -90; }, rotate: function (i) { return i % 2 ? 6 : -6; }, scale: 0.86, opacity: 0 },
                    { x: 0, rotate: 0, scale: 1, opacity: 1, duration: 1.1, ease: 'expo.out', stagger: 0.12, overwrite: 'auto' });
                return;
            }
            gsap.fromTo(batch,
                { rotateX: -18, y: 40, opacity: 0, transformPerspective: 900, transformOrigin: '50% 0%' },
                { rotateX: 0, y: 0, opacity: 1, duration: 0.9, ease: 'expo.out', stagger: 0.08, overwrite: 'auto' });
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

    // ---------- Touch screens: the hero opens with a burst ----------

    if (!finePointer) {
        // Hero grains burst once as the page opens, so the field arrives with energy.
        if (hero) {
            setTimeout(function () {
                hero.field.burst(hero.field.width / 2, hero.field.height * 0.65, 40);
            }, 900);
        }
    }

    // ---------- Buttons ripple where they are pressed ----------

    document.querySelectorAll('.btn').forEach(function (btn) {
        btn.addEventListener('pointerdown', function (e) {
            var r = btn.getBoundingClientRect();
            var dot = document.createElement('span');
            dot.className = 'ripple';
            dot.style.left = e.clientX - r.left + 'px';
            dot.style.top = e.clientY - r.top + 'px';
            btn.appendChild(dot);
            gsap.fromTo(dot, { scale: 0, opacity: 0.45 }, {
                scale: Math.max(r.width, r.height) / 6, opacity: 0, duration: 0.7, ease: 'power2.out',
                onComplete: function () { dot.remove(); }
            });
        });
    });

    // ---------- Pointer-only flourishes ----------

    if (!finePointer) return;

    // Magnetic buttons drift toward the cursor.
    document.querySelectorAll('.btn').forEach(function (btn) {
        var xTo = gsap.quickTo(btn, 'x', { duration: 0.5, ease: 'elastic.out(1, 0.4)' });
        var yTo = gsap.quickTo(btn, 'y', { duration: 0.5, ease: 'elastic.out(1, 0.4)' });
        btn.addEventListener('pointermove', function (e) {
            var r = btn.getBoundingClientRect();
            xTo((e.clientX - r.left - r.width / 2) * 0.3);
            yTo((e.clientY - r.top - r.height / 2) * 0.45);
        });
        btn.addEventListener('pointerleave', function () { xTo(0); yTo(0); });
    });

    // Cards tilt slightly toward the cursor.
    document.querySelectorAll('.card, .advisor').forEach(function (card) {
        card.addEventListener('pointermove', function (e) {
            var r = card.getBoundingClientRect();
            var px = (e.clientX - r.left) / r.width - 0.5, py = (e.clientY - r.top) / r.height - 0.5;
            gsap.to(card, { rotateY: px * 6, rotateX: -py * 6, transformPerspective: 800, duration: 0.4, ease: 'power2.out' });
            card.style.setProperty('--gx', (px + 0.5) * 100 + '%');
            card.style.setProperty('--gy', (py + 0.5) * 100 + '%');
        });
        card.addEventListener('pointerleave', function () {
            gsap.to(card, { rotateY: 0, rotateX: 0, duration: 0.6, ease: 'power3.out' });
        });
    });

    // Cursor: a small dot with a trailing ring that grows over interactive elements.
    var dot = document.createElement('div');
    var ring = document.createElement('div');
    dot.className = 'cursor-dot';
    ring.className = 'cursor-ring';
    dot.setAttribute('aria-hidden', 'true');
    ring.setAttribute('aria-hidden', 'true');
    document.body.append(dot, ring);
    root.classList.add('has-cursor');
    var dx = gsap.quickTo(dot, 'x', { duration: 0.08 }), dy = gsap.quickTo(dot, 'y', { duration: 0.08 });
    var rx = gsap.quickTo(ring, 'x', { duration: 0.45, ease: 'power3.out' }), ry = gsap.quickTo(ring, 'y', { duration: 0.45, ease: 'power3.out' });
    window.addEventListener('pointermove', function (e) {
        dx(e.clientX); dy(e.clientY); rx(e.clientX); ry(e.clientY);
        var interactive = e.target.closest('a, button, summary, input, select, textarea, label');
        root.classList.toggle('cursor-active', !!interactive);
        root.classList.toggle('cursor-on-dark', !!e.target.closest('.hero--field, .scene, .section--navy, .site-footer'));
    });
    document.addEventListener('pointerleave', function () { root.classList.add('cursor-away'); });
    document.addEventListener('pointerenter', function () { root.classList.remove('cursor-away'); });
})();
