import re

with open('e:\\OXYBIO\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the two buttons in the hero section
old_join = '<a href="#join" class="btn btn-primary">Join Waitlist</a>'
new_join = '<a href="#join" class="btn btn-primary magnetic-btn"><span class="magnetic-content">Join Waitlist</span></a>'
html = html.replace(old_join, new_join)

old_science = '<a href="problem.html" class="btn btn-outline">Read the Science</a>'
new_science = '<a href="problem.html" class="btn btn-outline magnetic-btn"><span class="magnetic-content">Read the Science</span></a>'
html = html.replace(old_science, new_science)

# Also adding magnetic to another instance of Join Waitlist (the one on the right with the inline style that I saw in grep)
old_menu_join = '<a href="#join" class="btn btn-primary" style="margin-left: 1rem;">Join Waitlist</a>'
new_menu_join = '<a href="#join" class="btn btn-primary magnetic-btn" style="margin-left: 1rem;"><span class="magnetic-content">Join Waitlist</span></a>'
html = html.replace(old_menu_join, new_menu_join)

with open('e:\\OXYBIO\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Applied magnetic classes to Hero buttons.')
