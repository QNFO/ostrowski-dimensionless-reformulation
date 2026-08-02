# MathJax PDF Build Pipeline — VERIFIED PERMANENT FIX (2026-08-02)

**Status:** VERIFIED WORKING — ODR v4.0.2 (DOI 10.5281/zenodo.21755771), 45 pages,
4,373 vector paths, 0 U+FFFD, 0 PUA chars, 0 SegoeFluentIcons, 0 header/footer artifacts.

## Why Every Other Approach Failed (all tested live)

| Approach | Failure |
|:---------|:--------|
| pandoc + XeLaTeX | Latin Modern font lacks Unicode math glyphs (μ χ ϕ ℚ ₃ ∫) → hundreds of `Missing character` warnings, unreadable math |
| `unicode-math` + `-V header-includes=` | Pandoc template loading order ignores `-V` → 391 warnings |
| `build-paper.py` unicode→LaTeX conversion | Breaks on papers already containing `$...$` → `Missing } inserted` |
| `-f markdown-tex_math_dollars-...` | **DESTROYS math**: pandoc parses `\tilde{R}` as markdown emphasis → `$_{} = <em>P^2 R</em>{}$` |
| `--print-to-pdf-no-header` (old flag) | Leaves headers/footers in new headless Chrome |

## The Working Pipeline (Obsidian-style: MathJax in browser → print)

```
1. pandoc --mathjax --standalone
     # CRITICAL: --mathjax parses $...$ as REAL math, emits \(...\) / \[...\],
     # preserving all backslashes. Do NOT disable tex_math_dollars.
2. Swap CHTML script -> SVG (tex-svg-full.js + SVG config)
     # CHTML injects PUA glyphs (\uedd9-\ueddc via SegoeFluentIcons) that
     # print-to-PDF exposes as icon glyphs. SVG embeds PURE VECTOR paths —
     # zero font dependence, crisper at all zooms.
3. Inline print.css
     # @page A4 + margins, Georgia serif, page-break rules. Without it the
     # output looks like a webpage screenshot, not a paper.
4. headless Chrome --no-pdf-header-footer --print-to-pdf
     # --no-pdf-header-footer is the NEW headless flag (old: --print-to-pdf-no-header)
     # Fresh --user-data-dir + ?cb= cache-bust query to avoid stale file:// cache.
5. Verify with PyMuPDF:
     # 0 U+FFFD, 0 PUA chars, no SegoeFluentIcons font, vector_paths > 0
```

## Source Sanitization (MANDATORY before build)

1. **Strip YAML frontmatter** (blank-line-separated YAML bleeds into PDF):
   `re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.DOTALL)`
2. **Remove control chars** (chr<32 except \n\r\t) — tab/FF/VT chars from Python
   escape bugs corrupt math (`\t`→TAB breaks `\tilde`; `\f` breaks `\varphi`).
3. **Replace emoji** (❌→✗ U+2717, ✅→✓ U+2713) — emoji render via
   SegoeFluentIcons/SegoeUISymbol on Windows, unprofessional in a paper.
4. **Never use `---` for horizontal rules** in paper markdown (YAML bleed);
   use `***`.

## Usage

```powershell
python build-mathjax-pdf.py paper.md paper.pdf --title "Paper Title"
```

## Key Files

- `build-mathjax-pdf.py` — the complete reusable pipeline (this repo)
- Dependencies: pandoc, Chrome/Edge, PyMuPDF (`pip install PyMuPDF`), internet
  (MathJax loads from jsdelivr CDN)
