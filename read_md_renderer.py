import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()

# Extract renderMarkdown function (lines around 11775-14350)
idx = js.find('function renderMarkdown(md)')
print('=== renderMarkdown function ===')
print(js[idx:idx+3000])
