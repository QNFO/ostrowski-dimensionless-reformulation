import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()

# Check _mdInline - how does it handle $...$ math?
idx = js.find('function _mdInline')
print('=== _mdInline ===')
print(js[idx:idx+1200])
