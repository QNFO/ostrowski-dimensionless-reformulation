import subprocess, sys, io, os, re, json, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Probe papers.qnfo.org for the ODR paper - how is it rendered?
url = 'https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='replace')
    print(f'Status: OK, {len(html)} bytes')
    # Check rendering method
    print('Has <table>:', '<table' in html)
    print('Has MathJax:', 'mathjax' in html.lower() or 'MathJax' in html)
    print('Has KaTeX:', 'katex' in html.lower())
    print('Has marked.js:', 'marked' in html.lower())
    print('Has markdown-it:', 'markdown-it' in html.lower())
    print('Has <pre> with raw markdown:', '<pre>' in html)
    # Find the paper body markers
    for probe in ['Class | Constants', 'line-block', 'Schroedinger', 'Ostrowski']:
        print(f'Contains {probe!r}:', probe in html)
    # Check for script tags
    import re
    scripts = re.findall(r'<script[^>]*src="([^"]*)"', html)
    print('Scripts:', scripts[:10])
    styles = re.findall(r'<link[^>]*href="([^"]*)"', html)
    print('Stylesheets:', styles[:10])
except Exception as e:
    print(f'ERROR: {e}')
