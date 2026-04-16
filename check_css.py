css = open('assets/css/styles.css', encoding='utf-8', errors='ignore').read()
idx = css.find('.container')
print(css[idx:idx+300])
