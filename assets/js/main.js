/* ── Main JS – Oxygen Bioinnovations v2 ──────────────────── */

// ── Cursor Glow (desktop only) ────────────────────────────
const glow = document.createElement('div');
glow.classList.add('cursor-glow');
document.body.appendChild(glow);

let glowActive = false;
document.addEventListener('mousemove', (e) => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
    const darkEl = e.target.closest('.hero-dark, .problem-section, .science-section, .cta-section, #footer');
    if (darkEl && !glowActive) {
        glow.style.opacity = '1';
        glowActive = true;
    } else if (!darkEl && glowActive) {
        glow.style.opacity = '0';
        glowActive = false;
    }
});

// ── Navigation ────────────────────────────────────────────
const header = document.getElementById('header');

function updateNav() {
    if (!header) return;
    const scrolled = window.scrollY > 40;

    // Determine if over dark background
    const heroEl = document.querySelector('.hero-dark');
    const onDark = heroEl && window.scrollY < heroEl.offsetHeight - header.offsetHeight;

    header.classList.toggle('scrolled', scrolled);
    header.classList.toggle('on-dark', !!onDark);
}

updateNav();
window.addEventListener('scroll', updateNav, { passive: true });

// ── Mobile Menu ───────────────────────────────────────────
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileOverlay = document.getElementById('mobileOverlay');
const mobileClose = document.getElementById('mobileClose');

function openMenu() {
    mobileMenu?.classList.add('open');
    mobileOverlay?.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeMenu() {
    mobileMenu?.classList.remove('open');
    mobileOverlay?.classList.remove('open');
    document.body.style.overflow = '';
}

menuBtn?.addEventListener('click', openMenu);
mobileClose?.addEventListener('click', closeMenu);
mobileOverlay?.addEventListener('click', closeMenu);

// Close on link click
mobileMenu?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));

// ── Scroll Reveal ─────────────────────────────────────────
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });

document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => {
    revealObserver.observe(el);
});

// ── Counter Animations ────────────────────────────────────
function animateCounter(el) {
    const target = parseFloat(el.dataset.target);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const duration = 2000;
    const decimals = String(target).includes('.') ? String(target).split('.')[1].length : 0;
    const startTime = performance.now();

    function step(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Ease out expo
        const eased = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        const current = (target * eased).toFixed(decimals);
        el.textContent = prefix + current + suffix;
        if (progress < 1) requestAnimationFrame(step);
    }

    requestAnimationFrame(step);
}

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('[data-target]').forEach(el => counterObserver.observe(el));

// ── Comparison Bars (animate on scroll) ───────────────────
const barObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.querySelectorAll('.compare-fill').forEach(bar => {
                bar.style.width = bar.dataset.width || '0%';
            });
            barObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.3 });

document.querySelectorAll('.science-compare').forEach(el => barObserver.observe(el));

// ── Roadmap Drag-to-Scroll ────────────────────────────────
const roadmapScroll = document.querySelector('.roadmap-scroll');
if (roadmapScroll) {
    let isDown = false, startX, scrollLeft;

    roadmapScroll.addEventListener('mousedown', e => {
        isDown = true;
        roadmapScroll.style.cursor = 'grabbing';
        startX = e.pageX - roadmapScroll.offsetLeft;
        scrollLeft = roadmapScroll.scrollLeft;
    });

    roadmapScroll.addEventListener('mouseleave', () => {
        isDown = false;
        roadmapScroll.style.cursor = 'grab';
    });

    roadmapScroll.addEventListener('mouseup', () => {
        isDown = false;
        roadmapScroll.style.cursor = 'grab';
    });

    roadmapScroll.addEventListener('mousemove', e => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - roadmapScroll.offsetLeft;
        roadmapScroll.scrollLeft = scrollLeft - (x - startX) * 1.5;
    });
}

// ── Footer Year ───────────────────────────────────────────
document.querySelectorAll('#year').forEach(el => {
    el.textContent = new Date().getFullYear();
});

// ── Mobile Sticky CTA (hide/show on scroll) ───────────────
const mobileCta = document.getElementById('mobileCta');
if (mobileCta) {
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const current = window.scrollY;
        if (current > 300) {
            mobileCta.style.opacity = '1';
            mobileCta.style.transform = 'translateX(-50%) translateY(0)';
        } else {
            mobileCta.style.opacity = '0';
            mobileCta.style.transform = 'translateX(-50%) translateY(20px)';
        }
        lastScroll = current;
    }, { passive: true });
}