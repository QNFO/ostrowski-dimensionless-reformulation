import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 1. Check the HTML for table structure
html = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\odr-final.html', encoding='utf-8').read()
tables = re.findall(r'<table>.*?</table>', html, re.DOTALL)
print(f'HTML tables found: {len(tables)}')
for i, t in enumerate(tables[:6]):
    rows = re.findall(r'<tr>.*?</tr>', t, re.DOTALL)
    print(f'\nTable {i+1}: {len(rows)} rows')
    if rows:
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', rows[0], re.DOTALL)
        print(f'  Header cells: {len(cells)}')
        for c in cells[:5]:
            clean = re.sub(r'<[^>]+>', '', c).strip()
            print(f'    [{clean[:60]}]')
    for j, row in enumerate(rows[1:3]):
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL)
        print(f'  Row {j+1}: {len(cells)} cells')
        for c in cells[:4]:
            clean = re.sub(r'<[^>]+>', '', c).strip()
            print(f'    [{clean[:60]}]')

# 2. Check for pipe-in-math in source tables (the likely breakage)
md = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = md.split('\n')
print('\n\n=== Source tables with pipes inside math cells ===')
for i, line in enumerate(lines):
    if line.strip().startswith('|'):
        # find math spans with pipes
        for m in re.finditer(r'\$[^$]*\|[^$]*\$', line):
            ctx = line[max(0,m.start()-15):m.end()+15]
            print(f'  L{i+1}: {ctx}')
