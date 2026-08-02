#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-mathjax-pdf.py — VERIFIED MathJax→SVG→PDF pipeline (2026-08-02)
Replaces pandoc+XeLaTeX for Unicode-math-heavy papers.

WHY: XeLaTeX uses system fonts; Latin Modern lacks Unicode math glyphs
(mu, chi, phi, Q, subscripts, integrals) -> hundreds of font warnings.
unicode-math via -V header-includes is ignored by pandoc template order.
build-paper.py's unicode->latex conversion breaks on papers already
containing $...$ (Missing } inserted).

THIS PIPELINE (Obsidian-style):
  pandoc --mathjax --standalone   (parses math, emits \(...\) / \[...\])
  -> swap CHTML script for SVG (tex-svg-full.js)
  -> inline print.css (@page margins, Georgia serif, page-break rules)
  -> headless Chrome --no-pdf-header-footer --print-to-pdf
  -> verify with PyMuPDF

KEY GOTCHAS (all hit live):
1. `-f markdown-tex_math_dollars-...` DESTROYS math: pandoc then parses
   \tilde{R}_{\mu\nu} as markdown emphasis -> $_{} = <em>P^2 R</em>{}$.
   ALWAYS use --mathjax so pandoc parses $...$ as real math.
2. `--print-to-pdf-no-header` is the OLD flag; new headless uses
   `--no-pdf-header-footer`. The old flag leaves headers/footers.
3. CHTML renderer (pandoc --mathjax default) injects PUA glyphs
   (\uedd9-\ueddc via SegoeFluentIcons) that print-to-PDF exposes.
   SVG renderer embeds pure vector paths: zero font dependence.
4. Chrome caches file:// pages -> use fresh --user-data-dir + ?cb= query.
5. Do NOT use `-V header-includes` for LaTeX preamble; it's ignored.
6. Tab/FF/VT control chars in source (from Python escape bugs in prior
   steps) corrupt math: scan source for chr<32 before building.
7. Emoji (U+2700-27BF, U+1F000+) render via SegoeFluentIcons/SegoeUISymbol
   on Windows -> replace with ✓ (U+2713) / ✗ (U+2717) or text.

VERIFIED: ODR v4.0.2, 44 pages, 4416 vector paths, 0 U+FFFD, 0 PUA,
0 header/footer artifacts. DOI 10.5281/zenodo.21755771.
"""
import subprocess, re, os, sys, tempfile, hashlib, fitz

CHROME_CANDIDATES = [
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
]

SVG_SCRIPT = '''<script>
window.MathJax = {
  loader: { load: ['[tex]/ams'] },
  tex: {
    inlineMath: [['$','$'], ['\\\\(','\\\\)']],
    displayMath: [['$$','$$'], ['\\\\[','\\\\]']],
    tags: 'none', processEscapes: true,
    packages: {'[+]': ['ams']}
  },
  svg: { scale: 1.1, fontCache: 'global', internalSpeechTitles: false },
  options: {
    skipHtmlTags: ['script','noscript','style','textarea','pre','code'],
    ignoreHtmlClass: 'tex2jax_ignore', processHtmlClass: 'tex2jax_process',
    enableMenu: false
  }
};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js" id="MathJax-script"></script>'''

DEFAULT_CSS = '''
@page { size: A4; margin: 24mm 20mm 24mm 20mm; }
body {
  font-family: "Source Serif 4", "STIX Two Text", Georgia, "Times New Roman", serif;
  font-size: 11pt; line-height: 1.6; color: #1a1a1a;
  max-width: 100%; margin: 0; padding: 0;
}
h1 { font-size: 17pt; margin: 0 0 4mm 0; page-break-before: auto; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 13.5pt; margin: 7mm 0 3mm 0; page-break-after: avoid;
     border-bottom: 0.4pt solid #bbb; padding-bottom: 1.2mm; }
h3 { font-size: 12pt; margin: 5mm 0 2mm 0; page-break-after: avoid; }
p { margin: 0 0 2.5mm 0; text-align: justify; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 2.5mm 0; padding-left: 7mm; }
li { margin-bottom: 1mm; }
mjx-container { font-size: 1.05em; line-height: 1.5; overflow-x: auto; max-width: 100%; }
mjx-container[display="true"] { margin: 3mm 0 !important; text-align: center !important; page-break-inside: avoid; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0 4mm 0; font-size: 9.5pt; page-break-inside: avoid; }
th { background: #f2f2f2; font-weight: 700; border-top: 1pt solid #000;
     border-bottom: 0.6pt solid #000; padding: 1.5mm 2mm; text-align: left; }
td { border-bottom: 0.3pt solid #ccc; padding: 1.2mm 2mm; vertical-align: top; }
tr:last-child td { border-bottom: 1pt solid #000; }
pre { font-family: Consolas, "Courier New", monospace; font-size: 8.5pt;
      background: #f7f7f7; border: 0.3pt solid #ddd; padding: 2.5mm; margin: 3mm 0;
      white-space: pre-wrap; page-break-inside: avoid; }
code { font-family: Consolas, "Courier New", monospace; font-size: 0.92em; }
blockquote { margin: 3mm 0; padding: 2mm 4mm; border-left: 2.5pt solid #888;
             background: #fafafa; color: #333; font-size: 10.5pt; }
a { color: inherit; text-decoration: none; }
figure { margin: 3mm 0; text-align: center; page-break-inside: avoid; }
figcaption { font-size: 9.5pt; color: #444; margin-top: 1mm; }
hr { border: none; border-top: 0.6pt solid #999; margin: 4mm 0; }
@media print {
  h2, h3 { break-after: avoid; }
  table, figure, pre, blockquote { break-inside: avoid; }
}
'''


def find_chrome():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    return None


def find_pandoc():
    for c in [r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe',
              r'C:\Program Files\Pandoc\pandoc.exe']:
        if os.path.exists(c):
            return c
    # PATH fallback
    from shutil import which
    return which('pandoc')


def sanitize_source(md_text):
    """Remove control chars and emoji that break math/print rendering."""
    out = []
    for ch in md_text:
        cp = ord(ch)
        if cp < 32 and cp not in (10, 13, 9):
            continue  # drop control chars (tab/FF/VT from escape bugs)
        if 0x1F000 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x26FF or 0x2B00 <= cp <= 0x2BFF:
            continue  # drop emoji blocks
        out.append(ch)
    text = ''.join(out)
    text = text.replace('\u274c', '\u2717')  # ❌ -> ✗
    text = text.replace('\u2705', '\u2713')  # ✅ -> ✓
    return text


def build_pdf(md_path, pdf_path, title=None, css=None, chrome=None, pandoc=None):
    md_path = os.path.abspath(md_path)
    pdf_path = os.path.abspath(pdf_path)
    workdir = os.path.dirname(pdf_path)
    chrome = chrome or find_chrome()
    pandoc = pandoc or find_pandoc()
    if not chrome or not pandoc:
        print('ERROR: pandoc or Chrome not found')
        return False

    # 1. Read + sanitize source
    md = open(md_path, encoding='utf-8').read()
    md = sanitize_source(md)
    # Strip YAML frontmatter (blank-line-separated YAML bleeds into PDF)
    md = re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.DOTALL)
    md_tmp = os.path.join(workdir, '_md_sanitized.md')
    open(md_tmp, 'w', encoding='utf-8').write(md)

    # 2. pandoc --mathjax (CRITICAL: parses $...$ as math, preserves backslashes)
    html_raw = os.path.join(workdir, '_html_raw.html')
    cmd = [pandoc, md_tmp, '--mathjax', '--standalone']
    if title:
        cmd += ['--metadata', f'title={title}', '--metadata', 'date=2026-08-02']
    cmd += ['-o', html_raw]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print('PANDOC FAIL:', r.stderr[-800:])
        return False

    html = open(html_raw, encoding='utf-8').read()

    # 3. Swap CHTML -> SVG, inject config + css
    html = re.sub(r'<script[^>]*tex-chtml[^>]*></script>', '', html)
    html = html.replace('</head>', SVG_SCRIPT + '\n</head>')
    css_text = css or DEFAULT_CSS
    html = html.replace('</head>', f'<style>\n{css_text}\n</style>\n</head>')
    html_final = os.path.join(workdir, '_html_final.html')
    open(html_final, 'w', encoding='utf-8').write(html)

    # 4. headless Chrome print-to-PDF (fresh profile + cache-bust)
    profile = os.path.join(workdir, '_chrome_prof')
    subprocess.run(['rmdir', '/s', '/q', profile], shell=True, capture_output=True)
    cb = hashlib.md5(html.encode('utf-8')).hexdigest()[:10]
    url = f'file:///{html_final}?cb={cb}'
    cmd = [chrome, '--headless=new', f'--user-data-dir={profile}',
           '--disable-gpu', '--no-sandbox', '--allow-file-access-from-files',
           '--virtual-time-budget=60000', '--run-all-compositor-stages-before-draw',
           '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}', url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired:
        print('CHROME TIMEOUT')
        return False

    if not os.path.exists(pdf_path):
        print('CHROME FAIL:', r.stdout[-300:] if r.stdout else r.stderr[-300:])
        return False

    # 5. Verify with PyMuPDF
    d = fitz.open(pdf_path)
    full = ''.join(p.get_text() for p in d)
    pua = sum(1 for ch in full if 0xE000 <= ord(ch) <= 0xF8FF)
    fffd = full.count(chr(0xFFFD))
    icons = any('SegoeFluentIcons' in f[3] for pg in range(d.page_count) for f in d[pg].get_fonts())
    report = {
        'pages': d.page_count,
        'vector_paths': sum(len(d[i].get_drawings()) for i in range(d.page_count)),
        'U+FFFD': fffd,
        'PUA_chars': pua,
        'SegoeFluentIcons': icons,
    }
    print('VERIFY:', report)
    ok = fffd == 0 and pua == 0 and not icons
    print('RESULT:', 'PASS' if ok else 'FAIL')
    return ok


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: build-mathjax-pdf.py <input.md> <output.pdf> [--title "..."]')
        sys.exit(2)
    md_in, pdf_out = sys.argv[1], sys.argv[2]
    title = None
    if '--title' in sys.argv:
        title = sys.argv[sys.argv.index('--title') + 1]
    ok = build_pdf(md_in, pdf_out, title=title)
    sys.exit(0 if ok else 1)
