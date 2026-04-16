with open('problem.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="layer-03"')
end_idx = text.find('</section>', idx)
text = text[:end_idx] + '</div>\n    ' + text[end_idx:]

with open('problem.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()
head_idx = about.find('</head>')
print(about[head_idx-150:head_idx+100])
