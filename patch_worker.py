import re, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()
orig_len = len(js)

# ============ PATCH 1: renderMarkdown table parser - handle blank lines ============
# Original: requires contiguous rows (L[i+1] separator, while L[i] contiguous)
old_table = '''    if (t.indexOf("|") >= 0 && i + 1 < L.length && /^\\|?[\\s:]*-{3,}[\\s:]*\\|/.test(L[i + 1].trim())) {
      o += "<table><thead><tr>";
      let hs = t.split("|").map((x) => x.trim()).filter((x) => x);
      for (let h = 0; h < hs.length; h++) o += "<th>" + _mdInline(hs[h]) + "</th>";
      o += "</tr></thead><tbody>";
      i += 2;
      while (i < L.length && L[i].trim().indexOf("|") >= 0) {
        o += "<tr>";
        let cs = L[i].trim().split("|").map((x) => x.trim()).filter((x) => x);
        for (let c = 0; c < cs.length; c++) o += "<td>" + _mdInline(cs[c]) + "</td>";
        o += "</tr>";
        i++;
      }
      o += "</tbody></table>";
      continue;
    }'''

new_table = '''    if (t.indexOf("|") >= 0) {
      // Find the separator row, skipping blank lines (2026-08-02 fix:
      // papers with blank lines between table rows were NOT parsed as tables)
      let si = i + 1;
      while (si < L.length && L[si].trim() === "") si++;
      if (si < L.length && /^\\|?[\\s:]*-{3,}[\\s:]*\\|/.test(L[si].trim())) {
        o += "<table><thead><tr>";
        let hs = t.split("|").map((x) => x.trim()).filter((x) => x);
        for (let h = 0; h < hs.length; h++) o += "<th>" + _mdInline(hs[h]) + "</th>";
        o += "</tr></thead><tbody>";
        i = si + 1;
        while (i < L.length) {
          if (L[i].trim() === "") { i++; continue; }
          if (L[i].trim().indexOf("|") < 0) break;
          o += "<tr>";
          let cs = L[i].trim().split("|").map((x) => x.trim()).filter((x) => x);
          for (let c = 0; c < cs.length; c++) o += "<td>" + _mdInline(cs[c]) + "</td>";
          o += "</tr>";
          i++;
        }
        o += "</tbody></table>";
        continue;
      }
    }'''

if old_table in js:
    js = js.replace(old_table, new_table)
    print('PATCH 1 applied: table parser handles blank lines')
else:
    print('PATCH 1 FAILED: old table block not found')

# ============ PATCH 2: renderPaperHTML - load MathJax + add math/table CSS ============
old_paper_head = '''<style>' + COMMON_CSS + '</style></head>'''
new_paper_head = '''<style>' + COMMON_CSS + '.rendered-md table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.9em}.rendered-md th{background:#f2f2f2;font-weight:700;border-top:1.5px solid #000;border-bottom:1px solid #000;padding:.45rem .6rem;text-align:left}.rendered-md td{border-bottom:1px solid #ddd;padding:.4rem .6rem;vertical-align:top}.rendered-md tr:last-child td{border-bottom:1.5px solid #000}.rendered-md .math-display{text-align:center;margin:1rem 0;overflow-x:auto}.rendered-md .math-display mjx-container{font-size:1.05em}</style>
<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]},svg:{scale:1.1,fontCache:'global'},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js" id="MathJax-script"></script>
</head>'''

if old_paper_head in js:
    js = js.replace(old_paper_head, new_paper_head)
    print('PATCH 2 applied: MathJax + table CSS injected')
else:
    print('PATCH 2 FAILED: paper head block not found')

open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker-patched.js', 'w', encoding='utf-8').write(js)
print(f'Patched worker: {orig_len} -> {len(js)} bytes')
