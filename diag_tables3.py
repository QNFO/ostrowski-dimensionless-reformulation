import subprocess, re, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
MD = os.path.join(DIR, 'ostrowski-dimensionless-reformulation.md')
HTML = os.path.join(DIR, 'diag.html')
PANDOC = r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe'

html = open(HTML, encoding='utf-8').read()
print(f'HTML size: {len(html)}')
print(f'<table occurrences: {html.count("<table")}')
print(f'"table" word occurrences: {len(re.findall(r"table", html))}')
print(f'"|" pipe chars: {html.count("|")}')

# Find where "Class | Constants" would be if rendered as text
idx = html.find('Class')
print(f'\nFirst "Class" at: {idx}')
if idx > 0:
    print(f'Context: ...{html[idx-100:idx+200]}...')

# Check pandoc version + what format flags
r = subprocess.run([PANDOC, '--version'], capture_output=True, text=True)
print(f'\nPandoc version: {r.stdout.splitlines()[0]}')

# Try building with explicit extensions to force pipe_tables
test_md = os.path.join(DIR, '_diag.md')
r2 = subprocess.run([PANDOC, test_md, '-f', 'markdown+pipe_tables+raw_tex', '--mathjax', '--standalone', '-o', HTML],
                    capture_output=True, text=True)
print(f'\nWith +pipe_tables exit: {r2.returncode}')
html2 = open(HTML, encoding='utf-8').read()
print(f'<table occurrences with pipe_tables: {html2.count("<table")}')
