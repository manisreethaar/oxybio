import os
import re

html_file = 'e:\\OXYBIO\\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the separate containers with a single scrolling wrapper
old_labels = """                <!-- Column labels -->
                <div class="container">
                    <div
                        style="display:grid; grid-template-columns:1fr 1fr 1fr; border-left:1px solid var(--border); border-right:1px solid var(--border);">"""

new_labels = """                <!-- Column labels and Table Wrapper -->
                <div class="container" style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin-bottom: 6rem; padding-bottom: 1rem;">
                    <div style="min-width: 650px;">
                        <div
                            style="display:grid; grid-template-columns:1fr 1fr 1fr; border-left:1px solid var(--border); border-right:1px solid var(--border); border-top:1px solid var(--border); border-radius: 20px 20px 0 0; overflow:hidden;">"""

html = html.replace(old_labels, new_labels)

old_duel_rows = """                <!-- Duel Rows -->
                <div class="container"
                    style="border:1px solid var(--border); border-top:none; border-radius:0 0 20px 20px; overflow:hidden; margin-bottom: 6rem;">"""

new_duel_rows = """                <!-- Duel Rows -->
                <div style="border:1px solid var(--border); border-top:none; border-radius:0 0 20px 20px; overflow:hidden;">"""
html = html.replace(old_duel_rows, new_duel_rows)

# the end of the duel rows is a </div>. Finding exactly the last </div> before "</section>"
# "No Transparency</span>\n                        </div>\n                    </div>\n\n                </div>\n            </section>"
# Let's do a precise string replace for the end of row 7
end_target = """                        <div style="padding:1.5rem; display:flex; align-items:center; gap:0.75rem;">
                            <span style="font-size:1rem; color:var(--text-muted); flex-shrink:0;">✖</span>
                            <span style="font-size:0.9rem; color:var(--text-muted);">No Transparency</span>
                        </div>
                    </div>

                </div>"""

new_end = """                        <div style="padding:1.5rem; display:flex; align-items:center; gap:0.75rem;">
                            <span style="font-size:1rem; color:var(--text-muted); flex-shrink:0;">✖</span>
                            <span style="font-size:0.9rem; color:var(--text-muted);">No Transparency</span>
                        </div>
                    </div>

                </div>
            </div> <!-- End scrolling min-width wrapper -->
        </div> <!-- End container wrapper -->"""

html = html.replace(end_target, new_end)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated comparison table wrapper in index.html to fix mobile collapse.")
