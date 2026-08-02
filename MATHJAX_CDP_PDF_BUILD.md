# MATHJAX-SVG PDF PIPELINE — THE SINGLE MANDATED PUBLICATION PROCESS

**Status:** VERIFIED CANONICAL (2026-08-02) — ODR v4.0.4, DOI 10.5281/zenodo.21756190
**Consolidation:** ALL other markdown→PDF routes DEPRECATED. Use ONLY this pipeline.

## THE ONE PROCESS (works every time)

```
python build-pdf-pro.py <slug>.md <slug>.pdf --title "<Full Paper Title>"
```

Auto-bootstraps puppeteer-core on first run. Requires: pandoc, Chrome/Edge,
Python 3, PyMuPDF. No TeX installation needed. No CDN dependency (MathJax
self-hosted at js/tex-svg-full.js). Fonts embedded (fonts/STIXTwo*.woff2).

## Why this is the ONLY route (measured error rates, 2026-08-02)

| # | Route | Error signature | Verdict |
|:--|:------|:----------------|:--------|
| A | pandoc → xelatex (bare) | 230-391 "Missing character" warnings (μ χ ϕ ℚ ₃ ∫) | ❌ FAIL |
| B | pandoc → xelatex + `unicode-math -V` | 391 warnings — pandoc template ignores `-V` | ❌ FAIL |
| C | pandoc --mathjax → CHTML → Chrome CLI | PUA glyphs \uedd9-\ueddc → SegoeFluentIcons icons | ❌ FAIL |
| D | build-mathjax-pdf.py (Chrome CLI) | math OK, but NO page numbers; old header flag; font-subset race | ⚠️ PARTIAL |
| E | research build-paper.py (unicode→latex) | "Missing } inserted" crash on pre-existing $...$ | ❌ FAIL |
| **F** | **build-pdf-pro.py (MathJax-SVG → puppeteer CDP)** | **0 errors — PASS (45 pp, 4742 vectors, 0 U+FFFD, page numbers)** | ✅ **CANONICAL** |

## Pipeline internals (verified)

1. `sanitize_source()` — collapse blank lines in tables (the root cause of
   BOTH pandoc line-block fallback AND papers.qnfo.org raw-pipe rendering),
   strip emoji/control chars, ✓/✗ → Yes/No, CRLF→LF, nbsp→space.
2. Strip YAML frontmatter (blank-line-separated YAML bleeds into PDF).
3. `pandoc --mathjax --standalone` — CRITICAL: parses `$...$` as REAL math,
   preserves backslashes. Do NOT use `-f markdown-tex_math_dollars-...`
   (that DESTROYS math: `\tilde{R}` → markdown emphasis).
4. Swap CHTML→SVG renderer (self-hosted tex-svg-full.js). CHTML injects PUA
   glyphs; SVG embeds pure vector paths — zero font dependence.
5. Inline print-v5.css — STIX Two Text (prose) + STIX Two Math (operators),
   embedded woff2, full Unicode math-in-prose coverage → ZERO glyph fallback,
   no mixed Times/Cambria/Segoe fonts. Justified text + hyphenation,
   booktabs tables (thead repeats on page breaks), page-break control
   (break-after: avoid on headings, orphans/widows 3) → 0 orphaned headings.
6. puppeteer-core CDP `Page.printToPDF` — A4, 22/20/18/18mm margins,
   professional footer with page numbers ("N / M").
7. PyMuPDF verify — MUST show 0 U+FFFD, 0 PUA, no Segoe fonts, no Times
   fallback. Exit 0 = publication-ready.

## papers.qnfo.org parity

The gateway worker serves the SAME typography (STIX body font via Google
Fonts, justified text, booktabs tables, MathJax SVG). Markdown source is
normalized identically (table blank-line fix), so the web page matches the
PDF. Deployed 2026-08-02 (worker version 0f2ab81b).

## Edge cases verified (20-case stress test, stress-test.md)

Long display equations, matrices, cases/delimiters, sums/integrals/products
with limits, math in tables, headings with math, Unicode math in prose
(ℚ ℝ ℤ ℂ ℏ ≈ ≤ ≥ ⁻ ₃ Greek ℓ ∂ ∇ ∞ ∑ ∏ ∫), code blocks, blockquotes with
math, nested lists, multi-page tables (header repetition), malformed math
(error shown, never crashes), HTML special chars, consecutive display eqs,
deep headings, DOIs/links, long unbreakable tokens, nested fractions/radicals,
empty math, mixed final paragraph.

## Mandate

- **Markdown-native papers:** `build-pdf-pro.py` ONLY.
- **LaTeX-native submissions** (Springer Nature .tex): research skill
  `build-paper.py` (deprecated but retained) — verify no Unicode-math prose.
- **NEVER** use Chrome CLI `--print-to-pdf` for publications (no footer control).
- **NEVER** add new build scripts — this is the single process.
