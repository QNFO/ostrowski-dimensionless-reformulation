import subprocess, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

# Minimal pipe table test
minimal = "| A | B |\n|---|---|\n| 1 | 2 |\n"
open(os.path.join(DIR, '_min.md'), 'w', encoding='utf-8').write(minimal)

r = subprocess.run([PANDOC, os.path.join(DIR, '_min.md'), '-t', 'html'],
                   capture_output=True, text=True)
print('MINIMAL TABLE OUTPUT:', repr(r.stdout))
print('stderr:', r.stderr[:200])

# Now test the ACTUAL first table region from the paper in isolation
table_region = """We classify 53 fundamental physics equations into seven formula classes based on which dimensional constants they contain:

| Class | Constants | Count | Example |
|:------|:----------|:------|:--------|
| A | hbar only | 8 | Schroedinger equation |

Follow-up text.
"""
open(os.path.join(DIR, '_t1.md'), 'w', encoding='utf-8').write(table_region)
r2 = subprocess.run([PANDOC, os.path.join(DIR, '_t1.md'), '-t', 'html'],
                    capture_output=True, text=True)
print('\nPAPER TABLE REGION OUTPUT:')
print(r2.stdout[:600])

# Check the stripped _diag.md first 15 lines
diag = open(os.path.join(DIR, '_diag.md'), encoding='utf-8').read()
print('\nSTRIPPED _diag.md first 12 lines:')
for i, l in enumerate(diag.split('\n')[:12]):
    print(f'  {i}: {repr(l[:80])}')
