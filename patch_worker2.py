import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()

# ============ PATCH 1: table parser (same as before) ============
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
    print('PATCH 1 FAILED - table block not found')

# ============ PATCH 2: paper page head - inject MathJax + table CSS ============
# Target the PAPER page specifically (has "— QNFO Papers</title>" pattern)
# The paper page head: <style>' + COMMON_CSS + '</style></head>
# We need to insert before </style> in the PAPER page only.
# Find the paper page function's style injection uniquely:
# renderPaperHTML uses: '<meta charset="UTF-8"><title>' + esc(paper.title) + ' \u2014 QNFO Papers</title>'
paper_marker = '\\u2014 QNFO Papers</title>'
pidx = js.find(paper_marker)
print(f'Paper page marker found at: {pidx}')
if pidx > 0:
    # Find the <style>' + COMMON_CSS + '</style></head> AFTER this point
    style_anchor = "<style>' + COMMON_CSS + '</style></head>"
    sidx = js.find(style_anchor, pidx)
    print(f'Style anchor in paper page at: {sidx}')
    if sidx > 0:
        # Build replacement: add table CSS before </style>, MathJax before </head>
        # Must be valid inside JS string concatenation - use \\n escapes for newlines
        addition_css = ".rendered-md table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.9em}.rendered-md th{background:#f2f2f2;font-weight:700;border-top:1.5px solid #000;border-bottom:1px solid #000;padding:.45rem .6rem;text-align:left}.rendered-md td{border-bottom:1px solid #ddd;padding:.4rem .6rem;vertical-align:top}.rendered-md tr:last-child td{border-bottom:1.5px solid #000}.rendered-md .math-display{text-align:center;margin:1rem 0;overflow-x:auto}.rendered-md .math-display mjx-container{font-size:1.05em}"
        mj_script = "<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\\\\\\\(','\\\\\\\\)']],displayMath:[['$$','$$'],['\\\\\\\\[','\\\\\\\\]']]},svg:{scale:1.1,fontCache:'global'},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script><script async src=\\\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js\\\" id=\\\"MathJax-script\\\"></script>"

        old_anchor = "<style>' + COMMON_CSS + '</style></head>"
        new_anchor = "<style>' + COMMON_CSS + '" + addition_css + "</style>" + mj_script + "</head>"
        js = js.replace(old_anchor, new_anchor, 1)
        print('PATCH 2 applied: MathJax + table CSS injected into paper page head')
    else:
        print('PATCH 2 FAILED - style anchor not found after paper marker')
else:
    print('PATCH 2 FAILED - paper page marker not found')

open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker-patched.js', 'w', encoding='utf-8', newline='\n').write(js)
print(f'Patched: {len(js)} bytes')
