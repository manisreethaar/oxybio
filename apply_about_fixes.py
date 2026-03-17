import os
import re

file_path = 'e:/OXYBIO/about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# THE REPLACEMENT BLOCK for Origin Story
new_origin = """                        <div class="editorial-col" style="font-size:1.15rem; line-height:1.7; color:var(--text-muted);">

                            <p style="margin-bottom:1.5rem;">I always had a dream of starting a business on my own. I was fed up with working for someone else's growth. Why work 8 to 10 hours a day for someone else, instead of working those same hours for your own growth to make something useful? We all have one life—we should do something remarkable.</p>
                            
                            <p style="margin-bottom:2rem;">Why this specific problem? Due to modernization, our lifestyles have changed dramatically. The core issue behind most lifestyle problems revolves around the food we are eating—processed, low quality, chemical-filled, and sold on fake promises. There is an ancient Tamil quote, <strong>"Unnave marundhu" (Food is medicine)</strong>, but we have forgotten it.</p>

                            <!-- Premium Research Result Block -->

                            <div
                                style="background:var(--bg); border:1px solid var(--border); border-radius:12px; padding:3rem; margin:3rem 0; position:relative; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.03);">

                                <h4
                                    style="font-family:var(--font-mono); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--text-main); margin-bottom:1rem;">
                                    Radical Transparency //</h4>

                                <p
                                    style="font-family:var(--font-serif); font-size:1.25rem; line-height:1.6; color:var(--text-main); margin-bottom:0;">
                                    My idea is to provide healthy, quality, scientifically-backed food without fake promises. With my background in biotechnology, I want to use my knowledge to actually solve this. Unvarnished truth? I don't know a lot of things yet. I don't know if this precise idea will work, if I can make the prototype exactly right, or if it will behave the way I expect. A lot of things can go wrong.
                                </p>

                            </div>

                            <div style="border-left:2px solid var(--text-main); padding-left:1.5rem;">

                                <p
                                    style="color:var(--text-main); font-size:1.35rem; font-family:var(--font-serif); font-style:italic; margin-bottom:0;">
                                    "But I am building this for everyone who deserves real, scientifically-backed nutrition—starting with the professionals, students, and athletes who need it most."
                                </p>

                            </div>

                        </div>"""

origin_pattern = re.compile(r'<div class="editorial-col" style="font-size:1.15rem; line-height:1.7; color:var\(--text-muted\);">.*?</div>\s*</div>\s*<!-- Chapter 02', re.DOTALL)

# Insert the new origin text + the closing div (which was matched) and Chapter 02 marker
content = origin_pattern.sub(new_origin + "\n\n                    </div>\n\n\n\n                    <!-- Chapter 02", content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"about.html processed.")
