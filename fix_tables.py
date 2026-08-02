import subprocess, sys, io, os, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

def pandoc_html(text, label):
    p = os.path.join(DIR, '_test.md')
    open(p, 'w', encoding='utf-8').write(text)
    r = subprocess.run([PANDOC, p, '-t', 'html'], capture_output=True, text=True)
    return r.stdout

# Simulate: header, blank line, separator
broken = "| A | B |\n\n|---|---|\n| 1 | 2 |\n"
out = pandoc_html(broken, 'blank-between')
print(f'Blank-between: <table>={out.count("<table")} line-block={out.count("line-block")}')

# Fixed: no blank line
fixed = "| A | B |\n|---|---|\n| 1 | 2 |\n"
out = pandoc_html(fixed, 'no-blank')
print(f'No-blank: <table>={out.count("<table")} line-block={out.count("line-block")}')

# Now write a table-normalization function and apply to the FULL paper
def normalize_tables(md_text):
    lines = md_text.split('\n')
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Detect a pipe header row followed by blank line(s) then a separator row
        if stripped.startswith('|') and stripped.endswith('|') and '|' in stripped[1:-1]:
            # Look ahead: skip blank lines, check if next non-blank is a separator
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines):
                sep = lines[j].strip()
                if re.match(r'^\|[\s:|-]+\|$', sep) and '-' in sep and '|' in sep:
                    # Found header -> blank(s) -> separator: collapse blanks
                    out.append(line)
                    out.append(sep)
                    fixed += 1
                    i = j + 1
                    continue
        out.append(line)
        i += 1
    return '\n'.join(out), fixed

md = open(os.path.join(DIR, '_diag.md'), encoding='utf-8').read()
norm, n = normalize_tables(md)
print(f'\nNormalization fixed {n} tables')

out = pandoc_html(norm, 'normalized')
print(f'Normalized full doc: <table>={out.count("<table>")} line-block={out.count("line-block")}')
open(os.path.join(DIR, '_diag_norm.md'), 'w', encoding='utf-8').write(norm)
