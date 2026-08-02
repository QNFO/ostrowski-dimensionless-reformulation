import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()

# ============ PATCH 1: table parser handles blank lines ============
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
    print('PATCH 1 applied')
else:
    print('PATCH 1 FAILED')

# ============ PATCH 2: paper page ONLY - MathJax + table CSS ============
# Find renderPaperHTML function start
fn_idx = js.find('function renderPaperHTML(')
print(f'renderPaperHTML at: {fn_idx}')
if fn_idx < 0:
    print('PATCH 2 FAILED: renderPaperHTML not found')
else:
    # Find the style anchor AFTER fn_idx (within paper page)
    anchor = "<style>' + COMMON_CSS + '</style></head>"
    sidx = js.find(anchor, fn_idx)
    print(f'Paper page style anchor at: {sidx}')
    if sidx < 0:
        print('PATCH 2 FAILED: paper page style anchor not found')
    else:
        # Table CSS (no single quotes!) appended before </style>
        css_add = ".rendered-md table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.9em}.rendered-md th{background:#f2f2f2;font-weight:700;border-top:1.5px solid #000;border-bottom:1px solid #000;padding:.45rem .6rem;text-align:left}.rendered-md td{border-bottom:1px solid #ddd;padding:.4rem .6rem;vertical-align:top}.rendered-md tr:last-child td{border-bottom:1.5px solid #000}.rendered-md .math-display{text-align:center;margin:1rem 0;overflow-x:auto}.rendered-md .math-display mjx-container{font-size:1.05em}"
        # MathJax script: use DOUBLE quotes inside to avoid breaking outer single-quoted JS string
        mj = "<script>window.MathJax={tex:{inlineMath:[[\"$\",\"$\"]],displayMath:[[\"$$\",\"$$\"]],processEscapes:true},svg:{scale:1.1,fontCache:\"global\"},options:{skipHtmlTags:[\"script\",\"noscript\",\"style\",\"textarea\",\"pre\",\"code\"],enableMenu:false}};</script><script async src=\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js\" id=\"MathJax-script\"></script>"
        new_anchor = "<style>' + COMMON_CSS + '" + css_add + "</style>" + mj + "</head>"
        js = js[:sidx] + new_anchor + js[sidx+len(anchor):]
        print('PATCH 2 applied (paper page only)')

open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker-patched.js', 'w', encoding='utf-8', newline='\n').write(js)
print(f'Patched: {len(js)} bytes')
