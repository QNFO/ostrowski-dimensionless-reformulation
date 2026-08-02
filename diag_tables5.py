import subprocess, sys, io, os, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

md = open(os.path.join(DIR, '_diag.md'), encoding='utf-8').read()

def pandoc_html(text):
    p = os.path.join(DIR, '_test.md')
    open(p, 'w', encoding='utf-8').write(text)
    r = subprocess.run([PANDOC, p, '-t', 'html'], capture_output=True, text=True)
    return r.stdout

# Test 1: table 1 (Class) in isolation from real source
lines = md.split('\n')
t1 = '\n'.join(lines[126:150])  # around L133 table
out = pandoc_html(t1)
print(f'Table1 isolated: <table>={out.count("<table")}, line-block={out.count("line-block")}')

# Test 2: the document prefix + table1
prefix = '\n'.join(lines[0:126])
out = pandoc_html(prefix + '\n\n' + t1)
print(f'Prefix+Table1: <table>={out.count("<table")}, line-block={out.count("line-block")}')

# Test 3: full doc but only first 200 lines
out = pandoc_html('\n'.join(lines[:200]))
print(f'First 200 lines: <table>={out.count("<table")}, line-block={out.count("line-block")}')

# Test 4: full doc
out = pandoc_html(md)
print(f'FULL doc: <table>={out.count("<table")}, line-block={out.count("line-block")}')

# Test 5: find which line contains a lone pipe that might open a line-block
for i, l in enumerate(lines):
    if l.strip() == '|':
        print(f'L{i+1}: EMPTY PIPE LINE')
        break

# Test 6: check for 4-space indented table rows (breaks tables)
for i, l in enumerate(lines):
    if l.startswith('    |') or l.startswith('\t|'):
        print(f'L{i+1}: INDENTED PIPE: {repr(l[:60])}')
        break

# Test 7: any table row with odd pipe count?
for i, l in enumerate(lines):
    if l.strip().startswith('|'):
        # count unescaped pipes
        np = l.count('|')
        if np % 2 == 0:
            print(f'L{i+1}: EVEN pipe count ({np}): {l[:70]}')
