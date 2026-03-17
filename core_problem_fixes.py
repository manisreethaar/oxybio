import re

file_path = 'e:/OXYBIO/problem.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "The Savior" block
old_block = """                    <div

                        style="margin-top:var(--space-lg); padding:2rem; border-left:4px solid var(--text-main); background:var(--bg);">

                        <p style="font-size:1.125rem; line-height:1.6; color:var(--text-main);">

                            The market has affordable products that are inadequate. Quality products that are

                            inaccessible. Indian products that lack rigour. Rigorous products that lack Indian

                            relevance.

                        </p>

                        <p style="font-size:1.125rem; font-weight:600; font-family:var(--font-serif); margin-top:1rem;">

                            Affordable. Quality. Indian. Rigorous. This intersection is currently empty. Oxygen is being

                            built to occupy it.

                        </p>

                    </div>"""

new_block = """                    <div

                        style="margin-top:var(--space-lg); padding:2rem; border-left:4px solid #ef4444; background:var(--bg);">

                        <p style="font-size:1.15rem; line-height:1.6; color:var(--text-main);">
                            The market provides affordable, massive-scale products that lack scientific rigor, or premium imported products that ignore Indian indigenous sources and are too expensive for daily use.
                        </p>

                        <p style="font-size:1.2rem; font-family:var(--font-serif); font-style:italic; margin-top:1rem; color:var(--text-muted);">
                            "The intersection of affordable, scientifically rigorous, and indigenous is currently empty. We are in the lab right now trying to build something that occupies it. We do not know for sure if we will succeed, but this is the mandate we have set for ourselves."
                        </p>

                    </div>"""

content = content.replace(old_block, new_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("problem.html savior complex removed.")
