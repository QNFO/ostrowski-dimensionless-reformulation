import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

md = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = md.split('\n')

# Show raw table regions: find lines starting with | and show context
print('=== Raw table regions (first 400 lines with |) ===')
count = 0
for i, line in enumerate(lines):
    if line.strip().startswith('|'):
        print(f'L{i+1}: {repr(line[:110])}')
        count += 1
        if count > 40:
            break
