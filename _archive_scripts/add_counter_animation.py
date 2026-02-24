import os
import glob

animation_script = """
<!-- Premium Number Counter Animation -->
<script>
document.addEventListener('DOMContentLoaded', () => {
    const animateValue = (obj, start, end, duration) => {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            // Ease out cubic
            const easeOut = 1 - Math.pow(1 - progress, 3);
            obj.innerHTML = Math.floor(easeOut * (end - start) + start);
            if (obj.dataset.suffix) obj.innerHTML += obj.dataset.suffix;
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    };

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const endVal = parseInt(target.dataset.target, 10);
                if (!isNaN(endVal)) {
                    animateValue(target, 0, endVal, 2000);
                }
                obs.unobserve(target); // Only animate once
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.count-up').forEach(el => observer.observe(el));
});
</script>
</body>
"""

# 1. Update about.html
file_path = 'e:\\OXYBIO\\about.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace static numbers with count-up spans
html = html.replace('14 Months</div>', '<span class="count-up" data-target="14" data-suffix=" Months">0</span></div>')
html = html.replace('200+ Studies</div>', '<span class="count-up" data-target="200" data-suffix="+ Studies">0</span></div>')

if 'Premium Number Counter Animation' not in html:
    html = html.replace('</body>', animation_script)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected count-up animation into about.html")
