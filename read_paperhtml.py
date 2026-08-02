import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()

# Read rest of renderMarkdown (from 11781+3000)
idx = js.find('function renderMarkdown(md)')
print('=== renderMarkdown (rest) ===')
print(js[idx+3000:idx+6000])

# Find PaperHTML
pidx = js.find('PaperHTML(paper)')
print('\n\n=== PaperHTML function ===')
print(js[pidx-100:pidx+2500])
