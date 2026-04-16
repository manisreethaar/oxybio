with open('science.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<section class="sci-metrics">')
end = html.find('</section>', start)
print(html[start:end+15])
