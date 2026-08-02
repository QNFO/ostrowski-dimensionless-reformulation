# MathJax PDF Build Pipeline — Permanent Fix for Unicode Math Rendering

**Status:** VERIFIED WORKING (ODR v4.0.2, DOI 10.5281/zenodo.21755771, 2026-08-02)

## Root Cause

pandoc + XeLaTeX uses system fonts. The default Latin Modern font **lacks glyphs**
for Unicode math characters (μ, χ, ϕ, ℚ, ₃, ∫, ℏ, π when outside `$...$`), producing
hundreds of `Missing character` warnings and unreadable mathematical expressions.
`unicode-math` + `-V header-includes` does NOT work with pandoc's template loading
order (verified live — 391 warnings). `build-paper.py` (unicode→latex conversion)
breaks on papers that already contain `$...$` math mode (verified live — "Missing }
inserted" error).

## The Fix: Do What Obsidian Does

Obsidian renders math via **MathJax** in the browser. Replicate exactly that:

### Steps (VERIFIED)

```powershell
# 1. STRIP YAML frontmatter (blank-line-separated YAML breaks pandoc parsing and bleeds into PDF)
#    python: re.sub(r'^---\n.*?\n---\n', '', content, count=1, flags=re.DOTALL)

# 2. Convert markdown to HTML with MathJax (CDN-injected, full Unicode math support)
pandoc odr-nofm.md --mathjax --standalone --metadata title="..." -o paper.html

# 3. Render PDF with headless Chrome (file:// URL works; HTTP server timed out)
chrome.exe --headless=new --disable-gpu --no-sandbox --allow-file-access-from-files `
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw `
  --print-to-pdf=paper.pdf --print-to-pdf-no-header "file:///path/to/paper.html"

# 4. VERIFY with PyMuPDF (MANDATORY — Anti-Phantom Gate)
python: fitz.open(pdf) → page_count, U+FFFD count == 0, key math glyphs present
```

### Verification Results (ODR v4.0.2)

| Check | Result |
|:------|:-------|
| Pages | 41 |
| U+FFFD (tofu) | 0 |
| ℏ (U+210F) glyphs | 85 rendered |
| μ (U+03BC) glyphs | 62 rendered |
| ℚ (U+211A) glyphs | 47 rendered |
| YAML bleed | None |
| LaTeX escape artifacts | None (fix `\"{U}` → `Ü` before build) |

### Kaizen Anti-Patterns (permanent)

1. **NEVER use `---` for horizontal rules** in paper markdown — pandoc misparses
   it as a second YAML block → frontmatter bleeds into PDF. Use `***`.
2. **NEVER use `-V header-includes=`** for LaTeX preamble injection — use
   `--include-in-header=file.tex` (correct layer). MathJax pipeline supersedes both.
3. **`unicode-math` + `Latin Modern Math` via pandoc does NOT activate the math font**
   — tested live, 391 warnings. Do not retry this path.
4. **Do NOT wrap Unicode math in `$...$` inside an already-`$...$`-rich paper**
   (build-paper.py failure mode) — the MathJax pipeline needs no wrapping at all.
5. **Fix LaTeX escape artifacts in references** (`\"{U}` → `Ü`, `\ss{}` → `ß`)
   BEFORE the HTML build — pandoc passes LaTeX syntax through to HTML literally.
