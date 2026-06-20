"""
Extract all text from PPTX slide by slide, write to a text file.
"""
import zipfile, os, re
from xml.etree import ElementTree as ET

pptx_path = r'e:\OXYBIO-WEBSITE\OBI_SISFS_Updated_v3_FIXED.pptx'
out_path = r'e:\OXYBIO-WEBSITE\_ppt_content.txt'

def extract_text_from_xml(xml_bytes):
    root = ET.fromstring(xml_bytes)
    texts = []
    for elem in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
        if elem.text and elem.text.strip():
            texts.append(elem.text.strip())
    return texts

lines = []
with zipfile.ZipFile(pptx_path, 'r') as z:
    slides = sorted([f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml') and 'layout' not in f and 'master' not in f])
    lines.append(f"Total slides: {len(slides)}")
    lines.append("="*70)
    for i, slide_path in enumerate(slides, 1):
        with z.open(slide_path) as f:
            xml_content = f.read()
        texts = extract_text_from_xml(xml_content)
        if texts:
            lines.append(f"\n--- SLIDE {i}: {slide_path} ---")
            for t in texts:
                # Replace problematic chars
                clean = t.encode('ascii', 'replace').decode('ascii')
                lines.append(f"  {clean}")

with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Written to {out_path}")
print(f"Total lines: {len(lines)}")
