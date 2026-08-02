import subprocess, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

def pandoc_html(text, label):
    p = os.path.join(DIR, '_test.md')
    open(p, 'w', encoding='utf-8').write(text)
    r = subprocess.run([PANDOC, p, '-t', 'html'], capture_output=True, text=True)
    print(f'{label}: <table>={r.stdout.count("<table")} line-block={r.stdout.count("line-block")}')

# 1. Exact paper table header + sep (with colons)
t = "| Class | Constants | Count | Example |\n|:------|:----------|:------|:--------|\n| A | hbar only | 8 | X |\n"
pandoc_html(t, 'Colon-sep table')

# 2. Same but no colons
t2 = "| Class | Constants | Count | Example |\n|-------|-----------|------|--------|\n| A | hbar only | 8 | X |\n"
pandoc_html(t2, 'No-colon table')

# 3. Show raw bytes of the real header line (detect invisible chars)
md = open(os.path.join(DIR, '_diag.md'), encoding='utf-8').read()
lines = md.split('\n')
for i, l in enumerate(lines):
    if 'Class' in l and 'Constants' in l and 'Count' in l:
        print(f'\nReal header line L{i+1} repr: {repr(l)}')
        print(f'Bytes: {l.encode("utf-8")[:60]}')
        # get next 3 lines
        for j in range(i, i+4):
            print(f'  L{j+1} repr: {repr(lines[j])}')
        break
