import urllib.request, json, os

TOKEN = os.environ.get('ZENODO_TOKEN')
HEADERS = {'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json'}
BASE = 'https://zenodo.org/api/deposit/depositions'
PREV_ID = 21755771
PAPER_DIR = os.path.expandvars(r'%TEMP%\odr-inspect')
SLUG = 'ostrowski-dimensionless-reformulation'

# 1. Create newversion from v4.0.2
print("1. Creating newversion from 21755771...")
req = urllib.request.Request(f'{BASE}/{PREV_ID}/actions/newversion', headers=HEADERS, method='POST')
result = json.loads(urllib.request.urlopen(req).read())
draft_id = result['links']['latest_draft'].split('/')[-1]
print(f"   Draft: {draft_id}")

# 2. Delete ALL stale files (GATE P5.CLEAN)
print("2. Deleting stale files...")
req = urllib.request.Request(f'{BASE}/{draft_id}/files', headers={'Authorization': 'Bearer ' + TOKEN})
files = json.loads(urllib.request.urlopen(req).read())
for f in files:
    urllib.request.urlopen(urllib.request.Request(
        f'{BASE}/{draft_id}/files/{f["id"]}', headers={'Authorization': 'Bearer ' + TOKEN}, method='DELETE'))
print(f"   Deleted {len(files)}")

# 3. Get bucket
req = urllib.request.Request(f'{BASE}/{draft_id}', headers=HEADERS)
record = json.loads(urllib.request.urlopen(req).read())
bucket = record['links']['bucket']
print(f"3. Bucket: {bucket}")

# 4. Upload preview-first: PDF, README, MD
HEADERS_OCTET = {'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/octet-stream'}
uploads = [
    (f'{PAPER_DIR}\\{SLUG}.pdf', f'{SLUG}.pdf'),
    (f'{PAPER_DIR}\\README.md', 'README.md'),
    (f'{PAPER_DIR}\\{SLUG}.md', f'{SLUG}.md'),
]
print("4. Uploading...")
for fpath, fname in uploads:
    if os.path.exists(fpath):
        sz = os.path.getsize(fpath)
        print(f"   {fname} ({sz}b)...", end=' ')
        req = urllib.request.Request(f'{bucket}/{fname}', data=open(fpath,'rb').read(), headers=HEADERS_OCTET, method='PUT')
        print(f"HTTP {urllib.request.urlopen(req).getcode()}")
    else:
        print(f"   SKIP {fname}")

# 5. Metadata
metadata = {
    "metadata": {
        "title": "The Ostrowski Dimensionless Reformulation v4.0.3: A Place-Democratic Foundation for Fundamental Physics — Definitive Edition",
        "upload_type": "publication",
        "publication_type": "preprint",
        "description": "Version 4.0.3 (2026-08-02). PDF re-rendered with the VERIFIED MathJax-SVG pipeline: pandoc --mathjax (preserves LaTeX math) → MathJax SVG output (pure vector paths, no font dependence) → print.css (A4 margins, Georgia serif, page breaks) → headless Chrome --no-pdf-header-footer. Result: 45 pages, 4,373 vector paths, 0 U+FFFD, 0 PUA chars, no SegoeFluentIcons, no header/footer artifacts. Source sanitized (control chars removed, emoji replaced with typographic symbols). Replaces v4.0.2's PDF which was rendered via the older XeLaTeX pipeline with font warnings. IsNewVersionOf: 10.5281/zenodo.21755771 (v4.0.2).",
        "creators": [{"name": "Quni-Gudzinas, Rowan Brad", "affiliation": "Independent Researcher", "orcid": "0009-0002-4317-5604"}],
        "access_right": "open",
        "license": "CC-BY-4.0",
        "version": "4.0.3",
        "publication_date": "2026-08-02",
        "keywords": ["Ostrowski theorem", "Planck units", "dimensional analysis", "Buckingham Pi theorem", "dimensionless reformulation", "place democracy", "p-adic completions", "5-smooth semigroup", "adele ring", "Bruhat-Tits tree", "cross-ratio", "ratio primacy", "running coupling", "Tate thesis", "Hensel codes", "Hecke algebra", "ultrametric noise", "renormalization group", "Standard Model", "formula derivation", "MathJax SVG PDF"],
        "related_identifiers": [
            {"relation": "isNewVersionOf", "identifier": "10.5281/zenodo.21755771", "scheme": "doi"},
            {"relation": "isVersionOf", "identifier": "10.5281/zenodo.21749884", "scheme": "doi"},
            {"relation": "isSupplementedBy", "identifier": "https://github.com/QNFO/ostrowski-dimensionless-reformulation", "scheme": "url"}
        ],
        "language": "eng"
    }
}
print("5. Setting metadata...")
body = json.dumps(metadata).encode('utf-8')
req = urllib.request.Request(f'{BASE}/{draft_id}', data=body, headers=HEADERS, method='PUT')
urllib.request.urlopen(req)
print("   OK")

# 6. Publish
print("6. Publishing...")
req = urllib.request.Request(f'{BASE}/{draft_id}/actions/publish', headers=HEADERS, method='POST')
result = json.loads(urllib.request.urlopen(req).read())
print(f"   PUBLISHED: {result['doi']} (ID: {result['id']})")

with open(os.path.join(PAPER_DIR, '_v403_doi.txt'), 'w') as f:
    f.write(result['doi'])
with open(os.path.join(PAPER_DIR, '_v403_id.txt'), 'w') as f:
    f.write(str(result['id']))
