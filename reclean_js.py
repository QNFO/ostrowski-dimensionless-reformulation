import re, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Re-extract the JS from the multipart response CLEANLY
raw = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gw-content.json', encoding='utf-8').read()

marker = 'Content-Type: application/javascript+module'
idx = raw.find(marker)
body_start = raw.find('\r\n\r\n', idx) + 4
js = raw[body_start:]
# Strip trailing boundary
js = re.sub(r'\r\n--[a-f0-9]+-{0,2}\s*$', '', js, flags=re.DOTALL)
# Also strip leading boundary leftovers if any
js = re.sub(r'^--[a-f0-9]+\s*', '', js)
# Trim BOM
if js.startswith('\ufeff'):
    js = js[1:]

open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', 'w', encoding='utf-8', newline='\n').write(js)
print(f'Clean extraction: {len(js)} bytes')
print('First 80 chars:', repr(js[:80]))
