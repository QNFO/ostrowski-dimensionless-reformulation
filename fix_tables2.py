import subprocess, sys, io, os, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

md = open(os.path.join(DIR, '_diag.md'), encoding='utf-8').read()
lines = md.split('\n')
print('Raw lines 133-150 (0-indexed 132-149):')
for i in range(132, 150):
    print(f'  L{i+1}: {repr(lines[i][:90])}')

# Comprehensive fix: collapse ALL blank lines within a table block.
# A table block = consecutive | lines possibly separated by single blank lines,
# bounded by non-| lines above and below.
def normalize_tables_v2(md_text):
    lines = md_text.split('\n')
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped[1:-1]:
            # Collect the table block: keep | rows, drop internal blank lines
            block = []
            j = i
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith('|'):
                    block.append(lines[j])
                    j += 1
                elif s == '' and j + 1 < len(lines) and lines[j+1].strip().startswith('|'):
                    # internal blank between rows - skip it
                    j += 1
                else:
                    break
            if len(block) >= 2:  # header + separator at minimum
                out.extend(block)
                fixed += 1
                i = j
                continue
        out.append(line)
        i += 1
    return '\n'.join(out), fixed

norm, n = normalize_tables_v2(md)
print(f'\nNormalization v2 fixed {n} table blocks')

p = os.path.join(DIR, '_t.md')
open(p, 'w', encoding='utf-8').write(norm)
r = subprocess.run([PANDOC, p, '-t', 'html'], capture_output=True, text=True)
print(f'Normalized v2 HTML: <table>={r.stdout.count("<table")}, line-block={r.stdout.count("line-block")}')
open(os.path.join(DIR, '_diag_norm2.md'), 'w', encoding='utf-8').write(norm)
