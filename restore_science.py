import subprocess

# Restore science.html from the last good git commit that modified it
result = subprocess.run(
    ['git', 'show', '9015ff4:science.html'],
    capture_output=True
)
html = result.stdout.decode('utf-8', errors='replace')
print(f"Restored {len(html)} chars from git:9015ff4")

# Now apply the Levilactobacillus brevis substitution
html = html.replace('Lactobacillus plantarum', 'Levilactobacillus brevis')
html = html.replace('*Lactobacillus plantarum*', '*Levilactobacillus brevis*')

# Confirm
print("Levilactobacillus brevis in file:", 'Levilactobacillus brevis' in html)
print("Lactobacillus plantarum remaining:", 'Lactobacillus plantarum' in html)
print("GABA present:", 'GABA' in html)

with open('science.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("science.html written OK")
