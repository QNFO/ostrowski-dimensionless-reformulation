import urllib.request, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

url = 'https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='replace')
    print(f'Status OK, {len(html)} bytes')
    print('Has <table>:', '<table' in html)
    print('Has MathJax script:', 'MathJax-script' in html or 'tex-svg-full' in html)
    print('Has MathJax config:', 'window.MathJax' in html)
    print('Has table CSS:', '.rendered-md table' in html)
    print('Has math-display div:', 'math-display' in html)

    # Extract the table HTML
    tables = re.findall(r'<table>.*?</table>', html, re.DOTALL)
    print(f'\nTables rendered: {len(tables)}')
    for i, t in enumerate(tables[:3]):
        rows = re.findall(r'<tr>.*?</tr>', t, re.DOTALL)
        hdr = re.sub(r'<[^>]+>', '', rows[0]).strip() if rows else ''
        print(f'  Table {i+1}: {len(rows)} rows | header: {hdr[:70]}')

    # Check for raw pipe text (tables NOT rendered)
    raw_pipes = html.count('| Class |') + html.count('| Quantity |')
    print(f'\nRaw pipe-table text (should be ~0): {raw_pipes}')

    # Show the paper body sample with math
    m = re.search(r'<div class="rendered-md">(.*?)</div></article>', html, re.DOTALL)
    if m:
        body = m.group(1)
        print(f'\nRendered body length: {len(body)}')
        print('Body sample:', re.sub(r'<[^>]+>', '', body)[:200])
except Exception as e:
    print(f'ERROR: {e}')
