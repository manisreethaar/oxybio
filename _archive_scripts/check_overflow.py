import bs4

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')
slides = soup.find_all(class_='apple-slide')
if slides:
    slide = slides[0]
    for parent in slide.parents:
        if parent.name == 'body': break
        print(f"{parent.name} | class={parent.get('class')} | id={parent.get('id')} | style={parent.get('style')}")
else:
    print('No apple-slide found')
