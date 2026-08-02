import re, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

raw = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gw-content.json', encoding='utf-8').read()

# The content is multipart form-data; find the JS body after the headers
# Extract everything after the last blank line before the JS
marker = 'Content-Type: application/javascript+module'
idx = raw.find(marker)
if idx > 0:
    # find the \r\n\r\n after content-type line
    body_start = raw.find('\r\n\r\n', idx) + 4
    js = raw[body_start:]
    # Remove trailing boundary
    js = re.sub(r'\r\n--[a-f0-9]+.*$', '', js, flags=re.DOTALL)
    open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', 'w', encoding='utf-8').write(js)
    print(f'Extracted {len(js)} bytes of JS')

    # Find paper rendering logic
    print('\n=== Paper/markdown rendering search ===')
    for pattern in ['papers', 'markdown', 'marked', 'katex', 'MathJax', 'render', 'body_md', 'escapeHtml', '<pre>', 'paper']:
        matches = [m.start() for m in re.finditer(pattern, js, re.IGNORECASE)]
        if matches:
            print(f'{pattern}: {len(matches)} occurrences')
            if matches[:2]:
                for m in matches[:2]:
                    print(f'  @{m}: {js[max(0,m-60):m+80].replace(chr(10)," ")[:140]}')
