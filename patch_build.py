import re

# Patch build-mathjax-pdf.py: add normalize_tables to sanitize_source
path = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\build-mathjax-pdf.py'
src = open(path, encoding='utf-8').read()

normalize_fn = '''
def normalize_tables(md_text):
    """Collapse blank lines inside pipe-table blocks.

    Root cause (2026-08-02): papers with blank lines between table rows
    (header -> blank -> separator -> blank -> row -> blank -> row ...) are
    NOT parsed as tables by pandoc. Pandoc requires contiguous rows; blank
    lines make it fall back to 'line-block' rendering (literal '| a | b |'
    text instead of <table>). This also breaks papers.qnfo.org rendering.
    """
    lines = md_text.split('\\n')
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped[1:-1]:
            block = []
            j = i
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith('|'):
                    block.append(lines[j])
                    j += 1
                elif s == '' and j + 1 < len(lines) and lines[j + 1].strip().startswith('|'):
                    j += 1
                else:
                    break
            if len(block) >= 2:
                out.extend(block)
                fixed += 1
                i = j
                continue
        out.append(line)
        i += 1
    return '\\n'.join(out), fixed

'''

if 'def normalize_tables' not in src:
    # Insert before sanitize_source
    anchor = 'def sanitize_source'
    idx = src.find(anchor)
    if idx > 0:
        src = src[:idx] + normalize_fn + src[idx:]
        # Call it inside sanitize_source
        src = src.replace(
            "    text = text.replace('\\u274c', '\\u2717')  # ❌ -> ✗\n",
            "    text = text.replace('\\u274c', '\\u2717')  # ❌ -> ✗\n"
            "    text, _ = normalize_tables(text)\n"
        )
        open(path, 'w', encoding='utf-8').write(src)
        print('Patched build-mathjax-pdf.py with normalize_tables')
    else:
        print('ANCHOR NOT FOUND')
else:
    print('Already patched')

# Verify
src = open(path, encoding='utf-8').read()
print('normalize_tables defined:', 'def normalize_tables' in src)
print('normalize_tables called:', 'normalize_tables(text)' in src)
