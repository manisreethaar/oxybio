html = open('science.html', 'r', encoding='utf-8').read()

# Insert </main> just before the Site Footer comment
footer_marker = '\n\n\n\n    <!-- Site Footer -->'
idx = html.find(footer_marker)
print(f"Footer marker at: {idx}")
print(repr(html[idx-20:idx+60]))

if idx != -1:
    fixed = html[:idx] + '\n\n</main>' + html[idx:]
    open('science.html', 'w', encoding='utf-8').write(fixed)
    print("</main> restored. Count now:", fixed.count('</main>'))
else:
    # try alternative
    alt = '    <!-- Site Footer -->'
    idx2 = html.find(alt)
    print(f"Alt marker at: {idx2}")
    print(repr(html[idx2-20:idx2+60]))
