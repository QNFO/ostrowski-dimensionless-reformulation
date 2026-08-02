import fitz, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

d = fitz.open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\odr-tables-test.pdf')
print(f'Pages: {d.page_count}')

# Find pages with table content (search for table-specific text)
full_pages = []
for i in range(d.page_count):
    t = d[i].get_text()
    if 'Class' in t and 'Constants' in t and 'Count' in t:
        full_pages.append((i+1, 'classification table'))
    if 'Quantity' in t and 'Constant' in t and 'Ratio' in t:
        full_pages.append((i+1, 'ratio table'))
    if 'Completion' in t and 'Tree Valence' in t:
        full_pages.append((i+1, 'completion table'))
    if 'Program' in t and 'Status' in t and 'Deliverable' in t:
        full_pages.append((i+1, 'roadmap table'))
    if 'Prediction' in t and 'Timeline' in t and 'Strength' in t:
        full_pages.append((i+1, 'calibration table'))

print(f'Table pages found: {full_pages}')

# Verify a specific table's content reads correctly (not pipe-littered)
for pg, label in full_pages[:2]:
    t = d[pg-1].get_text()
    # Check the table area - look for cells
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    print(f'\n--- Page {pg} ({label}) first 15 lines ---')
    for l in lines[:15]:
        print(f'  {l[:80]}')

# Count pipe characters (should be ~0 in table regions if rendered as cells)
pipes = sum(d[i].get_text().count('|') for i in range(d.page_count))
print(f'\nTotal | chars in PDF text: {pipes}')
