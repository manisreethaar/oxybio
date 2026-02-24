
/* -- Main JS  Oxygen Bioinnovations v3 (Monochrome) -------- */

// -- Navigation --------------------------------------------
const header = document.getElementById('header');

function updateNav() {
    if (!header) return;
    const scrolled = window.scrollY > 40;
    header.classList.toggle('scrolled', scrolled);
}

updateNav();
window.addEventListener('scroll', updateNav, { passive: true });

// -- Active Navigation Link Highlight -------------------------
document.addEventListener('DOMContentLoaded', () => {
    let currentPath = window.location.pathname.split('/').pop() || 'index.html';
    if (currentPath === '') currentPath = 'index.html';

    // Map sub-pages to their parent nav items
    const routeMap = {
        'problem.html': 'science.html',
        'ingredients.html': 'science.html',
        'blog-origin.html': 'blog.html',
        'blog-bootstrapping.html': 'blog.html',
        'blog-minerals.html': 'blog.html',
        'blog.html': 'blog.html',
        'about.html': 'about.html',
        'science.html': 'science.html',
        'careers.html': 'careers.html',
        'contact.html': 'contact.html',
        'index.html': 'index.html'
    };

    const targetUrl = routeMap[currentPath] || currentPath;

    // Desktop Nav
    const desktopLinks = document.querySelectorAll('.desktop-nav > a, .desktop-nav .nav-item > a');
    desktopLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === targetUrl) {
            link.classList.add('nav-active');
        }
    });

    // Mobile Menu
    const mobileLinks = document.querySelectorAll('.mobile-menu .menu-link');
    mobileLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === targetUrl) {
            link.classList.add('nav-active');
        }
    });
});

// -- Mobile Menu -------------------------------------------
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileOverlay = document.getElementById('mobileOverlay');
const mobileClose = document.getElementById('mobileClose');

function openMenu() {
    if (mobileMenu) mobileMenu.classList.add('open');
    if (mobileOverlay) mobileOverlay.classList.add('open');
    if (menuBtn) menuBtn.classList.add('is-open');
    document.body.style.overflow = 'hidden';
}

function closeMenu() {
    if (mobileMenu) mobileMenu.classList.remove('open');
    if (mobileOverlay) mobileOverlay.classList.remove('open');
    if (menuBtn) menuBtn.classList.remove('is-open');
    document.body.style.overflow = '';
}

if (menuBtn) menuBtn.addEventListener('click', openMenu);
if (mobileClose) mobileClose.addEventListener('click', closeMenu);
if (mobileOverlay) mobileOverlay.addEventListener('click', closeMenu);

// Close on link click
if (mobileMenu) {
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

document.querySelectorAll('[data-target]:not(.index-nav-item)').forEach(el => {
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



// ── Hash-based Tabbed Navigation ──────────────────────────
function handleHashTabs() {
    const hash = window.location.hash;
    const visionSec = document.getElementById('about-vision');
    const founderSec = document.getElementById('about-founder');

    // Only run if we are on the about page exactly
    if (!visionSec || !founderSec) return;

    // Reset both to hidden
    visionSec.style.display = 'none';
    founderSec.style.display = 'none';

    if (hash === '#about-founder') {
        founderSec.style.display = 'block';
        window.scrollTo(0, 0);

        // Re-initialize ScrollSpy when entering this tab
        setTimeout(initScrollSpy, 100);
    } else {
        // Default to vision if empty or #about-vision
        visionSec.style.display = 'block';
        window.scrollTo(0, 0);
    }
}

// Listen for hash changes from clicking the mega-menu
window.addEventListener('hashchange', handleHashTabs);

// Run on initial load
document.addEventListener('DOMContentLoaded', () => {
    handleHashTabs();
    initScrollSpy();
});


// ── ScrollSpy for About Us ────────────────────────────────
function initScrollSpy() {
    const chapters = document.querySelectorAll('.chapter-section');
    const navItems = document.querySelectorAll('.index-nav-item');

    if (chapters.length === 0 || navItems.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove active styling from all items
                navItems.forEach(item => {
                    item.style.color = 'var(--text-muted)';
                    item.style.fontWeight = '400';
                });

                // Find corresponding nav item
                const id = entry.target.getAttribute('id');
                const activeLink = document.querySelector(`.index-nav-item[data-target="${id}"]`);
                if (activeLink) {
                    activeLink.style.color = 'var(--text-main)';
                    activeLink.style.fontWeight = '600';
                }
            }
        });
    }, {
        rootMargin: '-20% 0px -60% 0px',
        threshold: 0.1
    });

    chapters.forEach(chapter => {
        observer.observe(chapter);
    });

    // Smooth scrolling for the index clicks
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            const targetId = item.getAttribute('data-target');
            const targetEl = document.getElementById(targetId);
            if (targetEl) {
                const headerOffset = 100;
                const elementPosition = targetEl.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });
}

