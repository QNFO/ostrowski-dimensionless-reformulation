import subprocess, sys, io, os, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

norm = open(os.path.join(DIR, '_diag_norm.md'), encoding='utf-8').read()
html = open(os.path.join(DIR, 'diag.html'), encoding='utf-8').read()

# Find all table headers in source
lines = norm.split('\n')
table_headers = []
for i, l in enumerate(lines):
    s = l.strip()
    if s.startswith('|') and s.endswith('|') and '|' in s[1:-1]:
        # check next non-blank is separator
        j = i+1
        while j < len(lines) and lines[j].strip() == '':
            j += 1
        if j < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[j].strip()):
            table_headers.append((i, s[:60]))

print(f'Table headers found in normalized source: {len(table_headers)}')
for i, h in table_headers:
    print(f'  L{i+1}: {h}')

# Extract the actual tables from the normalized HTML
html = open(os.path.join(DIR, 'diag.html'), encoding='utf-8').read()
# Rebuild HTML from normalized source
def build_html(md):
    p = os.path.join(DIR, '_t.md')
    open(p, 'w', encoding='utf-8').write(md)
    r = subprocess.run([PANDOC, p, '-t', 'html'], capture_output=True, text=True)
    return r.stdout

h = build_html(norm)
print(f'\nNormalized HTML: <table>={h.count("<table")}, line-block={h.count("line-block")}')

# Show line-block regions with their content (find which tables became line-blocks)
# Search for line-block divs containing table-looking content
for m in re.finditer(r'<div class="line-block">(.*?)</div>', h, re.DOTALL):
    content = re.sub(r'<[^>]+>', '', m.group(1))[:70]
    if '|' in content or 'Class' in content or 'Quantity' in content:
        print(f'  LINE-BLOCK: {content}')
