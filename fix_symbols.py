import os

html_files = [
    r'e:\OXYBIO\careers.html',
    r'e:\OXYBIO\problem.html'
]

replacements = {
    '?18K - 25K/mo': '₹18K - 25K/mo',
    'View Full Role ?': 'View Full Role →',
    '?4.5 Lakh Crore': '₹4.5 Lakh Crore',
    '(?350-500/serving)': '(₹350-500/serving)'
}

for filepath in html_files:
    content = None
    for enc in ['utf-8', 'windows-1252', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
            
    if content:
        for old_str, new_str in replacements.items():
            content = content.replace(old_str, new_str)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print('Careers and Problem HTML symbols rectified.')
