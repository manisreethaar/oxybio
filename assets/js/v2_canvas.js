/**
 * OXYGEN V2 - INTERACTIVE BIOLOGY MESH
 * Creates a reactive HTML5 canvas network of nodes that represent
 * precision biology systems. The nodes slowly drift and react
 * to the user's mouse movements.
 */

window.addEventListener('DOMContentLoaded', () => {
    initBiologyMesh();
});

function initBiologyMesh() {
    const canvas = document.getElementById('biology-mesh');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width, height;

    // Config
    const config = {
        particleCount: window.innerWidth > 768 ? 80 : 25, // Fewer on mobile
        baseRadius: 2,
        connectionDistance: window.innerWidth > 768 ? 150 : 80,
        mouseRepelRadius: 150,
        mouseRepelStrength: 0.05,
        speed: 0.3,
        color: 'rgba(0, 0, 0, 0.4)' // Deep Black for contrast
    };

    let particles = [];
    let mouse = { x: -1000, y: -1000 };

    function resize() {
        const parent = canvas.parentElement;
        width = parent.clientWidth;
        height = parent.clientHeight;
        canvas.width = width;
        canvas.height = height;
        initParticles();
    }

    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.vx = (Math.random() - 0.5) * config.speed;
            this.vy = (Math.random() - 0.5) * config.speed;
            this.baseX = this.x;
            this.baseY = this.y;
            this.radius = Math.random() * config.baseRadius + 1;
        }

        update() {
            // Mouse interaction (Repel)
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < config.mouseRepelRadius) {
                const force = (config.mouseRepelRadius - distance) / config.mouseRepelRadius;
                this.x -= (dx / distance) * force * config.mouseRepelStrength * 100;
                this.y -= (dy / distance) * force * config.mouseRepelStrength * 100;
            }

            // Normal drift
            this.x += this.vx;
            this.y += this.vy;

            // Bounce off edges smoothly
            if (this.x < 0 || this.x > width) this.vx *= -1;
            if (this.y < 0 || this.y > height) this.vy *= -1;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = config.color;
            ctx.fill();
        }
    }

    function initParticles() {
        particles = [];
        for (let i = 0; i < config.particleCount; i++) {
            particles.push(new Particle());
        }
    }

    function drawConnections() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distSq = dx * dx + dy * dy;

                if (distSq < config.connectionDistance * config.connectionDistance) {
                    const distance = Math.sqrt(distSq);
                    const opacity = 1 - (distance / config.connectionDistance);
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(0, 0, 0, ${opacity * 0.25})`; // Darker strokes
                    ctx.lineWidth = 1;
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }
    }

    let lastTime = 0;
    const interval = 1000 / 30; // 30fps

    function animate(timestamp) {
        rafId = requestAnimationFrame(animate);
        if (timestamp - lastTime < interval) return;
        lastTime = timestamp;

        ctx.clearRect(0, 0, width, height);

        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
        }

        drawConnections();
    }

    // Event Listeners
    window.addEventListener('resize', resize);

    // Only track mouse over the hero section
    const heroSection = canvas.closest('.structure-section');
    if (heroSection) {
        heroSection.addEventListener('mousemove', (e) => {
            const rect = heroSection.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
        });
        heroSection.addEventListener('mouseleave', () => {
            mouse.x = -1000;
            mouse.y = -1000;
        });
    }

    // Initialize
    resize();
    animate();
}
