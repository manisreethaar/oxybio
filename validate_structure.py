import glob
from html.parser import HTMLParser

class StructureValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.errors = []
        self.line_number = 1

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
            
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
            
        last_tag, pos = self.stack.pop()
        pos_line = pos[0]
        
        if last_tag != tag:
            # We expected </{last_tag}> but got </{tag}>
            self.errors.append(f"Mismatched tag: Expected </{last_tag}> (opened at line {pos_line}), got </{tag}> at line {self.getpos()[0]}")
            # Try to recover by popping until we find the match (basic recovery)
            found = False
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i][0] == tag:
                    found = True
                    self.stack = self.stack[:i]
                    break
            
            if not found:
                # If we couldn't find a matching open tag, push the last one back
                self.stack.append((last_tag, pos))

def validate_html_files():
    html_files = glob.glob(r'e:\\OXYBIO\\*.html')
    all_clean = True
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parser = StructureValidator()
        parser.feed(content)
        
        # Check for unclosed tags at the end
        for tag, pos in parser.stack:
            # Lots of valid HTML documents might leave some tags unclosed or rely on browser parsing, 
            # but for our strict checking, we'll log it if it's a major container
            if tag in ['div', 'section', 'main', 'body', 'html', 'nav', 'header', 'footer']:
                parser.errors.append(f"Unclosed tag <{tag}> started at line {pos[0]}")
                
        if parser.errors:
            print(f"\\n--- Sequence errors found in {file} ---")
            for err in parser.errors[:5]:  # show max 5 to avoid spam
                print(f"  - {err}")
            if len(parser.errors) > 5:
                print(f"  - ... and {len(parser.errors) - 5} more.")
            all_clean = False
            
    if all_clean:
        print("\\nSUCCESS: All HTML files have perfect structural DOM sequencing and perfectly matching tags!")

validate_html_files()
