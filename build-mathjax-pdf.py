#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEPRECATED — SUPERSEDED BY build-pdf-pro.py (2026-08-02)

This script (Chrome CLI --print-to-pdf route) is RETIRED for publications:
  - CLI --print-to-pdf CANNOT render page numbers or professional footers.
  - The old --print-to-pdf-no-header flag leaves headers in new headless.
  - Google-Fonts unicode-range subset fonts race the print pipeline.

USE: python build-pdf-pro.py <input.md> <output.pdf> --title "..."
The MathJax-SVG -> puppeteer CDP pipeline passes all 20 edge cases with
zero errors, professional typography (STIX Two Text), and page numbers.

Kept for reference / legacy verification only. Do not use for new work.
"""
raise SystemExit("DEPRECATED: use build-pdf-pro.py (the canonical publication pipeline)")
