import os

ROOT = r'e:\OXYBIO'
JSON_LD = """
    <!-- Google Structured Data (Organization) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Oxygen Bioinnovations",
      "url": "https://oxygenbioinnovations.com/",
      "logo": "https://oxygenbioinnovations.com/assets/images/logo-dark.png",
      "description": "India's first precision nutrition system grounded in biotechnology, indigenous ingredients, and an unbreakable commitment to evidence."
    }
    </script>
"""

count = 0
for file in os.listdir(ROOT):
    if file.endswith('.html'):
        path = os.path.join(ROOT, file)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Don't add if already present
        if 'application/ld+json' not in html:
            # Inject right before </head>
            html = html.replace('</head>', JSON_LD + '</head>')
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'Added structured data to {file}')
            count += 1
        else:
            print(f'Structured data already exists in {file}')

print(f'Finished adding structured data to {count} files.')
