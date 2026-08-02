import subprocess, re, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
MD = os.path.join(DIR, 'ostrowski-dimensionless-reformulation.md')
HTML = os.path.join(DIR, 'diag.html')
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

# Step 1: strip YAML + build HTML via pandoc --mathjax
md = open(MD, encoding='utf-8').read()
md = re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.DOTALL)
tmp = os.path.join(DIR, '_diag.md')
open(tmp, 'w', encoding='utf-8').write(md)
r = subprocess.run([PANDOC, tmp, '--mathjax', '--standalone', '-o', HTML],
                   capture_output=True, text=True)
print('PANDOC exit:', r.returncode)
if r.stderr:
    print('PANDOC stderr (first 400):', r.stderr[:400])

html = open(HTML, encoding='utf-8').read()
tables = re.findall(r'<table>.*?</table>', html, re.DOTALL)
print(f'HTML tables found: {len(tables)}')

for i, t in enumerate(tables):
    rows = re.findall(r'<tr>.*?</tr>', t, re.DOTALL)
    # count columns per row
    col_counts = [len(re.findall(r'<t[dh][^>]*>', row)) for row in rows]
    print(f'\nTable {i+1}: {len(rows)} rows, col counts: {col_counts[:6]}')
    if rows:
        hdr = re.sub(r'<[^>]+>', '', rows[0]).strip()
        print(f'  Header text: {hdr[:100]}')

# Step 2: check source for pipe-in-math inside table rows
mdlines = md.split('\n')
print('\n=== Source table rows with pipes in math ===')
for i, line in enumerate(mdlines):
    if line.strip().startswith('|') and '$' in line:
        # pipe inside $...$ ?
        matches = re.findall(r'\$[^$]*\|[^$]*\$', line)
        if matches:
            print(f'  L{i+1}: {matches[0][:80]}')
