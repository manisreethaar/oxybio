document.addEventListener("DOMContentLoaded", () => {
            // 1. Dynamic Year
            document.getElementById('year').textContent = new Date().getFullYear();

            // 2. Mobile Menu Logic
            const menuBtn = document.getElementById('menuBtn');
            const mobileMenu = document.getElementById('mobileMenu');
            const mobileOverlay = document.getElementById('mobileOverlay');
            const menuLinks = document.querySelectorAll('.menu-link');

            const toggleMenu = () => {
                menuBtn.classList.toggle('open');
                mobileMenu.classList.toggle('open');
                mobileOverlay.classList.toggle('open');
                document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
            };

            menuBtn.addEventListener('click', toggleMenu);
            mobileOverlay.addEventListener('click', toggleMenu);
            menuLinks.forEach(link => {
                link.addEventListener('click', toggleMenu);
            });

            // 3. Scroll Interactions (Header background & Mobile Sticky CTA)
            const header = document.getElementById('header');
            const mobileCta = document.getElementById('mobileCta');
            const footer = document.getElementById('footer');

            window.addEventListener('scroll', () => {
                // Sticky Header styling
                if (window.scrollY > 50) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }

                // Mobile CTA Show/Hide (Hide when near footer)
                if (window.innerWidth < 768) {
                    const footerRect = footer.getBoundingClientRect();
                    const viewHeight = window.innerHeight;

                    // Show past hero, hide near footer
                    if (window.scrollY > 400 && footerRect.top > viewHeight) {
                        mobileCta.classList.add('visible');
                    } else {
                        mobileCta.classList.remove('visible');
                    }
                }
            }, { passive: true });

            // 4. Intersection Observer for Fade-Up Animations
            const revealElements = document.querySelectorAll('.reveal');

            const revealSettings = {
                threshold: 0.15,
                rootMargin: "0px 0px -50px 0px"
            };

            const revealObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target); // Reveal only once
                    }
                });
            }, revealSettings);

            revealElements.forEach(el => revealObserver.observe(el));

            // 5. Stat Counter Animation
            const counters = document.querySelectorAll('.stat-number');

            const counterObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = entry.target;
                        const finalValue = parseInt(target.getAttribute('data-target'));
                        const duration = 2000;
                        const stepTime = Math.abs(Math.floor(duration / finalValue));
                        let current = 0;

                        const timer = setInterval(() => {
                            current += 1;
                            target.textContent = current;
                            if (current === finalValue) {
                                clearInterval(timer);
                            }
                        }, stepTime);

                        observer.unobserve(target);
                    }
                });
            }, { threshold: 0.5 });

            counters.forEach(counter => counterObserver.observe(counter));
        });