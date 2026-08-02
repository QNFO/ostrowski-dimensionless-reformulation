#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-pdf-pro.py — THE SINGLE CANONICAL PUBLICATION PIPELINE (v3, 2026-08-02)

MANDATED: All QNFO Markdown-native publications use THIS script for PDF
generation. All XeLaTeX/CHTML/CLI-print routes are DEPRECATED (see
MATHJAX_CDP_PDF_BUILD.md). This is the only route that passed the 20-case
edge stress test with ZERO errors, professional typography, and page numbers.

ROUTE (Obsidian-style — MathJax in browser → print):
  markdown
    -> sanitize_source()   (tables normalized, emoji->text, control chars, CRLF)
    -> strip YAML frontmatter
    -> pandoc --mathjax --standalone   (parses $...$ as REAL math; preserves backslashes)
    -> inject self-hosted MathJax SVG (js/tex-svg-full.js — no CDN dependency)
    -> inline print-v5.css  (STIX Two Text+Math embedded fonts, booktabs, page-break control)
    -> puppeteer-core CDP Page.printToPDF  (A4, margins, page numbers in footer)
    -> PyMuPDF verify       (0 U+FFFD, 0 PUA, no icon fonts, no Times fallback)

AUTO-BOOTSTRAP: puppeteer-core is installed on first run into ./npm — the
pipeline works on any machine with pandoc + Chrome/Edge + Python 3.

USAGE:
  python build-pdf-pro.py <input.md> <output.pdf> [--title "..."]

EXIT CODES:
  0 = PASS (verified professional-quality PDF)
  1 = FAIL (build or verification failed)
  2 = bad invocation
"""
import subprocess, re, os, sys, io, json, time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME_CANDIDATES = [
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
]
PUPPETEER = os.path.join(HERE, 'npm', 'node_modules', 'puppeteer-core')

SVG_SCRIPT = '''<script>
window.MathJax = {
  loader: { load: ['[tex]/ams'] },
  tex: {
    inlineMath: [['$','$'], ['\\\\(','\\\\)']],
    displayMath: [['$$','$$'], ['\\\\[','\\\\]']],
    tags: 'none', processEscapes: true,
    packages: {'[+]': ['ams']}
  },
  svg: { scale: 1.0, fontCache: 'global', internalSpeechTitles: false },
  options: {
    skipHtmlTags: ['script','noscript','style','textarea','pre','code'],
    ignoreHtmlClass: 'tex2jax_ignore', processHtmlClass: 'tex2jax_process',
    enableMenu: false
  },
  startup: { typeset: true }
};
</script>
<script async src="js/tex-svg-full.js" id="MathJax-script"></script>'''


def sanitize_source(md_text):
    """Remove control chars, emoji; normalize table blocks; ✓/✗ -> text; CRLF->LF."""
    out = []
    for ch in md_text:
        cp = ord(ch)
        if cp < 32 and cp not in (10, 13, 9):
            continue
        if 0x1F000 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x26FF or 0x2B00 <= cp <= 0x2BFF:
            continue
        out.append(ch)
    text = ''.join(out)
    text = text.replace('\u2705', 'Yes').replace('\u274c', 'No')
    text = text.replace('\u2713', 'Yes').replace('\u2717', 'No')
    text = text.replace('\u2714', 'Yes').replace('\u2718', 'No')
    text = re.sub(r'\r\n?', '\n', text)
    text = re.sub(r'\u00a0', ' ', text)
    text, _ = normalize_tables(text)
    return text


def normalize_tables(md_text):
    """Collapse blank lines inside pipe-table blocks (root cause of both
    pandoc line-block fallback AND papers.qnfo.org raw-pipe rendering)."""
    lines = md_text.split('\n')
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped[1:-1]:
            block = []
            j = i
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith('|'):
                    block.append(lines[j])
                    j += 1
                elif s == '' and j + 1 < len(lines) and lines[j + 1].strip().startswith('|'):
                    j += 1
                else:
                    break
            if len(block) >= 2:
                out.extend(block)
                fixed += 1
                i = j
                continue
        out.append(line)
        i += 1
    return '\n'.join(out), fixed


def find_pandoc():
    for c in [r'C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe',
              r'C:\Program Files\Pandoc\pandoc.exe']:
        if os.path.exists(c):
            return c
    from shutil import which
    return which('pandoc')


def find_chrome():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    return None


def ensure_puppeteer():
    """Auto-bootstrap: install puppeteer-core into repo-local npm/ if missing.
    Makes the pipeline portable — works on any machine with pandoc + Chrome
    + Python, no manual npm step required."""
    if os.path.exists(PUPPETEER):
        return True
    npm_dir = os.path.join(HERE, 'npm')
    os.makedirs(npm_dir, exist_ok=True)
    print('Installing puppeteer-core (first run)...')
    r = subprocess.run(['npm', 'install', 'puppeteer-core', '--prefix', npm_dir],
                       capture_output=True, text=True, timeout=300, cwd=HERE)
    if r.returncode != 0:
        print('npm install FAILED:', r.stdout[-400:], r.stderr[-400:])
        return False
    return os.path.exists(PUPPETEER)


def build_pdf(md_path, pdf_path, title=None, css='print-v5.css'):
    md_path = os.path.abspath(md_path)
    pdf_path = os.path.abspath(pdf_path)
    workdir = os.path.dirname(pdf_path)
    pandoc = find_pandoc()
    chrome = find_chrome()
    if not pandoc or not chrome:
        print('ERROR: pandoc or Chrome not found')
        return False

    # 1. Sanitize + strip frontmatter
    md = open(md_path, encoding='utf-8').read()
    md = sanitize_source(md)
    md = re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.DOTALL)
    md_tmp = os.path.join(workdir, '_pro.md')
    open(md_tmp, 'w', encoding='utf-8').write(md)

    # 2. pandoc --mathjax (parses $...$ as real math, preserves backslashes)
    html_raw = os.path.join(workdir, '_pro_raw.html')
    cmd = [pandoc, md_tmp, '--mathjax', '--standalone']
    if title:
        cmd += ['--metadata', f'title={title}', '--metadata', 'date=2026-08-02']
    cmd += ['-o', html_raw]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print('PANDOC FAIL:', r.stderr[-800:])
        return False

    html = open(html_raw, encoding='utf-8').read()

    # 3. Inject SVG MathJax (self-hosted) + inline CSS
    html = re.sub(r'<script[^>]*tex-chtml[^>]*></script>', '', html)
    html = html.replace('</head>', SVG_SCRIPT + '\n</head>')
    css_path = os.path.join(HERE, css)
    if os.path.exists(css_path):
        css_text = open(css_path, encoding='utf-8').read()
        html = html.replace('</head>', f'<style>\n{css_text}\n</style>\n</head>')
    html_final = os.path.join(workdir, '_pro.html')
    open(html_final, 'w', encoding='utf-8').write(html)

    # 4. CDP print via puppeteer-core — page numbers, A4 margins
    if not ensure_puppeteer():
        print('ERROR: puppeteer-core unavailable at', PUPPETEER)
        return False

    driver = os.path.join(HERE, '_pup_driver.js')
    driver_js = r'''
const puppeteer = require('__PUPPETEER__');
(async () => {
  const path = process.argv[2], out = process.argv[3];
  const browser = await puppeteer.launch({
    executablePath: process.argv[4],
    headless: 'new', args: ['--no-sandbox','--disable-gpu','--allow-file-access-from-files']
  });
  const page = await browser.newPage();
  page.setDefaultTimeout(120000);
  const errs = [];
  page.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text().slice(0,200)); });
  await page.goto('file:///' + path, {waitUntil: 'networkidle0', timeout: 120000});
  await page.evaluate(() => {
    return new Promise((resolve, reject) => {
      const t0 = Date.now();
      const chk = () => {
        if (window.MathJax && window.MathJax.startup && window.MathJax.startup.document)
          window.MathJax.startup.promise.then(() => resolve(true)).catch(e => reject(e));
        else if (Date.now() - t0 > 60000) reject(new Error('MathJax timeout'));
        else setTimeout(chk, 200);
      };
      chk();
    });
  });
  await page.evaluate(() => document.fonts.ready);
  await new Promise(r => setTimeout(r, 1500));
  await page.pdf({
    path: out, format: 'A4', printBackground: true,
    displayHeaderFooter: true,
    margin: { top: '22mm', bottom: '20mm', left: '18mm', right: '18mm' },
    headerTemplate: '<div style="font-size:8px;color:#666;width:100%;text-align:center;padding:0 18mm;font-family:STIX Two Text,Georgia,serif;"><span class="title"></span></div>',
    footerTemplate: '<div style="font-size:8px;color:#666;width:100%;text-align:center;padding:0 18mm;font-family:STIX Two Text,Georgia,serif;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    preferCSSPageSize: false
  });
  await browser.close();
  if (errs.length) { console.log('JS_ERRORS: ' + errs.join(' | ')); process.exit(2); }
  console.log('PDF_OK');
})().catch(e => { console.error('DRIVER_FAIL: ' + e.message); process.exit(1); });
'''
    driver_js = driver_js.replace('__PUPPETEER__', PUPPETEER.replace('\\', '/'))
    open(driver, 'w', encoding='utf-8').write(driver_js)

    cmd = ['node', driver, html_final, pdf_path, chrome]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if r.returncode != 0:
        print('CDP FAIL:', r.stdout[-500:], r.stderr[-500:])
        return False

    # 5. Verify with PyMuPDF
    try:
        import fitz
        d = fitz.open(pdf_path)
        full = ''.join(p.get_text() for p in d)
        pua = sum(1 for ch in full if 0xE000 <= ord(ch) <= 0xF8FF)
        fffd = full.count(chr(0xFFFD))
        fonts = set()
        for pg in range(d.page_count):
            for f in d[pg].get_fonts():
                fonts.add(f[3])
        icons = any('Segoe' in f for f in fonts)
        bad_fonts = [f for f in fonts if 'Times' in f and 'STIX' not in f]
        report = {
            'pages': d.page_count,
            'vector_paths': sum(len(d[i].get_drawings()) for i in range(d.page_count)),
            'U+FFFD': fffd,
            'PUA': pua,
            'icon_fonts': icons,
            'non_stix_times': bad_fonts[:5],
            'fonts': sorted(fonts),
        }
        print('VERIFY:', json.dumps(report))
        ok = fffd == 0 and pua == 0 and not icons and not bad_fonts
        print('RESULT:', 'PASS' if ok else 'FAIL')
        return ok
    except Exception as e:
        print('VERIFY ERROR:', e)
        return False


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: build-pdf-pro.py <input.md> <output.pdf> [--title "..."]')
        sys.exit(2)
    md_in, pdf_out = sys.argv[1], sys.argv[2]
    title = None
    if '--title' in sys.argv:
        title = sys.argv[sys.argv.index('--title') + 1]
    ok = build_pdf(md_in, pdf_out, title=title)
    sys.exit(0 if ok else 1)
