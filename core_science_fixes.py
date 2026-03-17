import re
import os

files = ['e:/OXYBIO/ingredients.html', 'e:/OXYBIO/science.html']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # ingredients.html specific fixes
    if 'ingredients.html' in file_path:
        # Change definitive claims to research goals
        content = content.replace('Sprouted and micro-milled to reduce phytic acid by 60%, unlocking India\'s most calcium-dense', 'We are testing sprouting and micro-milling protocols aiming to reduce phytic acid, unlocking India\'s most calcium-dense')
        content = content.replace('forgotten grain without the anti-nutrients.', 'grain without the associated anti-nutrients.')
        
        content = content.replace('Rich in natural iron and slowly digestible starch, preventing insulin spikes while building foundational energy.', 'Sourced for its natural iron and slowly digestible starch; our formulation models aim to prevent insulin spikes and build foundational energy reservoirs.')
        
        content = content.replace('Dual-extracted (hot water + ethanol) fruiting body. Contains hericenones and erinacines shown in studies to stimulate Nerve Growth Factor in the brain.', 'Evaluating dual-extracted (hot water + ethanol) fruiting bodies. We are standardizing for hericenones and erinacines, components shown in clinical literature to stimulate Nerve Growth Factor.')
        
        content = content.replace('Enhances cellular oxygen utilization and ATP production, delaying fatigue by working at the mitochondrial level.', 'Our targets require enhancing cellular oxygen utilization and ATP production. We are incorporating Cordyceps to test fatigue delay at the mitochondrial level.')
        
        content = content.replace('Heavy in triterpenes that modulate the immune system and promote deep, restorative calm without acting as a sedative.', 'We are testing extracts heavy in triterpenes to map immune system modulation and restorative calm without sedative effects.')
        
        content = content.replace('When paired with caffeine, it eliminates the jittery spikes, providing smooth, relaxed alertness.', 'We are experimenting with clinical L-Theanine:Caffeine ratios to eliminate jitter anomalies and provide smooth, protocol-based alertness.')
        
        content = content.replace('The Ayurvedic memory herb. We use an extract standardized to =50% bacosides, demonstrated to accelerate speed of visual information processing.', 'We are sourcing Ayurvedic Brahmi extracts standardized to =50% bacosides, researching its capacity to accelerate visual information processing speeds.')

        # Footer Certificate statement
        old_cert = '''<h2 style="font-family:var(--font-serif); font-size:2.5rem; color:var(--text-main); line-height:1.2; margin-bottom:1rem;">Full
                    Certificate of Analysis for every batch.</h2>
                <p style="font-size:1.15rem; color:var(--text-muted); line-height:1.6; max-width:600px;">When we launch, every batch will have a publicly available CoA with third-party verified test
                    results. Scan the QR code on any product to see the exact test report for your batch.</p>'''
        
        new_cert = '''<h2 style="font-family:var(--font-serif); font-size:2.5rem; color:var(--text-main); line-height:1.2; margin-bottom:1rem;">Absolute Data Transparency.</h2>
                <p style="font-size:1.15rem; color:var(--text-muted); line-height:1.6; max-width:600px;">When we finally manufacture a product, every batch will have a publicly available Certificate of Analysis with third-party verified test results. Until then, we publish our progress, our targets, and our failures from the lab.</p>'''
        
        content = content.replace(old_cert, new_cert)

    # science.html specific fixes
    if 'science.html' in file_path:
        # Change definitive science claims to hypothesis phrasing
        content = content.replace('Every formulation decision has a reason. Every reason has a reference. Every reference is available to you.', 'Every formulation target has a hypothesis. Every hypothesis has a reference. Every reference is available to you.')
        
        content = content.replace('We utilize Iron Bisglycinate', 'We are prioritizing Iron Bisglycinate')
        
        content = content.replace('This is the exact dosage and extraction methodology used in peer-reviewed clinical trials', 'We are mirroring the exact extraction methodology used in peer-reviewed clinical trials')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Science and Ingredients pages reframed for R&D transparency.")
