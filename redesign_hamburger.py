"""
Replace the standard 3-line hamburger with a unique premium icon:
- A circular bordered button with two ASYMMETRIC lines (wide + narrow)
- On open: lines rotate to form a slim elegant X (45deg crossing)
- On hover: a circular ring animates outward (ripple)
- Pure CSS, no images, very lightweight
"""
import os
import re

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

# ─── Read CSS ───────────────────────────────────────────
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the entire .menu-btn and .menu-btn span blocks
OLD_BTN_CSS = """.menu-btn {
    display: none;
    flex-direction: column;
    gap: 5px;
    padding: 8px;
    background: none;
    border: none;
    cursor: pointer;
    color: var(--text-main);
}

.menu-btn span {
    display: block;
    width: 24px;
    height: 2px;
    background: currentColor;
    border-radius: 2px;
    transition: transform 0.3s, opacity 0.3s;
}"""

NEW_BTN_CSS = """.menu-btn {
    display: none;
    flex-direction: column;
    align-items: flex-end; /* right-align for asymmetric look */
    gap: 6px;
    width: 44px;
    height: 44px;
    padding: 10px;
    background: none;
    border: 1.5px solid var(--border);
    border-radius: 50%;
    cursor: pointer;
    color: var(--text-main);
    position: relative;
    transition: border-color 0.3s, transform 0.3s;
    justify-content: center;
}

/* Ripple ring on hover */
.menu-btn::after {
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    border: 1px solid var(--text-main);
    opacity: 0;
    transform: scale(0.85);
    transition: opacity 0.35s, transform 0.35s;
    pointer-events: none;
}

.menu-btn:hover {
    border-color: var(--text-main);
}

.menu-btn:hover::after {
    opacity: 0.2;
    transform: scale(1);
}

/* TWO asymmetric lines — top line longer, bottom line shorter */
.menu-btn span {
    display: block;
    height: 1.5px;
    background: currentColor;
    border-radius: 2px;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                opacity 0.3s,
                width 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.menu-btn span:nth-child(1) {
    width: 20px; /* long line */
}

.menu-btn span:nth-child(2) {
    width: 12px; /* short line — asymmetric premium touch */
}

.menu-btn span:nth-child(3) {
    display: none; /* hide 3rd line — we only need 2 */
}

/* OPEN STATE — morphs into a slim X */
.menu-btn.is-open span:nth-child(1) {
    width: 18px;
    transform: translateY(7.5px) rotate(45deg);
}

.menu-btn.is-open span:nth-child(2) {
    width: 18px; /* equalize for X symmetry */
    transform: translateY(-7.5px) rotate(-45deg);
}"""

if OLD_BTN_CSS in css:
    css = css.replace(OLD_BTN_CSS, NEW_BTN_CSS)
    print('[CSS] Menu button replaced with premium asymmetric icon')
else:
    # Try to find the blocks separately
    css = re.sub(
        r'\.menu-btn \{[^}]+\}',
        NEW_BTN_CSS.split('\n\n')[0] + '}',
        css,
        count=1
    )
    print('[CSS] Inserted new menu-btn styles (partial match)')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)

# ─── Update JS to toggle .is-open class ─────────────────────
JS_FILE = os.path.join(ROOT, 'assets', 'js', 'main.js')
with open(JS_FILE, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace openMenu / closeMenu to also toggle .is-open on the button
old_open = """function openMenu() {
    if(mobileMenu) mobileMenu.classList.add('open');
    if(mobileOverlay) mobileOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeMenu() {
    if(mobileMenu) mobileMenu.classList.remove('open');
    if(mobileOverlay) mobileOverlay.classList.remove('open');
    document.body.style.overflow = '';
}"""

new_open = """function openMenu() {
    if(mobileMenu) mobileMenu.classList.add('open');
    if(mobileOverlay) mobileOverlay.classList.add('open');
    if(menuBtn) menuBtn.classList.add('is-open');
    document.body.style.overflow = 'hidden';
}

function closeMenu() {
    if(mobileMenu) mobileMenu.classList.remove('open');
    if(mobileOverlay) mobileOverlay.classList.remove('open');
    if(menuBtn) menuBtn.classList.remove('is-open');
    document.body.style.overflow = '';
}"""

if old_open in js:
    js = js.replace(old_open, new_open)
    print('[JS]  Added .is-open toggle to open/closeMenu functions')
else:
    print('[JS]  Could not find exact function text — check main.js manually')

with open(JS_FILE, 'w', encoding='utf-8') as f:
    f.write(js)

# ─── Cache bust to v32 ───────────────────────────────────
all_pages = [f for f in os.listdir(ROOT) if f.endswith('.html')]
for page in all_pages:
    path = os.path.join(ROOT, page)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'\?v=\d+"', '?v=32"', html)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f'[CACHE] All {len(all_pages)} pages bumped to v32')
print('[DONE] Unique hamburger icon deployed!')
