import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

raw = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gw-content.json', encoding='utf-8').read()

# Find the JS body: the boundary line ends, headers end at blank line, then JS
# The JS starts right after "Content-Type: application/javascript+module\n\n"
marker = 'application/javascript+module'
idx = raw.find(marker)
if idx < 0:
    print('MARKER NOT FOUND')
    sys.exit(1)

# Find the blank line after Content-Type (either \r\n\r\n or \n\n)
seg = raw[idx:]
if seg.startswith('\r\n\r\n'):
    body_start = idx + len('application/javascript+module') + 4
elif seg.startswith('\n\n'):
    body_start = idx + len('application/javascript+module') + 2
else:
    # find first blank line
    m = re.search(r'\r?\n\r?\n', seg)
    body_start = idx + m.end() if m else -1

js = raw[body_start:]
# Strip trailing boundary
js = re.sub(r'\r?\n--[a-f0-9]+-{0,2}\s*$', '', js, flags=re.DOTALL)
# Strip leading junk boundary remnants
js = re.sub(r'^--[a-f0-9]+\s*\r?\n', '', js)

open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', 'w', encoding='utf-8', newline='\n').write(js)
print(f'Extracted: {len(js)} bytes')
print('First 100 chars:', repr(js[:100]))
