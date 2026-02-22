
/* -- Main JS – Oxygen Bioinnovations v3 (Monochrome) -------- */

// -- Navigation --------------------------------------------
const header = document.getElementById('header');

function updateNav() {
    if (!header) return;
    const scrolled = window.scrollY > 40;
    header.classList.toggle('scrolled', scrolled);
}

updateNav();
window.addEventListener('scroll', updateNav, { passive: true });

// -- Mobile Menu -------------------------------------------
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileOverlay = document.getElementById('mobileOverlay');
const mobileClose = document.getElementById('mobileClose');

function openMenu() {
    if(mobileMenu) mobileMenu.classList.add('open');
    if(mobileOverlay) mobileOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeMenu() {
    if(mobileMenu) mobileMenu.classList.remove('open');
    if(mobileOverlay) mobileOverlay.classList.remove('open');
    document.body.style.overflow = '';
}

if(menuBtn) menuBtn.addEventListener('click', openMenu);
if(mobileClose) mobileClose.addEventListener('click', closeMenu);
if(mobileOverlay) mobileOverlay.addEventListener('click', closeMenu);

// Close on link click
if(mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
}

// -- Scroll Reveal -----------------------------------------
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

// -- Counter Animations ------------------------------------
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
            const el = entry.target;
            animateCounter(el);
            counterObserver.unobserve(el);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('[data-target]').forEach(el => {
    counterObserver.observe(el);
});

// -- Roadmap Horizontal Drag Scroll --------------------------
const roadmap = document.querySelector('.roadmap-scroll');
let isDown = false;
let startX;
let scrollLeft;

if (roadmap) {
    roadmap.addEventListener('mousedown', (e) => {
        isDown = true;
        roadmap.classList.add('active');
        startX = e.pageX - roadmap.offsetLeft;
        scrollLeft = roadmap.scrollLeft;
    });
    
    roadmap.addEventListener('mouseleave', () => {
        isDown = false;
        roadmap.classList.remove('active');
    });
    
    roadmap.addEventListener('mouseup', () => {
        isDown = false;
        roadmap.classList.remove('active');
    });
    
    roadmap.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - roadmap.offsetLeft;
        const walk = (x - startX) * 2; 
        roadmap.scrollLeft = scrollLeft - walk;
    });
}

// -- Footer Year -------------------------------------------
const yearEl = document.getElementById('year');
if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
}

// -- Mobile Sticky CTA -------------------------------------
const mobileCta = document.getElementById('mobileCta');
const joinSection = document.getElementById('join');

if (mobileCta && joinSection) {
    window.addEventListener('scroll', () => {
        if (window.innerWidth > 768) {
            mobileCta.style.display = 'none';
            return;
        }

        const joinRect = joinSection.getBoundingClientRect();
        if (window.scrollY > 300 && joinRect.top > window.innerHeight) {
            mobileCta.style.display = 'block';
        } else {
            mobileCta.style.display = 'none';
        }
    }, { passive: true });
}

