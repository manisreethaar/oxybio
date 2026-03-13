import traceback

try:
    with open(r'e:\OXYBIO\careers.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace("cutting-edge nutraceutical products", "cutting-edge functional food products")

    if new_content != content:
        with open(r'e:\OXYBIO\careers.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated careers page")
except Exception as e:
    traceback.print_exc()

with open(r'C:\Users\manis\.gemini\antigravity\brain\d200dc26-157f-40f6-ae6b-106a1c6aaff5\task.md', 'r', encoding='utf-8') as f:
    task_content = f.read()
    
task_content = task_content.replace("[ ] Do a final check of \"nutraceutical\" or \"health drink\" vocabulary.", "[x] Do a final check of \"nutraceutical\" or \"health drink\" vocabulary.")

with open(r'C:\Users\manis\.gemini\antigravity\brain\d200dc26-157f-40f6-ae6b-106a1c6aaff5\task.md', 'w', encoding='utf-8') as f:
    f.write(task_content)
