import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()

# Find all env.X references and their usage context to determine binding types
for m in re.finditer(r'env\.([A-Z_][A-Z0-9_]*)', js):
    name = m.group(1)
    start = max(0, m.start()-50)
    ctx = js[start:m.end()+50].replace('\n', ' ')
    print(f'env.{name}: ...{ctx[:130]}...')
    print()
